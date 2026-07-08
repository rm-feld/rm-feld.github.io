---
modified: 2026-01-20T11:00:33-08:00
created: 2026-01-19T22:36:05-08:00
---
runtime arou
# code 
otherwise same hyperparameters as [[EK1 - Sigma Scale Tolerance]]
```r
sigma_vec <- c(.5, .5, .5)

sim_counter <- 0
sample_setting <- 1 # for shared pull of rows from csv
sig_intensity <- 1:15 
per_setting <- 1:10
per_k <- 4

Ns = c(1000, 5000, 10000, 50000, 100000, 500000)


for (k in Ns) {
    sample_idx <- 0
    for (j in 1:per_k) {
        print(paste0("Redrawing sample for k=", k, ", iteration ", j))
        sample_idx <- sample_idx + 1
        idx <- sort(sample.int(N, k))
        triples <- extract_rows_by_index(csv_file, idx, c(col_i, col_j, col_k))
        for (n in per_setting) {
            sim_counter <- sim_counter + 1
            dt <- gen_sparse_tensor_from_dt(triples, p = p, 
                                            Sigma = Sigma, 
                                            sigma_vec = sigma_vec,
                                            beta0 = beta0, 
                                            sigmaE = 1,
                                            beta = beta,
                                            seed = k + 100 * j + n 
                                            )
            names(dt)[c(1, 2, 3)] <- c("i", "j", "k")  
            meta <- attributes(dt)$meta
            fit <- run_3s(dt)

            row <- data.table(
                sim_id = sim_counter, 
                seed = k + 100 * j + n,
                beta_sqerr = sum((fit$beta[2:(p + 1)] - beta)^2),
                beta_norm = sqrt(sum(fit$beta[2:(p + 1)]^2)),
                beta0_est = fit$beta[1],
                est_sigA = fit$sigmaA,
                est_sigB = fit$sigmaB,
                est_sigC = fit$sigmaC,
                true_sigA = sigma_vec[1],
                true_sigB = sigma_vec[2],
                true_sigC = sigma_vec[3],
                col_i = col_i,
                col_j = col_j,
                col_k = col_k,
                sample_setting = sample_setting,
                k = k,
                subsample_id = sample_idx,
                setting_name = setting_name)
            fwrite(row, out_csv, append = TRUE)
        }
    }
}

```