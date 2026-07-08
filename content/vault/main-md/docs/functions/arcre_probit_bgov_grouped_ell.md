---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `probit_bgov_grouped_ell`

```r
probit_bgov_grouped_ell <- function(delta, gamma, y, X, group_id, gh_out) {
    validate_binary_y(y, "probit")
    eta_base <- as.vector(X %*% gamma) * sqrt(1 + delta)
    sd_sh <- sqrt(delta)
    Q <- length(gh_out$nodes)
    total <- 0
    for (g in unique(group_id)) {
        sel <- which(group_id == g)
        y_g <- y[sel]
        eta_g <- eta_base[sel]
        log_prod <- numeric(Q)
        for (q in seq_len(Q)) {
            arg <- y_g * (eta_g + sd_sh * gh_out$nodes[q])
            log_prod[q] <- sum(pnorm(arg, log.p = TRUE))
        }
        total <- total + lse(log(gh_out$weights) + log_prod)
    }
    total
}
```

%% begin persistent %%

%% end persistent %%

