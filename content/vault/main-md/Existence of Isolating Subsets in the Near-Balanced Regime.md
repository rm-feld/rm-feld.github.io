---
type: theorem
aliases:
  - isolating subsets under sampling designs
  - near-balanced isolating subset existence
  - probabilistic existence of isolating subsets
tags:
  - crossed
  - genai/claude
  - research
  - stanford/y2
modified: 2026-07-07T23:36:49-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Existence of Isolating Subsets in the Near-Balanced Regime
>
> Work with $K=3$ and slice $\mathcal K=\{1\}$ (the general case is identical up to relabeling). Recall the four conditions of [[Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model#^slice-cramer-consistency|Theorem (slice-cramér)]] and the matching numbers $\nu_i$ of [[Observation Richness for K-Crossed Designs#^observation-richness|observation richness]].
>
> **(A) Deterministic version.** If there are $S=S_N\to\infty$ levels of category $1$ with $\nu_i\ge 4S+2$, then there exists $\tilde{\mathcal S}\subseteq\mathcal S$ consisting of $S$ disjoint $2$-cell partial-permutation blocks — satisfying conditions 2–4 of slice-cramér with $|\tilde{\mathcal S}|=2S$ and $|\tilde{\mathcal S}[\{1\}]|=S\to\infty$.
>
> **(B) Sampling version, near-balanced included.** Let the $N$ cells be drawn i.i.d. uniformly from $\mathcal I=[R_1]\times[R_2]\times[R_3]$ with $R_k=\Theta(N^{\kappa_k})$, $\kappa_k\in(0,1)$, $\sum_k\kappa_k>1$. Then with probability $\to1$ the hypothesis of (A) holds with
> $$S\ =\ \Big\lfloor \tfrac14\min\!\big(R_1,\ \tfrac{R_2}{2},\ \tfrac{R_3}{2}\big)\Big\rfloor\ =\ \Theta\!\big(\min_k R_k\big)\ =\ \Theta\!\big(N^{\min_k\kappa_k}\big).$$
> In particular the **near-balanced regime $\kappa_1=\kappa_2=\kappa_3$ is covered**, with $S=\Theta(N^{\kappa})$.
^near-balanced-existence

> [!success]- Proof of (A) (greedy off a matching)
>
> Process the qualifying levels in any order, maintaining the sets of used complement labels. When level $i$ is processed, at most $2S$ labels of category $2$ and at most $2S$ of category $3$ have been consumed. Fix a matching $M_i$ in $H_i$ of size $\nu_i\ge4S+2$: its cells have pairwise-distinct $j$-labels and pairwise-distinct $k$-labels. At most $2S$ of its cells are killed by a used $j$-label and at most $2S$ by a used $k$-label, so at least $2$ survive; any two surviving cells automatically have distinct $j$'s and distinct $k$'s (they belong to a matching). Take them as the block $B_i$ and mark their labels used.
>
> The resulting $\tilde{\mathcal S}=\bigcup_i B_i$ has: globally distinct complement labels across blocks and distinct labels within blocks (condition 2: each complement level appears in exactly one slice, and $|\tilde{\mathcal S}[\overline{\mathcal K}]|=2S=|\tilde{\mathcal S}[k]|$, $k\in\{2,3\}$); $\tilde N_{\boldsymbol j,\mathcal K}=2$ (condition 3); $|\tilde{\mathcal S}|=2S\to\infty$ (condition 4). $\blacksquare$

> [!success]- Proof of (B) (freshness + Chernoff + union bound)
>
> Set $S=\lfloor\frac14\min(R_1,R_2/2,R_3/2)\rfloor$ and run the greedy of (A) over levels of category $1$, but verify directly that each of the first $S$ processed levels yields a block (this is the same event as the hypothesis of (A) holding along the greedy path; a full matching of size $4S+2$ is not needed — two fresh cells suffice).
>
> **Counts.** $n_i\sim\mathrm{Bin}(N,1/R_1)$ with mean $N/R_1=\Theta(N^{1-\kappa_1})\to\infty$; by Chernoff, $\mathbb P\{n_i<N/(2R_1)\}\le e^{-N/(8R_1)}$.
>
> **Freshness.** Condition on the multiset of cells at level $i$: their $(j,k)$ labels are i.i.d. uniform on $[R_2]\times[R_3]$. At any point of the algorithm at most $2S\le R_2/4$ category-$2$ labels and $2S\le R_3/4$ category-$3$ labels are used globally, and at most $1$ of each is used within the current level before the second pick; so each successive cell at level $i$ is *fresh* (both labels unused globally and distinct from the level's first pick) with probability at least $1-\frac14-\frac14-\frac{2}{\min(R_2,R_3)}\ \ge\ \frac13$ for $N$ large, regardless of the past. The number of fresh cells among $n_i\ge N/(2R_1)$ stochastically dominates $\mathrm{Bin}(n_i,\tfrac13)$, so
> $$\mathbb P\{\text{level }i\text{ fails}\}\ \le\ e^{-N/(8R_1)}+\mathbb P\big\{\mathrm{Bin}(\lceil N/(2R_1)\rceil,\tfrac13)\le1\big\}\ \le\ 2e^{-cN^{1-\kappa_1}}.$$
>
> **Union bound.** Over the $S\le R_1=\Theta(N^{\kappa_1})$ levels processed, the failure probability is at most $\Theta(N^{\kappa_1})\cdot e^{-cN^{1-\kappa_1}}\to0$ since $\kappa_1<1$. Replicated cells (sampling collisions) never help nor hurt: the distinct-label requirement automatically excludes picking the same cell twice. $\blacksquare$
>
> *(Simulated: greedy succeeds $20/20$ — at the more aggressive target $S=\lfloor\frac12\min(R_1,R_2/2,R_3/2)\rfloor$, so the proof's constant $\frac14$ is conservative — at $\kappa=(0.45,0.45,0.45)$ for $R\in\{40,80,160\}$, $N\in\{3.6\mathrm{k},17\mathrm{k},79\mathrm{k}\}$, and the constructed subset's latent covariance is exactly block-equicorrelated — [[Isolating Subset Existence - validation (greedy near-balanced).py]], Parts A–B.)*

> [!warning]- The fork: condition 1 (full cover) must be weakened — and the obstruction is sharp
>
> **Pigeonhole lemma.** Conditions 1–3 as stated require every observed level of category $1$ to carry a block with $m\ge2$ cells whose complement labels are globally disjoint, which forces
> $$m\,|\mathcal S[\{1\}]|\ \le\ \min\big(|\mathcal S[\{2\}]|,|\mathcal S[\{3\}]|\big).$$
> Under near-balance ($R_1\asymp R_2\asymp R_3$, all levels observed w.h.p.) this is **impossible**. So no proof technique can rescue conditions 1–4 verbatim in the near-balanced regime: either weaken condition 1, or give up the regime.
>
> **Claim (weakening).** Condition 1 may be replaced by $|\tilde{\mathcal S}[\mathcal K]|\to\infty$ (growing number of isolated clusters, full cover not required); (A)/(B) then deliver slice consistency in the near-balanced regime.
>
> *Why I believe this.* Walking through the proof chain of [[Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model#^slice-cramer-consistency|slice-cramér]]: the Markov-bound telescoping uses (i) that the working slice model is a genuine joint pmf on all of $y$ (true regardless of cover — it is a product over all slices of genuine within-slice laws), (ii) that the working marginal on $y_{[1]}$ agrees with the true law of $y_{[1]}$ (this is exactly what intra-/inter-slice **isolation** of $\tilde{\mathcal S}$ buys, via [[Regularity of the Slice Submodel (Equicorrelated Probit)#^slice-regularity|the regularity lemma]]), and (iii) that the number of independent clusters in $y_{[1]}$ grows, so the subset likelihood-ratio at a fixed misspecified parameter $\to0$. Full cover enters none of (i)–(iii).
>
> **Check before relying on this** (flagged for a pass against `@bellioSupplementaryMaterialConsistent`): whether the conditional-expectation step ($2\to3$ in the displayed chain) is taken under the *working* conditional law of $y_{[2]}$ given $y_{[1]}$ or the *true* one. Note this concern is **at par with the existing constructive case**: even under $\kappa_1<\min(\kappa_2,\kappa_3)$ with full cover, cells outside $\tilde{\mathcal S}$ share complement levels with $\tilde{\mathcal S}$, so the true conditional never equals the working conditional there either. Whatever resolves it for Bellio–Owen resolves it here identically; condition 1 does not help with it.

> [!note]- Corollary — simultaneous recovery of all components under near-balance
>
> Run (B) once per singleton slice $\mathcal K=\{k\}$, $k=1,2,3$, obtaining $\tilde{\mathcal S}_1,\tilde{\mathcal S}_2,\tilde{\mathcal S}_3$ (they may overlap — each consistency statement is marginal, no joint construction needed). Each has $\Theta(\min_k R_k)$ clusters, so **all** of $\hat\sigma^2_1,\hat\sigma^2_2,\hat\sigma^2_3$ are consistent in the near-balanced regime, given the weakened condition 1. This dissolves the "sparsest-category obstruction" of [[Existence of an Isolating Subset for Slice Consistency#^isolating-subset|Remark 1]]: the obstruction was an artifact of demanding full cover, not a feature of the problem.

**Role in the paper.** Answers objection B2 of [[Reviewer Objections and Next Steps (K-Crossed Probit Paper)]]: (a) the near-balanced case is settled by (A)+(B) *modulo one explicitly-scoped weakening* of condition 1, with the pigeonhole lemma showing that weakening is unavoidable; (b) the sampling model asked for in the objection is exactly (B); (c) simultaneous recovery of all components follows. Consumes [[Observation Richness for K-Crossed Designs]] (OR-2 is the hypothesis of (A)); feeds the cluster-count $S_{\mathcal K}=\Theta(\min_k R_k)$ into [[Rates of Convergence for the K-Crossed Composite Estimator]].
