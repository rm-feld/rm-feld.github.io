---
modified: 2026-07-07T19:39:48-07:00
created: 2026-03-14T12:59:21-07:00
tags:
  - update-notation
---

> [!attention] Assumptions for $K$-Crossed Random Effects
> Let $Y_{\mathbf{i}} \in \left\{ -1, 1 \right\}$ follow the crossed random effects model with binary link $g$. Further, inheriting from standard ARC, we further suppose
> 1. *(Bounded covariates)* $\left\lvert\left\lvert x_{\mathbf{i}} \right\rvert\right\rvert \leq B_{x} < \infty,$
> 2. *(Nondegenerate Covariates)* $N^{-1} \sum_{\mathbf{i}} Z_{\mathbf{i}}x_{\mathbf{i}}x_{\mathbf{i}}^{\intercal} \to V \succ 0$, $V \in \mathbb{R}^{p\times p}$,
> 3. *(No Perfectly Separating Hyperplane)* There does not exist nonzero $v$ for which $v^{\intercal}x_{\mathbf{i}} \geq 0$ for all observed $\mathbf{i}$ such that $y_{\mathbf{i}} = 1$, and $v^{\intercal}x_{\mathbf{i}} < 0$ for all observed $\mathbf{i}$ such that $y_{\mathbf{i}} = -1$. 
> 4. *(Asymptotic Sparsity)* the number of unique levels for random effect $k$, $R_{k}= \Theta(N^{\kappa_{k}})$ satisfies $\kappa_{k} \in (0, 1)$ for all $k \in K$ and $\sum_{k} \kappa_{k} > 1$. 

