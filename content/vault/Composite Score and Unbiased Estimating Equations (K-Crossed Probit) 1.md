---
type: lemma
aliases: [composite score and unbiased estimating equations, mean-zero composite score k-crossed probit]
tags: [crossed, genai/claude, research, rewrite-human, stanford/y2]
modified: 2026-07-07T21:27:08-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Composite Score and Unbiased Estimating Equations (K-Crossed Probit)
>
> The composite score $U(\psi)=\omega_{\mathrm{all}}U_{\mathrm{all}}+\sum_{\mathcal K}\omega_{\mathcal K}U_{\mathcal K}$ has the following components, each **mean-zero at the truth** (so $\hat\psi$ solves an unbiased estimating equation):
> - **All-score** (in $\gamma$ only):
> $$U_{\mathrm{all}}(\gamma)=\sum_{\ell=1}^N s_\ell(\gamma)\,x_\ell,\qquad s_\ell(\gamma)=\frac{\tilde y_\ell\,\varphi(x_\ell^{\mathsf T}\gamma)}{\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)},\qquad \mathbb E_{\psi_0}[s_\ell]=0.$$
> - **Slice-$\mathcal K$ score** (in $(\gamma,\rho_{\mathcal K})$), a sum of independent per-slice terms with $u\sim\mathcal N(0,1)$ and $\gamma_{\mathcal K}=\gamma/\sqrt{1-\rho_{\mathcal K}}$, $\tau_{\mathcal K}=\sqrt{\rho_{\mathcal K}/(1-\rho_{\mathcal K})}$:
> $$U_{\mathcal K}=\sum_{\boldsymbol j\in\pi_{\mathcal K}(\mathcal S_0)}\nabla\log L_{\boldsymbol j},\qquad L_{\boldsymbol j}=\int_{\mathbb R}\prod_{\ell\mid\boldsymbol j}\Phi\!\big(\tilde y_\ell(x_\ell^{\mathsf T}\gamma_{\mathcal K}+\tau_{\mathcal K}u)\big)\varphi(u)\,du,\qquad \mathbb E_{\psi_0}[\nabla\log L_{\boldsymbol j}]=0.$$
^composite-score

> [!success]- Proof
>
> **All-score form.** $\partial_\gamma\log\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)=\dfrac{\varphi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)\,\tilde y_\ell x_\ell}{\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)}$, and $\varphi$ even gives $\varphi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)=\varphi(x_\ell^{\mathsf T}\gamma)$; summing gives $U_{\mathrm{all}}$.
>
> **Mean-zero (all).** With $\eta=x_\ell^{\mathsf T}\gamma_0$, $\mathbb P(\tilde y_\ell=+1)=\Phi(\eta)$, so
> $$\mathbb E[s_\ell]=(+1)\frac{\varphi(\eta)}{\Phi(\eta)}\Phi(\eta)+(-1)\frac{\varphi(\eta)}{\Phi(-\eta)}\Phi(-\eta)=\varphi(\eta)-\varphi(\eta)=0.$$
> This is the first Bartlett identity for the correctly-specified marginal ([[Bartlett Identities]]); it is why the composite (dependence-ignoring) equation is still unbiased.
>
> **Slice-score form and mean-zero.** By Fisher's identity, $\nabla\log L_{\boldsymbol j}=\mathbb E_{u\mid Y_{\boldsymbol j}}\big[\nabla\log\big(\varphi(u)\prod_{\ell\mid\boldsymbol j}\Phi(\cdot)\big)\big]$, the posterior mean of the complete-data score. Because the slice submodel restricted to a valid slice is the **correctly specified** likelihood of an equicorrelated probit cluster ([[Regularity of the Slice Submodel (Equicorrelated Probit)#^slice-regularity|regularity lemma]]), the first Bartlett identity gives $\mathbb E_{\psi_0}[\nabla\log L_{\boldsymbol j}]=0$. Independence across slices $\boldsymbol j$ (under the isolating structure) makes $U_{\mathcal K}$ a sum of independent mean-zero terms.
>
> **Stacking.** $U=\omega_{\mathrm{all}}U_{\mathrm{all}}+\sum_{\mathcal K}\omega_{\mathcal K}U_{\mathcal K}$ is a linear combination of mean-zero components, hence mean-zero. $\blacksquare$

> [!note]- Remark — which coordinates carry which score
> $U_{\mathrm{all}}$ loads **only** the $\gamma$-block (the all-likelihood does not see any $\rho$). $U_{\mathcal K}$ loads the $\gamma$-block and the single $\rho_{\mathcal K}$-block. So in $\psi=(\gamma,\{\rho_{\mathcal K}\})$ the stacked score has an **arrow pattern**: dense in $\gamma$, one private variance coordinate per slice. This is the structure exploited in [[Sensitivity Matrix H for the K-Crossed Composite Estimator]] and [[Variability Matrix J for the K-Crossed Composite Estimator]].

**Role in the paper.** Supplies the score objects and the unbiasedness that make the [[Godambe Sandwich for the K-Crossed Composite Estimator#^godambe-sandwich|sandwich]] valid and $\hat\psi$ consistent. Reuses the correct-specification facts from [[Population Identification of gamma for the All Likelihood]] and [[Regularity of the Slice Submodel (Equicorrelated Probit)]].
