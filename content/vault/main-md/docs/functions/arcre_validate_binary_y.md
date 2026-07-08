---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `validate_binary_y`

```r
validate_binary_y <- function(y, family) {
    if (!all(y %in% c(-1L, 1L, -1, 1))) 
        stop("For ", family, " family, y must be in {-1, +1}. ", "Found: ", paste(sort(unique(y)), collapse = ", "))
}
```

%% begin persistent %%

%% end persistent %%

