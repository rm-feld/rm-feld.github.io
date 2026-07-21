---
type: setup
aliases: [k-crossed random effects probit model]
tags: [crossed, research, stanford/y2, genai/claude]
modified: 2026-07-09
created: 2026-04-20T13:34:23-07:00
---

> [!attention] K-Crossed Random Effects Probit Model 
> The **Standard K-Crossed Random Effects Probit Model** can be given in latent variable form by
> $$\begin{align*} Y_{\ell} := 2\cdot\mathbf{1}\left[x_{\ell}^{\intercal}\beta + a_{\ell}^{\intercal}\mathbf{1} + \varepsilon_{\ell} > 0 \right] - 1 \in \left\{ -1, +1 \right\},  \end{align*}$$
> for $\varepsilon_{\ell} \overset{\mathrm{i.i.d.}}{\sim}\mathcal{N}(0, \sigma^{2}_{E})$. 

In this case, it can be helpful to invoke $\sigma^{2} := \sigma^{2}_{E} + \sum_{k=1}^{K} \sigma^{2}_{k}$ the total variance. Our interest is in the estimation of $\theta = \left( \beta ^{\intercal}, \sigma_{1}^{2}, \dots, \sigma_{K}^{2} \right)^{\intercal}$. 