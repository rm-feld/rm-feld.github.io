---
type: proposition
aliases:
  - cumulative-to-component variance inversion
  - mobius inversion for interaction variance components
tags:
  - crossed
  - genai/claude
  - research
  - stanford/y2
modified: 2026-07-07T23:43:35-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Möbius Inversion for Interaction Variance Components
>
> Let $\mathbb A\subseteq2^{[K]}\setminus\{\varnothing\}$ satisfy the **subset rule** (if $\mathcal K\in\mathbb A$ then every nonempty $\mathcal K'\subseteq\mathcal K$ lies in $\mathbb A$). Write $\tilde\rho_{\mathcal K}=\sigma^2_{\mathcal K}/\sigma^2_{\mathrm{tot}}$ for the component ratios and, for the **cumulative** slice ratios,
> $$\rho_{\mathcal K}=\frac{\sigma^2_{\Sigma\mathcal K}}{\sigma^2_{\mathrm{tot}}}=\sum_{\substack{\mathcal K'\subseteq\mathcal K\\ \mathcal K'\in\mathbb A}}\tilde\rho_{\mathcal K'}.$$
> Then the components are recovered by inclusion–exclusion (Möbius inversion on the Boolean lattice):
> $$\boxed{\ \tilde\rho_{\mathcal K}=\sum_{\substack{\mathcal K'\subseteq\mathcal K\\ \mathcal K'\in\mathbb A}}(-1)^{|\mathcal K|-|\mathcal K'|}\,\rho_{\mathcal K'}\ }$$
> and, with $\sigma^2_E$ fixed, $\sigma^2_{\mathrm{tot}}=\sigma^2_E/\big(1-\sum_{\mathcal K\in\mathbb A}\tilde\rho_{\mathcal K}\big)$, $\ \sigma^2_{\mathcal K}=\tilde\rho_{\mathcal K}\,\sigma^2_{\mathrm{tot}}$, $\ \beta=\sigma\gamma$.
^mobius-inversion

> [!success]- Proof
>
> **Reduction to the full Boolean interval.** Fix $\mathcal K\in\mathbb A$. The subset rule guarantees $\{\mathcal K':\varnothing\subsetneq\mathcal K'\subseteq\mathcal K\}\subseteq\mathbb A$, so the restriction "$\mathcal K'\in\mathbb A$" is vacuous on the interval $[\varnothing,\mathcal K]$ in the subset lattice. Extend both indexed families to $\varnothing$ by setting $\tilde\rho_\varnothing:=0$ (no global random effect; $\varnothing\notin\mathbb A$). Then, using $\rho_\varnothing=\tilde\rho_\varnothing=0$,
> $$\rho_{\mathcal K}=\sum_{\varnothing\subseteq\mathcal K'\subseteq\mathcal K}\tilde\rho_{\mathcal K'}.$$
>
> **Möbius function of the Boolean lattice.** The subset lattice $(2^{[K]},\subseteq)$ has Möbius function $\mu(\mathcal K',\mathcal K)=(-1)^{|\mathcal K|-|\mathcal K'|}$ for $\mathcal K'\subseteq\mathcal K$. The Möbius inversion theorem states: if $\rho_{\mathcal K}=\sum_{\mathcal K'\subseteq\mathcal K}\tilde\rho_{\mathcal K'}$ for all $\mathcal K$, then
> $$\tilde\rho_{\mathcal K}=\sum_{\mathcal K'\subseteq\mathcal K}\mu(\mathcal K',\mathcal K)\,\rho_{\mathcal K'}=\sum_{\mathcal K'\subseteq\mathcal K}(-1)^{|\mathcal K|-|\mathcal K'|}\rho_{\mathcal K'}.$$
>
> **Drop $\varnothing$.** The $\mathcal K'=\varnothing$ term carries $\rho_\varnothing=0$, so it vanishes and the sum restricts to $\varnothing\subsetneq\mathcal K'\subseteq\mathcal K$, all of which lie in $\mathbb A$ by the subset rule. This is the boxed formula. Verified numerically on a full $K=3$, $\mathbb A_{\le2}$ example (max error $1.4\times10^{-17}$).
>
> **Back-solve.** Summing the boxed identity over $\mathcal K\in\mathbb A$ telescopes only trivially, but the scale is recovered from $\sum_{\mathcal K\in\mathbb A}\tilde\rho_{\mathcal K}=(\sigma^2_{\mathrm{tot}}-\sigma^2_E)/\sigma^2_{\mathrm{tot}}=1-\sigma^2_E/\sigma^2_{\mathrm{tot}}$, giving $\sigma^2_{\mathrm{tot}}=\sigma^2_E/(1-\sum_{\mathcal K}\tilde\rho_{\mathcal K})$, hence $\sigma^2_{\mathcal K}$ and $\beta$. $\blacksquare$

> [!note]- Corollary ($\mathbb A_{\le2}$, closed form)
> For $\mathbb A=\mathbb A_1\cup\mathbb A_2$, the boxed identity gives $\tilde\rho_k=\rho_k$ and $\tilde\rho_{\{k,k'\}}=\rho_{\{k,k'\}}-\rho_k-\rho_{k'}$, and the aggregate identity
> $$\sum_{\mathcal K\in\mathbb A}\rho_{\mathcal K}-(K-1)\sum_{\mathcal K\in\mathbb A_1}\rho_{\mathcal K}=1-\frac{\sigma^2_E}{\sigma^2_{\mathrm{tot}}},$$
> so $\sigma^2_{\mathrm{tot}}=\sigma^2_E/\big(1-\sum_{\mathcal K\in\mathbb A}\rho_{\mathcal K}+(K-1)\sum_{\mathcal K\in\mathbb A_1}\rho_{\mathcal K}\big)$, $\ \sigma^2_{\{k,k'\}}=\sigma^2_{\mathrm{tot}}(\rho_{\{k,k'\}}-\rho_k-\rho_{k'})$. *(Verified exactly, error $0$.)*
> **Positivity constraint (reviewer point):** the boxed $\tilde\rho_{\mathcal K}\ge0$ is a genuine restriction on the estimated $\{\rho_{\mathcal K}\}$ — e.g. $\rho_{\{k,k'\}}\ge\rho_k+\rho_{k'}$ — which must be imposed (or checked) at estimation, since unconstrained slice fits can violate it.

**Role in the paper.** Proves the "Möbius inversion gives …" statement in the Interaction Terms section, isolates the **subset rule** as the exact condition making the inversion valid, and surfaces the **nonnegativity constraint** the paper currently leaves implicit. Generalizes [[Validity of the Rho Reparameterization (No Interactions)#^rho-reparam|the no-interaction bijection]].
