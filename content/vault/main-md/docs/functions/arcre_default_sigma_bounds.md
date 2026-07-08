---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `default_sigma_bounds`

```r
default_sigma_bounds <- function(family, y, sigma_lower = NULL, sigma_upper = NULL) {
    if (is.null(sigma_lower)) 
        sigma_lower <- switch(family, gaussian = 0.05 * sd(y), probit = 0.01, logit = 0.01, poisson = 0.01)
    if (is.null(sigma_upper)) 
        sigma_upper <- switch(family, gaussian = 10 * sd(y), probit = 5, logit = 5, poisson = 3)
    sigma_lower <- max(sigma_lower, 1e-06)
    if (sigma_upper <= sigma_lower) 
        sigma_upper <- sigma_lower + 1
    c(sigma_lower, sigma_upper)
}
```

%% begin persistent %%

%% end persistent %%

