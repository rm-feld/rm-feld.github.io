---
modified: 2025-11-29T16:13:54-08:00
created: 2025-11-29T12:55:28-08:00
---
I think I need to start from the motivation. Issue is that it emerges in a few places. So let's break it up into what I think happens. 

# Two-Term Because Bivariate Response
Let $Y_{ij} \in \left\{ 0, 1 \right\}^{2}$. In this case, let my setup be guided by
$$\begin{align} Y_{ij} = \mathbf{1}\left[   X_{ij}^{\intercal}B + a_{i} + b_{j} + \varepsilon_{ij} > 0\right]\end{align}$$
for $Z_{ij}$ the value in the indicator brackets and $X_{ij} \in \mathbb{R}^{1\times (p + 1)}$ (intercept), $B \in \mathbb{R}^{(p + 1)\times 2}$ the $\beta$ matrix and $a_{i}$, $b_{j}$, $\varepsilon_{ij}$ bivariate normal with cross-covariance $r_{A}$, $r_{B}$, and $r_{\varepsilon}$, respectively. Vanilla [[ARC]], applied termwise, can be used to solve for $\sigma_{A 1}$, $\sigma_{A 2}$, $\sigma_{B 1}$, $\sigma_{B 2}$, and $B$. Then denoting by $\Phi_{r}$ the bivariate unit normal with cross-correlation $r$, and letting $W_{ij} = \text{diag}(w_{ij})$ encode the signs along the diagonal, we get through a termwise normalization that
$$\begin{align} \mathbb{P}(Y_{ij} = y_{ij} \mid a_{i}) &= \mathbb{P}\left( W_{ij}\left( X_{ij}^{\intercal}B + a_{i} + b_{j} + \varepsilon_{ij} \right) > 0 \mid a \right)  \\
&= \mathbb{P}\left( w_{ij}^{(1)}\left( X_{ij}^{\intercal}\beta_{1} + a_{i}^{(1)} + b_{j}^{(1)} + \varepsilon_{ij} ^{(1)}\right)  > 0, w_{ij}^{(2)}\left( X_{ij}^{\intercal}\beta_{2} + a_{i}^{(2)} + b_{j}^{(2)} + \varepsilon_{ij}^{(2)} \right) > 0 \mid a\right) \\
&= \Phi \left( \frac{w_{ij}^{(1)}\left( X_{ij}^{\intercal}\beta_{1} + a_{i}^{(1)} \right)}{\sqrt{ 1 + \sigma^{2}_{B 1} }},  \frac{w_{ij}^{(2)}\left( X_{ij}^{\intercal}\beta_{2} + a_{i}^{(2)} \right)}{\sqrt{ 1 + \sigma^{2}_{B 2} }}; \rho = \frac{r_{B} + r_{\varepsilon}}{\sqrt{ (1 + \sigma^{2}_{B 1})(1 + \sigma^{2}_{B 2}) }} \right)\end{align}$$
for which the normalizing square root of the correlation term is known. Thus a row likelihood can solve for the cross-correlation. To be 

# Two-Term Because Correlated
