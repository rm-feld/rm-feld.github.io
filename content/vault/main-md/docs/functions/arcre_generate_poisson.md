---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `generate_poisson`

```r
generate_poisson <- function(pat, beta, sigma_A, sigma_B, seed = 42) {
    set.seed(seed)
    N <- length(pat$row_id)
    p <- length(beta)
    a <- rnorm(pat$R, 0, sigma_A)
    b <- rnorm(pat$C, 0, sigma_B)
    X <- cbind(1, matrix(rnorm(N * (p - 1)), N, p - 1))
    eta <- as.vector(X %*% beta) + a[pat$row_id] + b[pat$col_id]
    list(y = rpois(N, exp(eta)), X = X)
}
```

%% begin persistent %%

%% end persistent %%

