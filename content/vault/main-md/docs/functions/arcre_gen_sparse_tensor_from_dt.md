---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/data/tensor_synth.R
---

# `gen_sparse_tensor_from_dt`

```r
gen_sparse_tensor_from_dt <- function(cross_dt, p = 4, Sigma = diag(p), sigma_vec = c(0.1, 0.1, 0.1), 
    SigmaE = 1, beta = runif(p, -1, 1), beta0 = 0, seed = NULL) {
    if (!is.null(seed)) 
        set.seed(seed)
    N <- nrow(cross_dt)
    if (N == 0) 
        stop("Empty data.table input.")
    cat_cols <- seq_len(ncol(cross_dt))
    Ns_vec <- integer(length(cat_cols))
    effects_list <- vector("list", length(cat_cols))
    for (m in seq_along(cat_cols)) {
        cross_dt[[m]] <- as.factor(cross_dt[[m]])
        Ns_vec[m] <- length(levels(cross_dt[[m]]))
        effects_list[[m]] <- rnorm(Ns_vec[m], 0, sigma_vec[m])
        cross_dt[[m]] <- as.integer(cross_dt[[m]])
    }
    X <- MASS::mvrnorm(n = N, mu = rep(0, p), Sigma = Sigma)
    colnames(X) <- paste0("x", seq_len(p))
    linear_pred <- as.vector(X %*% beta) + beta0
    for (m in seq_along(cat_cols)) {
        linear_pred <- linear_pred + effects_list[[m]][cross_dt[[m]]]
    }
    eps <- rnorm(N, 0, SigmaE)
    Z <- linear_pred + eps
    Y <- as.integer(Z > 0)
    out <- data.table::as.data.table(cbind(cross_dt, X, Z = Z, Y = Y))
    names(out)[c(1, 2, 3)] <- c("i", "j", "k")
    meta <- list(N_modes = length(cat_cols), Ns = Ns_vec, beta = beta, beta0 = beta0, Sigma = Sigma, 
        sigma = sigma_vec, SigmaE = SigmaE, effects = effects_list)
    attr(out, "meta") <- meta
    return(out)
}
```

%% begin persistent %%

%% end persistent %%

