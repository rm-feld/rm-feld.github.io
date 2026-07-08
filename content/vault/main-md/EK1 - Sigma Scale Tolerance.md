---
modified: 2026-07-07T23:36:29-07:00
created: 2026-01-19T21:09:02-08:00
---

# misc. notes
- 1/10 failure in .6, half at .7, all but 2 on .8, and wiped out by .9. formal identifiability?

# viz. 
![[Pasted image 20260120112705.png]]

![[Pasted image 20260120112814.png]]

![[Pasted image 20260120113907.png]]
# code
## specs

```r
# high-level specs
csv_file = "/Users/rfeld/Documents/Research/ROTATION F25/day_1.csv"
p = 5
Sigma = ar1_cov(p)
SigmaE = 1
beta0 = -1.2 
nq = 10
niter = 10

# mid-level specs
beta = -1.2 + 0.3 * seq(1, p) 
setting_name = "mild_beta"

col_i = 24
col_j = 25
col_k = 26

k = 50000
```

## loop 

```r
sim_counter <- 0
sample_setting <- 1 # for shared pull of rows from csv
sig_intensity <- 1:15 
per_setting <- 1:10


for (s in sig_intensity) {
    for (n in per_setting) {
        sim_counter <- sim_counter + 1
        dt <- gen_sparse_tensor_from_dt(triples, p = p, 
                                        Sigma = Sigma, 
                                        sigma_vec = .1 * s * c(1., 1., 1.),
                                        beta0 = beta0, 
                                        sigmaE = 1,
                                        beta = beta,
                                        seed = s * 100 + n
                                        )
        names(dt)[c(1, 2, 3)] <- c("i", "j", "k")  
        meta <- attributes(dt)$meta
        fit <- run_3s(dt)
...
```


