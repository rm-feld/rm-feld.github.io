---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `probit_ell_all`

```r
probit_ell_all <- function(gamma, y, X) {
    validate_binary_y(y, "probit")
    eta <- as.vector(X %*% gamma)
    sum(pnorm(y * eta, log.p = TRUE))
}
```

%% begin persistent %%

%% end persistent %%

