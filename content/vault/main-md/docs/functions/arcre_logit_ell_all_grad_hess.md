---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `logit_ell_all_grad_hess`

```r
logit_ell_all_grad_hess <- function(beta, sigma, y, X) {
    validate_binary_y(y, "logit")
    eta <- as.vector(X %*% beta)
    p <- ncol(X)
    sigma2 <- sigma^2
    A <- dA <- d2A <- numeric(length(y))
    for (k in seq_len(.ms_K)) {
        sk <- .ms_s[k]
        sk2 <- sk^2
        den <- sqrt(1 + sigma2 * sk2)
        z <- y * eta * sk/den
        phi_z <- dnorm(z)
        A <- A + .ms_p[k] * pnorm(z)
        dA <- dA + .ms_p[k] * y * sk/den * phi_z
        d2A <- d2A + .ms_p[k] * sk2/(1 + sigma2 * sk2) * (-z) * phi_z
    }
    ell <- sum(log(pmax(A, .xmin)))
    ratio1 <- dA/pmax(A, .xmin)
    if (p > 0) {
        score <- as.vector(crossprod(X, ratio1))
        hw <- d2A/pmax(A, .xmin) - ratio1^2
        hess <- -crossprod(X * sqrt(pmax(-hw, 1e-20)), X)
    }
    else {
        score <- numeric(0)
        hess <- matrix(0, 0, 0)
    }
    list(ell = ell, score_beta = score, hess_beta = hess)
}
```

%% begin persistent %%

%% end persistent %%

