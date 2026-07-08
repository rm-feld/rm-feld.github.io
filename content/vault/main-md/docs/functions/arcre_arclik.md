---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `arclik`

```r
arclik <- function(y, X, row_id, col_id, R, C, family = c("gaussian", "probit", "logit", "poisson"), 
    strategy = c("two_stage", "weighted_rc", "weighted_arc", "size_weighted", "bgov"), w_all = 1, w_row = 1, 
    w_col = 1, Q_all = 13, Q_in = 9, Q_out = 11, sigma_lower = NULL, sigma_upper = NULL, rho_eps = 0.01, 
    delta_lower = 1e-04, delta_upper = 25, logit_sigma0 = TRUE, verbose = TRUE, start = NULL) {
    family <- match.arg(family)
    strategy <- match.arg(strategy)
    N <- length(y)
    xv <- validate_X(X, N)
    X <- xv$X
    if (strategy == "bgov" && family != "probit") 
        stop("The bgov strategy is only available for the probit family. ", "It relies on the identity gamma = beta/sqrt(1+sigma^2) ", 
            "which holds only for the probit link.")
    if (family %in% c("probit", "logit")) 
        validate_binary_y(y, family)
    if (family == "poisson" && (any(y < 0) || any(y != floor(y)))) 
        stop("For poisson, y must be non-negative integers")
    result <- switch(strategy, two_stage = fit_two_stage(y, X, row_id, col_id, R, C, family, Q_all, Q_in, 
        Q_out, sigma_lower, sigma_upper, rho_eps, logit_sigma0, verbose), weighted_rc = fit_weighted_rc(y, 
        X, row_id, col_id, R, C, family, Q_all, Q_in, Q_out, sigma_lower, sigma_upper, rho_eps, logit_sigma0, 
        verbose), weighted_arc = fit_weighted_arc(y, X, row_id, col_id, R, C, family, w_all, w_row, w_col, 
        Q_all, Q_in, Q_out, logit_sigma0, start, verbose), size_weighted = fit_size_weighted(y, X, row_id, 
        col_id, R, C, family, Q_all, Q_in, Q_out, sigma_lower, sigma_upper, rho_eps, logit_sigma0, verbose), 
        bgov = fit_bgov(y, X, row_id, col_id, R, C, Q_out, delta_lower, delta_upper, verbose))
    result$family <- family
    result$strategy <- strategy
    result$N <- N
    result$R <- R
    result$C <- C
    if (family == "logit") 
        result$logit_sigma0 <- logit_sigma0
    class(result) <- "arclik"
    result
}
```

%% begin persistent %%

%% end persistent %%

