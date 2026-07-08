---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `fit_size_weighted`

```r
fit_size_weighted <- function(y, X, row_id, col_id, R, C, family, Q_all, Q_in, Q_out, sigma_lower, sigma_upper, 
    rho_eps, logit_sigma0, verbose) {
    p <- ncol(X)
    N <- length(y)
    rule_all <- if (family == "poisson") 
        gaussHermiteData(Q_all)
    else NULL
    rule_in <- if (family == "poisson") 
        gaussHermiteData(Q_in)
    else NULL
    gh_out <- ghq01(Q_out)
    sbounds <- default_sigma_bounds(family, y, sigma_lower, sigma_upper)
    sig0 <- (family == "probit") || (family == "logit" && logit_sigma0)
    row_tab <- table(row_id)
    col_tab <- table(col_id)
    row_wt <- 1/as.numeric(row_tab[as.character(row_id)])
    col_wt <- 1/as.numeric(col_tab[as.character(col_id)])
    if (sig0) {
        g0 <- if (p > 0) 
            rep(0, p)
        else numeric(0)
        if (family == "probit") {
            nr <- newton_gamma(g0, y, X)
            ghat <- nr$gamma
        }
        else {
            nr <- newton_beta(g0, 0, y, X, "logit")
            ghat <- nr$beta
        }
        if (verbose) 
            cat("Stage 2: size-weighted 2D search ...\n")
        neg_rc2 <- function(par) {
            sig <- exp(par[1])
            rA <- plogis(par[2])
            beta_t <- ghat * sqrt(1 + sig^2)
            e_r <- eval_row_lik(beta_t, sig, rA, y, X, row_id, family, rule_in, gh_out, obs_wt = row_wt)
            e_c <- eval_col_lik(beta_t, sig, rA, y, X, col_id, family, rule_in, gh_out, obs_wt = col_wt)
            -(e_r + e_c)
        }
        opt2 <- optim(c(log(0.5), 0), neg_rc2, method = "Nelder-Mead", control = list(maxit = 500))
        shat <- exp(opt2$par[1])
        rhat <- plogis(opt2$par[2])
        bhat <- ghat * sqrt(1 + shat^2)
    }
    else {
        beta_env <- new.env(parent = emptyenv())
        beta_env$b <- if (p > 0) 
            rep(0, p)
        else numeric(0)
        neg_profile <- function(sigma) {
            nr <- newton_beta(beta_env$b, sigma, y, X, family, rule_all)
            beta_env$b <- nr$beta
            -nr$ell
        }
        if (verbose) 
            cat("Stage 1: profile ell_all ...\n")
        opt1 <- optimize(neg_profile, sbounds)
        shat <- opt1$minimum
        bhat <- beta_env$b
        neg_rc <- function(rA) {
            e_r <- eval_row_lik(bhat, shat, rA, y, X, row_id, family, rule_in, gh_out, obs_wt = row_wt)
            e_c <- eval_col_lik(bhat, shat, rA, y, X, col_id, family, rule_in, gh_out, obs_wt = col_wt)
            -(e_r + e_c)
        }
        if (verbose) 
            cat("Stage 2: size-weighted Brent ...\n")
        opt2 <- optimize(neg_rc, c(rho_eps, 1 - rho_eps))
        rhat <- opt2$minimum
        boundary_warning(rhat, rho_eps, 1 - rho_eps, "rho_A")
    }
    sA <- shat * rhat
    sB <- shat * safe_sqrt(1 - rhat^2)
    if (verbose) 
        cat("  sigma_A =", signif(sA, 5), " sigma_B =", signif(sB, 5), "\n")
    list(beta = bhat, sigma_A = sA, sigma_B = sB, sigma = shat, rho_A = rhat)
}
```

%% begin persistent %%

%% end persistent %%

