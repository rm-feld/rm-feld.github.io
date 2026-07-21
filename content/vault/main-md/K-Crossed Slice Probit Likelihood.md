---
modified: 2026-07-09
created: 2026-04-20T13:54:36-07:00
tags: [genai/claude]
---
Let $\mathcal{K}, \overline{\mathcal{K}}$ be disjoint with $\mathcal{K}\cup \overline{\mathcal{K}} = [K]$.  By component independence, we can decompose variance as $\sigma^{2} = \sigma^{2}_{(\mathcal{K})} + \sigma^{2}_{(\overline{\mathcal{K}})}$, for 

$$\begin{align*} \sigma_{(\mathcal{K})}^{2} := \sum_{\mathcal{K}' \subseteq \mathcal{K}, \mathcal{K} \in \mathbb{A}} \sigma^{2}_{\mathcal{K'}}. \end{align*}$$
Note the use of parentheses to differentiate from the interaction terms indexed by $\mathcal{K}$.

Throughout, we use the shortand 
$$\begin{align*} a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} = \sum_{\mathcal{K}' \subseteq \mathcal{K}, \mathcal{K}' \in \mathbb{A}} a_{\ell, \mathcal{K}'}. \end{align*}$$


$$\begin{align*} \mathbb{P}(Y_{\ell} = y_{\ell} \mid x_{\ell}, a_{\ell}[\mathcal{K}]) &= \mathbb{P}\left( y_{\ell}\left[ x_{\ell}^{\intercal}\beta + a_{\ell}^{\intercal}\mathbf{1} + \varepsilon_{\ell} > 0 \right] \right) \\ 
&= \mathbb{P}\left( y_{\ell}\left[ x_{\ell}^{\intercal}\beta + a_{\ell}[\mathcal{K}]^{\intercal} \mathbf{1} + a_{\ell}[\overline{\mathcal{K}}]^{\intercal} \mathbf{1} + \varepsilon_{\ell}  \right] > 0\right) \\ 
&= \mathbb{P}\left( y_{\ell} \left[ x_{\ell}^{\intercal}\beta + a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} + \xi \sqrt{ \sigma^{2}_{(\overline{\mathcal{K}})} +  \sigma^{2}_{E}} \right] > 0\right) \\ 
&= \Phi\left( \frac{y_{\ell}\left[ x_{\ell}^{\intercal}\beta + a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} \right]}{\sqrt{ \sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E} }}  \right) \\ 
&= \Phi\left( \frac{y_{\ell}\left[ x_{\ell}^{\intercal}\beta + a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} \right]}{\sqrt{\sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E} }} \cdot \frac{\sqrt{ \sigma^{2}_{(\mathcal{K})} + \sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E} }}{\sqrt{ \sigma^{2}_{(\mathcal{K})} + \sigma^{2}_{(\overline{\mathcal{K}})}+ \sigma^{2}_{E}  }} \right) \\ 
&:= \Phi\left(y_{\ell}x_{\ell}^{\intercal}\gamma \sqrt{ 1 + \tau^{2}_{\mathcal{K}} } + \frac{a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1}}{\sqrt{ \sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E} }} \right) \\
&:= \Phi\left( y_{\ell}x_{\ell}^{\intercal}\gamma_{\mathcal{K}} + \tau_{\mathcal{K}} u_{\boldsymbol{j}}\right),
\end{align*}$$

where $\gamma_{\mathcal{K}_0} = \gamma \sqrt{ 1 + \tau^{2}_{\mathcal{K}} }$ and $u_{\boldsymbol{j}} = a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} / \tau_{\mathcal{K}}$ ($\boldsymbol{j}:= \boldsymbol{i}_{\ell}[\mathcal{K}]$) for 
$$\begin{align*} \tau^{2}_{\mathcal{K}} = \frac{\sigma_{(\mathcal{K})}^{2}}{\sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E}} = \frac{\sigma^{2}_{(\mathcal{K})}}{\sigma^{2} - \sigma _{(\mathcal{K})}^{2}}.   \end{align*}$$
Note $u_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} \sim \mathcal{N}(0, 1)$. 

The corresponding **slice likelihood** in this case can be given by 
$$\begin{align*} L_{\mathcal{K}}(\tau^{2}_{\mathcal{K}}) &:= \prod_{\boldsymbol{j} \in \mathcal{S}[\mathcal{K}]} \int _{\mathbb{R}} L_{\boldsymbol{j}}(\gamma_{\mathcal{K}} \mid u_{\boldsymbol{j}}) \,\tau_{\mathcal{K}}^{-1}  \varphi \left( \frac{u_{\boldsymbol{j}}}{\tau_{\mathcal{K}}} \right) \, du_{\boldsymbol{j}} \\ 
&= \tau_{\mathcal{K}}^{-|\mathcal{S}[\mathcal{K}]|} \prod_{\boldsymbol{j} \in \mathcal{S}[\mathcal{K}]} \int _{\mathbb{R}} L_{\boldsymbol{j}}(\gamma_{\mathcal{K}} \mid u_{j}) \, \varphi \left( \frac{u_{\boldsymbol{j}}}{\tau_{\mathcal{K}}} \right) \, du_{\boldsymbol{j}}, \end{align*}$$
^slice-likelihood

where
$$\begin{align*} L_{\boldsymbol{j}}(\gamma_{\mathcal{K}} \mid u_{\boldsymbol{j}}) &:= \prod_{\ell \in [N]: \boldsymbol{i}_{\ell}[\mathcal{K}] = \boldsymbol{j}} \Phi\left( x_{\ell}^{\intercal}\gamma_{\mathcal{K}} + \tau_{\mathcal{K}} u_{\boldsymbol{j}} \right) \\ 
&:= \prod_{\boldsymbol{i}_{\ell} \mid \boldsymbol{j}} \Phi\left( x_{\ell}^{\intercal} \gamma_{\mathcal{K}} + \tau_{\mathcal{K}} u_{\boldsymbol{j}} \right).  \end{align*}$$
As standard in our regime, we generally restrict likelihood to be over only terms with at least two terms in the inner product, $N_{\boldsymbol{j}, \mathcal{K}} \geq 2$. 