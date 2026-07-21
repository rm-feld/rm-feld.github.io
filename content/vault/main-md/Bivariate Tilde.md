---
modified: 2026-07-09
created: 2026-05-25T16:51:46-07:00
tags: [update-notation, genai/claude]
---
**Here, letting everything be the signed version**

We consider the bivariate case where 
$$\begin{align*} B^{\intercal} = \begin{pmatrix}
\tilde{\beta} & \tilde{\beta}'
\end{pmatrix}, \end{align*}$$
$B\in\mathbb{R}^{2\times (p + 1)}$, with 

$$\begin{align*} \boldsymbol{Y}_{\ell} := \begin{pmatrix}
Y_{\ell} \\ Y_{\ell}'
\end{pmatrix}  &= 2\cdot\mathbf{1}\left[\begin{pmatrix}
x_{\ell}^{\intercal}\tilde{\beta} + \mathbf{1}_{|\mathbb{A}|}^{\intercal}\tilde{a}_{\boldsymbol{i}(\ell)} + \tilde{\varepsilon} \\ x_{\ell}^{\intercal}\tilde{\beta}' + \mathbf{1}_{|\mathbb{A}|}^{\intercal} \tilde{a}_{\boldsymbol{i}(\ell)}' + \tilde{\varepsilon}'
\end{pmatrix} > \begin{pmatrix}
0 \\ 0
\end{pmatrix} \right] - \begin{pmatrix} 1 \\ 1 \end{pmatrix},  \end{align*}$$
with the indicator (and subtraction) taken component-wise, so $Y_{\ell}, Y_{\ell}' \in \left\{ -1, +1 \right\}$ directly. 

 $1:x^circ:x$


Xl = (1, xo, x)
Here, $\tilde{a}_{\boldsymbol{i}(\ell)}, \tilde{a}_{\boldsymbol{i}(\ell)}' \in \mathbb{R}^{|\mathbb{A}|}$ with independent terms  
$$\begin{align*} \begin{pmatrix}
\tilde{a}_{\boldsymbol{i}, \mathcal{K}} \\ \tilde{a}_{\boldsymbol{i}, \mathcal{K}}'
\end{pmatrix} \sim \mathcal{N}\left(\begin{pmatrix}
0 \\ 0
\end{pmatrix}, \begin{pmatrix}
 \tilde{\sigma}^{2}_{\mathcal{K}} & \tilde{\rho}_{\mathcal{K}}\tilde{\sigma}_{\mathcal{K}} \tilde{\sigma}_{\mathcal{K}}' \\ \tilde{\rho}_{\mathcal{K}} \tilde{\sigma}_{\mathcal{K}} \tilde{\sigma}_{\mathcal{K}}' & \tilde{\sigma}'^{2}_{\mathcal{K}}
\end{pmatrix}\right)\end{align*}$$
and latent variable 
$$\begin{align*} \begin{pmatrix}
\tilde{\varepsilon} \\ \tilde{\varepsilon}'
\end{pmatrix} \sim \mathcal{N}\left( \begin{pmatrix}
0 \\ 0
\end{pmatrix}, \begin{pmatrix}
\tilde{\sigma}^{2}_{E} & \tilde{\rho}_{E} \tilde{\sigma}_{E} \tilde{\sigma}_{E}' \\ \tilde{\rho}_{E} \tilde{\sigma}_{E} \tilde{\sigma}_{E}' & \tilde{\sigma}'^{2}_{E}
\end{pmatrix} \right).  \end{align*}$$
We vectorize in bold, ie. $\boldsymbol{\tilde{\rho}}$, $\boldsymbol{\tilde{\sigma}^{2}}$, $\boldsymbol{\tilde{\sigma}'^{2}}$ are of the same shape as $a_{\boldsymbol{i}}$. 

Then 

$$\begin{align*} \mathbb{P}(Y_{\ell} = y_{\ell}, Y_{\ell}' = y'_{\ell}) &= \mathbb{P}\left( \begin{pmatrix}
y_{\ell} \\ y_{\ell}'
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
x_{\ell}^{\intercal}\tilde{\beta} \\ x_{\ell}^{\intercal}\tilde{\beta}'
\end{pmatrix} + \begin{pmatrix}
 \mathbf{1}_{|\mathbb{A}|}^{\intercal} \tilde{a}_{\boldsymbol{i}(\ell)} + \tilde{\varepsilon}_{\ell} \\ \mathbf{1}_{|\mathbb{A}|}^{\intercal}\tilde{a}_{\boldsymbol{i}(\ell)}' + \tilde{\varepsilon}_{\ell}'
\end{pmatrix} \right\}  > \begin{pmatrix}
 0 \\ 0
\end{pmatrix}\right)  \\ &= \mathbb{P}\left( \begin{pmatrix}
y_{\ell} \\ y_{\ell}'
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
x_{\ell}^{\intercal}\tilde{\beta} \\ x_{\ell}^{\intercal}\tilde{\beta}'
\end{pmatrix} + \begin{pmatrix}
\sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal} \boldsymbol{\tilde{\sigma}^{2}} + \tilde{\sigma}^{2}_{E} } & 0 \\ 0 & \sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal}\boldsymbol{\tilde{\sigma}'^{2}} + \tilde{\sigma}'^{2}_{E} }
\end{pmatrix}\xi_{\tilde{r}} \right\} > \begin{pmatrix}
0 \\ 0
\end{pmatrix} \right) \\ 
&= \mathbb{P}\left( \xi_{\tilde{r}} > -\begin{pmatrix}
y_{\ell} x_{\ell}^{\intercal}\tilde{\beta} / \sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal} \boldsymbol{\tilde{\sigma}^{2}} + \tilde{\sigma}^{2}_{E}   }  \\ y_{\ell}' x_{\ell}^{\intercal}\tilde{\beta}' / \sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal}\boldsymbol{\tilde{\sigma}'^{2}} + \tilde{\sigma}'^{2}_{E} }
\end{pmatrix}   \right) \\ 
&=: \mathbb{P}\left( \xi_{\tilde{r}} > - \begin{pmatrix}
 y_{\ell} x_{\ell}^{\intercal} \tilde{\gamma} \\ y_{\ell}'x_{\ell}^{\intercal} \tilde{\gamma}'
\end{pmatrix} \right)  \\
&=: \Phi_{2}(\tilde{\eta}_{\ell}, \tilde{\eta}_{\ell}' ; y_{\ell} y_{\ell}' \tilde{r}), 
\end{align*}$$

