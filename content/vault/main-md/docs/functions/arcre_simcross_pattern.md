---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `simcross_pattern`

```r
simcross_pattern <- function(N, rho = 0.88, kappa = 0.57, seed = 20260114) {
    set.seed(seed)
    R <- ceiling(N^rho)
    C <- ceiling(N^kappa)
    colsizes <- as.vector(rmultinom(1, N, rep(1/C, C)))
    stopifnot(max(colsizes) <= R)
    row_id <- integer(N)
    col_id <- integer(N)
    ind <- 1L
    for (j in seq_len(C)) {
        rows_j <- sample.int(R, colsizes[j])
        n_j <- colsizes[j]
        row_id[ind:(ind + n_j - 1)] <- rows_j
        col_id[ind:(ind + n_j - 1)] <- j
        ind <- ind + n_j
    }
    ord <- order(row_id)
    list(row_id = row_id[ord], col_id = col_id[ord], R = R, C = C)
}
```

%% begin persistent %%

%% end persistent %%

