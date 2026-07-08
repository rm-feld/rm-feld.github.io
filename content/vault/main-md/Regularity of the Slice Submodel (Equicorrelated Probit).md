---
type: lemma
aliases: [regularity of the slice submodel, slice restricted to isolating subset is equicorrelated probit]
tags: [crossed, genai/claude, research, stanford/y2]
modified: 2026-07-01T00:00:00-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Regularity of the Slice Submodel (Equicorrelated Probit)
>
> Let $\tilde{\mathcal S}\subseteq\mathcal S_0$ satisfy the inter-/intra-slice isolation conditions of [[Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model#^slice-cramer-consistency|Theorem (slice-cramér)]] for a slice $\mathcal K$. Then, with $\gamma_{\mathcal K}$ held at its (consistent) value, the $\mathcal K$-slice likelihood restricted to $\tilde{\mathcal S}$ is **exactly the likelihood of a one-way random-intercept (equicorrelated) probit model**: independent clusters indexed by $\boldsymbol j\in\pi_{\mathcal K}(\tilde{\mathcal S})$, cluster sizes $\tilde N_{\boldsymbol j,\mathcal K}\ge2$, latent intra-cluster correlation $\rho_{\mathcal K}=\tau^2_{\mathcal K}/(1+\tau^2_{\mathcal K})$. This one-parameter family in $\tau^2_{\mathcal K}$ is **regular**: correctly specified on $\tilde{\mathcal S}$, smooth in $\tau^2_{\mathcal K}$, and identifiable.

^slice-regularity

> [!success]- Proof
>
> **Factorization into independent clusters.** By inter-slice isolation (condition 1) together with the disjointness enforced by condition 2, no category level of the complement $\mathcal K^{c}$ is shared across two distinct slices $\boldsymbol j\neq\boldsymbol j'$; and units in different slices differ in their $\mathcal K$-index. Hence two units in different slices share **no** random effect and are independent. The restricted likelihood therefore factorizes as $\prod_{\boldsymbol j\in\pi_{\mathcal K}(\tilde{\mathcal S})}L_{\boldsymbol j}$ over independent clusters. Numerically (see verification script): the induced latent covariance is block-diagonal, with within-slice off-diagonal entries equal to $\sigma^2_{\Sigma\mathcal K}$ only and zero across slices.
>
> **Each cluster is an equicorrelated probit likelihood.** Within a slice $\boldsymbol j$, intra-slice isolation (condition 2) ensures the units share only the single slice effect $a_{\Sigma\mathcal K}=\tau_{\mathcal K}u_{\boldsymbol j}$, $u_{\boldsymbol j}\sim\mathcal N(0,1)$, so from the [[K-Crossed Slice Probit Likelihood|slice derivation]],
> $$L_{\boldsymbol j}(\tau^2_{\mathcal K})=\int_{\mathbb R}\prod_{\ell:\pi_{\mathcal K}(\boldsymbol i(\ell))=\boldsymbol j}\Phi\!\big(\tilde y_\ell(x_\ell^{\mathsf T}\gamma_{\mathcal K}+\tau_{\mathcal K}u_{\boldsymbol j})\big)\varphi(u_{\boldsymbol j})\,du_{\boldsymbol j},$$
> which is precisely the marginal likelihood of a probit model with exchangeable (equicorrelated) latent errors within the cluster, correlation $\rho_{\mathcal K}$. This is the model whose MLE Jiang's argument targets.
>
> **Regularity.** (i) *Correct specification*: the display is the true marginal of the responses in slice $\boldsymbol j$ under the generating model, restricted to $\tilde{\mathcal S}$. (ii) *Smoothness*: the integrand is $C^\infty$ in $\tau^2_{\mathcal K}$ and dominated (bounded by $1$), so $L_{\boldsymbol j}\in C^\infty$ by dominated convergence; scores/informations exist. (iii) *Identifiability*: for cluster size $\ge2$, the exchangeable pair probability $\mathbb P(Y_{\ell}=Y_{\ell'}=1\mid\boldsymbol j)=\int\Phi(\cdot)\Phi(\cdot)\varphi$ is strictly monotone in $\rho_{\mathcal K}$, hence $\tau^2_{\mathcal K}$ is identified from the within-cluster concordance. These are exactly the conditions under which [[@jiangSubsetArgumentConsistency2013]] gives a consistent root, invoked in [[@bellioSupplementaryMaterialConsistent]]. $\blacksquare$

**Role in the paper.** Discharges the phrase "Regularity of the likelihood" that appears (flagged with a `check` comment) in the proof of [[Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model#^slice-cramer-consistency|Theorem (slice-cramér)]]. It converts the abstract "regular likelihood" assumption into the concrete statement "the slice submodel is an equicorrelated probit likelihood," which is what makes the cited subset argument applicable. Existence of a qualifying $\tilde{\mathcal S}$ is [[Existence of an Isolating Subset for Slice Consistency#^isolating-subset|separately established]].
