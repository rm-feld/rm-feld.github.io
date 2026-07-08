---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `bgov_solve`

```r
bgov_solve <- function(delta_A, delta_B, gamma) {
    dAdB <- delta_A * delta_B
    if (dAdB >= 1) {
        warning("bgov_solve: delta_A * delta_B >= 1 (", signif(dAdB, 4), "), clamping to 0.999")
        dAdB <- 0.999
    }
    sigA2 <- delta_A * (1 + delta_B)/(1 - dAdB)
    sigB2 <- delta_B * (1 + delta_A)/(1 - dAdB)
    sigma2 <- sigA2 + sigB2
    beta <- gamma * sqrt(1 + sigma2)
    list(sigma_A = sqrt(sigA2), sigma_B = sqrt(sigB2), beta = beta)
}
```

%% begin persistent %%

%% end persistent %%

