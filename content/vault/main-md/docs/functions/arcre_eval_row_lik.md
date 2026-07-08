---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `eval_row_lik`

```r
eval_row_lik <- function(beta, sigma, rho_A, y, X, row_id, family, rule_in, gh_out, obs_wt = NULL) {
    rho_B <- safe_sqrt(1 - rho_A^2)
    switch(family, gaussian = gauss_ell_grouped(beta, sigma * rho_A, sigma * rho_B, y, X, row_id, obs_wt), 
        probit = probit_ell_grouped(beta, sigma, rho_A, y, X, row_id, gh_out, obs_wt), logit = logit_ell_grouped(beta, 
            sigma, rho_A, y, X, row_id, gh_out, obs_wt), poisson = pois_ell_grouped(beta, sigma, rho_A, 
            y, X, row_id, rule_in, gh_out, obs_wt))
}
```

%% begin persistent %%

%% end persistent %%

