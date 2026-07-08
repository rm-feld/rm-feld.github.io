---
aliases: [2D AGH, Bivariate AGH]
modified: 2026-07-07T21:17:25-07:00
created: 2025-12-03T12:37:06-08:00
class:
  - goal
tags: []
---
We desire an implementation of [[Adaptive Gauss Hermite Quadrature]] where we perform integration of $f: \mathbb{R}^{2} \to \mathbb{R}$ over a unit bivariate normal with correlation $\rho$, 

$$\begin{align*} I = \int _{\mathbb{R}^{2}} f(x) \varphi_{2}(x; \rho)\, dx . \end{align*}$$

This is fairly immediate in the sense that a sum over a tensorized version of the standard univariate weights and nodes provides the analogous approximation. However, we need to be a little careful about the "adaptive" component of AGH, and in particular the standard error scale that emerges. 



