---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `pois_ell_grouped`

```r
pois_ell_grouped <- function(beta, sigma, rho_shared, y, X, group_id, rule_in, gh_out, obs_wt = NULL) {
    eta <- as.vector(X %*% beta)
    s_sh <- sigma * rho_shared
    s_in <- sigma * safe_sqrt(1 - rho_shared^2)
    yf <- as.double(y)
    lgam <- lgamma(yf + 1)
    Q_out <- length(gh_out$nodes)
    Q_in <- length(rule_in$x)
    hx_in <- rule_in$x
    hw_in <- rule_in$w
    agh_adj_vec <- log(hw_in) + hx_in^2
    groups <- sort(unique(group_id))
    ng <- length(groups)
    gidx <- match(group_id, groups)
    log_gs <- matrix(0, ng, Q_out)
    for (k in seq_len(Q_out)) {
        eta_sh <- eta + s_sh * gh_out$nodes[k]
        if (s_in > 1e-12) {
            m <- pois_modes_vec(yf, eta_sh, s_in)
            w_mat <- m$what + sqrt(2) * outer(m$tau, hx_in)
            lam_mat <- exp(eta_sh + s_in * w_mat)
            agh_adj <- matrix(agh_adj_vec, nrow = length(yf), ncol = Q_in, byrow = TRUE)
            lt <- agh_adj + yf * log(pmax(lam_mat, 9.99999999999999e-301)) - lam_mat - lgam - 0.5 * w_mat^2 - 
                0.5 * log(2 * pi)
            mx <- apply(lt, 1, max)
            log_I <- mx + log(rowSums(exp(lt - mx))) + log(sqrt(2) * m$tau)
        }
        else {
            lam <- exp(eta_sh)
            log_I <- yf * log(pmax(lam, 9.99999999999999e-301)) - lam - lgam
        }
        if (!is.null(obs_wt)) 
            log_I <- log_I * obs_wt
        log_gs[, k] <- tapply(log_I, gidx, sum)
    }
    lt_out <- log_gs + matrix(log(gh_out$weights), ng, Q_out, byrow = TRUE)
    mx_out <- apply(lt_out, 1, max)
    sum(mx_out + log(rowSums(exp(lt_out - mx_out))))
}
```

%% begin persistent %%

%% end persistent %%

