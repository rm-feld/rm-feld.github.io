---
modified: 2025-12-02T20:56:53-08:00
created: 2025-11-29T16:23:01-08:00
---
# Univariate
## Generic Univariate Hessian for AGH Mode 
$$\begin{align} \frac{ \partial  }{ \partial x } \frac{\varphi(f(x))}{\Phi(f(x))} &= -\frac{\varphi^{2}(x)\cdot f'(x)}{[\Phi(f(x))]^{2}} - \frac{f(x)f'(x)\varphi(x)}{\Phi [f(x)]} \\
&= -\frac{\varphi(x)f'(x)}{\Phi^{2}(f(x))}(\varphi(x) + f(x) \cdot \Phi[f(x)]).\end{align}$$


## Generic Bivariate AGH Mode
### First Component Partial
For bivariate unit normal with correlation $r$, 
$$\begin{align*} \frac{ \partial  }{ \partial x_{1} } \Phi_{2}(x_{1}, x_{2}; r) = \varphi(x_{1}) \Phi\left( \frac{x_{2} - rx_{1}}{\sqrt{ 1 - r^{2} }} \right).    \end{align*}$$

### Hessian
$$\begin{align*} \nabla_{x}^{2} \log \Phi_{2}(x; \rho) \end{align*}$$

$$
\begin{aligned}  
\frac{\partial^{2}}{\partial x_{1}\partial x_{2}}\Phi_{2}(x;\rho) &= \varphi_{2}(x;\rho) \\
\frac{ \partial^{2} }{ \partial x_{1}^{2} } \Phi_{2}(x; \rho) &= -x_{1} \varphi(x_{1}) \Phi\left( (x_{2} - x_{1}) / \sqrt{ 1 - \rho^{2} } \right) - \rho \varphi_{2}(x; \rho)\\
\end{aligned}$$
