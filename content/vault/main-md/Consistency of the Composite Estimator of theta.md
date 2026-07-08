---
type: corollary
aliases:
  - back-solved theta is consistent
  - consistency of the composite estimator of theta
tags:
  - crossed
  - genai/claude
  - research
  - rewrite-human
  - stanford/y2
modified: 2026-07-07T21:28:15-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Consistency of the Composite Estimator of $\theta$
>
> Let $\hat\gamma$ maximize the all likelihood and, for each $\mathcal K\in\mathbb A$, let $\hat\tau^2_{\mathcal K}$ be the consistent slice root. Define $\hat\theta=(\hat\beta,\{\hat\sigma^2_{\mathcal K}\})$ by the back-solve of [[Mobius Inversion for Interaction Variance Components#^mobius-inversion|Möbius inversion]] (equivalently [[Validity of the Rho Reparameterization (No Interactions)#^rho-reparam|the $\rho$-reparameterization]] when $\mathbb A=\mathbb A_1$). If the conditions of [[Consistency of All Likelihood for K-Crossed Random Effects Probit Model#^all-consistency|Theorem (all-consistency)]] and of [[Existence of an Isolating Subset for Slice Consistency#^isolating-subset|slice consistency]] hold for every $\mathcal K\in\mathbb A$, then
> $$\hat\theta\ \xrightarrow{\ p\ }\ \theta_0.$$
^theta-consistency

> [!success]- Proof
>
> **Component convergences.** By [[Consistency of All Likelihood for K-Crossed Random Effects Probit Model#^all-consistency|Theorem (all-consistency)]], $\hat\gamma\xrightarrow{p}\gamma_0$. By the slice results, $\hat\tau^2_{\mathcal K}\xrightarrow{p}\tau^2_{\mathcal K,0}$ for each of the finitely many $\mathcal K\in\mathbb A$; the map $\tau^2\mapsto\rho=\tau^2/(1+\tau^2)$ is continuous, so $\hat\rho_{\mathcal K}\xrightarrow{p}\rho_{\mathcal K,0}$. A finite collection of $o_P(1)$ terms is jointly $o_P(1)$, so $\hat\psi:=(\hat\gamma,\{\hat\rho_{\mathcal K}\})\xrightarrow{p}\psi_0$.
>
> **Continuity of the back-solve.** The back-solve $\Psi:\hat\psi\mapsto\hat\theta$ is
> $$\tilde\rho_{\mathcal K}=\sum_{\mathcal K'\subseteq\mathcal K,\mathcal K'\in\mathbb A}(-1)^{|\mathcal K|-|\mathcal K'|}\rho_{\mathcal K'},\quad \sigma^2_{\mathrm{tot}}=\frac{\sigma^2_E}{1-\sum_{\mathcal K}\tilde\rho_{\mathcal K}},\quad \sigma^2_{\mathcal K}=\tilde\rho_{\mathcal K}\sigma^2_{\mathrm{tot}},\quad \beta=\sigma\gamma.$$
> Each map is a polynomial/rational function; the only possible discontinuity is the vanishing of $1-\sum_{\mathcal K}\tilde\rho_{\mathcal K}$. At the truth this denominator equals $\sigma^2_E/\sigma^2_{\mathrm{tot},0}>0$, so on a neighborhood of $\psi_0$ it is bounded away from $0$ and $\Psi$ is continuous there.
>
> **Continuous mapping.** By the continuous mapping theorem, $\hat\theta=\Psi(\hat\psi)\xrightarrow{p}\Psi(\psi_0)=\theta_0$. $\blacksquare$

> [!note]- Remark — why this corollary is the actual paper payoff
> The two theorems in the draft prove consistency of $\hat\gamma$ (a direction/scale ratio) and of $\hat\tau^2_{\mathcal K}$ (per-slice) **separately**. Neither statement, alone, is consistency of the estimand of interest $\theta=(\beta,\{\sigma^2_{\mathcal K}\})$. This corollary is the missing bridge, and it exposes the one genuine regularity requirement — the back-solve denominator must stay away from $0$, i.e. the error variance must be a nonvanishing fraction of the total. On the boundary ($\sum\tilde\rho\to1$, error variance $\to0$) the map degenerates and a separate boundary analysis is needed.

**Role in the paper.** States and proves the "$\hat\theta$ is consistent" conclusion that the draft implies but never asserts. Consumes [[Validity of the Rho Reparameterization (No Interactions)#^rho-reparam|the reparameterization]] / [[Mobius Inversion for Interaction Variance Components#^mobius-inversion|Möbius inversion]] as the continuity backbone.
