---
modified: 2026-05-10T17:45:26-07:00
created: 2026-05-10T16:49:11-07:00
---

The generalization from [[Initial Notation for K crossed random effects|the univariate case]] follows fairly naturally. Being explicit with shapes, let us have $m = 1, \dots, M$ components and $k = 1, \dots, K$ categories, and model definition $\mathbb{A} \subseteq 2^{[K]}$. Then we can adopt the original notation almost wholesale, with $Y_{\ell} \in \mathbb{R}^{M}$ and $a_{\boldsymbol{i}(\ell)} \in \mathbb{R}^{|\mathbb{A}| \times M}$, $x_{\ell} \in \mathbb{R}^{p}$, and $B \in \mathbb{R}^{M\times p}$, so that
$$\begin{align*} \mathbb{E}(Y_{\ell} \mid x_{\ell}) = g^{-1} \left( Bx_{\ell} + a_{\ell}^{\intercal}\mathbf{1}_{|\mathbb{A}|} \right) . \end{align*}$$

We work in the probit case: 

![[Multivariate Crossed Probit Model]]

The indicator is applied component-wise. 
