---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/estimation/arc_kway.R
---

# `arcbin3s.fit`

```r
arcbin3s.fit <- function(x, y, f1, f2, f3, obj_glm, nq = 10, niter = 10, get_effects = FALSE, get_se = TRUE) {
    w <- 2 * y - 1
    gamma <- obj_glm$coefficients
    eta <- as.vector(x %*% gamma)
    listw1 <- split(w, f1)
    len1 <- unlist(lapply(listw1, length))
    sel1 <- which(len1 == 1)
    which.list1 <- which(len1 > 1)
    listw1 <- listw1[which.list1]
    listeta1 <- split(eta, f1)[which.list1]
    listw2 <- split(w, f2)
    len2 <- unlist(lapply(listw2, length))
    sel2 <- which(len2 == 1)
    which.list2 <- which(len2 > 1)
    listw2 <- listw2[which.list2]
    listeta2 <- split(eta, f2)[which.list2]
    listw3 <- split(w, f3)
    len3 <- unlist(lapply(listw3, length))
    sel3 <- which(len3 == 1)
    which.list3 <- which(len3 > 1)
    listw3 <- listw3[which.list3]
    listeta3 <- split(eta, f3)[which.list3]
    obj.gh <- statmod::gauss.quad(nq, "hermite")
    ws <- obj.gh$weights * exp(obj.gh$nodes^2)
    rhoa <- stats::optimise(arcProbit:::likAGH, interval = c(0, 1), list_eta = listeta1, list_w = listw1, 
        niter = niter, ws = ws, z = obj.gh$nodes, maximum = TRUE)$maximum
    rhob <- stats::optimise(arcProbit:::likAGH, interval = c(0, 1), list_eta = listeta2, list_w = listw2, 
        niter = niter, ws = ws, z = obj.gh$nodes, maximum = TRUE)$maximum
    rhoc <- stats::optimise(arcProbit:::likAGH, interval = c(0, 1), list_eta = listeta3, list_w = listw3, 
        niter = niter, ws = ws, z = obj.gh$nodes, maximum = TRUE)$maximum
    sigma2A <- rhoa/(1 - rhoa - rhob - rhoc)
    sigma2B <- rhob/(1 - rhoa - rhob - rhoc)
    sigma2C <- rhoc/(1 - rhoa - rhob - rhoc)
    betaABC <- gamma * sqrt(1 + sigma2A + sigma2B + sigma2C)
    if (get_effects) {
        a.est <- arcProbit:::getEffects(rhoa, list_eta = listeta1, list_w = listw1, niter = niter, ws = ws, 
            z = obj.gh$nodes) * sqrt(sigma2A)
        k1 <- length(unique(f1))
        a.out <- numeric(k1)
        a.out[sel1] <- 0
        a.out[setdiff(1:k1, sel1)] <- a.est
        b.est <- arcProbit:::getEffects(rhob, list_eta = listeta2, list_w = listw2, niter = niter, ws = ws, 
            z = obj.gh$nodes) * sqrt(sigma2B)
        k2 <- length(unique(f2))
        b.out <- numeric(k2)
        b.out[sel2] <- 0
        b.out[setdiff(1:k2, sel2)] <- b.est
        c.est <- arcProbit:::getEffects(rhoc, list_eta = listeta3, list_w = listw3, niter = niter, ws = ws, 
            z = obj.gh$nodes) * sqrt(sigma2C)
        k3 <- length(unique(f3))
        c.out <- numeric(k3)
        c.out[sel3] <- 0
        c.out[setdiff(1:k3, sel3)] <- c.est
    }
    else a.out <- b.out <- c.out <- NULL
    if (get_se) {
        df1f2f3 <- data.frame(f1 = f1, f2 = f2, f3 = f3)
        vCL <- sandwich::vcovCL(obj_glm, cluster = df1f2f3, multi0 = TRUE)
        H <- (1 + sigma2A + sigma2B + sigma2C) * vCL
        beta.se <- sqrt(diag(H))
    }
    else beta.se <- NULL
    return(list(beta = betaABC, beta.se = beta.se, sigmaA = sqrt(sigma2A), sigmaB = sqrt(sigma2B), sigmaC = sqrt(sigma2C), 
        rhoa = rhoa, rhob = rhob, rhoc = rhoc, a.est = a.out, b.est = b.out, c.est = c.out))
}
```

%% begin persistent %%

%% end persistent %%

