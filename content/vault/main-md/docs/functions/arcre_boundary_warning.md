---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `boundary_warning`

```r
boundary_warning <- function(val, lo, hi, name) {
    if (abs(val - lo) < 1e-04) 
        warning(name, " optimum (", signif(val, 4), ") is at the LOWER boundary ", signif(lo, 4), ". Consider decreasing the lower bound.")
    if (abs(val - hi) < 1e-04) 
        warning(name, " optimum (", signif(val, 4), ") is at the UPPER boundary ", signif(hi, 4), ". Consider increasing the upper bound.")
}
```

%% begin persistent %%

%% end persistent %%

