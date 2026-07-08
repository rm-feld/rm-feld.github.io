---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `fit_weighted_arc`

```r
fit_weighted_arc <- function(y, X, row_id, col_id, R, C, family, w_all, w_row, w_col, Q_all, Q_in, Q_out, 
    logit_sigma0, start, verbose) {
    p <- ncol(X)
    rule_all <- if (family == "poisson") 
        gaussHermiteData(Q_all)
    else NULL
    rule_in <- if (family == "poisson") 
        gaussHermiteData(Q_in)
    else NULL
    gh_out <- ghq01(Q_out)
    if (is.null(start)) {
        f0 <- fit_two_stage(y, X, row_id, col_id, R, C, family, Q_all, Q_in, Q_out, NULL, NULL, 0.01, 
            logit_sigma0, FALSE)
        start <- c(f0$beta, log(f0$sigma_A), log(f0$sigma_B))
    }
    neg_warc <- function(par) {
        b <- par[seq_len(p)]
        sA <- exp(par[p + 1])
        sB <- exp(par[p + 2])
        sig <- sqrt(sA^2 + sB^2)
        rA <- sA/sig
        val <- 0
        if (w_all > 0) {
            e_all <- switch(family, gaussian = gauss_ell_all(b, sig^2, y, X), probit = {
                gam <- b/sqrt(1 + sig^2)
                probit_ell_all(gam, y, X)
            }, logit = logit_ell_all(b, sig, y, X), poisson = pois_ell_all(b, sig, y, X, rule_all))
            val <- val + w_all * e_all
        }
        if (w_row > 0) 
            val <- val + w_row * eval_row_lik(b, sig, rA, y, X, row_id, family, rule_in, gh_out)
        if (w_col > 0) 
            val <- val + w_col * eval_col_lik(b, sig, rA, y, X, col_id, family, rule_in, gh_out)
        -val
    }
    if (verbose) 
        cat("Optimising weighted ARC ...\n")
    opt <- optim(start, neg_warc, method = "BFGS", control = list(maxit = 500, reltol = 1e-10))
    if (opt$convergence != 0) 
        warning("weighted_arc optim: code ", opt$convergence, " (", opt$message, ")")
    bhat <- opt$par[seq_len(p)]
    sA <- exp(opt$par[p + 1])
    sB <- exp(opt$par[p + 2])
    if (verbose) 
        cat("  sigma_A =", signif(sA, 5), " sigma_B =", signif(sB, 5), "\n")
    list(beta = bhat, sigma_A = sA, sigma_B = sB)
}
```

%% begin persistent %%

%% end persistent %%

