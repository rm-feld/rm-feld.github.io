---
type: theorem
aliases: [cluster-count rate for slice variance components, gamma-hat rate, rates of convergence for the k-crossed composite estimator]
tags: [crossed, genai/claude, OPEN, research, stanford/y2]
modified: 2026-07-06T12:58:04-07:00
created: 2026-07-01T00:00:00-07:00
---

# Rates of Convergence for the $K$-Crossed Composite Estimator

Upgrades the two $o_P(1)$ statements of the draft to explicit rates. Headline exponents (near-balanced, $\epsilon_k\asymp R_k^{-1}$, $R_k=\Theta(N^{\kappa_k})$):

$$\|\hat\gamma-\gamma_0\|=O_P\big(N^{-\min_k\kappa_k/2}\big),\qquad \hat\tau^2_{\mathcal K}-\tau^2_{\mathcal K,0}=O_P\big(S_{\mathcal K}^{-1/2}\big),\qquad S_{\mathcal K}=\Theta\big(N^{\min_k\kappa_k}\big),$$

i.e. **level-count rates, not $\sqrt N$** — and for the variance components this is *information-theoretically forced*, not an artifact of the estimator (Theorem R2 below). That is itself a finding the paper should state.

## Theorem R1 — rate for $\hat\gamma$ from the all likelihood

