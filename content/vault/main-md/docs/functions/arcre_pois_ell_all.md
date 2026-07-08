---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `pois_ell_all`

```r
pois_ell_all <- function(beta, sigma, y, X, rule, obs_wt = NULL) {
    eta <- as.vector(X %*% beta)
    yf <- as.double(y)
    hx <- rule$x
    hw <- rule$w
    Q <- length(hx)
    m <- pois_modes_vec(yf, eta, sigma)
    w_mat <- m$what + sqrt(2) * outer(m$tau, hx)
    lam_mat <- exp(eta + sigma * w_mat)
    agh_adj <- matrix(log(hw) + hx^2, nrow = length(yf), ncol = Q, byrow = TRUE)
    log_terms <- agh_adj + yf * log(pmax(lam_mat, 9.99999999999999e-301)) - lam_mat - lgamma(yf + 1) - 
        0.5 * w_mat^2 - 0.5 * log(2 * pi)
    max_lt <- apply(log_terms, 1, max)
    log_I <- max_lt + log(rowSums(exp(log_terms - max_lt))) + log(sqrt(2) * m$tau)
    if (!is.null(obs_wt)) 
        log_I <- log_I * obs_wt
    sum(log_I)
}
```

%% begin persistent %%

%% end persistent %%