where 
$$\begin{align*} \tilde{\gamma} = \frac{\tilde{\beta}}{\sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal} \boldsymbol{\tilde{\sigma}^{2}} + \tilde{\sigma}^{2}_{E} }}, \qquad \tilde{\gamma}' = \frac{\tilde{\beta}'}{\sqrt{ \mathbf{1}_{|\mathbb{A}|}^{\intercal} \boldsymbol{\tilde{\sigma}'^{2}} + \tilde{\sigma}'^{2}_{E} }} , \qquad \tilde{r} = \end{align*}$$
and 


We thus define the pairwise likelihood as
$$\begin{align*} L_{\text{pair}} \left(\tilde{\gamma}, \tilde{\gamma}', \tilde{r}; \left\{ Y_{\ell} \right\}_{\ell = 1}^{N}, \left\{ Y_{\ell}' \right\} _{\ell = 1}^{N} \right) := \prod_{\ell =1}^{N} \Phi_{2}\left( Y_{\ell}x_{\ell}^{\intercal} \tilde{\gamma}, Y_{\ell}'x_{\ell}^{\intercal}\tilde{\gamma}'; Y_{\ell} Y_{\ell}' \tilde{r} \right),  \end{align*}$$
So that 

$$\begin{align*} L_{mm'}(\gamma[m], \gamma[m'], r[m, m']) := L_{\text{pair}}\left(\gamma [m], \gamma[m'], r[m, m']; \left\{ Y_{\ell}[m] \right\}_{\ell = 1}^{N}, \left\{ Y_{\ell}[m'] \right\}_{\ell = 1}^{N}  \right).  \end{align*}$$

We thus have a natural composite likelihood 

$$\begin{align*} L_{\text{all}} (\Gamma, r) := \prod_{m < m'}^{M} L_{mm'}(\gamma[m], \gamma[m'], r[m, m']) \end{align*}$$
for 

$$\begin{align*} \Gamma ^{\intercal} := \begin{pmatrix}
\gamma[1] & \cdots & \gamma[M]
\end{pmatrix} , \qquad r:= \begin{pmatrix}
1 & r[1, 2] & \cdots & r[1, M] \\ r[2, 1] & 1 & \cdots & r[2, M] \\ \vdots & \ddots & \cdots & \vdots \\ r[M, 1] & r[M, 2] & \cdots & 1
\end{pmatrix}.\end{align*}$$
and corresponding log-likelihood/weighted log-likelihood 

$$\begin{align*} \mathcal{L}_{\text{all}}(\Gamma, r; w) := \sum_{m < m'}^{M} w_{mm'} \log L_{mm'}(\gamma[m], \gamma[m'], r[m, m']). \end{align*}$$
The more appropriate composite likelihood might be 
$$\begin{align*} \sum_{m < m'}^{M}  w_{mm'} \log L_{mm'}(\gamma[m], \gamma[m'], r[m, m']) + \sum_{m =1}^{M} w_{m} \log L_{m}(\cdot)\end{align*}$$
%% can add the marginal ones? %%
for $w_{m}$ the weight on the all likelihood. 