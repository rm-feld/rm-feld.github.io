---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `probit_ell_grouped`

```r
probit_ell_grouped <- function(beta, sigma, rho_shared, y, X, group_id, gh_out, obs_wt = NULL) {
    validate_binary_y(y, "probit")
    eta <- as.vector(X %*% beta)
    s_sh <- sigma * rho_shared
    s_in <- sigma * safe_sqrt(1 - rho_shared^2)
    denom_in <- sqrt(1 + s_in^2)
    Q_out <- length(gh_out$nodes)
    total <- 0
    for (g in unique(group_id)) {
        sel <- which(group_id == g)
        y_g <- y[sel]
        eta_g <- eta[sel]
        wt <- if (!is.null(obs_wt)) 
            mean(obs_wt[sel])
        else 1
        log_prod <- numeric(Q_out)
        for (q in seq_len(Q_out)) {
            arg <- y_g * (eta_g + s_sh * gh_out$nodes[q])/denom_in
            log_prod[q] <- sum(pnorm(arg, log.p = TRUE))
        }
        total <- total + wt * lse(log(gh_out$weights) + log_prod)
    }
    total
}
```

%% begin persistent %%

%% end persistent %%

