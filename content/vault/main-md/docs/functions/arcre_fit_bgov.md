---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `fit_bgov`

```r
fit_bgov <- function(y, X, row_id, col_id, R, C, Q_out, delta_lower, delta_upper, verbose) {
    p <- ncol(X)
    gh_out <- ghq01(Q_out)
    if (verbose) 
        cat("Stage 1: probit GLM for gamma ...\n")
    g0 <- if (p > 0) 
        rep(0, p)
    else numeric(0)
    nr <- newton_gamma(g0, y, X)
    ghat <- nr$gamma
    if (verbose) 
        cat("  gamma =", signif(ghat, 5), "\n")
    if (verbose) 
        cat("Stage 2a: Brent on delta_A (rows) ...\n")
    neg_row <- function(dA) {
        -probit_bgov_grouped_ell(dA, ghat, y, X, row_id, gh_out)
    }
    opt_r <- optimize(neg_row, c(delta_lower, delta_upper))
    dA_hat <- opt_r$minimum
    boundary_warning(dA_hat, delta_lower, delta_upper, "delta_A")
    if (verbose) 
        cat("  delta_A =", signif(dA_hat, 5), "\n")
    if (verbose) 
        cat("Stage 2b: Brent on delta_B (cols) ...\n")
    neg_col <- function(dB) {
        -probit_bgov_grouped_ell(dB, ghat, y, X, col_id, gh_out)
    }
    opt_c <- optimize(neg_col, c(delta_lower, delta_upper))
    dB_hat <- opt_c$minimum
    boundary_warning(dB_hat, delta_lower, delta_upper, "delta_B")
    if (verbose) 
        cat("  delta_B =", signif(dB_hat, 5), "\n")
    sol <- bgov_solve(dA_hat, dB_hat, ghat)
    if (verbose) 
        cat("  sigma_A =", signif(sol$sigma_A, 5), " sigma_B =", signif(sol$sigma_B, 5), "\n")
    list(beta = sol$beta, sigma_A = sol$sigma_A, sigma_B = sol$sigma_B, gamma = ghat, delta_A = dA_hat, 
        delta_B = dB_hat)
}
```

%% begin persistent %%

%% end persistent %%

