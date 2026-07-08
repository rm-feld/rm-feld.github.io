---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `gauss_ell_all_grad_hess`

```r
gauss_ell_all_grad_hess <- function(beta, nu2, y, X) {
    p <- ncol(X)
    N <- length(y)
    r <- y - as.vector(X %*% beta)
    ell <- sum(dnorm(r, 0, sqrt(nu2), log = TRUE))
    if (p > 0) {
        score_beta <- as.vector((1/nu2) * crossprod(X, r))
        hess_beta <- -(1/nu2) * crossprod(X)
    }
    else {
        score_beta <- numeric(0)
        hess_beta <- matrix(0, 0, 0)
    }
    list(ell = ell, score_beta = score_beta, hess_beta = hess_beta)
}
```

%% begin persistent %%

%% end persistent %%

