---
modified: 2026-07-07T19:36:44-07:00
created: 2026-03-09T15:19:10-07:00
aliases:
  - Gaussian Mixture All Likelihood
tags:
  - to-atomize
---

# Mixture of Gaussians Link
Use $Y_{ij} \in \left\{ -1, 1 \right\}$, and let $g$ be a symmetric binary link for which the corresponding cdf (or its reasonable approximation) can be written as some mixture of gaussians, of the form 

$$\begin{align*} \Lambda(t) = \sum_{r = 1}^{k} p_{r}\Phi(s_{r}t).  \end{align*}$$

The marginal likelihood for the corresponding two random effects model is 
$$\begin{align*} f(y_{ij}) &= \int_{\mathbb{R}} \Lambda\left( y_{ij}\left[ x_{ij}^{\intercal}\beta + \sigma u_{ij} \right] \right) \varphi (u_{ij}) \, du_{ij} \\ 
&\approx \int_{\mathbb{R}} \sum_{r = 1}^{k} p_{r} \Phi\left( s_{r}y_{ij}\left[ x_{ij}^{\intercal}\beta + \sigma u_{ij} \right] \right) \varphi (u_{ij})  \, du_{ij} \\ 
&= \sum_{r = 1}^{k} p_{r} \int \Phi\left( s_{r}y_{ij}\left[ x_{ij}^{\intercal}\beta + \sigma u_{ij} \right] \right) \varphi (u_{ij})\, du_{ij} \\ 
&\overset{(\star)  }{ = } \sum_{r = 1}^{k} p_{r} \Phi\left( \frac{s_{r}y_{ij}x_{ij}^{\intercal}\beta}{\sqrt{ 1 + s_{r}^{2} \sigma^{2} }} \right) \\ 
&=: \sum_{r = 1}^{k}p_{r} \Phi(y_{ij}\tilde{\sigma}_{r} \tilde{\eta}_{ij}),\end{align*}$$
where $\tilde{\sigma}_{r} = s_{r} / \sqrt{ 1 + s_{r}^{2} \sigma^{2} }$, $\tilde{\eta}_{ij} = x_{ij}^{\intercal}\beta$. 

Note the approximation only comes from the normal substitution to $\Lambda(t)$; we are otherwise exact. $(\star)$ is immediate from probit convolution. 

We do not have shared scale, so we need to consider solving jointly for $(\beta, \sigma^{2})$. Note probit is the degenerate case where $s_{r} \equiv 1$ for all $s_{r}$; it is clear that, more generally, $s_{r}$ all equal is also fine, provided that it is (for now) known.

The log likelihood can be given by 
$$\begin{align*} \ell_{\text{all}}(\beta, \sigma^{2}) &=\sum_{ij}Z_{ij} \log \left\{ \sum_{r = 1}^{k} p_{r} \Phi \left( \frac{s_{r}y_{ij}x_{ij}^{\intercal}\beta}{\sqrt{ 1 + s_{r}^{2}\sigma^{2} }} \right) \right\}.\\
\end{align*}$$
Note termwise expectation
$$\begin{align*} \mathbb{E}[\cdot] &= \left( \sum_{r = 1}^{k} p_{r} \Phi\left( \frac{s_{r}x_{ij}^{\intercal}\beta_{0}}{\sqrt{ 1 + s_{r}^{2} \sigma_{0}^{2} }} \right) \right)\log \left\{ \sum_{r = 1}^{k} p_{r} \Phi\left( \frac{s_{r}x_{ij}^{\intercal}\beta}{\sqrt{ 1 + s_{r}^{2} \sigma^{2} }} \right) \right\}  + \left( \sum_{r = 1}^{k} p_{r} \Phi\left( -\frac{s_{r}x_{ij}^{\intercal}\beta_{0}}{\sqrt{ 1 + s_{r}^{2} \sigma_{0}^{2} }} \right) \right)\log \left\{ \sum_{r = 1}^{k} p_{r} \Phi\left( -\frac{s_{r}x_{ij}^{\intercal}\beta}{\sqrt{ 1 + s_{r}^{2} \sigma^{2} }} \right) \right\}.  \end{align*}$$


