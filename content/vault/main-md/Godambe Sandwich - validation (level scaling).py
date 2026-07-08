import numpy as np
from scipy.stats import norm
phi=norm.pdf; Phi=norm.cdf
def Rm(t): return phi(t)/np.clip(Phi(t),1e-12,None)

def run(Rlev,D,seed=3):
    rng=np.random.default_rng(seed)
    R1=R2=Rlev
    r,c=np.meshgrid(np.arange(R1),np.arange(R2),indexing='ij'); r=r.ravel(); c=c.ravel(); N=r.size
    X=np.column_stack([np.ones(N),rng.normal(size=N)]); p=2
    beta=np.array([0.3,0.8]); sa2,sb2=0.6,0.4; sig=np.sqrt(1+sa2+sb2); g0=beta/sig
    def gen():
        a=rng.normal(0,np.sqrt(sa2),R1); b=rng.normal(0,np.sqrt(sb2),R2)
        return ((X@beta+a[r]+b[c]+rng.normal(size=N))>0).astype(float)
    def fit(y):
        ty=2*y-1; g=np.zeros(p)
        for _ in range(60):
            t=ty*(X@g); s=ty*phi(X@g)/np.clip(Phi(t),1e-12,None)
            w=Rm(t)*(t+Rm(t)); H=(X*w[:,None]).T@X
            st=np.linalg.solve(H,X.T@s); g=g+st
            if np.max(np.abs(st))<1e-11: break
        return g
    G=np.zeros((D,p)); Vs=np.zeros((D,p,p))
    for d in range(D):
        y=gen(); g=fit(y); G[d]=g
        ty=2*y-1; t=ty*(X@g); s=ty*phi(X@g)/np.clip(Phi(t),1e-12,None)
        w=Rm(t)*(t+Rm(t)); H=(X*w[:,None]).T@X; sx=s[:,None]*X
        Srow=np.zeros((R1,p)); np.add.at(Srow,r,sx); Scol=np.zeros((R2,p)); np.add.at(Scol,c,sx)
        J=Srow.T@Srow+Scol.T@Scol-sx.T@sx; Hi=np.linalg.inv(H); Vs[d]=Hi@J@Hi
    Vmc=np.cov(G.T); Vsand=Vs.mean(0)
    return np.sqrt(np.diag(Vsand)/np.diag(Vmc))
for Rlev,D in [(15,3000),(30,2000),(60,1200)]:
    ratio=run(Rlev,D)
    print(f"R1=R2={Rlev:3d} (N={Rlev*Rlev:5d}): sandwich/MC SE ratio = {np.round(ratio,3)}  (->1 confirms formula)")
