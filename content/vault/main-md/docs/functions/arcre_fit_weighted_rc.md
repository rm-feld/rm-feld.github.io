---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/arclik.R
---

# `fit_weighted_rc`

```r
fit_weighted_rc <- function(y, X, row_id, col_id, R, C, family, Q_all, Q_in, Q_out, sigma_lower, sigma_upper, 
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
            g0 <- if (p > 0) 
                rep(0, p)
            else numeric(0)
            nr <- newton_gamma(g0, y, X)
            ghat <- nr$gamma
        }
        else {
            g0 <- if (p > 0) 
                rep(0, p)
            else numeric(0)
            nr <- newton_beta(g0, 0, y, X, "logit")
            ghat <- nr$beta
        }
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
    }
    if (verbose) 
        cat("Stage 2: grid(w) ...\n")
    w_grid <- seq(0.1, 0.9, by = 0.1)
    best_val <- -Inf
    best_rho <- 0.5
    best_w <- 0.5
    best_sig <- 0.5
    for (w in w_grid) {
        if (sig0) {
            neg_wrc2 <- function(par) {
                sig <- exp(par[1])
                rA <- plogis(par[2])
                beta_t <- ghat * sqrt(1 + sig^2)
                e_r <- eval_row_lik(beta_t, sig, rA, y, X, row_id, family, rule_in, gh_out)
                e_c <- eval_col_lik(beta_t, sig, rA, y, X, col_id, family, rule_in, gh_out)
                -(w * e_r + (1 - w) * e_c)
            }
            opt <- optim(c(log(0.5), 0), neg_wrc2, method = "Nelder-Mead", control = list(maxit = 300))
            if (-opt$value > best_val) {
                best_val <- -opt$value
                best_w <- w
                best_sig <- exp(opt$par[1])
                best_rho <- plogis(opt$par[2])
            }
        }
        else {
            neg_wrc <- function(rA) {
                e_r <- eval_row_lik(bhat, shat, rA, y, X, row_id, family, rule_in, gh_out)
                e_c <- eval_col_lik(bhat, shat, rA, y, X, col_id, family, rule_in, gh_out)
                -(w * e_r + (1 - w) * e_c)
            }
            opt <- optimize(neg_wrc, c(rho_eps, 1 - rho_eps))
            if (-opt$objective > best_val) {
                best_val <- -opt$objective
                best_rho <- opt$minimum
                best_w <- w
            }
        }
    }
    if (sig0) {
        shat <- best_sig
        bhat <- ghat * sqrt(1 + shat^2)
    }
    sA <- shat * best_rho
    sB <- shat * safe_sqrt(1 - best_rho^2)
    if (verbose) 
        cat("  w =", best_w, " sigma_A =", signif(sA, 5), " sigma_B =", signif(sB, 5), "\n")
    list(beta = bhat, sigma_A = sA, sigma_B = sB, sigma = shat, rho_A = best_rho, w = best_w)
}
```

%% begin persistent %%

%% end persistent %%

