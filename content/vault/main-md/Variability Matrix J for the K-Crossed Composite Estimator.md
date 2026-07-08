---
type: proposition
aliases: [crossed score covariance, godambe J for k-crossed composite estimator, variability matrix J]
tags: [crossed, genai/claude, research, stanford/y2]
modified: 2026-07-01T13:13:33-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Variability Matrix $J$ for the $K$-Crossed Composite Estimator
>
> The variability (Godambe "meat") $J(\psi)=\mathrm{Var}(U(\psi))$ is **not** the sum of per-observation variances: because units are dependent through shared random effects and the same data feed every criterion, $J$ carries crossed covariances. For the all-score with $\mathbb A=\mathbb A_1$, $K=2$ (rows $i$, columns $j$), it has the exact **row/column-sum-of-scores** form
> $$J_{\mathrm{all}}=\sum_{i}S_{i\bullet}S_{i\bullet}^{\mathsf T}+\sum_{j}S_{\bullet j}S_{\bullet j}^{\mathsf T}-\sum_{\ell}s_\ell^2\,x_\ell x_\ell^{\mathsf T},\qquad S_{i\bullet}=\sum_{\ell\in\text{row }i}s_\ell x_\ell,\ \ S_{\bullet j}=\sum_{\ell\in\text{col }j}s_\ell x_\ell.$$
> For general $K$ / interactions, $J_{\mathrm{all}}=\sum_{\mathcal K\in\mathbb A}\sum_{\boldsymbol j\in\pi_{\mathcal K}}\big(\sum_{\ell\mid\boldsymbol j}s_\ell x_\ell\big)^{\otimes2}$ corrected by inclusion–exclusion over shared-index sets. The full $J$ additionally contains all–slice and slice–slice blocks (criterion reuse), obtained by the same shared-index grouping on the stacked score.
^variability-J

> [!success]- Proof
>
> **Crossed covariance.** $U_{\mathrm{all}}=\sum_\ell s_\ell x_\ell$ with $\mathbb E s_\ell=0$, so $J_{\mathrm{all}}=\sum_{\ell,\ell'}\mathrm{Cov}(s_\ell,s_{\ell'})x_\ell x_{\ell'}^{\mathsf T}$. Two units are independent unless they share a random effect: $\mathrm{Cov}(s_\ell,s_{\ell'})=0$ unless $\pi_{\{k\}}(\boldsymbol i(\ell))=\pi_{\{k\}}(\boldsymbol i(\ell'))$ for some $k$ (same dependency graph as [[Pairwise Dependency Bound for the All Log-Likelihood#^dep-bound|the dependency-bound lemma]]).
>
> **Row/column-sum collapse ($K=2$).** With one observation per cell, distinct units share **either** a row **or** a column (not both). Summing over same-row pairs gives $\sum_i S_{i\bullet}S_{i\bullet}^{\mathsf T}$ (which includes the diagonal $\ell=\ell'$), over same-column pairs $\sum_j S_{\bullet j}S_{\bullet j}^{\mathsf T}$ (also including the diagonal). The diagonal $\sum_\ell s_\ell^2 x_\ell x_\ell^{\mathsf T}$ is thereby counted **twice**, so subtract it once:
> $$J_{\mathrm{all}}=\sum_i S_{i\bullet}S_{i\bullet}^{\mathsf T}+\sum_j S_{\bullet j}S_{\bullet j}^{\mathsf T}-\sum_\ell s_\ell^2 x_\ell x_\ell^{\mathsf T}.$$
> This is exactly the "row and column sums of composite weights" structure of Varin's linear $J_{\beta\beta}$ ([[Towards Optimal Weighting of the Crossed Random Effects Model]]), now with probit scores $s_\ell$.
>
> **General $K$ / interactions.** The shared-index indicator expands by inclusion–exclusion (same expansion as the dependency-bound lemma); grouping pairs by their shared slice $\boldsymbol j\in\pi_{\mathcal K}$ yields outer products of slice-sums $\sum_{\ell\mid\boldsymbol j}s_\ell x_\ell$, with signed corrections for pairs sharing several categories. The pairwise covariance for a sharing pair is a bivariate-probit functional of $(\eta_\ell,\eta_{\ell'})$ and latent correlation $\rho_{\ell\ell'}=\sum_{\mathcal K:\text{shared}}\tilde\rho_{\mathcal K}$; it need not be evaluated because the slice-sum outer products estimate $J_{\mathrm{all}}$ directly.
>
> **Cross-criterion blocks.** Stack the scores as $\tilde U_\ell=(\,\omega_{\mathrm{all}}s_\ell x_\ell\,;\ \omega_{\mathcal K}\times\text{slice contributions}\,)$; $J=\mathrm{Var}(\sum_\ell\tilde U_\ell)$ is assembled by the identical shared-index grouping, whose off-diagonal (all–slice, slice–slice) blocks are nonzero because the same $Y_\ell$ enter multiple criteria. $\blacksquare$

> [!note]- Validation
> Simulated $K=2$ crossed probit, $\hat\gamma$ from the all-likelihood. The plug-in $\hat H^{-1}\hat J_{\mathrm{all}}\hat H^{-1}$ (with $\hat J$ the row/column-sum estimator above) matches the Monte-Carlo covariance of $\hat\gamma$; SE ratio $\to1$ as levels grow ($0.90,0.95,0.98$ at $R=15,30,60$). The **naive** meat $\hat J_{\mathrm{naive}}=\sum_\ell s_\ell^2 x_\ell x_\ell^{\mathsf T}$ (independence) understates the intercept SE by $56\%$ at $R=15$ — the row/column terms carry most of the intercept's uncertainty. Scripts archived.

> [!note]- Estimation & CLT caveat
> $\hat J$ is a **sum** (not average) of outer products of row/column score totals, evaluated at $\hat\psi$; no bivariate-normal integrals are needed. **But** its effective sample size is the number of levels $\{R_k\}$, not $N$: the CLT that makes $J$ meaningful is over the $R_k$ row/column totals, so SEs are only trustworthy when every category has many levels. Thin categories (few levels, or one dominant level) are exactly the regime where the sandwich degrades — connect to [[One Slice Doesn't Grow]] / [[Heuristics of the Single-Large-Row Weighting]].

**Role in the paper.** The "meat" of the [[Godambe Sandwich for the K-Crossed Composite Estimator#^godambe-sandwich|sandwich]], and the concrete object a referee asks for. Exposes the crossed correction (naive understatement) and the level-count CLT caveat. Pairs with [[Sensitivity Matrix H for the K-Crossed Composite Estimator]].
