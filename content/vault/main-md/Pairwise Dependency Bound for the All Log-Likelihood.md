---
type: lemma
aliases: [inclusion-exclusion variance bound for the all log-likelihood, pairwise dependency bound]
tags: [crossed, genai/claude, research, stanford/y2]
modified: 2026-07-07T23:49:35-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Pairwise Dependency Bound for the All Log-Likelihood
>
> Let $\eta_\ell(\gamma)=\log\Phi(\tilde y_\ell x_\ell^{\mathsf T}\gamma)$ with $|\eta_\ell|\le B$ (guaranteed on compact $\gamma$-sets by bounded covariates). In the [[K-Crossed Random Effects Probit Model]], two summands $\eta_\ell,\eta_{\ell'}$ are dependent **only if** the units share at least one category level. Consequently
> $$\mathrm{Var}\!\left(\frac{\mathcal L_{\mathrm{all}}(\gamma)}{N}\right)\ \le\ \frac{2^{K-1}B^{2}}{N^{2}}\sum_{k=1}^{K}\sum_{i_k=1}^{R_k}N_{i_k,k}^{2}\ \le\ B'^{2}\sum_{k=1}^{K}\epsilon_k,$$
> where $\epsilon_k=\max_{i_k}N_{i_k,k}/N$. Hence $\max_{k}\epsilon_k\to0$ (equivalently $\sum_k\epsilon_k\to0$) implies $\mathrm{Var}(\mathcal L_{\mathrm{all}}/N)\to0$.
^dep-bound

> [!success]- Proof
>
> **Dependency structure.** $\eta_\ell$ is a function of $(x_\ell,Y_\ell)$, and $Y_\ell,Y_{\ell'}$ are independent unless they share a random effect, i.e. unless $\pi_{\{k\}}(\boldsymbol i(\ell))=\pi_{\{k\}}(\boldsymbol i(\ell'))$ for some $k$. Write $D_{\ell\ell'}=\mathbf 1[\exists\,k:\ i_k(\ell)=i_k(\ell')]$. Then $\mathrm{Cov}(\eta_\ell,\eta_{\ell'})=0$ whenever $D_{\ell\ell'}=0$, and $|\mathrm{Cov}(\eta_\ell,\eta_{\ell'})|\le B^{2}$ always (bounded summands). Thus
> $$\mathrm{Var}\!\left(\tfrac1N\mathcal L_{\mathrm{all}}\right)=\frac1{N^2}\sum_{\ell,\ell'}\mathrm{Cov}(\eta_\ell,\eta_{\ell'})\ \le\ \frac{B^2}{N^2}\sum_{\ell,\ell'}D_{\ell\ell'}.$$
>
> **Inclusion–exclusion / union bound.** By inclusion–exclusion on the shared-level events $A_k=\{i_k(\ell)=i_k(\ell')\}$,
> $$D_{\ell\ell'}=\mathbf 1\Big[\bigcup_k A_k\Big]=\sum_{\varnothing\neq\mathcal K\subseteq[K]}(-1)^{|\mathcal K|+1}\prod_{k\in\mathcal K}\mathbf 1[i_k(\ell)=i_k(\ell')].$$
> This is the [[Inclusion-Exclusion Factorization|inclusion–exclusion factorization]]. Retaining only the first-order (union-bound) terms gives the upper bound $D_{\ell\ell'}\le\sum_{k=1}^{K}\mathbf 1[i_k(\ell)=i_k(\ell')]$; the higher-order terms are dominated because each product $\prod_{k\in\mathcal K}\mathbf 1[\cdots]\le\mathbf 1[i_{k_0}(\ell)=i_{k_0}(\ell')]$ for any $k_0\in\mathcal K$, and there are at most $2^{K-1}$ subsets containing a fixed $k_0$; hence $D_{\ell\ell'}\le 2^{K-1}\sum_k\mathbf 1[i_k(\ell)=i_k(\ell')]$.
>
> **Pair counting.** Summing the union bound over ordered pairs collapses to level-wise squared counts:
> $$\sum_{\ell,\ell'}\mathbf 1[i_k(\ell)=i_k(\ell')]=\sum_{i_k=1}^{R_k}N_{i_k,k}^{2},$$
> since $N_{i_k,k}=\#\{\ell:i_k(\ell)=i_k\}$ (see [[K-Crossed Random Effects Model]] for the count objects). Therefore
> $$\mathrm{Var}\!\left(\tfrac1N\mathcal L_{\mathrm{all}}\right)\le\frac{2^{K-1}B^2}{N^2}\sum_{k}\sum_{i_k}N_{i_k,k}^2.$$
>
> **Decay.** Bound one factor of each square by its max, $N_{i_k,k}\le N\epsilon_k$, and use $\sum_{i_k}N_{i_k,k}=N$:
> $$\frac{1}{N^2}\sum_{i_k}N_{i_k,k}^2\le\frac{N\epsilon_k}{N^2}\sum_{i_k}N_{i_k,k}=\epsilon_k.$$
> Summing over $k$ and absorbing $2^{K-1}B^2$ into $B'^2$ gives $\mathrm{Var}(\mathcal L_{\mathrm{all}}/N)\le B'^2\sum_k\epsilon_k\to0$. $\blacksquare$

**Remark (why the union bound, not the signed expansion).** The signed inclusion–exclusion expansion is exact for the *count* of dependent pairs, but for the variance bound we only need an **upper** bound on $\sum D_{\ell\ell'}$, so the first-order union bound suffices and avoids tracking signs. The exact signed form is the right tool if one later wants a matching lower bound / a sharp dependency-graph constant.

**Role in the paper.** Makes rigorous the middle display of the proof of [[Consistency of All Likelihood for K-Crossed Random Effects Probit Model#^all-consistency|Theorem (all-consistency)]], where the inclusion–exclusion step currently appears with an ambiguous sign. Pairs with [[Concavity of the All Log-Likelihood (K-Crossed Probit)#^all-concavity|concavity]] and [[Population Identification of gamma for the All Likelihood#^gamma-identification|identification]].
