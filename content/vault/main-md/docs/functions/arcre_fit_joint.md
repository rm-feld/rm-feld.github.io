---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `fit_joint`

```r
fit_joint <- function(y, X, row_id, col_id, Q_in = 9, Q_out = 11, start = NULL, verbose = TRUE) {
    p <- ncol(X)
    rule_in <- hermite_rule(Q_in)
    gh_out <- ghq01(Q_out)
    if (is.null(start)) {
        if (verbose) 
            cat("Starting values via two-stage ...\n")
        f1 <- fit_twostage(y, X, row_id, col_id, Q_in = Q_in, Q_out = Q_out, verbose = verbose)
        start <- c(f1$beta, log(f1$sigma_A), log(f1$sigma_B))
        if (verbose) 
            cat("\n")
    }
    neg_rc <- function(par) {
        b <- par[1:p]
        sA <- exp(par[p + 1])
        sB <- exp(par[p + 2])
        sig <- sqrt(sA^2 + sB^2)
        -(ell_grouped_vec(b, sig, sA/sig, y, X, row_id, rule_in, gh_out) + ell_grouped_vec(b, sig, sB/sig, 
            y, X, col_id, rule_in, gh_out))
    }
    if (verbose) 
        cat("Joint optimization ...\n")
    opt <- optim(start, neg_rc, method = "BFGS", control = list(maxit = 500, reltol = 1e-10))
    bhat <- opt$par[1:p]
    sA <- exp(opt$par[p + 1])
    sB <- exp(opt$par[p + 2])
    if (verbose) 
        cat("  beta =", round(bhat, 3), " sigma_A =", round(sA, 4), " sigma_B =", round(sB, 4), "\n")
    list(beta = bhat, sigma_A = sA, sigma_B = sB)
}
```

%% begin persistent %%

%% end persistent %%

