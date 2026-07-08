---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `print.arclik`

```r
print.arclik <- function(x, digits = 5, ...) {
    cat("arclik:", x$family, "/", x$strategy, "\n")
    cat("N=", x$N, " R=", x$R, " C=", x$C, "\n")
    if (length(x$beta) > 0) 
        cat("beta =", signif(x$beta, digits), "\n")
    if (!is.null(x$gamma)) 
        cat("gamma =", signif(x$gamma, digits), "\n")
    cat("sigma_A =", signif(x$sigma_A, digits), " sigma_B =", signif(x$sigma_B, digits), "\n")
    if (!is.null(x$delta_A)) 
        cat("delta_A =", signif(x$delta_A, digits), " delta_B =", signif(x$delta_B, digits), "\n")
    if (!is.null(x$sigma)) 
        cat("sigma   =", signif(x$sigma, digits), "\n")
    invisible(x)
}
```

%% begin persistent %%

%% end persistent %%

