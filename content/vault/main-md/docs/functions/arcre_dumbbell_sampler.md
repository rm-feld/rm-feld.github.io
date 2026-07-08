---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/sampling/samplers.R
---

# `dumbbell_sampler`

```r
dumbbell_sampler <- function(N = 10000, R = 1000, C = 1000, overlap = 2) {
    R_mid <- floor(R/2)
    C_mid <- floor(C/2)
    N_per_block <- floor((N - overlap)/2)
    row_id <- c(sample(1:R_mid, N_per_block, replace = TRUE), sample((R_mid + 1):R, N_per_block, replace = TRUE), 
        sample(1:R_mid, overlap, replace = TRUE))
    col_id <- c(sample(1:C_mid, N_per_block, replace = TRUE), sample((C_mid + 1):C, N_per_block, replace = TRUE), 
        sample((C_mid + 1):C, overlap, replace = TRUE))
    ord <- sample(seq_along(row_id))
    list(row_id = row_id[ord], col_id = col_id[ord], R = R, C = C)
}
```

%% begin persistent %%

%% end persistent %%