> [!tip] Theorem R1 ($\hat\gamma$ at the $\sqrt{\sum_k\epsilon_k}$ scale)
>
> Under the assumptions of [[Consistency of All Likelihood for K-Crossed Random Effects Probit Model#^all-consistency|Theorem (all-consistency)]],
> $$\|\hat\gamma-\gamma_0\|\ =\ O_P\Big(\sqrt{\textstyle\sum_{k=1}^{K}\epsilon_k}\Big),\qquad \epsilon_k=\max_{i_k}N_{i_k,k}/N.$$
> Under balanced levels ($\epsilon_k\asymp R_k^{-1}$) this is $O_P\big((\min_kR_k)^{-1/2}\big)$.

^gamma-rate

> [!success]- Proof (concave $M$-estimation, Hjort–Pollard style)
>
> Write $\mathbb M_N(\gamma)=\mathcal L_{\mathrm{all}}(\gamma)/N$, $M_N=\mathbb E\,\mathbb M_N$, $r_N^2=\sum_k\epsilon_k$, $u=\gamma-\gamma_0$.
>
> **(1) Exact stationarity and local strong concavity of $M_N$.** Each $m_\ell(\gamma)=\mathbb E\,\eta_\ell(\gamma)$ is the Bernoulli cross-entropy of [[Population Identification of gamma for the All Likelihood#^gamma-identification|the identification lemma]]; it is maximized at $\gamma_0$ term by term (correct marginals), so $\nabla M_N(\gamma_0)=0$ **exactly**, for every $N$. On a ball $\|u\|\le\delta_0$ the indices $|x_\ell^{\mathsf T}\gamma|\le B_x(\|\gamma_0\|+\delta_0)$ live in a compact set on which the index-curvature of $\log\Phi$ is bounded below ([[Concavity of the All Log-Likelihood (K-Crossed Probit)#^all-concavity|concavity lemma]]), so with $V_N=N^{-1}\sum_\ell x_\ell x_\ell^{\mathsf T}\to V\succ0$,
> $$M_N(\gamma_0)-M_N(\gamma)\ \ge\ \tfrac{\lambda}{2}\|u\|^2,\qquad \lambda=c\,\lambda_{\min}(V)>0,\ \ \|u\|\le\delta_0,\ N\ \text{large}.$$
>
> **(2) Score at the $r_N$ scale.** $\nabla\mathbb M_N(\gamma_0)$ has mean $0$ and bounded summand gradients; the pair-count argument of [[Pairwise Dependency Bound for the All Log-Likelihood#^dep-bound|the dependency bound]] applies verbatim coordinatewise (two gradient terms covary only if their units share a level), giving $\mathrm{Var}\big(\nabla\mathbb M_N(\gamma_0)\big)\preceq C\,r_N^2\,I$, hence $\|\nabla\mathbb M_N(\gamma_0)\|=O_P(r_N)$.
>
> **(3) Second-order remainder, uniformly on spheres.** Let $W_N(\gamma)=\big[\mathbb M_N-M_N\big](\gamma)-\big[\mathbb M_N-M_N\big](\gamma_0)-u^{\mathsf T}\nabla\big[\mathbb M_N-M_N\big](\gamma_0)$. Each summand's remainder is bounded by $L_2\|u\|^2$ and is Lipschitz in the direction with constant $O(\|u\|)$ (bounded second and third index-derivatives of $\log\Phi$ on compacta). Pointwise, the same pair-count bound gives $\mathrm{sd}\,W_N(\gamma)\le C\|u\|^2r_N$. On the sphere $\|u\|=r$, a direction-net of **constant** (in $N$) cardinality $O((C/\lambda)^p)$ with fineness $\propto\lambda r$ converts pointwise to uniform control at Chebyshev cost only, since the net fineness needed is proportional to the gap $\lambda r^2$ divided by the Lipschitz constant $O(r)$. Hence $\sup_{\|u\|=r}|W_N|=O_P(r^2r_N)=o_P(r^2)$.
>
> **(4) Assemble on the sphere $\|u\|=Mr_N$** (with $Mr_N\le\delta_0$; consistency puts $\hat\gamma$ in this ball w.h.p.):
> $$\mathbb M_N(\gamma)-\mathbb M_N(\gamma_0)\ \le\ -\tfrac\lambda2M^2r_N^2+Mr_N\cdot O_P(r_N)+o_P(M^2r_N^2)\ <\ 0$$
> with probability $\ge1-\varepsilon$ once $M=M(\varepsilon)$ is large. By **concavity** of $\mathbb M_N$, negativity on the sphere forces the maximizer inside: $\|\hat\gamma-\gamma_0\|\le Mr_N$. $\blacksquare$

> [!note]- Sharpness, and the validation
>
> The rate matches the [[Godambe Sandwich for the K-Crossed Composite Estimator#^godambe-sandwich|sandwich]]: $\mathrm{avar}(\hat\gamma)\asymp H^{-1}\mathrm{Var}(U/N)H^{-1}$ and $\mathrm{Var}(U/N)\asymp\sum_k\epsilon_k$ whenever some $\sigma^2_k>0$ (the shared-level score covariances are order-one per dependent pair and do not cancel in, e.g., the intercept direction). So $\sqrt{\sum_k\epsilon_k}$ is the exact scale, not just an upper bound. Numerically, $\mathrm{Var}(\mathcal L_{\mathrm{all}}/N)\cdot R$ stabilizes ($2.96,1.81,1.17,1.14\times10^{-2}$ at $R=10,20,40,80$, complete $R\times R$, $K=2$) — [[Rates - validation (score variance and cluster saturation).py]], Part A. It also matches the linear-ARC benchmark $\mathrm{Var}(\hat\beta)\asymp\max_kR_k^{-1}$ ([[Towards Optimal Weighting of the Crossed Random Effects Model]]).
>
> *Refinement left open:* covariate directions that vary freely within levels may converge faster than the intercept direction (as in the Gaussian case); the statement above is the worst-case direction. #OPEN

## Theorem R2 — cluster-count rate for slice components, with a matching lower bound

> [!tip] Theorem R2 (per-cluster information about $\tau^2$ saturates)
>
> Consider the equicorrelated-probit cluster model of [[Regularity of the Slice Submodel (Equicorrelated Probit)#^slice-regularity|the regularity lemma]]: independent clusters $j=1,\dots,S$, cluster $j$ observes $Y_{jt}=\operatorname{sign}(\mu_{jt}+\tau u_j+e_{jt})$, $t\le n_j$, $n_j\ge2$. Then:
>
> **(a) Lower bound (no estimator beats the cluster count).** The Fisher information about $\tau^2$ carried by one cluster satisfies, for every cluster size $n_j$,
> $$I_{\mathrm{cluster}}(\tau^2)\ \le\ \frac{1}{2\tau^4},$$
> so the total information is at most $S/(2\tau^4)$ and every regular estimator has $\mathrm{sd}(\hat\tau^2)\ \gtrsim\ \tau^2\sqrt{2/S}$ — **within-cluster replication cannot improve the rate.**
>
> **(b) Upper bound (the MLE achieves it).** With $n_j\ge2$ and non-degenerate means, $I_{\mathrm{cluster}}\ge c>0$ (identifiability via the strictly monotone concordance probability), so the cluster MLE satisfies $\hat\tau^2-\tau^2=O_P(S^{-1/2})$.
^cluster-count-rate

> [!success]- Proof
>
> **(a)** The cluster data $Y_j$ is a deterministic function of $(u_j,e_j)$, whose joint law depends on $\tau^2$ only through $u_j\sim\mathcal N(0,\tau^2)$. By the data-processing inequality for Fisher information (a statistic never carries more information than the data), $I_{Y_j}(\tau^2)\le I_{(u_j,e_j)}(\tau^2)=I_{u_j}(\tau^2)=\frac1{2\tau^4}$, the information of a single $\mathcal N(0,\tau^2)$ draw about its variance. Summing over independent clusters and applying the Cramér–Rao/LAN lower bound gives the claim. *(Intuition: even if the cluster revealed $u_j$ exactly, it is still only one draw from $\mathcal N(0,\tau^2)$.)*
>
> **(b)** For $n_j\ge2$ the pair concordance $\mathbb P(Y_{jt}=Y_{jt'}=1)$ is strictly increasing in $\rho=\tau^2/(1+\tau^2)$ ([[Regularity of the Slice Submodel (Equicorrelated Probit)]]), so the per-cluster information is bounded below on compact $\tau^2$-sets; the model is a smooth, identifiable one-parameter family over independent (non-identically-distributed, but uniformly regular) clusters, and standard MLE theory gives $\sqrt{\sum_jI_j}\,(\hat\tau^2-\tau^2)=O_P(1)$, i.e. the $S^{-1/2}$ rate. $\blacksquare$
>
> *(Validated: SD$(\hat\tau^2)$ at $\tau^2=0.5$: quadrupling $S$ halves the SD; growing $n$ from $8$ to $32$ barely helps, approaching the floor $\tau^2\sqrt{2/S}$ — observed $0.0438$ vs floor $0.0354$ at $S=400$, $n=32$. [[Rates - validation (score variance and cluster saturation).py]], Part B.)*

> [!warning]- Scope: subset-restricted vs full slice root #OPEN
>
> R2 applies verbatim to the estimator restricted to an isolating subset $\tilde{\mathcal S}$ — exactly the object [[Existence of Isolating Subsets in the Near-Balanced Regime#^near-balanced-existence|the existence theorem]] furnishes, with $S_{\mathcal K}=\Theta(\min_kR_k)$ clusters. The consistent root of the **full** slice likelihood uses all $N$ observations, but by R2(a) applied slice-wise its information is still at most $\big(\#\text{slices}\big)/(2\tau^4)\asymp R_{\mathcal K}/(2\tau^4)$ — the cluster-count ceiling holds for the full criterion too. What is *not* yet rigorous for the full root is the CLT normalization: cross-slice score covariance (slices sharing complement levels) must be controlled — the slice–slice blocks of [[Variability Matrix J for the K-Crossed Composite Estimator]]. Conjecture: same $R_{\mathcal K}^{-1/2}$ rate, constants improved over the subset estimator. Time-box per the sequencing note.

## Corollary R3 — rate for the composite estimand $\hat\theta$

> [!tip] Corollary R3
>
> Under R1, R2, and the conditions of [[Consistency of the Composite Estimator of theta#^theta-consistency|theta-consistency]], the back-solve $\Psi$ is Lipschitz on a neighborhood of $\psi_0$ (denominator bounded away from $0$), so
> $$\|\hat\theta-\theta_0\|\ =\ O_P\Big(\sqrt{\textstyle\sum_k\epsilon_k}\ +\ \max_{\mathcal K\in\mathbb A}S_{\mathcal K}^{-1/2}\Big)\ \overset{\text{near-bal.}}{=}\ O_P\big(N^{-\min_k\kappa_k/2}\big).$$
> The slice term dominates or ties: variance components are the rate bottleneck of the pipeline, at the cluster-count scale.
^theta-rate

**Role in the paper.** Answers objection B3 of [[Reviewer Objections and Next Steps (K-Crossed Probit Paper)]]. R1 gives the concave-$M$-estimation rate for $\hat\gamma$ governed by $\sum_k\epsilon_k$ and $\lambda_{\min}(V)$, as requested; R2 turns the "slice rides on the slower cluster-count rate" flag into a theorem *with a matching information-theoretic lower bound* (the quotable finding: replication inside slices buys constants, never rates); R3 propagates both through the back-solve. Consumes [[Pairwise Dependency Bound for the All Log-Likelihood]], [[Concavity of the All Log-Likelihood (K-Crossed Probit)]], [[Population Identification of gamma for the All Likelihood]], [[Regularity of the Slice Submodel (Equicorrelated Probit)]], [[Existence of Isolating Subsets in the Near-Balanced Regime]]; consistent with the numerical remark in [[Godambe Sandwich for the K-Crossed Composite Estimator]] that the crossed CLT is driven by level counts, not $N$.
