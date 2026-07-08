---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `gauss_ell_grouped`

```r
gauss_ell_grouped <- function(beta, sig_shared, tau_resid, y, X, group_id, obs_wt = NULL) {
    r <- y - as.vector(X %*% beta)
    tau2 <- tau_resid^2
    sig2 <- sig_shared^2
    total <- 0
    for (g in unique(group_id)) {
        sel <- which(group_id == g)
        n_g <- length(sel)
        r_g <- r[sel]
        S_g <- sum(r_g)
        Q_g <- sum(r_g^2)
        wt <- if (!is.null(obs_wt)) 
            mean(obs_wt[sel])
        else 1
        denom <- n_g * sig2 + tau2
        ll_g <- -n_g/2 * log(2 * pi * tau2) - 0.5 * log(denom/tau2) - Q_g/(2 * tau2) + sig2 * S_g^2/(2 * 
            tau2 * denom)
        total <- total + wt * ll_g
    }
    total
}
```

%% begin persistent %%

%% end persistent %%

