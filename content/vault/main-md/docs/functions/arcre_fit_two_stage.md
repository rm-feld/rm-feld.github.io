---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `fit_two_stage`

```r
fit_two_stage <- function(y, X, row_id, col_id, R, C, family, Q_all, Q_in, Q_out, sigma_lower, sigma_upper, 
    rho_eps, logit_sigma0, verbose) {
    p <- ncol(X)
    rule_all <- if (family == "poisson") 
        gaussHermiteData(Q_all)
    else NULL
    rule_in <- if (family == "poisson") 
        gaussHermiteData(Q_in)
    else NULL
    gh_out <- ghq01(Q_out)
    sbounds <- default_sigma_bounds(family, y, sigma_lower, sigma_upper)
    sig0 <- (family == "probit") || (family == "logit" && logit_sigma0)
    if (sig0) {
        if (family == "probit") {
            if (verbose) 
                cat("Stage 1: probit GLM for gamma ...\n")
            g0 <- if (p > 0) 
                rep(0, p)
            else numeric(0)
            nr <- newton_gamma(g0, y, X)
            ghat <- nr$gamma
        }
        else {
            if (verbose) 
                cat("Stage 1: logistic regression for gamma (sigma=0) ...\n")
            g0 <- if (p > 0) 
                rep(0, p)
            else numeric(0)
            nr <- newton_beta(g0, 0, y, X, "logit")
            ghat <- nr$beta
        }
        if (verbose) 
            cat("  gamma =", signif(ghat, 5), "\n")
        if (verbose) 
            cat("Stage 2: 2D search (sigma, rho_A) ...\n")
        neg_rc2 <- function(par) {
            sig <- exp(par[1])
            rA <- plogis(par[2])
            beta_trial <- ghat * sqrt(1 + sig^2)
            -eval_rc(beta_trial, sig, rA, y, X, row_id, col_id, family, rule_in, gh_out)
        }
        start2 <- c(log(0.5), 0)
        opt2 <- optim(start2, neg_rc2, method = "Nelder-Mead", control = list(maxit = 500, reltol = 1e-08))
        if (opt2$convergence != 0) 
            warning(family, " Stage 2 optim: code ", opt2$convergence)
        shat <- exp(opt2$par[1])
        rhat <- plogis(opt2$par[2])
        bhat <- ghat * sqrt(1 + shat^2)
        sA <- shat * rhat
        sB <- shat * safe_sqrt(1 - rhat^2)
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
            cat("Stage 1: profile ell_all over sigma ...\n")
        opt1 <- optimize(neg_profile, sbounds)
        shat <- opt1$minimum
        bhat <- beta_env$b
        boundary_warning(shat, sbounds[1], sbounds[2], "sigma")
        if (verbose) 
            cat("  beta =", signif(bhat, 5), " sigma =", signif(shat, 5), "\n")
        neg_rc <- function(rA) {
            -eval_rc(bhat, shat, rA, y, X, row_id, col_id, family, rule_in, gh_out)
        }
        if (verbose) 
            cat("Stage 2: Brent on rho_A ...\n")
        opt2 <- optimize(neg_rc, c(rho_eps, 1 - rho_eps))
        rhat <- opt2$minimum
        boundary_warning(rhat, rho_eps, 1 - rho_eps, "rho_A")
        sA <- shat * rhat
        sB <- shat * safe_sqrt(1 - rhat^2)
    }
    if (verbose) 
        cat("  sigma_A =", signif(sA, 5), " sigma_B =", signif(sB, 5), "\n")
    list(beta = bhat, sigma_A = sA, sigma_B = sB, sigma = shat, rho_A = rhat)
}
```

%% begin persistent %%

%% end persistent %%

