---
tags:
  - no-index
up: "[[Multivariate Writeup 1 (realign)]]"
modified: 2026-07-13T11:28:31-07:00
created: 2026-07-13T11:24:20-07:00
---

\section{Notation and Model Definition}

The generalization from the univariate case follows fairly naturally. Being explicit with shapes, let us have $m = 1, \dots, M$ components and $k = 1, \dots, K$ categories, and model definition $\mathbb{A} \subseteq 2^{[K]}$. Then we can adopt the original notation almost wholesale, with $Y_{\ell} \in \mathbb{R}^{M}$ and $\boldsymbol{a}_{\boldsymbol{i}(\ell)} \in \mathbb{R}^{|\mathbb{A}| \times M}$ (bold, since the $\lvert\mathbb{A}\rvert$ dimension is the conforming one), $x_{\ell} \in \mathbb{R}^{p}$, and $B \in \mathbb{R}^{M\times p}$, so that

\begin{align\textit{} \mathbb{E}(Y_{\ell} \mid x_{\ell}) = g^{-1} \left( Bx_{\ell} + \boldsymbol{a}_{\boldsymbol{i}(\ell)}^{\intercal}\mathbf{1}_{|\mathbb{A}|} \right) . \end{align}}


We work in the probit case: 

\textbf{Multivariate Crossed Probit Model}
The \textbf{Multivariate Crossed Probit Model in Latent Variable Form} can be given by 

\begin{align\textit{} Y_{\ell} = \mathbf{1}\left[ Bx_{\ell} + \boldsymbol{a}_{\boldsymbol{i}(\ell)}^{\intercal} \mathbf{1}_{|\mathbb{A}|} + \varepsilon_{\ell} > 0\right] .  \end{align}}


The indicator is applied component-wise.

Here, $\varepsilon_{\ell} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(\mathbf{0}_{M}, \Sigma_{E})$ and $a_{\boldsymbol{i}(\ell), \mathcal{K}} \sim \mathcal{N}(\mathbf{0}_{M}, \Sigma_{\mathcal{K}})$. With total covariance $\Sigma = \Sigma_{E} + \sum_{\mathcal{K} \in \mathbb{A}} \Sigma_{\mathcal{K}}$, the all likelihood \textit{can} be written as a product of $N$ $M$-variate normal cdfs; since this is intractable for moderate $M$, we work pairwise across components.

\section{Pairwise Marginal Likelihood (the introducing step, in the cleaner tilde form)}

The bivariate case below uses primes for the second component and tildes for the signed response, and is the cleaner rewrite of the introducing step. Vectorize $\boldsymbol{\tilde{\rho}}, \boldsymbol{\tilde{\sigma}^{2}}, \boldsymbol{\tilde{\sigma}'^{2}}$ as length-$\lvert\mathbb{A}\rvert$ vectors (same shape as $\boldsymbol{a}_{\boldsymbol{i}}$); the composite likelihood $L_{\text{all}}(\Gamma, r)$ at the end of the section generalizes to $M$ components directly.

\textbf{Here, letting everything be the signed version}

We consider the bivariate case where 

\begin{align*} B^{\intercal} = \begin{pmatrix}
\tilde{\beta} & \tilde{\beta}'
\end{pmatrix}, \end{align\textit{}

$B\in\mathbb{R}^{2\times (p + 1)}$, with 


\begin{align}} Y_{\ell} := \begin{pmatrix}
\tilde{Y}_{\ell} \\ \tilde{Y}_{\ell}'
\end{pmatrix}  &= \mathbf{1}\left[\begin{pmatrix}
x_{\ell}^{\intercal}\tilde{\beta} + \mathbf{1}_{|\mathbb{A}|}^{\intercal}\tilde{a}_{\boldsymbol{i}(\ell)} + \tilde{\varepsilon} \\ x_{\ell}^{\intercal}\tilde{\beta}' + \mathbf{1}_{|\mathbb{A}|}^{\intercal} \tilde{a}_{\boldsymbol{i}(\ell)}' + \tilde{\varepsilon}'
\end{pmatrix} > \begin{pmatrix}
0 \\ 0
\end{pmatrix} \right],  \end{align\textit{}

with the indicator taken component-wise. 

Here, $\tilde{a}_{\boldsymbol{i}(\ell)}, \tilde{a}_{\boldsymbol{i}(\ell)}' \in \mathbb{R}^{|\mathbb{A}|}$ with independent terms  

\begin{align}} \begin{pmatrix}
\tilde{a}_{\boldsymbol{i}, \mathcal{K}} \\ \tilde{a}_{\boldsymbol{i}, \mathcal{K}}'
\end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix}
0 \\ 0
\end{pmatrix}, \begin{pmatrix}
 \tilde{\sigma}^{2}_{\mathcal{K}} & \tilde{\rho}_{\mathcal{K}}\tilde{\sigma}_{\mathcal{K}} \tilde{\sigma}_{\mathcal{K}}' \\ \tilde{\rho}_{\mathcal{K}} \tilde{\sigma}_{\mathcal{K}} \tilde{\sigma}_{\mathcal{K}}' & \tilde{\sigma}'^{2}_{\mathcal{K}}
