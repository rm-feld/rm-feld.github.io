---
modified: 2026-04-24T10:13:08-07:00
created: 2026-04-20T13:25:49-07:00
---
The marginal likelihood for the [[K-Crossed Random Effects Probit Model|probit model]] can be given by
$$\begin{align*} \mathbb{P}(Y_{\ell} = y_{\ell} \mid x_{\ell}) &= \mathbb{P}\left( \tilde{y}_{\ell} \left[ x_{\ell}^{\intercal}\beta + a_{\ell}^{\intercal}\mathbf{1} + \varepsilon_{\ell} \right] > 0 \right) \\ 
&= \mathbb{P}\left( \tilde{y}_{\ell} \left[x_{\ell}^{\intercal}\beta + \sigma\xi \right] > 0 \right) \\ 
&= \mathbb{P}\left( \frac{\tilde{y}_{\ell}x_{\ell}^{\intercal}\beta}{\sigma } > -\xi\right) \\
&:= \Phi\left( \tilde{y}_{\ell}x_{\ell}^{\intercal}\gamma \right)
\end{align*}$$
for $\gamma = \sigma^{-1 / 2} \beta$. 

In turn, it is natural to define the all likelihood as 

$$\begin{align*} L_{\text{all}}(\gamma) := \prod_{\ell = 1}^{N} \Phi\left( \tilde{y}_{\ell}x_{\ell}^{\intercal}\gamma \right) \end{align*}$$
and corresponding log-likelihood 
$$\begin{align*} \mathcal{L}_{\text{all}}(\gamma) := \sum_{\ell = 1}^{N} \log \Phi\left( \tilde{y}_{\ell} x_{\ell}^{\intercal} \gamma \right)  .\end{align*}$$
