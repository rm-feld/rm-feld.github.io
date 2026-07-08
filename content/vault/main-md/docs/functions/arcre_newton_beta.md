---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `newton_beta`

```r
newton_beta <- function(beta0, sigma, y, X, family, rule = NULL, max_iter = 12, tol = 1e-10) {
    beta <- beta0
    p <- length(beta)
    if (p == 0) {
        ell <- switch(family, gaussian = gauss_ell_all(numeric(0), sigma^2, y, X), logit = logit_ell_all(numeric(0), 
            sigma, y, X), poisson = pois_ell_all(numeric(0), sigma, y, X, rule))
        return(list(beta = beta, ell = ell, niter = 0))
    }
    ell <- -Inf
    for (it in seq_len(max_iter)) {
        gh <- switch(family, gaussian = {
            g <- gauss_ell_all_grad_hess(beta, sigma^2, y, X)
            list(ell = g$ell, score = g$score_beta, hess = g$hess_beta)
        }, logit = {
            g <- logit_ell_all_grad_hess(beta, sigma, y, X)
            list(ell = g$ell, score = g$score_beta, hess = g$hess_beta)
        }, poisson = {
            g <- pois_ell_all_grad_hess(beta, sigma, y, X, rule)
            list(ell = g$ell, score = g$score_beta, hess = g$hess_beta)
        })
        ell <- gh$ell
        step <- tryCatch(solve(gh$hess, gh$score), error = function(e) {
            warning("newton_beta: solve failed at iter ", it)
            NULL
        })
        if (is.null(step)) 
            break
        beta <- beta - step
        if (max(abs(step)) < tol) 
            break
    }
    list(beta = beta, ell = ell, niter = it)
}
```

%% begin persistent %%

%% end persistent %%

