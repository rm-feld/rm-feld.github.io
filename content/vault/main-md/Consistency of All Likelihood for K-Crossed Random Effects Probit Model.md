---
type: theorem
aliases:
  - consistency of all likelihood for k-crossed random effects probit model
tags:
  - crossed
  - research
  - stanford/y2
modified: 2026-07-07T21:28:02-07:00
created: 2026-04-20T15:45:27-07:00
---

> [!tip] Consistency of All Likelihood for K-Crossed Random Effects Probit Model
> 
> 
> Let $\left\{ (x_{\ell}, Y_{\ell}) \right\}_{\ell =1}^{N}$ follow the $k$-crossed random effects probit model with true parameter $\gamma_{0} = \beta / \sigma$. Let $N \to \infty$, while $\max_{k \in [K]} \epsilon_{k} \to 0$. Further, let us satisfy the following: 
> 1. **(Uniform Boundedness of $x_{\ell}$)** $\left\lvert\left\lvert x_{\ell} \right\rvert\right\rvert \leq B < \infty$, 
> 2. **(Nondegeneracy of $x_{\ell}$)** $N^{-1} \sum_{\ell=1}^{N} x_{\ell}x_{\ell}^{\intercal} \to V \in \mathbb{R}^{p\times p}$ [[Positive Semidefinite|positive definite]], 
> 3. **(No Linear Subspace)** there does not exist $v \in \mathbb{R}^{p}$ such that $v^{\intercal}x_{\ell} \geq 0$ for all $Y_{\ell} = 1$ and $v^{\intercal}x \leq 0$ for all $Y_{\ell} = 0$. 
> If $\hat{\gamma}$ is any maximizer of the [[K-Crossed Marginal Probit Likelihood|all likelihood]], Then we have [[Convergence in Probability|convergence in probability]] of $\hat{\gamma}$ to $\gamma_{0}$,
> $$\begin{align*} \mathbb{P}(\left\lvert\left\lvert \hat{\gamma} - \gamma_{0} \right\rvert\right\rvert  > \epsilon) \to  0 \end{align*}$$
> as $N \to \infty$. 
^all-consistency

> [!success]- %% %%
>
> 
> We follow the proof of $\gamma$ consistency as given in [[@bellioConsistentScalableComposite2025]]. Letting 
> $$\begin{align*} \eta_{\ell}(\gamma) := Y_{\ell} \log \Phi\left( x_{\ell}^{\intercal}\gamma  \right) + (1 - Y_{\ell}) \log \Phi\left( -x_{\ell}^{\intercal}\gamma \right),\end{align*}$$
> we have $\eta_{\ell}(\gamma) < B$ for some $B$ by the uniform boundedness condition on $x_{\ell}$. In this case
> $$\begin{align*} \text{Var}\left( \frac{\mathcal{L}_{\text{all}}(\gamma)}{N} \right)  &\leq \frac{B^{2}}{N^{2}} \sum_{\ell = 1}^{N} \sum_{\ell' = 1}^{N} \left\{ \sum_{\emptyset \neq \mathcal{K} \subseteq [K]} (-1)^{|\mathcal{K}|} \prod_{k \in \mathcal{K}} \mathbf{1}\left[i_{k}(\ell) = i_{k}(\ell')\right]  \right\}. \\
> 
> \end{align*}$$
> Note that the expansion of the incluson-exclusion nets at most $2^{K} -1$ terms (some negative); by the fact that $\mathbf{1}\left[i_{k} = i'_{k} \right] \geq \prod_{k'\in \mathcal{K}} \mathbf{1}\left[i_{k'} =i'_{k'} \right]$ when $k \in \mathcal{K}$, we can upper bound the inclusion-exclusion expansion. Following the logic, 
> 
> $$\begin{align*} \text{Var}\left( \frac{\mathcal{L}_{\text{all}}(\gamma)}{N} \right) &\leq \frac{B^{2}2^{K-1}}{N^{2}} \sum_{\ell =1}^{N} \sum_{\ell' =1}^{N}  \left\{ \sum_{k =1}^{K} \mathbf{1}\left[i_{k}(\ell) = i_{k}(\ell') \right]  \right\} \\ 
> &= \frac{B_{1}^{2}}{N^{2}} \sum_{k =1}^{K}\sum_{i_{k} =1}^{R_{k}} N_{i_{k}, k}^{2} \\
> &\leq \frac{B_{1}^{2}}{N^{2}} \sum_{k =1}^{K} \sum_{i_{k} =1}^{R_{k}} N_{i_{k}, k}N\epsilon_{k} \\ 
> &\leq B^{2} \left\{ \sum_{k=1}^{K}\epsilon_{k} \right\} \to  0. 
> \end{align*}$$
> Again by the proof in [[@bellioConsistentScalableComposite2025]], both sides of the limiting log likelihood statement are concave in $\gamma$, and $\gamma_{0}$ is a maximizer the limiting log-likelihood. We thus get that $\gamma$ is a unique maximizer. $\blacksquare$ 