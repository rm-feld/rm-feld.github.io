---
modified: 2025-11-18T19:11:02-08:00
created: 2025-11-18T16:28:38-08:00
---

# V1 (only `rho = 0.1` stabilizing)
```r
run <- random_slopes_run_procedure(
  sim_fun  = gen_sparse_tensor_random_slopes,
  sim_args = list(
    N = 100000,
    kaps = c(0.6,0.6),
    p = 4,
    pA = 2,
    pB = 2,
    Sigma_A = diag(2)*0.5,
    Sigma_B = diag(2)*0.7,
    beta = c(0.5, -0.3, 0.2, 0.0),
    beta0 = 0.5
  ),
  niter = 100,
  arcbin_nq = 5,
  min_obs_per_group = 5,
  arcbin_niter = 10,
  verbose = TRUE
)
```

![[Pasted image 20251118162808.png]]



```r
run <- random_slopes_run_procedure(
  sim_fun  = gen_sparse_tensor_random_slopes,
  sim_args = list(
    N = 10000,
    kaps = c(0.6,0.6),
    p = 4,
    pA = 2,
    pB = 2,
    Sigma_A = diag(2)*0.5,
    Sigma_B = diag(2)*0.7,
    beta = c(0.5, -0.3, 0.2, 0.0),
    beta0 = 0.5
  ),
  niter = 250,
  arcbin_nq = 5,
  min_obs_per_group = 2,
  arcbin_niter = 10,
  verbose = TRUE
)

# Step-0 results:
run$history[[1]]$beta_full
run$history[[1]]$Sigma_A
run$history[[1]]$Sigma_B

# Iteration t:
run$history[[3]]$beta_full
run$history[[3]]$Sigma_A
run$history[[3]]$Sigma_B

# Final:
run$final$beta_full
run$final$Sigma_A
run$final$Sigma_B

plot_beta_mse <- function(run, beta_true, include_intercept = TRUE, 
                          main = "β MSE Across Iterations",
                          bg_col = "white") {

  oldpar <- par(no.readonly = TRUE)
  on.exit(par(oldpar))

  par(bg = bg_col)

  history <- run$history
  nsteps  <- length(history)

  beta_mat <- sapply(history, function(h) h$beta_full)
  beta_mat <- t(beta_mat)

  if (!include_intercept) {
    beta_true_use <- beta_true[-1]
    beta_mat_use  <- beta_mat[, -1, drop = FALSE]
  } else {
    beta_true_use <- beta_true
    beta_mat_use  <- beta_mat
  }

  mse <- rowMeans((beta_mat_use - rep(1, nsteps) %*% t(beta_true_use))^2)

  plot(
    x = 0:(nsteps-1),
    y = log(mse),
    type = "b",
    xlab = "Iteration",
    ylab = if (include_intercept) "log MSE(β including intercept)"
           else "log MSE(β slopes only)",
    main = main
  )
}

```
![[Pasted image 20251118164206.png]]

```r
run <- random_slopes_run_procedure(
  sim_fun  = gen_sparse_tensor_random_slopes,
  sim_args = list(
    N = 10000,
    kaps = c(0.6,0.6),
    p = 4,
    pA = 2,
    pB = 2,
    Sigma_A = diag(2)*0.5,
    Sigma_B = diag(2)*0.7,
    beta = c(0.5, -0.3, 0.2, 1.0),
    beta0 = 0.5
  ),
  niter = 50,
  arcbin_nq = 5,
  min_obs_per_group = 3,
  arcbin_niter = 10,
  verbose = TRUE
)
```

![[Pasted image 20251118174430.png]]

![[Pasted image 20251118174522.png]]



