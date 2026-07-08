---
modified: 2026-02-11T12:44:56-08:00
created: 2026-01-31T16:01:50-08:00
---

Okay, my goal is to figure out weighting for crossed random effects, because nontrivial contribution is common amongst observations. Need to read through Art's point on a weighting game/etc. 

However, here's a starting point; grid a lambda on the weights, average a few draws, and see what comes out. also try art version. also rerun the empirical example with row-weights. I'm still intrigued by directionality of $\beta$ in this regime, and it is unclear to me that the correct scale is utilized in the backsolve, but maybe I'm wrong. 

# Iterative Weighting 


# Naive Direction 1 

# Naive Direction 2

# Experiments
## Experiment 1
Corrected $\beta_{0}$, $\beta$ scale inference via weighted glm. true `sigma_vec = c(0.5, 0.5)`. This is for dominant class having `$p$ = 0.5`. 

![[Pasted image 20260203110115.png]]

## Experiment 2 
same glm weighting, then using inverse proportion weighting on `likAGH` (now `likAGHweighted`).

$$\begin{align*} \left\lvert\left\lvert \beta - \hat{\beta} \right\rvert\right\rvert ^{2} = \left( \beta - \sqrt{ \sigma^{2}_{A} + \sigma^{2}_{B} + 1 }\cdot \beta \right)^{2} \end{align*}$$


![[Pasted image 20260203121312.png]]

`sigma_b` inferred smaller, `sigma_a` uniformly inferred larger; $\beta$ holding decently strong. 



## Experiment 3
**Wrong Because Weighting in GLM step is different.** Write out weights (look at notebooklm) and rerun. 

![[Pasted image 20260203194618.png]]


## Rerun with inverse proportion weights 

```r
a_curve <- function(dt_, a, prop_large, beta, beta0, sigma_vec) {
    sigmaA <- sigma_vec[1]; sigmaB <- sigma_vec[2]
    dt <- clip_and_resim(dt = dt_, p = prop_large, 
                         beta = beta, beta0 = beta0, 
                         sigmaB = sigmaB, a = a, 
                         b_vec = attributes(dt_)$meta$effects[[2]])

    dt[, w_raw := 1 / .N, by = f1] 
    dt[, w_f1 := w_raw * (nrow(dt) / sum(w_raw))]

    x_vars <- grep("^x", colnames(dt), value = TRUE)
    form <- as.formula(paste("Y ~", paste(x_vars, collapse = " + ")))

    
    # calculate beta direction
    mod.glm <- glm(form, 
                   family = binomial(link = "probit"), 
                   data = dt, weights = w_f1)
    x <- model.matrix(mod.glm)
    y <- dt$Y

    f1 = dt$f1; f2 = dt$f2

    out <- arcbin.fit(x = x, y = y, f1, f2, mod.glm, weights_f1 = dt$w_f1)
    return(list(dt = dt, arcfit = out))
}
```

![[Pasted image 20260211114251.png]]


 ![[Pasted image 20260211124434.png]]