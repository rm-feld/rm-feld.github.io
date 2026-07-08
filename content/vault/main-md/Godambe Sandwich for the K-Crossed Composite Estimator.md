---
type: theorem
aliases:
  - composite likelihood asymptotic variance k-crossed probit
  - godambe sandwich for the k-crossed composite estimator
tags:
  - crossed
  - genai/claude
  - research
  - stanford/y2
modified: 2026-07-07T23:37:41-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Godambe Sandwich for the $K$-Crossed Composite Estimator
>
> Work in the [[Validity of the Rho Reparameterization (No Interactions)|working coordinates]] $\psi=(\gamma,\{\rho_{\mathcal K}\}_{\mathcal K\in\mathbb A})$ and let $\hat\psi$ maximize the weighted composite criterion
> $$c\ell(\psi)=\omega_{\mathrm{all}}\,\mathcal L_{\mathrm{all}}(\gamma)+\sum_{\mathcal K\in\mathbb A}\omega_{\mathcal K}\,\mathcal L_{\mathcal K}(\gamma,\rho_{\mathcal K}),\qquad U(\psi):=\nabla_\psi c\ell(\psi),\quad U(\hat\psi)=0.$$
> Under [[Base Assumptions for K-crossed Random Effects with Symmetric Binary Link|the base assumptions]] and the design/growth conditions of the two consistency theorems, $\hat\psi$ is asymptotically normal with the **Godambe (sandwich) variance**
> $$\boxed{\ \widehat{\mathrm{avar}}(\hat\psi)=H(\psi_0)^{-1}\,J(\psi_0)\,H(\psi_0)^{-1}\ },\qquad H=\mathbb E[-\nabla_\psi U],\quad J=\mathrm{Var}(U),$$
> and the variance of the estimand $\hat\theta=(\hat\beta,\{\hat\sigma^2_{\mathcal K}\})$ follows by the delta method through the reparameterization diffeomorphism $\Psi:\psi\mapsto\theta$ of [[Consistency of the Composite Estimator of theta|the back-solve]]:
> $$\widehat{\mathrm{avar}}(\hat\theta)=\dot\Psi\,\big[H^{-1}JH^{-1}\big]\,\dot\Psi^{\mathsf T},\qquad \dot\Psi=\frac{\partial\theta}{\partial\psi}\Big|_{\psi_0}.$$
^godambe-sandwich

