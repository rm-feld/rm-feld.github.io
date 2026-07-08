---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `validate_X`

```r
validate_X <- function(X, N) {
    if (is.null(X) || (length(X) == 1 && X == 0)) 
        return(list(X = matrix(0, N, 0), p = 0))
    if (length(X) == 1 && X == 1) 
        return(list(X = matrix(1, N, 1), p = 1))
    X <- as.matrix(X)
    if (nrow(X) != N) 
        stop("nrow(X) must equal length(y)")
    if (!any(apply(X, 2, function(col) all(col == col[1])))) 
        warning("X does not appear to include an intercept column.")
    list(X = X, p = ncol(X))
}
```

%% begin persistent %%

%% end persistent %%

