import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from scipy.stats import norm, poisson
from scipy.integrate import quad
from scipy.special import gammaln
np.random.seed(0)

print("="*70)
print("(1) Gaussian-mixture convolution identity for symmetric binary links")
print("="*70)
# probit convolution identity: int Phi(s(eta+sigma u)) phi(u) du = Phi(s*eta/sqrt(1+s^2 sigma^2))
s, eta, sigma = 1.7, 0.6, 1.3
lhs = quad(lambda u: norm.cdf(s*(eta+sigma*u))*norm.pdf(u), -40,40)[0]
rhs = norm.cdf(s*eta/np.sqrt(1+s**2*sigma**2))
print(f"  probit convolution: LHS={lhs:.10f} RHS={rhs:.10f} diff={abs(lhs-rhs):.2e}")

# Fit a small Gaussian-scale mixture to logistic CDF Lambda(t)=1/(1+e^-t)
# Lambda(t) ~ sum p_r Phi(s_r t). Fit on a grid by NNLS-ish over fixed s grid.
from scipy.optimize import nnls
t = np.linspace(-8,8,2001)
Lam = 1/(1+np.exp(-t))
s_grid = np.linspace(0.4, 1.2, 40)   # scales s_r
# model 0.5 + sum p_r (Phi(s_r t)-0.5) ; enforce sum p_r =1 via columns (Phi(s t)-.5)
A = np.column_stack([norm.cdf(sr*t)-0.5 for sr in s_grid])
b = Lam-0.5
p,_ = nnls(A,b)
p = p/p.sum()
approx = 0.5 + A@p
maxerr = np.max(np.abs(approx-Lam))
keep = p>1e-4
print(f"  fitted {keep.sum()}-component scale mixture, sup|Lambda-approx| = {maxerr:.2e}")
print(f"  scales used: {np.round(s_grid[keep],3)}")
print(f"  weights    : {np.round(p[keep],3)}")

# marginal logistic-Gaussian: exact vs mixture-closed-form
def marg_exact(eta,sig):
    return quad(lambda u: (1/(1+np.exp(-(eta+sig*u))))*norm.pdf(u),-40,40)[0]
def marg_mix(eta,sig):
    return 0.5 + sum(pk*(norm.cdf(sr*eta/np.sqrt(1+sr**2*sig**2))-0.5) for pk,sr in zip(p[keep],s_grid[keep]))
for (e,sg) in [(0.5,1.0),(1.5,2.0),(-1.0,0.7)]:
    print(f"  marg logistic eta={e},sig={sg}: exact={marg_exact(e,sg):.6f} mix={marg_mix(e,sg):.6f} diff={abs(marg_exact(e,sg)-marg_mix(e,sg)):.2e}")

print()
print("="*70)
print("(2) Probit slice rho reparameterization + Mobius inversion, K=3, A<=2")
print("="*70)
# variance components: singles + pairs.  sigma^2_E + sum sigma^2_K
sE=1.0
ss={frozenset([1]):0.7, frozenset([2]):0.4, frozenset([3]):0.9,
    frozenset([1,2]):0.3, frozenset([1,3]):0.2, frozenset([2,3]):0.5}
A=list(ss.keys())
allscale = sE + sum(ss.values())
# tilde_rho_K = sigma^2_K/allscale ; rho_K = sigsum_K/allscale (cumulative over subsets in A)
def sigsum(K):
    return sum(ss[Kp] for Kp in A if Kp.issubset(K))
rho={K: sigsum(K)/allscale for K in A}
trho={K: ss[K]/allscale for K in A}
# Mobius: trho_K = sum_{K'⊆K,K'∈A} (-1)^{|K|-|K'|} rho_K'
def mobius(K):
    tot=0.0
    for Kp in A:
        if Kp.issubset(K):
            tot += (-1)**(len(K)-len(Kp))*rho[Kp]
    return tot
