---
modified: 2026-02-22T21:21:59-08:00
created: 2026-02-22T19:35:49-08:00
---
# Perfect Diagonal (3 Random Effects) 
Let $\kappa_{1} = \kappa_{2}$, and consider the case where we follow the balance conditions of two random effects for $(i, k)$, but observe triples $(i, i, k)$. That is, we only ever observe $a_{i}$ or $b_{j}$ through the sum $a_{i} + b_{i}$. 

It is not difficult to observe that consistency of $\gamma$ inference is preserved; also unaffected is estimation of $\tau^{2}_{C}$, which collapses to the equivalent $k = 2$ ARC model where $c_{k}$ takes on the identity of the column effect, for $a_{i} + b_{i}$ the row effect. 

What fails, then, is the estimates of $\tau^{2}_{A}$ and $\tau^{2}_{B}$ the original row and column effects. As these cases are symmetric, we stick to $\tau^{2}_{A}$. 

Recall $\tau^{2}_{A}$ is found as the maximizer of the row (log)-likelihood 

$$\begin{align*} \ell_{A}(\tau^{2}_{A}) = \sum_{i = 1}^{R_{1}} \log \left\{ \int_{\mathbb{R}} \prod_{(j, k) \mid i} \Phi\left( y_{ijk}\left( x_{ijk}^{\intercal} \gamma \sqrt{ 1 + \tau^{2}_{A} }  + u_{i}\right) \right)\, \tau_{A}^{-1} \varphi \left( \frac{u_{i}}{\tau_{A}} \right) \, du_{i}  \right\} .  \end{align*}$$
However, since $j = i$, this again collapses to $k = 2$, so that optimal $\tau^{2}_{A}$ in this regime resolves to 
$$\begin{align*} \tau^{2}_{A} = \frac{\sigma^{2}_{A} + \sigma^{2}_{B}}{1 + \sigma^{2}_{C}} .\end{align*}$$
So what does this do to the backsolve? In implementation, we let $\tau^{2}_{A} = \frac{\rho_{A}}{ 1 - \rho_{A}}$, solve for $\rho_{A}$, and reconstitute with $\sigma^{2}_{A} = \rho_{A} / (1 - \rho_{A} - \rho_{B} - \rho_{C})$. Then from $\rho_{A} = \tau^{2}_{A} / (1 + \tau^{2}_{A})$, 

$$\begin{align*} \rho_{A} = \rho_{B} = \frac{\sigma^{2}_{A} + \sigma^{2}_{B}}{1 + \sigma^{2}_{C}} \cdot \left[ \frac{S}{1 + \sigma^{2}_{C}} \right]^{-1} = \frac{\sigma^{2}_{A} + \sigma^{2}_{B}}{S}, \end{align*}$$
and thus
$$\begin{align*} \hat{\sigma}^{2}_{A} = \hat{\sigma}^{2}_{B} &= \frac{\sigma^{2}_{A} + \sigma^{2}_{B}}{S} \cdot \left[ 1 - \frac{2(\sigma^{2}_{A} + \sigma^{2}_{B})}{S} - \frac{\sigma^{2}_{C}}{S} \right]^{-1} \\ 
&= \frac{\sigma^{2}_{A} + \sigma^{2}_{B}}{S} \cdot \left[ \frac{1 - \sigma^{2}_{A} - \sigma^{2}_{B}}{S} \right]^{-1} \\ 
&= \frac{\sigma^{2}_{A} + \sigma^{2}_{B}}{1 - \sigma^{2}_{A} - \sigma^{2}_{B}} \end{align*}$$
which is decently catastrophic. However, we do have some detection capability; namely, correctly inferred $\hat{\sigma}^{2}_{A}$ is never negative, but the above will be negative if $\sigma^{2}_{A} + \sigma^{2}_{B} > 1$. Though this event can happen, it's not necessarily a reliable indicator. I'll assume for now that it's smaller for interpretation purposes. 

Meanwhile,
$$\begin{align*} \hat{\sigma}^{2}_{C} = \frac{\sigma^{2}_{C}}{1 - \sigma^{2}_{A} - \sigma^{2}_{B}}.  \end{align*}$$
Checking behavior of the sum, we get that
$$\begin{align*} \hat{S} = \frac{1 - \sigma^{2}_{A} - \sigma^{2}_{B} + 2(\sigma^{2}_{A} + \sigma^{2}_{B}) + \sigma^{2}_{C}}{1 - \sigma^{2}_{A} - \sigma^{2}_{B}} = \frac{S}{1 - \sigma^{2}_{A} - \sigma^{2}_{B}}, \end{align*}$$
so the $\beta$ estimate will be inflated by $[1 - \sigma^{2}_{A} - \sigma^{2}_{B}]^{-1}$. 


