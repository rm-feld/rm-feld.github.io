---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/estimation/arc_kway.R
---

# `run_3s`

```r
run_3s <- function(dt, nq = 10, niter = 10, get_effects = FALSE, get_se = TRUE) {
    meta <- attributes(dt)$meta
    x_vars <- grep("^x", colnames(dt), value = TRUE)
    form <- as.formula(paste("Y ~", paste(x_vars, collapse = " + ")))
    mod.glm <- glm(form, family = binomial(link = "probit"), data = dt)
    x <- model.matrix(mod.glm)
    y <- dt$Y
    fit <- arcbin3s.fit(x, y, f1 = dt$i, f2 = dt$j, f3 = dt$k, mod.glm, nq, niter, get_effects, get_se)
    return(fit)
}
```

%% begin persistent %%

%% end persistent %%

