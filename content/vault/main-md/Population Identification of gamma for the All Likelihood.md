---
type: lemma
aliases: [population identification of gamma, unique population maximizer of the all likelihood]
tags: [crossed, genai/claude, research, stanford/y2]
modified: 2026-07-01T00:00:00-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Population Identification of $\gamma$ for the All Likelihood
>
> In the [[K-Crossed Random Effects Probit Model]], the marginal law of each response is correctly specified as $\mathbb P(Y_\ell=y_\ell\mid x_\ell)=\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma_0)$ with $\gamma_0=\beta/\sigma$ (the [[K-Crossed Marginal Probit Likelihood|marginal collapse]]). Under bounded covariates, nondegeneracy $N^{-1}\sum_\ell x_\ell x_\ell^{\mathsf T}\to V\succ0$, and no perfectly separating hyperplane, the population criterion
> $$M(\gamma)=\lim_N\frac1N\sum_{\ell}\mathbb E\big[\log\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)\big]$$
> has $\gamma_0$ as its **unique** maximizer over $\mathbb R^{p}$.

^gamma-identification

> [!success]- Proof
>
> **$\gamma_0$ is a maximizer (information inequality).** Because the marginal of $Y_\ell$ is exactly $\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma_0)$, each summand of $M$ is, up to an additive constant, the negative cross-entropy between the true marginal $p_{0,\ell}=\Phi(x_\ell^{\mathsf T}\gamma_0)$ and the model marginal $p_\ell(\gamma)=\Phi(x_\ell^{\mathsf T}\gamma)$:
> $$m_\ell(\gamma):=\mathbb E\big[\log\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)\big]=p_{0,\ell}\log p_\ell(\gamma)+(1-p_{0,\ell})\log(1-p_\ell(\gamma)).$$
> By Gibbs' inequality, $m_\ell(\gamma)\le m_\ell(\gamma_0)$ with equality iff $p_\ell(\gamma)=p_{0,\ell}$, i.e. iff $x_\ell^{\mathsf T}\gamma=x_\ell^{\mathsf T}\gamma_0$. Summing, $M(\gamma)\le M(\gamma_0)$, so $\gamma_0$ maximizes $M$. (This is why the *composite* all-likelihood — which ignores dependence — still targets the correct $\gamma_0$: only the marginal, not the joint, must be correctly specified.)
>
> **Uniqueness (identifiability).** Equality $M(\gamma)=M(\gamma_0)$ requires $x_\ell^{\mathsf T}(\gamma-\gamma_0)=0$ for (asymptotically almost) all design points. Set $v=\gamma-\gamma_0$. Then
> $$v^{\mathsf T}\Big(\tfrac1N\sum_\ell x_\ell x_\ell^{\mathsf T}\Big)v=\tfrac1N\sum_\ell (x_\ell^{\mathsf T}v)^2\to v^{\mathsf T}Vv.$$
> If the equality set has limiting mass, the left side $\to0$, forcing $v^{\mathsf T}Vv=0$; since $V\succ0$ this gives $v=0$, i.e. $\gamma=\gamma_0$. Hence the maximizer is unique.
>
> **Finiteness of the maximizer.** The no-separating-hyperplane condition rules out a direction $v$ with $\tilde y_\ell x_\ell^{\mathsf T}v\ge0$ for all $\ell$; along any such $v$, $\|\gamma\|\to\infty$ would keep $\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)$ nondecreasing and drive the objective to its supremum at infinity. Excluding separation keeps the argmax in a compact set, so the strictly concave (by [[Concavity of the All Log-Likelihood (K-Crossed Probit)#^all-concavity|concavity lemma]]) $M$ attains its unique maximum at the interior point $\gamma_0$. $\blacksquare$

**Role in the paper.** Discharges the clause "$\gamma_0$ is a maximizer of the limiting log-likelihood … we thus get that $\gamma$ is a unique maximizer" in [[Consistency of All Likelihood for K-Crossed Random Effects Probit Model#^all-consistency|Theorem (all-consistency)]]. The three design conditions map to: correctness of the target (marginal collapse), uniqueness (nondegeneracy $V\succ0$), and interiority (no separation).
