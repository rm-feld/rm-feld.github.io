---
type: proposition
aliases: [constructive sufficient condition for slice consistency, existence of an isolating subset]
tags: [crossed, genai/claude, OPEN, research, stanford/y2]
modified: 2026-07-06T13:46:06-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Existence of an Isolating Subset for Slice Consistency (Sufficient Condition)
>
> Consider a **complete** $K=3$ design $\mathcal S_0=[R_1]\times[R_2]\times[R_3]$, $R_k=\Theta(N^{\kappa_k})$, and the single-category slice $\mathcal K=\{1\}$ (recovering $\sigma^2_1$). If category $1$ is the sparsest in the sense
> $$\kappa_1<\min(\kappa_2,\kappa_3),$$
> then there exists $\tilde{\mathcal S}\subseteq\mathcal S_0$ satisfying conditions 1–4 of [[Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model#^slice-cramer-consistency|Theorem (slice-cramér)]] with $|\tilde{\mathcal S}|=2R_1\to\infty$. Consequently $\hat\tau^2_{\{1\}}$ (hence $\hat\sigma^2_1$) is consistent.
^isolating-subset

> [!success]- Proof (constructive)
>
> Choose block size $m=2$. Allocate to each level $i\in[R_1]$ two cells $B_i=\{(i,j_{i,1},k_{i,1}),(i,j_{i,2},k_{i,2})\}$ such that:
> - within $B_i$ the two $j$-labels are distinct and the two $k$-labels are distinct;
> - across $i\neq i'$, all $j$-labels are globally distinct and all $k$-labels are globally distinct.
>
> This is a collection of $R_1$ disjoint $2\times2$ partial permutation blocks with globally disjoint row/column supports. It uses $2R_1$ distinct $j$-labels and $2R_1$ distinct $k$-labels, feasible as long as $2R_1\le\min(R_2,R_3)$, i.e. asymptotically $\kappa_1<\min(\kappa_2,\kappa_3)$. Completeness of $\mathcal S_0$ guarantees every chosen cell $(i,j,k)$ is observed. Set $\tilde{\mathcal S}=\bigcup_i B_i$.
>
> **Verify the four conditions.** (1) Every level of category $1$ appears, so $|\pi_{\{1\}}(\tilde{\mathcal S})|=R_1=|\pi_{\{1\}}(\mathcal I)|$ (inter-slice). (2) Because $j$- and $k$-labels are globally disjoint across slices, each complement level occurs in exactly one slice, giving the intra-slice cardinality match (intra-slice isolation). (3) $\tilde N_{\boldsymbol j,\{1\}}=m=2\ge2$. (4) $|\tilde{\mathcal S}|=2R_1=2N^{\kappa_1}\to\infty$ since $\kappa_1>0$.
>
> By [[Regularity of the Slice Submodel (Equicorrelated Probit)#^slice-regularity|the regularity lemma]] the restricted slice likelihood is a genuine equicorrelated-probit likelihood over $R_1\to\infty$ independent clusters of size $2$, so the [[Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model#^slice-cramer-consistency|slice-cramér theorem]] applies. I verified the construction yields exactly block-equicorrelated latent covariance (within-slice off-diagonal $=\sigma^2_1$, cross-slice $=0$; script archived). $\blacksquare$

> [!warning]- Remark 1 — the "sparsest category" obstruction (reviewer point)
> The condition $\kappa_1<\min(\kappa_2,\kappa_3)$ says the slice category must be **sparser** than the complement, so the complement is rich enough to give each slice its own private, replicated, isolated observations. This cannot hold simultaneously for all three singletons (they can't all be strictly sparsest). Recovering **all** of $\sigma^2_1,\sigma^2_2,\sigma^2_3$ from single-category slices therefore needs either different isolating subsets per component (with overlapping data) or a genuinely different argument in the balanced regime $\kappa_1\approx\kappa_2\approx\kappa_3$ — this is the **saturation** phenomenon flagged in [[Sufficient Conditions for Cramer Consistency]]. **Update (2026-07-01):** resolved in [[Existence of Isolating Subsets in the Near-Balanced Regime]] — full cover (condition 1) is provably impossible near balance (pigeonhole), but weakening it to $|\tilde{\mathcal S}[\mathcal K]|\to\infty$ restores existence with $S=\Theta(\min_k R_k)$ blocks w.h.p. under uniform sampling, and all components become simultaneously recoverable. The weakening's compatibility with the Jiang chain still needs a check against Bellio's supplement.

> [!fail]- Remark 2 — necessity of a richness condition (degeneracy counterexample)
> Some non-degeneracy is genuinely necessary. If only "diagonal" triples $(i,i,k)$ are observed, then levels of categories $1$ and $2$ always co-occur, so $a_i$ and $b_i$ enter every observation together and $\sigma^2_1,\sigma^2_2$ are **not separately identified** — no isolating subset can exist. (Numerically: the incidence matrix $[D_a\mid D_b]$ drops from full rank to rank $R_1$, confirming confounding.) Any general theorem must exclude such collinear observation patterns.

**Role in the paper.** Supplies the missing existence/growth statement behind the standing assumption "$|\tilde{\mathcal S}|\to\infty$" in the slice-cramér theorem — the sentence the draft leaves cut off ("Clearly under perfect balance we get the appropriate decay condition, but …"). It gives a clean constructive sufficient condition, isolates the sparsest-category obstruction, and records the degeneracy that forces a richness assumption. The general near-balanced sufficient condition is the paper's main remaining theoretical gap ([[Sufficient Conditions for Cramer Consistency]]).
