---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `lse`

```r
lse <- function(x) {
    m <- max(x)
    m + log(sum(exp(x - m)))
}
```

%% begin persistent %%

%% end persistent %%

