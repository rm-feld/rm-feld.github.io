---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/families/poisson_raw.R
---

# `demo_two`

```r
demo_two <- function() {
    beta_true <- c(1, 2, 3, 4)
    sigA_true <- 0.4
    sigB_true <- 0.3
    sig_true <- sqrt(sigA_true^2 + sigB_true^2)
    cat("True: beta =", beta_true, " sigA =", sigA_true, " sigB =", sigB_true, " sigma =", round(sig_true, 
        4), "\n\n")
    Ns <- c(100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 1e+05, 2e+05)
    cat(sprintf("%8s  %7s  %5s  %7s  %7s  %7s  %7s  %7s  %7s  %7s %7s %7s\n", "N", "R", "C", "b1", "bR", 
        "bC", "bJ", "sA", "sB", "sig", "sec", "usec/N"))
    cat(strrep("-", 105), "\n")
    for (N in Ns) {
        pat <- simcross_pattern(N)
        dat <- generate_poisson_1rcj(pat, beta_true, sigA_true, sigB_true)
        t0 <- proc.time()
        fit <- fit_twostage(dat$y, dat$X, pat$row_id, pat$col_id, verbose = FALSE)
        elapsed <- (proc.time() - t0)[3]
        cat(sprintf("%8d  %7d  %5d  %7.3f  %7.3f  %7.3f  %7.3f  %7.3f  %7.3f %7.3f %7.1f  %8.1f\n", N, 
            pat$R, pat$C, fit$beta[1], fit$beta[2], fit$beta[3], fit$beta[4], fit$sigma_A, fit$sigma_B, 
            fit$sigma, elapsed, elapsed/N * 1e+06))
    }
    cat(sprintf("%8s  %7s  %5s  %7.3f  %7.3f  %7.3f  %7.3f  %7.3f  %7.3f  %7.3f\n", "True", "", "", beta_true[1], 
        beta_true[2], fit$beta[3], fit$beta[4], sigA_true, sigB_true, sig_true))
}
```

%% begin persistent %%

%% end persistent %%

