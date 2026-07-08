---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/sampling/samplers.R
---

# `bigrowcol_sampler`

```r
bigrowcol_sampler <- function(N = 10000, R = 1000, C = 1000, rowbig, colbig) {
    if (missing(rowbig)) 
        rowbig <- 1/R
    if (missing(colbig)) 
        colbig <- 1/C
    stopifnot(rowbig <= 1, colbig <= 1)
    nbb <- floor(N * rowbig * colbig)
    nbo <- floor(N * rowbig * (1 - colbig))
    nob <- floor(N * (1 - rowbig) * colbig)
    noo <- N - nbb - nbo - nob
    ivals <- c(rep(1, nbb), rep(1, nbo), sample(2:R, nob, replace = TRUE), sample(2:R, noo, replace = TRUE))
    jvals <- c(rep(1, nbb), sample(2:C, nbo, replace = TRUE), rep(1, nob), sample(2:C, noo, replace = TRUE))
    list(row_id = ivals, col_id = jvals, R = R, C = C)
}
```

%% begin persistent %%

%% end persistent %%

