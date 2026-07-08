---
type: definition
aliases:
  - co-occurrence graph richness
  - observation richness
  - richness assumption for k-crossed designs
tags:
  - crossed
  - genai/claude
  - research
  - stanford/y2
modified: 2026-07-07T23:48:48-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Observation Richness for $K$-Crossed Designs
>
> For a design $\mathcal S\subseteq\mathcal I=[R_1]\times\cdots\times[R_K]$, define for each pair $k\neq k'$ the **co-occurrence graph** $G_{kk'}$: a bipartite graph on $[R_k]\sqcup[R_{k'}]$ with an edge $(i_k,i_{k'})$ iff some observed cell has those two labels. Write $d_{k\to k'}(i)=\deg_{G_{kk'}}(i)$ and, for a slice $\mathcal K$, let $H_i$ be the bipartite graph between the complement labels co-occurring with slice level $i$, with **matching number** $\nu_i$ (for $K=3$, $\mathcal K=\{1\}$: edges are observed cells $(i,j,k)$, viewed as $j$–$k$ pairs). The richness conditions, ordered weakest to strongest:
>
> - **(OR-0, no married pair — identification-necessary flavor)** For every pair $k\neq k'$: $\#\{i\in[R_k]:d_{k\to k'}(i)\ge2\}\to\infty$.
> - **(OR-1, rank form)** For every pair, the number of connected components $c_{kk'}$ of $G_{kk'}$ satisfies $c_{kk'}=o\!\left(\min(R_k,R_{k'})\right)$; equivalently (Lemma below) $\mathrm{rank}\,[D_k\mid D_{k'}]=R_k+R_{k'}-c_{kk'}$ stays within $o(\cdot)$ of its maximum $R_k+R_{k'}-1$.
> - **(OR-2, matching form — powers the constructive existence)** For slice $\mathcal K$, there is $S_N\to\infty$ and levels $i_1,\dots,i_{S_N}$ with $\nu_{i_s}\ \ge\ 4S_N+2$ for all $s$.
^observation-richness

> [!success]- Lemma (rank–component identity) and proof
>
> Let $D_k\in\{0,1\}^{N\times R_k}$ be the membership (incidence) matrices. Then
> $$\mathrm{rank}\,[D_k\mid D_{k'}]\ =\ R_k+R_{k'}-c_{kk'},$$
> where $c_{kk'}$ counts connected components of $G_{kk'}$ (restricted to observed levels).
>
> *Proof.* A vector $(u,v)\in\mathbb R^{R_k}\times\mathbb R^{R_{k'}}$ is in the kernel iff $u_{i_k(\ell)}+v_{i_{k'}(\ell)}=0$ for every observation $\ell$, i.e. iff $u_i=-v_j$ along every edge of $G_{kk'}$. Walking along a path alternates the constraint back and forth, forcing $u$ constant $=c$ and $v$ constant $=-c$ on each connected component. Hence the kernel has one free constant per component: nullity $=c_{kk'}$, and the identity follows from rank–nullity. $\blacksquare$
>
> *(Numerically verified — random design and diagonal design both match; script: [[Isolating Subset Existence - validation (greedy near-balanced).py]], Part C.)*

> [!success]- Proposition (married categories are unidentifiable) and proof
>
> Call $k,k'$ **married on $\mathcal S$** if every observed level of $k$ co-occurs with exactly one level of $k'$ and vice versa ($G_{kk'}$ a perfect partial matching, $c_{kk'}=R_k=R_{k'}$; the diagonal design $(i,i,k)$ of [[Existence of an Isolating Subset for Slice Consistency#^isolating-subset|Remark 2]] is the canonical case). If $k,k'$ are married, then the law of the data depends on $(\sigma^2_k,\sigma^2_{k'})$ only through $\sigma^2_k+\sigma^2_{k'}$, so the two components are **not separately identified** and no isolating subset for $\{k\}$ or $\{k'\}$ can exist.
>
> *Proof.* Under marriage with matching $i\mapsto m(i)$, the effects enter every linear predictor as the sum $a^{(k)}_i+a^{(k')}_{m(i)}\sim\mathcal N(0,\sigma^2_k+\sigma^2_{k'})$, i.i.d. across matched pairs. Any $(\sigma^2_k,\sigma^2_{k'})$ with the same sum induces the same joint law of these sums, hence of all observables. The rank drop of the Lemma ($\mathrm{rank}=R_k$) is the finite-sample witness. $\blacksquare$

> [!note]- Connection to the tree-crawl diagnostic
>
> The crawl sketched in [[Sufficient Conditions for Cramer Consistency]] walks the subset lattice comparing distinct-cell counts $|\mathcal S[\mathcal K]|$ down cardinality. The pairwise step is exactly an OR-0 check: since $|\mathcal S[\{k,k'\}]|=\sum_i d_{k\to k'}(i)$ (edges counted from the $k$ side, in the simple-graph sense),
> $$|\mathcal S[\{k,k'\}]|-|\mathcal S[\{k\}]|\ =\ \sum_i\big(d_{k\to k'}(i)-1\big)\ \ge\ \#\{i:d_{k\to k'}(i)\ge2\},$$
> so a **zero cardinality gap** at the pair level is precisely marriage of $k$ and $k'$ — this is what catches the $(i,i,k)$ case, answering the "don't know if it's doing that" worry in the note. The crawl's higher levels ($N_{\boldsymbol i,[K]}$ spikes = replicates, then $N_{\boldsymbol i,\neg k}$, …) sit above this in the same lattice; the identification content lives at the pairwise level, while OR-2 (matching numbers $\nu_i$) is the quantitative refinement the constructive existence theorem consumes. Computing all pairwise gaps is $O(N\binom K2)$ with hashing — cheap; per-level $\nu_i$ is a bipartite matching per level, still polynomial.

> [!note]- Proposed assumption text for the paper (extends the base block)
>
> *(Observation richness).* For every pair $k\neq k'$, the co-occurrence graph $G_{kk'}$ has $c_{kk'}=o(\min(R_k,R_{k'}))$ connected components; and for every slice $\mathcal K\in\mathbb A$ used for estimation there exist $S_N\to\infty$ levels whose complement-label graphs admit matchings of size at least $4S_N+2$.
>
> The first clause rules out (asymptotic) marriage — the degeneracy that is *necessary* to exclude; the second is the *sufficient* strength under which [[Existence of Isolating Subsets in the Near-Balanced Regime#^near-balanced-existence|isolating subsets exist]]. Under the sampling model both hold w.h.p., so the assumption is only binding for adversarial fixed designs.

**Hierarchy.** OR-2 $\Rightarrow$ OR-0 for the pairs meeting $\mathcal K$ (a matching of size $\ge2$ at level $i$ gives $d(i)\ge2$); OR-0 and OR-1 are close but not identical (OR-1 additionally limits *how many* islands the design fragments into). None of these follow from the decay conditions $\epsilon_{\mathcal K}\to0$ — the diagonal design can have perfectly balanced, decaying counts and still be degenerate, which is why richness must be a **separate** assumption.

**Role in the paper.** Answers objection B8 of [[Reviewer Objections and Next Steps (K-Crossed Probit Paper)]]: gives the explicit "observation richness" assumption whose necessity is shown by the degeneracy counterexample ([[Existence of an Isolating Subset for Slice Consistency]] Remark 2, rank drop to $R_1$ now explained by the rank–component identity), and formalizes the tree-crawl diagnostic of [[Sufficient Conditions for Cramer Consistency]] as the empirical check of the same condition. Consumed by [[Existence of Isolating Subsets in the Near-Balanced Regime]].