> [!success]- Proof (M-estimation / stacked estimating equations)
>
> **Unbiased estimating equation.** $U(\psi)=\sum(\text{component scores})$; by [[Composite Score and Unbiased Estimating Equations (K-Crossed Probit)#^composite-score|the score lemma]] each component score has mean zero at $\psi_0$ because the all-marginal and each slice submodel are **correctly specified** ([[Population Identification of gamma for the All Likelihood]], [[Regularity of the Slice Submodel (Equicorrelated Probit)]]). Hence $\mathbb E[U(\psi_0)]=0$ and $\psi_0$ solves the population equation.
>
> **Taylor expansion.** With $U(\hat\psi)=0$, a first-order expansion about $\psi_0$ gives
> $$0=U(\psi_0)+\nabla_\psi U(\tilde\psi)(\hat\psi-\psi_0)\ \Rightarrow\ \hat\psi-\psi_0=\big[-\nabla_\psi U(\tilde\psi)\big]^{-1}U(\psi_0).$$
> By consistency ($\hat\psi\xrightarrow{p}\psi_0$, from the two theorems + continuous mapping) and a uniform LLN, $-\nabla_\psi U(\tilde\psi)/a_N\to H/a_N$ for the appropriate norming; the sensitivity $H=\mathbb E[-\nabla_\psi U]$ is given in [[Sensitivity Matrix H for the K-Crossed Composite Estimator#^sensitivity-H|the H atom]] and is nonsingular under $V\succ0$ and $\omega_{\mathcal K}>0$.
>
> **Crossed CLT for the score.** $U(\psi_0)$ is a sum of contributions dependent only through shared random effects; its variance $J=\mathrm{Var}(U)$ has the crossed row/column-sum structure of [[Variability Matrix J for the K-Crossed Composite Estimator#^variability-J|the J atom]]. A CLT for this dependency graph (finitely many shared-index neighbours per unit, number of levels $R_k\to\infty$) gives $J^{-1/2}U(\psi_0)\rightsquigarrow\mathcal N(0,I)$. Combining, $\hat\psi-\psi_0\rightsquigarrow\mathcal N(0,H^{-1}JH^{-1})$.
>
> **Delta method to $\theta$.** $\theta=\Psi(\psi)$ is a diffeomorphism on the region where the back-solve denominator $1-\sum_{\mathcal K}\tilde\rho_{\mathcal K}$ is bounded away from $0$ ([[Validity of the Rho Reparameterization (No Interactions)]], [[Mobius Inversion for Interaction Variance Components]]), so $\hat\theta-\theta_0\rightsquigarrow\mathcal N(0,\dot\Psi\,H^{-1}JH^{-1}\dot\Psi^{\mathsf T})$. $\blacksquare$

> [!note]- Validation
> The novel piece — the crossed $J$ for the all-score — was checked by simulation ($K=2$ crossed probit, $\gamma$ estimated from the all-likelihood; scripts archived). The model sandwich $\hat H^{-1}\hat J\hat H^{-1}$ matches the Monte-Carlo sampling covariance of $\hat\gamma$, with the SE ratio $\to1$ as the number of levels grows: $R=15\!\to\!0.90$, $R=30\!\to\!0.95$, $R=60\!\to\!0.98$ (the residual gap is finite-sample: the crossed CLT is driven by the $R_k$ row/column totals, not $N$). Dropping the cross terms (naive independence $J$) **understates the intercept SE by $56\%$** at $R=15$ — the crossed correction is not optional.

> [!warning]- Remark 1 — Varin's $\beta$-decoupling does NOT transfer to probit
> In the linear-Gaussian composite likelihood (Varin, row+column) the mean and variance parameters are information-orthogonal, so $H$ is block-diagonal and $\mathrm{avar}(\hat\beta)$ is "as if the variances were known." **This is a Gaussian luxury.** For probit the cross-block $H_{\gamma\rho_{\mathcal K}}$ is generally nonzero (the slice criterion couples $\gamma$ and $\rho_{\mathcal K}$ through $\gamma_{\mathcal K}=\gamma/\sqrt{1-\rho_{\mathcal K}}$), so $\hat\gamma$ and $\hat\rho$ are asymptotically correlated and the full sandwich must be retained. *(Confirm the magnitude of $H_{\gamma\rho}$ numerically — flagged as a to-verify.)*

> [!warning]- Remark 2 — single criterion vs. staged estimator
> The boxed result is for the **single joint** criterion $c\ell$. The two-stage ARC estimator (all $\to\hat\gamma$, then slices $\to\hat\rho$) is the triangular special case; its sandwich is $A^{-1}B A^{-\mathsf T}$ with $A=\mathbb E[-\nabla_\psi\Psi_{\mathrm{stack}}]$ **block-lower-triangular** (stage 2 sees $\hat\gamma$), i.e. it carries the standard first-stage-nuisance correction. Choosing joint vs. staged is a modeling decision (discuss).

**Two sources of non-triviality (the punchline).** The sandwich departs from the naive inverse information for two independent reasons: (i) **cross-observation dependence** through shared random effects (the crossed $J$); and (ii) **criterion reuse** — the same responses enter the all- and every slice-criterion, so those scores are correlated and $J$ has nonzero all–slice and slice–slice blocks. Both are handled by the same shared-index grouping.

**Depends on:** [[Composite Score and Unbiased Estimating Equations (K-Crossed Probit)]] · [[Sensitivity Matrix H for the K-Crossed Composite Estimator]] · [[Variability Matrix J for the K-Crossed Composite Estimator]] · [[Validity of the Rho Reparameterization (No Interactions)]] · [[Bartlett Identities]]. **Answers** objection B1 of [[Reviewer Objections and Next Steps (K-Crossed Probit Paper)]].
