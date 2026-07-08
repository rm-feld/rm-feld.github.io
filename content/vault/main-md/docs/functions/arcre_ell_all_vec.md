---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `ell_all_vec`

```r
ell_all_vec <- function(beta, sigma, y, X, rule) {
    eta <- as.vector(X %*% beta)
    yf <- as.double(y)
    hx <- rule$x
    hw <- rule$w
    Q <- length(hx)
    m <- pois_modes_vec(yf, eta, sigma)
    w_mat <- m$what + sqrt(2) * outer(m$tau, hx)
    lam_mat <- exp(eta + sigma * w_mat)
    log_dpois <- yf * log(pmax(lam_mat, 9.99999999999999e-301)) - lam_mat - lgamma(yf + 1)
    log_dnorm <- -0.5 * w_mat^2 - 0.5 * log(2 * pi)
    base_wt <- log(hw) + hx^2
    log_terms <- sweep(log_dpois + log_dnorm, 2, base_wt, "+")
    max_lt <- apply(log_terms, 1, max)
    log_I <- max_lt + log(rowSums(exp(log_terms - max_lt)))
    log_I <- log_I + log(sqrt(2) * m$tau)
    sum(log_I)
}
```

%% begin persistent %%

%% end persistent %%

