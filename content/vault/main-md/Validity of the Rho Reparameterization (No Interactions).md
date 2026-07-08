---
type: proposition
aliases: [gamma-rho reparameterization bijection, validity of the rho reparameterization]
tags: [crossed, genai/claude, research, stanford/y2]
modified: 2026-07-01T00:00:00-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Validity of the $\rho$-Reparameterization (No Interactions)
>
> Take the [[K-Crossed Random Effects Probit Model]] with $\mathbb A=\mathbb A_1$ and the probit scale normalization $\sigma^2_E=1$. The map
> $$\theta=(\beta,\sigma^2_1,\dots,\sigma^2_K)\ \longmapsto\ \psi=(\gamma,\rho_1,\dots,\rho_K),\qquad \gamma=\frac{\beta}{\sigma},\ \ \rho_k=\frac{\sigma^2_k}{\sigma^2},\ \ \sigma^2=1+\textstyle\sum_k\sigma^2_k,$$
> is a smooth bijection (a diffeomorphism) from $\Theta=\mathbb R^{p}\times(0,\infty)^{K}$ onto
> $$\Psi=\Big\{(\gamma,\rho)\in\mathbb R^{p}\times(0,1)^{K}:\ \textstyle\sum_k\rho_k<1\Big\},$$
> with inverse
> $$\sigma^2=\frac{1}{1-\sum_k\rho_k},\qquad \sigma^2_k=\rho_k\,\sigma^2,\qquad \beta=\sigma\gamma.$$

^rho-reparam

> [!success]- Proof
>
> **Well-defined and lands in $\Psi$.** For $\theta\in\Theta$, $\sigma^2=1+\sum_k\sigma^2_k>1$, each $\rho_k=\sigma^2_k/\sigma^2\in(0,1)$, and $\sum_k\rho_k=(\sigma^2-1)/\sigma^2=1-\sigma^{-2}\in(0,1)$. So $\psi\in\Psi$.
>
> **Inverse.** Given $\psi\in\Psi$, $1-\sum_k\rho_k\in(0,1)$, so $\sigma^2=(1-\sum_k\rho_k)^{-1}\in(1,\infty)$ is well-defined; then $\sigma^2_k=\rho_k\sigma^2>0$ recovers the variances and $\beta=\sigma\gamma$ the mean coefficients. Direct substitution shows the two maps compose to the identity in both directions (verified numerically: round-trip error $\le2\times10^{-16}$). Note the key algebraic identity $1-\sum_k\rho_k=\sigma^2_E/\sigma^2$ used in the back-solve.
>
> **Smoothness.** Both maps are rational with denominators bounded away from $0$ on $\Theta,\Psi$ respectively (namely $\sigma^2>0$ and $1-\sum_k\rho_k>0$), hence $C^\infty$; a smooth bijection with smooth inverse is a diffeomorphism. $\blacksquare$

**Remark (necessity of fixing $\sigma^2_E$).** The bijection requires the probit normalization $\sigma^2_E=1$ (equivalently, some fixed scale). If $\sigma^2_E$ were a free parameter, $\theta$ would carry $K+1$ variance parameters while the marginal collapse ([[K-Crossed Marginal Probit Likelihood]]) identifies only the $K$ ratios plus the direction $\gamma$: the overall latent scale is not identified, and the map is not injective. This is the probit-specific "scale collapse" and is exactly what fails for logistic/Poisson — see [[K-Crossed Logistic and Poisson Extension]] §2.

**Role in the paper.** Proves the claim "$\psi=(\gamma^{\mathsf T},\rho_1,\dots,\rho_K)^{\mathsf T}$ is a valid reparameterization of $\theta$" stated without proof in the Singular Factorization section. Underlies [[Consistency of the Composite Estimator of theta#^theta-consistency|composite consistency]] via continuity of the inverse. The interaction generalization is [[Mobius Inversion for Interaction Variance Components#^mobius-inversion|Möbius inversion]].
