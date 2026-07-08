---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `generate_poisson_1rcj`

```r
generate_poisson_1rcj <- function(pat, beta, sigma_A, sigma_B, seed = 42) {
    set.seed(seed)
    N <- length(pat$row_id)
    p <- length(beta)
    a <- rnorm(pat$R, 0, sigma_A)
    b <- rnorm(pat$C, 0, sigma_B)
    i <- pat$row_id
    j <- pat$col_id
    xR <- qnorm((i - 1/2)/max(i))
    xC <- qnorm((j - 1/2)/max(j))
    xJ <- rnorm(N)
    X <- cbind(1, xR, xC, xJ)
    eta <- as.vector(X %*% beta) + a[pat$row_id] + b[pat$col_id]
    list(y = rpois(N, exp(eta)), X = X)
}
```

%% begin persistent %%

%% end persistent %%

