---
modified: 2026-07-09
created: 2026-04-20T15:08:43-07:00
tags: [genai/claude]
---

Under the structure of [[K-Crossed Slice Probit (Singular)|the derived slice likelihood]], we can take in particular $\mathcal{K} = \left\{ k \right\}$. In this case, 

$$\begin{align*} L_{k}(\tau^{2}_{k}) := \tau^{-R_{k}}\prod_{j=1}^{R_{k}} \int _{\mathbb{R}}  L_{j} (\gamma_{k}\mid u_{j})\,  \varphi \left( \frac{u_{j}}{\tau_{k}} \right) \, du_{j} \end{align*}$$
for
$$\begin{align*} L_{j} (\gamma_{k} \mid u_{j}) &= \prod_{\boldsymbol{i}_{\ell} \mid j} \Phi\left( x_{\ell}^{\intercal}\gamma_{k} + \tau_{k}u_{j} \right).  \end{align*}$$
In this formulation, we can write 
$$\begin{align*} \tau_{k}^{2} = \frac{\sigma^{2}_{k}}{\sigma^{2} - \sigma^{2}_{k}} \in [0, 1] .  \end{align*}$$
In implementation, we often invoke the one-to-one transformation $\rho_{k} = \tau^{2}_{k} / [1 + \tau^{2}_{k}]$, inverted by $\tau^{2}_{k} = \rho_{k} / [1 - \rho_{k}]$. What is nice in this case is that  ^c05d20
$$\begin{align*} \rho_{k} &= \frac{\sigma^{2}_{k} / [\sigma^{2} - \sigma^{2}_{k}]}{1 + \sigma^{2}_{k} / [\sigma^{2} - \sigma^{2}_{k}]} \\ 
&= \frac{\sigma^{2}_{k}}{\sigma^{2} - \sigma^{2}_{k} + \sigma^{2}_{k}} \\
&= \sigma^{2}_{k} / \sigma^{2}
. \end{align*}$$
^singular-rho

What is important in this regime is that $\psi = \left( \gamma ^{\intercal}, \rho_{1}, \dots, \rho_{K} \right)^{\intercal}$ is a valid reparameterization of $\theta$. From $\sum_{k=1}^{K} \rho_{k} = 1 - \sigma^{2}_{E} / \sigma^{2}$, we can recover $\theta$ by 
$$\begin{align*} \sigma^{2} = \frac{\sigma^{2}_{E}}{1 - \sum_{k=1}^{K} \rho_{k}}, \qquad \sigma^{2}_{k} = \rho_{k} \sigma^{2}, \qquad \beta =\gamma / \sigma.  \end{align*}$$

Thus we can evaluate slice likelihoods over $\mathcal{K} \in \mathbb{A}_{1}$ to determine component-wise variances. 