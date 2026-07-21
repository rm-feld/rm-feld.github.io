---
modified: 2026-07-09
created: 2026-04-20T13:25:49-07:00
tags: [genai/claude]
---
The marginal likelihood for the [[K-Crossed Random Effects Probit Model|probit model]] can be given by
$$\begin{align*} \mathbb{P}(Y_{\ell} = y_{\ell} \mid x_{\ell}) &= \mathbb{P}\left( y_{\ell} \left[ x_{\ell}^{\intercal}\beta + a_{\ell}^{\intercal}\mathbf{1} + \varepsilon_{\ell} \right] > 0 \right) \\ 
&= \mathbb{P}\left( y_{\ell} \left[x_{\ell}^{\intercal}\beta + \sigma\xi \right] > 0 \right) \\ 
&= \mathbb{P}\left( \frac{y_{\ell}x_{\ell}^{\intercal}\beta}{\sigma } > -\xi\right) \\
&:= \Phi\left( y_{\ell}x_{\ell}^{\intercal}\gamma \right)
\end{align*}$$
for $\gamma = \sigma^{-1 / 2} \beta$. 

In turn, it is natural to define the all likelihood as 

$$\begin{align*} L_{\text{all}}(\gamma) := \prod_{\ell = 1}^{N} \Phi\left( y_{\ell}x_{\ell}^{\intercal}\gamma \right) \end{align*}$$
and corresponding log-likelihood 
$$\begin{align*} \mathcal{L}_{\text{all}}(\gamma) := \sum_{\ell = 1}^{N} \log \Phi\left( y_{\ell} x_{\ell}^{\intercal} \gamma \right)  .\end{align*}$$
