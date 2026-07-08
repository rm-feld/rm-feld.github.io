---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `newton_gamma`

```r
newton_gamma <- function(gamma0, y, X, max_iter = 20, tol = 1e-10) {
    gamma <- gamma0
    p <- length(gamma)
    if (p == 0) 
        return(list(gamma = gamma, ell = probit_ell_all(numeric(0), y, X), niter = 0))
    ell <- -Inf
    for (it in seq_len(max_iter)) {
        g <- probit_ell_all_grad_hess(gamma, y, X)
        ell <- g$ell
        step <- tryCatch(solve(g$hess, g$score), error = function(e) NULL)
        if (is.null(step)) 
            break
        gamma <- gamma - step
        if (max(abs(step)) < tol) 
            break
    }
    list(gamma = gamma, ell = ell, niter = it)
}
```

%% begin persistent %%

%% end persistent %%

