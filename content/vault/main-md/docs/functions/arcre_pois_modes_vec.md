---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `pois_modes_vec`

```r
pois_modes_vec <- function(y, eta, sigma, niter = 6) {
    yf <- pmax(y, 0.5)
    w <- (log(yf) - eta)/sigma
    for (iter in seq_len(niter)) {
        lam <- exp(eta + sigma * w)
        f <- sigma * y - sigma * lam - w
        fp <- -sigma^2 * lam - 1
        w <- w - f/fp
    }
    lam <- exp(eta + sigma * w)
    tau <- 1/sqrt(sigma^2 * lam + 1)
    list(what = w, tau = tau)
}
```

%% begin persistent %%

%% end persistent %%

