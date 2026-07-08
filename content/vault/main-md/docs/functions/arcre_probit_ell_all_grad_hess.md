---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `probit_ell_all_grad_hess`

```r
probit_ell_all_grad_hess <- function(gamma, y, X) {
    validate_binary_y(y, "probit")
    p <- ncol(X)
    N <- length(y)
    eta <- as.vector(X %*% gamma)
    z <- y * eta
    ratio <- y * dnorm(z)/pmax(pnorm(z), .xmin)
    ell <- sum(pnorm(z, log.p = TRUE))
    if (p > 0) {
        score <- as.vector(crossprod(X, ratio))
        r <- dnorm(z)/pmax(pnorm(z), .xmin)
        hw <- -(z * r + r^2)
        hess <- crossprod(X * sqrt(pmax(-hw, 1e-20)), X)
        hess <- -hess
    }
    else {
        score <- numeric(0)
        hess <- matrix(0, 0, 0)
    }
    list(ell = ell, score = score, hess = hess)
}
```

%% begin persistent %%

%% end persistent %%

