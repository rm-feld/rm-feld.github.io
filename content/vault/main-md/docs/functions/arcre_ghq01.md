---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `ghq01`

```r
ghq01 <- function(n) {
    rule <- hermite_rule(n)
    list(nodes = rule$x * sqrt(2), weights = rule$w/sqrt(pi))
}
```

%% begin persistent %%

%% end persistent %%

