---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/data/tensor_synth.R
---

# `gen_sparse_tensor`

```r
gen_sparse_tensor <- function(N, kap1 = NULL, kap2 = NULL, kap3 = NULL, kaps = NULL, p = 4, Sigma = diag(p), 
    SigmaA = NULL, SigmaB = NULL, SigmaC = NULL, sigma = NULL, SigmaE = 1, beta = runif(p, -1, 1), beta0 = 0, 
    seed = NULL) {
    if (!is.null(seed)) 
        set.seed(seed)
    if (is.null(kaps)) {
        if (!is.null(kap1) && !is.null(kap2) && !is.null(kap3)) {
            kaps <- c(kap1, kap2, kap3)
        }
        else {
            stop("Provide either 'kaps' or all of 'kap1','kap2','kap3'")
        }
    }
    k <- length(kaps)
    if (k < 2) 
        stop("k (length of kaps) must be at least 2")
    if (is.null(sigma)) {
        if (!is.null(SigmaA) && !is.null(SigmaB) && !is.null(SigmaC) && k == 3) {
            sigma <- c(SigmaA, SigmaB, SigmaC)
        }
        else {
            sigma <- rep(0.1, k)
        }
    }
    if (length(sigma) != k) 
        stop("Length of 'sigma' must match length of 'kaps'")
    Ns_vec <- ceiling(N^kaps)
    if (k == 3) {
        fname <- c("i", "j", "k")
    }
    else {
        fname <- paste0("f", seq_len(k))
    }
    samp_dt <- function() {
        as.list(lapply(seq_len(k), function(m) sample(seq_len(Ns_vec[m]), N, replace = TRUE)))
    }
    support <- data.table::as.data.table(setNames(samp_dt(), fname))
    support <- unique(support)
    while (nrow(support) < N) {
        add <- data.table::as.data.table(setNames(samp_dt(), fname))
        support <- unique(data.table::rbindlist(list(support, add), use.names = TRUE))
    }
    if (nrow(support) > N) 
        support <- support[seq_len(N)]
    effects_list <- lapply(seq_len(k), function(m) rnorm(Ns_vec[m], 0, sigma[m]))
    X <- MASS::mvrnorm(n = N, mu = rep(0, p), Sigma = Sigma)
    colnames(X) <- paste0("x", seq_len(p))
    eps <- rnorm(N, 0, SigmaE)
    linear_pred <- as.vector(X %*% beta) + beta0
    for (m in seq_len(k)) {
        colm <- fname[m]
        linear_pred <- linear_pred + effects_list[[m]][support[[colm]]]
    }
    Z <- linear_pred + eps
    Y <- as.integer(Z > 0)
    out <- data.table::as.data.table(cbind(support, X, Z = Z, Y = Y))
    meta <- list(N_modes = k, Ns = Ns_vec, beta = beta, beta0 = beta0, Sigma = Sigma, sigma = sigma, 
        sigmaE = SigmaE, effects = effects_list)
    for (m in seq_len(k)) meta[[paste0("N", m)]] <- Ns_vec[m]
    attr(out, "meta") <- meta
    return(out)
}
```

%% begin persistent %%

%% end persistent %%

