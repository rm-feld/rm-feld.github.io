---
type: lemma
aliases: [concavity of the all log-likelihood for k-crossed random effects probit model]
tags: [crossed, genai/claude, research, rewrite-human, stanford/y2]
modified: 2026-07-07T21:27:32-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Concavity of the All Log-Likelihood (K-Crossed Probit)
>
> For the [[K-Crossed Random Effects Probit Model]], both the sample all log-likelihood
> $$\mathcal L_{\mathrm{all}}(\gamma)=\sum_{\ell=1}^{N}\log\Phi\!\big(\tilde y_\ell\, x_\ell^{\mathsf T}\gamma\big)$$
> and its population counterpart $M(\gamma)=\lim_N N^{-1}\mathbb E\,\mathcal L_{\mathrm{all}}(\gamma)$ are concave in $\gamma\in\mathbb R^{p}$. Under the nondegeneracy condition $N^{-1}\sum_\ell x_\ell x_\ell^{\mathsf T}\to V\succ0$, both are **strictly** concave in the limit.
^all-concavity

> [!success]- Proof
>
> **Log-concavity of $\Phi$.** The standard normal CDF $\Phi$ is log-concave: $\big(\log\Phi\big)''(t)=-R(t)\big(t+R(t)\big)<0$ for all $t$, where $R(t)=\varphi(t)/\Phi(t)$ is the inverse Mills ratio (both factors positive since $R(t)>\max(0,-t)$). Hence $t\mapsto\log\Phi(t)$ is concave. See also [[Claude Unimodal Link Analysis]] Lemma 1 for the analogous $w$-parameterized statement. Numerically, $\sup_t(\log\Phi)''(t)\approx0^{-}$ (checked to $-1.9\times10^{-8}$ on a grid).
>
> **Composition.** For each $\ell$, $\gamma\mapsto\tilde y_\ell\,x_\ell^{\mathsf T}\gamma$ is affine and $\log\Phi$ is concave, so $\gamma\mapsto\log\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)$ is concave (concavity is preserved under affine precomposition). A sum of concave functions is concave, giving concavity of $\mathcal L_{\mathrm{all}}$; taking expectations and the limit preserves concavity, giving concavity of $M$.
>
> **Strictness.** The Hessian is
> $$\nabla^2\mathcal L_{\mathrm{all}}(\gamma)=\sum_{\ell}\big(\log\Phi\big)''\!\big(\tilde y_\ell x_\ell^{\mathsf T}\gamma\big)\,x_\ell x_\ell^{\mathsf T}\preceq0,$$
> with each scalar curvature strictly negative wherever $\tilde y_\ell x_\ell^{\mathsf T}\gamma\neq0$. On the design points, $-\nabla^2\mathcal L_{\mathrm{all}}(\gamma)\succeq c(\gamma)\sum_\ell x_\ell x_\ell^{\mathsf T}$ for a constant $c(\gamma)>0$ on compacta; since $N^{-1}\sum_\ell x_\ell x_\ell^{\mathsf T}\to V\succ0$, the limiting Hessian is negative definite, i.e. $M$ is strictly concave. $\blacksquare$

**Role in the paper.** This lemma discharges the clause "both sides of the limiting log likelihood statement are concave in $\gamma$" that is imported without proof from [[@bellioConsistentScalableComposite2025]] inside [[Consistency of All Likelihood for K-Crossed Random Effects Probit Model#^all-consistency|Theorem (all-consistency)]]. Combined with [[Population Identification of gamma for the All Likelihood#^gamma-identification|unique population maximizer]] and the [[Pairwise Dependency Bound for the All Log-Likelihood#^dep-bound|variance bound]], it yields consistency via the convexity/argmax lemma for concave processes.