\end{pmatrix}\right)\end{align\textit{}

and latent variable 

\begin{align}} \begin{pmatrix}
\tilde{\varepsilon} \\ \tilde{\varepsilon}'
\end{pmatrix} \sim \mathcal{N}\left( \begin{pmatrix}
0 \\ 0
\end{pmatrix}, \begin{pmatrix}
\tilde{\sigma}^{2}_{E} & \tilde{\rho}_{E} \tilde{\sigma}_{E} \tilde{\sigma}_{E}' \\ \tilde{\rho}_{E} \tilde{\sigma}_{E} \tilde{\sigma}_{E}' & \tilde{\sigma}'^{2}_{E}
\end{pmatrix} \right).  \end{align\textit{}

We vectorize in bold, ie. $\boldsymbol{\tilde{\rho}}$, $\boldsymbol{\tilde{\sigma}^{2}}$, $\boldsymbol{\tilde{\sigma}'^{2}}$ are of the same shape as $\boldsymbol{a}_{\boldsymbol{i}}$. 

Then 


\begin{align}} \mathbb{P}(\tilde{Y}_{\ell} = \tilde{y}_{\ell}, \tilde{Y}_{\ell}' = \tilde{y}'_{\ell}) &= \mathbb{P}\left( \begin{pmatrix}
\tilde{y}_{\ell} \\ \tilde{y}_{\ell}'
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
x_{\ell}^{\intercal}\tilde{\beta} \\ x_{\ell}^{\intercal}\tilde{\beta}'
\end{pmatrix} + \begin{pmatrix}
 \mathbf{1}_{|\mathbb{A}|}^{\intercal} \tilde{a}_{\boldsymbol{i}(\ell)} + \tilde{\varepsilon}_{\ell} \\ \mathbf{1}_{|\mathbb{A}|}^{\intercal}\tilde{a}_{\boldsymbol{i}(\ell)}' + \tilde{\varepsilon}_{\ell}'
\end{pmatrix} \right\}  > \begin{pmatrix}
 0 \\ 0
\end{pmatrix}\right)  \\ &= \mathbb{P}\left( \begin{pmatrix}
\tilde{y}_{\ell} \\ \tilde{y}_{\ell}'
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
x_{\ell}^{\intercal}\tilde{\beta} \\ x_{\ell}^{\intercal}\tilde{\beta}'
\end{pmatrix} + \begin{pmatrix}
\sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal} \boldsymbol{\tilde{\sigma}^{2}} + \tilde{\sigma}^{2}_{E} } & 0 \\ 0 & \sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal}\boldsymbol{\tilde{\sigma}'^{2}} + \tilde{\sigma}'^{2}_{E} }
\end{pmatrix}\xi_{\tilde{r}} \right\} > \begin{pmatrix}
0 \\ 0
\end{pmatrix} \right) \\ 
&= \mathbb{P}\left( \xi_{\tilde{r}} > -\begin{pmatrix}
\tilde{y}_{\ell} x_{\ell}^{\intercal}\tilde{\beta} / \sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal} \boldsymbol{\tilde{\sigma}^{2}} + \tilde{\sigma}^{2}_{E}   }  \\ \tilde{y}_{\ell}' x_{\ell}^{\intercal}\tilde{\beta}' / \sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal}\boldsymbol{\tilde{\sigma}'^{2}} + \tilde{\sigma}'^{2}_{E} }
\end{pmatrix}   \right) \\ 
&=: \mathbb{P}\left( \xi_{\tilde{r}} > - \begin{pmatrix}
 \tilde{y}_{\ell} x_{\ell}^{\intercal} \tilde{\gamma} \\ \tilde{y}_{\ell}'x_{\ell}^{\intercal} \tilde{\gamma}'
\end{pmatrix} \right)  \\
&=: \Phi_{2}(\tilde{\eta}_{\ell}, \tilde{\eta}_{\ell}' ; \tilde{y}_{\ell} \tilde{y}_{\ell}' \tilde{r}), 
\end{align\textit{}


where 

\begin{align}} \tilde{\gamma} = \frac{\tilde{\beta}}{\sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal} \boldsymbol{\tilde{\sigma}^{2}} + \tilde{\sigma}^{2}_{E} }}, \qquad \tilde{\gamma}' = \frac{\tilde{\beta}'}{\sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal} \boldsymbol{\tilde{\sigma}'^{2}} + \tilde{\sigma}'^{2}_{E} }} , \qquad \tilde{r} = \end{align\textit{}

and 


We thus define the pairwise likelihood as

\begin{align}} L_{\text{pair}} \left(\tilde{\gamma}, \tilde{\gamma}', \tilde{r}; \left\{ \tilde{Y}_{\ell} \right\}_{\ell = 1}^{N}, \left\{ \tilde{Y}_{\ell}' \right\} _{\ell = 1}^{N} \right) := \prod_{\ell =1}^{N} \Phi_{2}\left( \tilde{Y}_{\ell}x_{\ell}^{\intercal} \tilde{\gamma}, \tilde{Y}_{\ell}'x_{\ell}^{\intercal}\tilde{\gamma}'; \tilde{Y}_{\ell} \tilde{Y}_{\ell}' \tilde{r} \right),  \end{align\textit{}

So that 


\begin{align}} L_{mm'}(\gamma[m], \gamma[m'], r[m, m']) := L_{\text{pair}}\left(\gamma [m], \gamma[m'], r[m, m']; \left\{ \tilde{Y}_{\ell}[m] \right\}_{\ell = 1}^{N}, \left\{ \tilde{Y}_{\ell}[m'] \right\}_{\ell = 1}^{N}  \right).  \end{align\textit{}


We thus have a natural composite likelihood 


\begin{align}} L_{\text{all}} (\Gamma, r) := \prod_{m < m'}^{M} L_{mm'}(\gamma[m], \gamma[m'], r[m, m']) \end{align\textit{}

for 


\begin{align}} \Gamma ^{\intercal} := \begin{pmatrix}
\gamma[1] & \cdots & \gamma[M]
\end{pmatrix} , \qquad r:= \begin{pmatrix}
1 & r[1, 2] & \cdots & r[1, M] \\ r[2, 1] & 1 & \cdots & r[2, M] \\ \vdots & \ddots & \cdots & \vdots \\ r[M, 1] & r[M, 2] & \cdots & 1
\end{pmatrix}.\end{align\textit{}

and corresponding log-likelihood/weighted log-likelihood 


\begin{align}} \mathcal{L}_{\text{all}}(\Gamma, r; w) := \sum_{m < m'}^{M} w_{mm'} \log L_{mm'}(\gamma[m], \gamma[m'], r[m, m']). \end{align\textit{}

The more appropriate composite likelihood might be 

\begin{align}} \sum_{m < m'}^{M}  w_{mm'} \log L_{mm'}(\gamma[m], \gamma[m'], r[m, m']) + \sum_{m =1}^{M} w_{m} \log L_{m}(\cdot)\end{align\textit{}


for $w_{m}$ the weight on the all likelihood.

\section{Pairwise Conditional Slice Likelihood (slice over}$\mathcal{K}$)

With the pairwise marginal in hand, we now condition on the $\mathcal{K}$-partial sum of random effects and derive the corresponding \textbf{slice likelihood} over $\mathcal{K}$. Throughout, $\mathcal{K}, \overline{\mathcal{K}}$ are disjoint with $\mathcal{K}\cup\overline{\mathcal{K}}=[K]$, and we work pairwise across components $(m, m')$. We deliberately keep component selectors as brackets $[m], [m, m']$ (canonical for multivariate); set selectors over $\mathcal{K}$ use $\pi_{\mathcal{K}}$ as in the univariate setting.

Conditioning on the bold partial-sum $\boldsymbol{a}_{\boldsymbol{i}(\ell)}^{\intercal}\boldsymbol{v}_{\mathcal{K}} = a_{\boldsymbol{j}, (\mathcal{K})}$ (where $\boldsymbol{j} := \pi_{\mathcal{K}}(\boldsymbol{i}(\ell))$),


\begin{align}} \mathbb{P}\!\left( Y_{\ell}[m] = y_{\ell}[m],\, Y_{\ell}[m'] = y_{\ell}[m']\,\middle|\, \boldsymbol{a}_{\boldsymbol{i}(\ell)}^{\intercal}\boldsymbol{v}_{\mathcal{K}} = a_{\boldsymbol{j}, (\mathcal{K})}\right) &= \mathbb{P}\!\left(\begin{pmatrix} \tilde{y}_{\ell}[m] \\ \tilde{y}_{\ell}[m'] \end{pmatrix}\odot\left\{\begin{pmatrix} \beta[m]^{\intercal}x_{\ell} + a_{\boldsymbol{j},\mathcal{K}}[m] \\ \beta[m']^{\intercal}x_{\ell} + a_{\boldsymbol{j},\mathcal{K}}[m'] \end{pmatrix} + \text{(K-complement noise)}\right\} > \mathbf{0}\right) \\
&=: \Phi_{2}\!\left( \eta_{\ell,(\mathcal{K})}[m],\, \eta_{\ell,(\mathcal{K})}[m']\,;\, \tilde{y}_{\ell}[m]\tilde{y}_{\ell}[m']\, r_{(\mathcal{K})}[m, m'] \right),
\end{align\textit{}


where the per-component slice quantities take the same shapes as in the bivariate-tilde marginal but with the $\mathcal{K}$-residual variance in the denominator:


\begin{align}} \gamma_{(\mathcal{K})}[m] &= \frac{\beta[m]}{\sqrt{\Sigma_{(\overline{\mathcal{K}})}[m, m] + \Sigma_E[m, m]}}, & \alpha_{\boldsymbol{j}, (\mathcal{K})}[m] &= \frac{a_{\boldsymbol{j}, \mathcal{K}}[m]}{\sqrt{\Sigma_{(\overline{\mathcal{K}})}[m, m] + \Sigma_E[m, m]}}, \\ r_{(\mathcal{K})}[m, m'] &= \frac{\Sigma_{(\mathcal{K})}[m, m']}{\sqrt{\Sigma_{(\mathcal{K})}[m, m]\,\Sigma_{(\mathcal{K})}[m', m']}}, & \eta_{\ell, (\mathcal{K})}[m] &= \tilde{y}_{\ell}[m]\!\left( \gamma_{(\mathcal{K})}[m]^{\intercal} x_{\ell} + \alpha_{\boldsymbol{j}, (\mathcal{K})}[m] \right). \end{align\textit{}


The standard $\tau$-construction lifts component-wise:


\begin{align}} \tau^{2}_{\mathcal{K}}[m] = \frac{\Sigma_{(\mathcal{K})}[m, m]}{\Sigma[m, m] - \Sigma_{(\mathcal{K})}[m, m]}, \qquad \gamma_{(\mathcal{K})}[m] = \gamma[m]\sqrt{1 + \tau^{2}_{\mathcal{K}}[m]}. \end{align\textit{}


The scaled random-effect contribution factors as $\alpha_{\boldsymbol{j},(\overline{\mathcal{K}})} = \mathrm{diag}(\tau_{\mathcal{K}})\,u_{\boldsymbol{j}}$ with bivariate


\begin{align}} \begin{pmatrix} u_{\boldsymbol{j}}[m] \\ u_{\boldsymbol{j}}[m'] \end{pmatrix} \sim \mathcal{N}\!\left(\mathbf{0},\, \begin{pmatrix} 1 & \rho_{\mathcal{K}}[m, m'] \\ \rho_{\mathcal{K}}[m, m'] & 1 \end{pmatrix}\right), \end{align\textit{}


so that the off-diagonal $\rho_{\mathcal{K}}[m, m'] = \Sigma_{(\mathcal{K})}[m, m'] / \sqrt{(\Sigma[m,m]-\Sigma_{(\mathcal{K})}[m,m])(\Sigma[m',m']-\Sigma_{(\mathcal{K})}[m',m'])}$ recovers the (univariate) slice ICC on the diagonal.



The slice contributes the same bivariate normal cdf shape as the marginal, with $\boldsymbol{j}$-dependent location and $\mathcal{K}$-dependent correlation. The per-slice pairwise likelihood is


\begin{align}} L_{mm'}(\gamma, \gamma', \tau^{2}, \tau'^{2}, t\,;\, \mathcal{K}) &= \prod_{\boldsymbol{j}\,\in\,\pi_{\mathcal{K}}(\mathcal{I}_{0})}\, \int_{\mathbb{R}^{2}} \left[\,\prod_{\boldsymbol{i}(\ell)\mid \boldsymbol{j}} \Phi_{2}\!\left(\eta_{\ell}[m],\, \eta_{\ell}[m']\,;\, \tilde{y}_{\ell}[m]\tilde{y}_{\ell}[m']\,t\right)\right] \mathrm{diag}(\tau, \tau')\, \varphi_{2}\!\left(u_{\boldsymbol{j}}[m],\, u_{\boldsymbol{j}}[m']\,;\, \rho_{\mathcal{K}}\right) \left[2\pi\sqrt{1-\rho_{\mathcal{K}}^{2}}\right]^{-1} d\boldsymbol{u}_{\boldsymbol{j}}, \end{align\textit{}


and the $\mathcal{K}$-slice composite likelihood follows the same pairwise-weighted form as $L_{\text{all}}$:


\begin{align}} L_{\mathcal{K}}(\Sigma_{\mathcal{K}}\,;\, \gamma) := \sum_{m > m'}\, w_{mm'}\, L_{mm'}\!\left(\gamma[m], \gamma[m'], \tau^{2}[m], \tau^{2}[m']\,;\, \mathcal{K}\right). \end{align*}


Note the $(\mathcal{K})$-parenthesized symbols ($\Sigma_{(\mathcal{K})}, \gamma_{(\mathcal{K})}, \alpha_{\boldsymbol{j},(\mathcal{K})}, r_{(\mathcal{K})}, \eta_{\ell,(\mathcal{K})}$) are the multivariate analogues of the deprecated univariate cumulative parens — they remain here only because the matrix-$\Sigma$ machinery has no length-$|\mathbb{A}|$ vector to plug into the selector form $\boldsymbol{v}_{\mathcal{K}}^{\intercal}\boldsymbol{\sigma^{2}}$. The reese-comment above flags the bivariate-tilde substitution that would remove them.

\section{High Cardinality and Numerical Notes}



\section{Case Studies}

