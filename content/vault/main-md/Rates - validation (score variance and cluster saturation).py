# Validation for: Rates of Convergence for the K-Crossed Composite Estimator
# (objection B3 of "Reviewer Objections and Next Steps (K-Crossed Probit Paper)")
#
# Part A: Var(L_all(gamma)/N) scales like sum_k eps_k (= 2/R for a complete
#         balanced RxR K=2 design), i.e. Var * R is roughly constant in R.
#         This is the variance side of the O_P(sqrt(sum_k eps_k)) rate for
#         gamma-hat: the rate is R_min^{-1/2}, NOT N^{-1/2} = R^{-1}.
# Part B: per-cluster information about tau^2 in the equicorrelated probit
#         SATURATES as cluster size n grows: SD(tau2-hat) ~ S^{-1/2} in the
#         number of clusters S, but stops improving in n. (Cluster-count rate.)

# RESULTS (2026-07-01, seed 11, reps A=300 / B=120, GH Q=20, bounded search):
#   Part A: Var(L/N):    R=10: 2.958e-3 | R=20: 9.053e-4 | R=40: 2.930e-4 | R=80: 1.422e-4
#           Var * R:     2.96e-2 -> 1.81e-2 -> 1.17e-2 -> 1.14e-2   (stabilizes; halving in R)
#           (small-R excess is the independent 1/N part; tail confirms Var ~ sum_k eps_k)
#   Part B: SD(tau2-hat):
#           S=100: n=2: 0.4743 | n=8: 0.1298 | n=32: 0.0796   (floor tau^2*sqrt(2/S)=0.0707)
#           S=400: n=2: 0.1715 | n=8: 0.0564 | n=32: 0.0438   (floor = 0.0354)
#           S x4 => SD ratio ~ 2 (1.8-2.8); n-gains saturate toward the S-only floor.

import numpy as np

rng = np.random.default_rng(11)

# ---------------- Part A: score/objective variance scaling ----------------
print("Part A: Var(L_all/N) * R  approx constant (complete RxR probit, K=2)")
gam = np.array([0.3, 0.8])
s1, s2 = 0.5, 0.5
sig = np.sqrt(1 + s1 + s2)
for R in (10, 20, 40, 80):
    N = R * R
    z = rng.standard_normal(N)          # fixed covariate per cell
    X = np.column_stack([np.ones(N), z])
    ii = np.repeat(np.arange(R), R)
    jj = np.tile(np.arange(R), R)
    reps = 400
    vals = np.empty(reps)
    for t in range(reps):
        a = np.sqrt(s1) * rng.standard_normal(R)
        b = np.sqrt(s2) * rng.standard_normal(R)
        e = rng.standard_normal(N)
        ystar = X @ (gam * sig) + a[ii] + b[jj] + e   # beta = gamma * sigma
        y = np.where(ystar > 0, 1.0, -1.0)
        from scipy.stats import norm
        vals[t] = np.mean(np.log(norm.cdf(y * (X @ gam))))
    v = vals.var(ddof=1)
    print(f"  R={R:3d} N={N:5d}  Var(L/N)={v:.3e}   Var*R={v * R:.3e}")

# ---------------- Part B: cluster-count rate & saturation ----------------
print("\nPart B: SD(tau2-hat), equicorrelated probit, GH-quadrature MLE")
from scipy.stats import norm
gh_x, gh_w = np.polynomial.hermite_e.hermegauss(40)  # N(0,1) weights
gh_w = gh_w / gh_w.sum()
tau2_true = 0.5
tau_grid = np.sqrt(np.linspace(0.01, 3.0, 90))


def fit_tau2(Y):
    # Y: (S, n) in {-1, 1}; profile loglik over tau grid
    best_ll, best_t2 = -np.inf, None
    for t in tau_grid:
        # cluster loglik: log sum_q w_q prod_t Phi(y_t * t * x_q)
        P = norm.cdf(Y[:, :, None] * (t * gh_x)[None, None, :])
        ll = np.log(np.maximum((np.exp(np.log(np.maximum(P, 1e-300)).sum(1))
                                * gh_w).sum(1), 1e-300)).sum()
        if ll > best_ll:
            best_ll, best_t2 = ll, t * t
    return best_t2


reps = 200
for S in (100, 400):
    row = []
    for n in (2, 8, 32):
        est = np.empty(reps)
        for r in range(reps):
            u = np.sqrt(tau2_true) * rng.standard_normal(S)
            e = rng.standard_normal((S, n))
            Y = np.where(u[:, None] + e > 0, 1.0, -1.0)
            est[r] = fit_tau2(Y)
        row.append(est.std(ddof=1))
    print(f"  S={S:4d}:  SD(tau2-hat) at n=2,8,32 -> "
          + ", ".join(f"{s:.4f}" for s in row))
print("  expect: SD halves when S x4 (cluster-count rate); "
      "improvement in n saturates")