Under what conditions can we get that a unique maximizer exists for $(\beta, \sigma^{2})$? First, we need identifiability. 

> [!success]- Identifiability
> 
> 
> We would like to show that if 
> $$\begin{align*} \sum_{r} p_{r} \Phi\left( \frac{s_{r}x^{\intercal}\beta}{\sqrt{ 1 + s_{r}^{2} \sigma^{2} }} \right)  = \sum_{r} p_{r} \Phi\left( \frac{s_{r}x^{\intercal}\beta'}{\sqrt{ 1 + s_{r}^{2} \sigma'^{2} }} \right) \end{align*}$$
> for a.e. $x$, then $(\beta, \sigma) = (\beta', \sigma')$. We add assumptions as we go. A first assumption is that the above is non-constant in $x$; it is clear that as long as $p_{r}, s_{r}$ are nondegenerate, this should be true. 
> 
> Note we can write $\beta' = c \beta$, ie. that $\beta$ and $\beta'$ share direction. We verify by contradiction. If $\beta \neq \beta' \neq 0$, then there exists $v \in \mathbb{R}^{p}$ for which $v^{\intercal}\beta \neq 0$ and $v^{\intercal}\beta' = 0$. But then along the curve $(x_{0} + tv)$ for any fixed $x_{0}$, RHS is constant while LHS is not. If $\beta = 0$ or $\beta' = 0$ or vice versa, we also get this constant issue. So we must have $\beta = c \beta'$. #TODO check positivity? 
> 
> Having written $\beta' = c \beta$, let $\gamma$ be the corresponding unit vector. Then 
> 
> $$\begin{align*} \sum_{r} p_{r} \Phi\left( \frac{s_{r}\left\lvert\left\lvert \beta \right\rvert\right\rvert _{2}}{\sqrt{ 1 + s_{r}^{2} \sigma^{2} }} x^{\intercal}\gamma\right) = \sum_{r} p_{r} \Phi\left( \frac{s_{r}c \left\lvert\left\lvert \beta \right\rvert\right\rvert _{2}}{\sqrt{ 1 + s_{r}^{2} \sigma'^{2} }} x^{\intercal}\gamma\right).  \end{align*}$$
> Let $t:= x^{\intercal}\gamma$, and collect $b_{r} = s_{r} \left\lvert\left\lvert \beta \right\rvert\right\rvert_{2} / \sqrt{ 1 + s_{r}^{2} \sigma^{2} }$, $b_{r}'$ analogous (with $c$). Clearly we need $b_{r} = b_{r}'$ for this to hold for every $t$; 
> 
> $$\begin{align*} & \frac{s_{r} \left\lvert\left\lvert \beta \right\rvert\right\rvert _{2}}{\sqrt{ 1 + s_{r}^{2} \sigma^{2} }} = \frac{s_{r}c \left\lvert\left\lvert \beta \right\rvert\right\rvert_{2} }{\sqrt{ 1 + s_{r}^{2} \sigma'^{2} }} \\ 
> \implies &  \frac{1}{1 +s_{r}^{2} \sigma^{2}} = \frac{c^{2}}{1 + s_{r}^{2} \sigma'^{2}} \\ 
> \implies &1 + s_{r}^{2} \sigma'^{2} = c^{2}(1 + s_{r}^{2}\sigma^{2}) \\ 
> \implies & c^{2} =\frac{1 + s_{r}^{2}\sigma'^{2}}{1 + s_{r}^{2} \sigma^{2}} \\ 
> \implies& c^{2} -1 = \frac{s_{r}^{2}(\sigma'^{2} - \sigma^{2})}{1 + s_{r}^{2} \sigma^{2}}.\end{align*}$$
> For fixed $c$, LHS is constant but RHS varies with $r$. Thus when $k \neq 1$ and there exists $s_{r} \neq s_{\tilde{r}}$, we are assured that $c = 1$ and $\sigma' = \sigma$, as desired. If $k = 1$, we get the degenerate probit case and the non-identifiability is fine. 


%% Differentiating with respect to $t$, almost everywhere equality gives us

$$\begin{align*} \sum_{r} p_{r} b_{r}\varphi (b_{r}t) = \sum_{r}p_{r}b_{r}' \varphi (b_{r}'t).  \end{align*}$$
For change of variables $u = t^{2} / 2$ and multiplying both sides by $\sqrt{ 2\pi }$, 
$$\begin{align*} \sum_{r} p_{r} b_{r} \exp \left\{ -b_{r}^{2} u \right\} = \sum_{r} p_{r}b'_{r} \exp \left\{ -b_{r}'^{2} u \right\}.   \end{align*}$$
 %%

So the above objective is not concave, but it is identifiable, and there seems to be some hope for some $M$-estimate. In particular, the argument that $(\beta_{0}, \sigma_{0})$ is a zero of the score should go through, so an $M$ estimation statement should likely be fine. Some finesse may be needed. 

**If the above is additionally unimodal, then the weak consistency argument in the ARC paper supplemental should go through immediately. This will be sufficient to get the inverse weighting on rows statement to go through, since we're only reliant on bounded log likelihood components If not, we might be able to get a Cramer consistency statement since we have an identifiable parameter which is a zero of the maximization problem.** 

---

# Other Utilities
Writing out some of the standard objects, 

$$\begin{align*} \nabla_{\beta} \log \left\{ \sum_{r = 1}^{k} p_{r} \Phi\left( \frac{s_{r}y_{ij}x_{ij}^{\intercal}\beta}{\sqrt{ 1 + s_{r}^{2}\sigma^{2} }}\right) \right\}  &= \left[\sum_{r = 1}^{k} p_{r} \Phi(y_{ij}\tilde{\sigma}_{r} \tilde{\eta}_{ij})\right]^{-1} \left\{ \sum_{r = 1}^{k} \tilde{\sigma}_{r} y_{ij}x_{ij}p_{r} \varphi (\tilde{\sigma}_{r} \tilde{\eta}_{ij}) \right\} ,  \end{align*}$$

$$\begin{align*} \nabla_{\sigma^{2}} \log \left\{ \sum_{r = 1}^{k} p_{r} \Phi\left( \frac{s_{r}y_{ij}x_{ij}^{\intercal}\beta}{\sqrt{ 1 + s_{r}^{2}\sigma^{2} }}\right) \right\}  &= \left[\sum_{r = 1}^{k} p_{r} \Phi(y_{ij}\tilde{\sigma}_{r} \tilde{\eta}_{ij})\right]^{-1} \left\{ \sum_{r = 1}^{k} -\frac{p_{r}y_{ij}\tilde{\eta}_{ij}}{2}  \varphi (\tilde{\sigma}_{r} \tilde{\eta}_{ij}) \cdot (1 + s_{r}^{2}\sigma^{2})^{-3 / 2} s_{r}^{3} \right\} \\ 
&= f(y_{ij})^{-1} \left\{ \sum_{r = 1}^{k} -\frac{y_{ij}\tilde{\eta}_{ij}\tilde{\sigma}_{r}^{2}}{2} \varphi (\tilde{\sigma}_{r} \tilde{\eta}_{ij}) \right\}. \end{align*}$$


# Manski-Type Stuff

Let's branch and say that I have a way of estimating $\beta$ as a consistent direction, without knowledge of scale; wlog, we can consider $\gamma = \beta/ \left\lvert\left\lvert \beta \right\rvert\right\rvert_{2}$. Then we have 

$$\begin{align*} \ell_{\text{all}}(\sigma^{2}; \gamma) = \sum_{ij}Z_{ij} \log \left\{ \sum_{r = 1}^{k} p_{r} \Phi\left( \frac{s_{r}y_{ij}x_{ij}^{\intercal}\gamma \left\lvert\left\lvert \beta \right\rvert\right\rvert _{2}}{\sqrt{ 1 + s_{r}^{2} \sigma^{2} }}. \right) \right\}   \end{align*}$$
