---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `ell_grouped_vec`

```r
ell_grouped_vec <- function(beta, sigma, rho_shared, y, X, group_id, rule_in, gh_out) {
    eta <- as.vector(X %*% beta)
    s_sh <- sigma * rho_shared
    s_in <- sigma * sqrt(max(1 - rho_shared^2, 0))
    yf <- as.double(y)
    lgam <- lgamma(yf + 1)
    N <- length(y)
    Q_out <- length(gh_out$nodes)
    Q_in <- length(rule_in$x)
    hx_in <- rule_in$x
    hw_in <- rule_in$w
    base_wt <- log(hw_in) + hx_in^2
    groups <- sort(unique(group_id))
    n_groups <- length(groups)
    gidx <- match(group_id, groups)
    log_gs <- matrix(0, n_groups, Q_out)
    for (k in seq_len(Q_out)) {
        eta_sh <- eta + s_sh * gh_out$nodes[k]
        if (s_in > 1e-12) {
            m <- pois_modes_vec(yf, eta_sh, s_in)
            w_mat <- m$what + sqrt(2) * outer(m$tau, hx_in)
            lam_mat <- exp(eta_sh + s_in * w_mat)
            log_dp <- yf * log(pmax(lam_mat, 9.99999999999999e-301)) - lam_mat - lgam
            log_dn <- -0.5 * w_mat^2 - 0.5 * log(2 * pi)
            log_terms <- sweep(log_dp + log_dn, 2, base_wt, "+")
            max_lt <- apply(log_terms, 1, max)
            log_I <- max_lt + log(rowSums(exp(log_terms - max_lt)))
            log_I <- log_I + log(sqrt(2) * m$tau)
        }
        else {
            lam <- exp(eta_sh)
            log_I <- yf * log(pmax(lam, 9.99999999999999e-301)) - lam - lgam
        }
        log_gs[, k] <- tapply(log_I, gidx, sum)
    }
    log_w_out <- log(gh_out$weights)
    log_terms_out <- sweep(log_gs, 2, log_w_out, "+")
    max_out <- apply(log_terms_out, 1, max)
    log_integrals <- max_out + log(rowSums(exp(log_terms_out - max_out)))
    sum(log_integrals)
}
```

%% begin persistent %%

%% end persistent %%