mob_ok=max(abs(mobius(K)-trho[K]) for K in A)
print(f"  max |Mobius(rho)_K - tilde_rho_K| = {mob_ok:.2e}")
# recover allscale from 1 - sum tilde_rho = sE/allscale
rec_allscale = sE/(1-sum(trho.values()))
print(f"  allscale true={allscale:.4f} recovered={rec_allscale:.4f} diff={abs(allscale-rec_allscale):.2e}")
# recover each sigma^2_K
rec_ok=max(abs(trho[K]*allscale-ss[K]) for K in A)
print(f"  max |recovered sigma^2_K - true| = {rec_ok:.2e}")
# check the A<=2 closed form: sum rho - (K-1) sum_singles rho = 1 - sE/allscale
singles=[K for K in A if len(K)==1]
lhs2=sum(rho.values())-(3-1)*sum(rho[K] for K in singles)
rhs2=1-sE/allscale
print(f"  A<=2 identity: LHS={lhs2:.4f} RHS={rhs2:.4f} diff={abs(lhs2-rhs2):.2e}")

print()
print("="*70)
print("(3) Poisson-lognormal marginal: MGF mean shift + AGHQ accuracy")
print("="*70)
# E[Y]=exp(eta+ sigma^2/2) when log-rate = eta + N(0,sigma^2)
eta,sig=0.3,0.8
N=4_000_000
w=np.random.randn(N)*sig
lam=np.exp(eta+w)
y=np.random.poisson(lam)
print(f"  E[Y] sim={y.mean():.4f} theory=exp(eta+sig^2/2)={np.exp(eta+sig**2/2):.4f}")
print(f"  Var[Y] sim={y.var():.4f} theory={np.exp(eta+sig**2/2)+ (np.exp(sig**2)-1)*np.exp(2*eta+sig**2):.4f}")

# marginal P(Y=k): exact quad vs adaptive GHQ centered at posterior mode
def logpmf_exact(k,eta,sig):
    val=quad(lambda u: np.exp(k*(eta+sig*u)-np.exp(eta+sig*u)-gammaln(k+1))*norm.pdf(u),-40,40)[0]
    return np.log(val)
def logpmf_aghq(k,eta,sig,Q=15):
    # posterior mode of f(w)= k(eta+sig w)-exp(eta+sig w) - w^2/2
    w=(np.log(max(k,0.5))-eta)/sig
    for _ in range(50):
        lam=np.exp(eta+sig*w); f=sig*k-sig*lam-w; fp=-sig**2*lam-1; w-=f/fp
    tau=1/np.sqrt(sig**2*np.exp(eta+sig*w)+1)
    h,gw=np.polynomial.hermite.hermgauss(Q)  # physicists' (weight e^-x^2)
    wq=w+np.sqrt(2)*tau*h
    lam=np.exp(eta+sig*wq)
    logterms=np.log(gw)+h**2 + k*np.log(lam)-lam-gammaln(k+1)-0.5*wq**2-0.5*np.log(2*np.pi)
    m=logterms.max()
    return m+np.log(np.sum(np.exp(logterms-m)))+np.log(np.sqrt(2)*tau)
for k in [0,1,3,8,20]:
    ex=logpmf_exact(k,eta,sig); ag=logpmf_aghq(k,eta,sig)
    print(f"  logP(Y={k:2d}): exact={ex:.8f} AGHQ(Q=15)={ag:.8f} diff={abs(ex-ag):.2e}")

print()
print("="*70)
print("(4) Identifiability signal: excess kurtosis of latent error")
print("="*70)
# probit latent = N(0,1): kappa4=0 (sigma^2 not separately identified from marginal)
# logistic latent: var=pi^2/3, excess kurtosis = 6/5
print(f"  probit  latent excess kurtosis = 0        -> sigma^2 NOT identified from marginal (only gamma)")
print(f"  logistic latent excess kurtosis = 6/5 = {6/5}  -> (beta,sigma^2) jointly identified (kappa4!=0)")
# numeric check logistic kurtosis
xs=np.linspace(-40,40,400001); import numpy as _np
pdf=_np.exp(-xs)/(1+_np.exp(-xs))**2
pdf/=_np.trapz(pdf,xs)
var=_np.trapz(xs**2*pdf,xs); m4=_np.trapz(xs**4*pdf,xs)
print(f"  numeric logistic: var={var:.4f} (pi^2/3={np.pi**2/3:.4f}), excess kurt={m4/var**2-3:.4f}")
