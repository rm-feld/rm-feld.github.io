import numpy as np
from scipy.stats import norm
rng=np.random.default_rng(7)

# ---- K=2 crossed probit, full grid; validate the ALL-likelihood Godambe sandwich ----
R1=R2=15
rows,cols=np.meshgrid(np.arange(R1),np.arange(R2),indexing='ij')
rows=rows.ravel(); cols=cols.ravel(); N=rows.size
p=2
# fixed design (same across datasets): intercept + one covariate
Xcov=rng.normal(size=N)
X=np.column_stack([np.ones(N),Xcov])
beta=np.array([0.3,0.8]); sa2,sb2=0.6,0.4; sE2=1.0
sig2=sE2+sa2+sb2; sig=np.sqrt(sig2)
gamma0=beta/sig
phi=norm.pdf; Phi=norm.cdf
def R_mills(t): return phi(t)/np.clip(Phi(t),1e-12,None)

def gen():
    a=rng.normal(0,np.sqrt(sa2),R1); b=rng.normal(0,np.sqrt(sb2),R2)
    z=X@beta+a[rows]+b[cols]+rng.normal(size=N)
    return (z>0).astype(float)

def fit_all(y):
    ty=2*y-1; g=np.zeros(p)
    for _ in range(50):
        t=ty*(X@g); Rm=R_mills(t)
        s=ty*phi(X@g)/np.clip(Phi(t),1e-12,None)       # per-obs score weight
        U=X.T@s
        w=Rm*(t+Rm)                                     # observed-info weight >=0
        H=(X*w[:,None]).T@X
        step=np.linalg.solve(H,U); g=g+step
        if np.max(np.abs(step))<1e-10: break
    return g

def sandwich_pieces(y,g):
    ty=2*y-1; t=ty*(X@g)
    s=ty*phi(X@g)/np.clip(Phi(t),1e-12,None)
    w=R_mills(t)*(t+R_mills(t))
    H=(X*w[:,None]).T@X
    sx=s[:,None]*X                                      # s_l x_l  (N x p)
    # crossed J via row-sum & col-sum blocks minus double-counted diagonal
    Srow=np.zeros((R1,p)); np.add.at(Srow,rows,sx)
    Scol=np.zeros((R2,p)); np.add.at(Scol,cols,sx)
    J_cross=Srow.T@Srow + Scol.T@Scol - (sx.T@sx)
    J_naive=sx.T@sx                                     # independence (ignores crossing)
    return H,J_cross,J_naive

D=3000
G=np.zeros((D,p)); Vs=np.zeros((D,p,p)); Vn=np.zeros((D,p,p))
for d in range(D):
    y=gen(); g=fit_all(y); G[d]=g
    H,Jc,Jn=sandwich_pieces(y,g)
    Hi=np.linalg.inv(H)
    Vs[d]=Hi@Jc@Hi; Vn[d]=Hi@Jn@Hi

Vmc=np.cov(G.T)                     # Monte-Carlo truth: sampling cov of gamma-hat
Vsand=Vs.mean(0); Vnaive=Vn.mean(0)
np.set_printoptions(precision=5,suppress=True)
print("gamma0            =",gamma0)
print("mean(gamma_hat)   =",G.mean(0),"  (unbiased check)")
print("\n--- avar(gamma_hat): compare model-based vs Monte-Carlo ---")
print("MC truth  Cov(gamma_hat):\n",Vmc)
print("Sandwich  H^-1 J_cross H^-1 (mean):\n",Vsand)
print("Naive     H^-1 J_naive H^-1 (mean, ignores crossing):\n",Vnaive)
print("\n--- SEs (sqrt diag) ---")
print("MC       :",np.sqrt(np.diag(Vmc)))
print("Sandwich :",np.sqrt(np.diag(Vsand)),"  ratio->",np.sqrt(np.diag(Vsand)/np.diag(Vmc)))
print("Naive    :",np.sqrt(np.diag(Vnaive)),"  ratio->",np.sqrt(np.diag(Vnaive)/np.diag(Vmc)))
print("\nunderstatement of naive SE (%):",100*(1-np.sqrt(np.diag(Vnaive)/np.diag(Vmc))))
