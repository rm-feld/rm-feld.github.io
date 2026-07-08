---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `logit_ell_all`

```r
logit_ell_all <- function(beta, sigma, y, X, obs_wt = NULL) {
    validate_binary_y(y, "logit")
    eta <- as.vector(X %*% beta)
    sigma2 <- sigma^2
    A <- numeric(length(y))
    for (k in seq_len(.ms_K)) {
        sk <- .ms_s[k]
        sk2 <- sk^2
        A <- A + .ms_p[k] * pnorm(y * eta * sk/sqrt(1 + sigma2 * sk2))
    }
    ll <- log(pmax(A, .xmin))
    if (!is.null(obs_wt)) 
        ll <- ll * obs_wt
    sum(ll)
}
```

%% begin persistent %%

%% end persistent %%

