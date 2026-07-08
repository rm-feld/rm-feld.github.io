---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
# --- user fields ---
status: reviewed
related: "[[arcre_gauss_ell_grouped]]"
---

# `gauss_ell_all`

```r
gauss_ell_all <- function(beta, nu2, y, X, obs_wt = NULL) {
    r <- y - as.vector(X %*% beta)
    ll <- dnorm(r, 0, sqrt(nu2), log = TRUE)
    if (!is.null(obs_wt)) 
        ll <- ll * obs_wt
    sum(ll)
}
```

%% begin persistent %%
Used as the all-pairs term in the Gaussian composite likelihood.
See also: gauss_ell_grouped for the grouped variant.
%% end persistent %%

