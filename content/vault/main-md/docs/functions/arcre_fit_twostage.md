---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `fit_twostage`

```r
fit_twostage <- function(y, X, row_id, col_id, Q_all = 13, Q_in = 9, Q_out = 11, sigma_start = 0.5, verbose = TRUE) {
    p <- ncol(X)
    rule_all <- hermite_rule(Q_all)
    rule_in <- hermite_rule(Q_in)
    gh_out <- ghq01(Q_out)
    fit0 <- glm.fit(X, y, family = poisson())
    beta0 <- fit0$coefficients
    neg_all <- function(par) {
        -ell_all_vec(par[1:p], exp(par[p + 1]), y, X, rule_all)
    }
    if (verbose) 
        cat("Stage 1: optimizing ell_all ...\n")
    opt1 <- optim(c(beta0, log(sigma_start)), neg_all, method = "BFGS", control = list(maxit = 500, reltol = 1e-10))
    bhat <- opt1$par[1:p]
    shat <- exp(opt1$par[p + 1])
    if (verbose) 
        cat("  beta =", round(bhat, 3), " sigma =", round(shat, 4), "\n")
    neg_rc <- function(rho_A) {
        rho_B <- sqrt(1 - rho_A^2)
        -(ell_grouped_vec(bhat, shat, rho_A, y, X, row_id, rule_in, gh_out) + ell_grouped_vec(bhat, shat, 
            rho_B, y, X, col_id, rule_in, gh_out))
    }
    if (verbose) 
        cat("Stage 2: optimizing ell_row + ell_col ...\n")
    opt2 <- optimize(neg_rc, c(0.02, 0.98))
    rhat <- opt2$minimum
    sA <- shat * rhat
    sB <- shat * sqrt(1 - rhat^2)
    if (verbose) 
        cat("  sigma_A =", round(sA, 4), " sigma_B =", round(sB, 4), "\n")
    list(beta = bhat, sigma_A = sA, sigma_B = sB, sigma = shat, rho_A = rhat)
}
```

%% begin persistent %%

%% end persistent %%

