---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `pois_ell_all_grad_hess`

```r
pois_ell_all_grad_hess <- function(beta, sigma, y, X, rule) {
    eta <- as.vector(X %*% beta)
    yf <- as.double(y)
    p <- ncol(X)
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
    terms <- exp(log_terms - max_lt)
    rs <- rowSums(terms)
    post_wt <- terms/rs
    ell <- sum(max_lt + log(rs) + log(sqrt(2) * m$tau))
    E_lam <- rowSums(post_wt * lam_mat)
    V_lam <- rowSums(post_wt * lam_mat^2) - E_lam^2
    if (p > 0) {
        score <- as.vector(crossprod(X, yf - E_lam))
        obs_curv <- pmax(E_lam - V_lam, 1e-10)
        hess <- -crossprod(X * sqrt(obs_curv))
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

