---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `eval_rc`

```r
eval_rc <- function(beta, sigma, rho_A, y, X, row_id, col_id, family, rule_in, gh_out, row_wt = NULL, 
    col_wt = NULL) {
    eval_row_lik(beta, sigma, rho_A, y, X, row_id, family, rule_in, gh_out, row_wt) + eval_col_lik(beta, 
        sigma, rho_A, y, X, col_id, family, rule_in, gh_out, col_wt)
}
```

%% begin persistent %%

%% end persistent %%

