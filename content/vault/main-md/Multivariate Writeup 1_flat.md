---
tags: [no-index]
up: "[[Multivariate Writeup 1]]"
modified: 2026-05-14T15:22:54-07:00
created: 2026-05-11T13:02:08-07:00
---
$\newcommand{\R}{\mathbb{R}}$

The generalization from [[Initial Notation for K crossed random effects|the univariate case]] follows fairly naturally. Being explicit with shapes, let us have $m = 1, \dots, M$ components and $k = 1, \dots, K$ categories, and model definition $\mathbb{A} \subseteq 2^{[K]}$. Then we can adopt the original notation almost wholesale, with $Y_{\ell} \in \mathbb{R}^{M}$ and $a_{\boldsymbol{i}(\ell)} \in \mathbb{R}^{|\mathbb{A}| \times M}$, $x_{\ell} \in \mathbb{R}^{p}$, and $B \in \mathbb{R}^{M\times p}$, so that 
$$\begin{align*} \mathbb{E}(Y_{\ell} \mid x_{\ell}) = g^{-1} \left( Bx_{\ell} + a_{\ell}^{\intercal}\mathbf{1}_{|\mathbb{A}|} \right) . \end{align*}$$

We work in the probit case: 

> [!attention] Multivariate Crossed Probit Model
> The **Multivariate Crossed Probit Model in Latent Variable Form** can be given by 
> $$\begin{align*} Y_{\ell} = \mathbf{1}\left[ Bx_{\ell} + a_{\boldsymbol{i}(\ell)}^{\intercal} \mathbf{1}_{|\mathbb{A}|} + \varepsilon_{\ell} > 0\right] .  \end{align*}$$

The indicator is applied component-wise.

Here, $\varepsilon_{\ell} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(\mathbf{0}_{M}, \Sigma_{E})$, $a_{\boldsymbol{i}(\ell), \mathcal{K}} \sim \mathcal{N}(\mathbf{0}_{M}, \Sigma_{\mathcal{K}})$. 

$$\begin{align*}  \mathbb{P}(Y_{\ell} = y_{\ell}) &= \mathbb{P}\left( \tilde{y}_{\ell} \odot \left\{ Bx_{\ell} + a_{\boldsymbol{i}(\ell)}^{\intercal} \mathbf{1}_{|\mathbb{A}|} + \varepsilon_{\ell}\right\} > 0  \right) \\ 
&= \mathbb{P}\left(\tilde{y}_{\ell} \odot \left\{ Bx_{\ell} + (\Sigma^{1 / 2} u_{\boldsymbol{i}(\ell)})^{\intercal}\mathbf{1}_{|\mathbb{A}|}  \right\} > 0 \right) \\ \end{align*}$$

for $\Sigma = \Sigma_{E} + \sum_{\mathcal{K} \in \mathbb{A}}\Sigma_{\mathcal{K}}$. The corresponding all likelihood *can* be written as the product of $N$ $M$-variate normal cdfs; since this is generally intractable for even moderate $M$, we consider a procedure applied pairwise. 

%% the mixed comes back into vogue  %%

## Option A:

$$\begin{align*}  \mathbb{P}(Y_{\ell} = y_{\ell}) &= \mathbb{P}\left( \tilde{y}_{\ell} \odot \left\{ Bx_{\ell} + a_{\boldsymbol{i}(\ell)}^{\intercal} \mathbf{1}_{|\mathbb{A}|} + \varepsilon_{\ell}\right\} > 0  \right) \\ 
&= \mathbb{P}\left(\tilde{y}_{\ell} \odot \left\{ Bx_{\ell} + (\Sigma^{1 / 2} u_{\boldsymbol{i}(\ell)})^{\intercal}\mathbf{1}_{|\mathbb{A}|}  \right\} > 0 \right) \\ 
&= \mathbb{P}\left( \tilde{y}_{\ell}[1] \cdot \left( \beta_{1}^{\intercal}x_{\ell} +  \right) \right)\end{align*}$$
Let 
$$\begin{align*} \xi_{r} \sim \mathcal{N}\left(\begin{pmatrix}
0 \\ 0
\end{pmatrix}, \begin{pmatrix}
 1 & r \\ r & 1
\end{pmatrix}\right).  \end{align*}$$
The likelihood for a single data point can be given by 
$$\begin{align*} \mathbb{P}(Y_{\ell} [m] = y_{\ell} [m], Y_{\ell}[m'] = y_{\ell}[m'])
&= \mathbb{P}\left(\begin{pmatrix}
\tilde{y}_{\ell}[m] \\ \tilde{y}_{\ell}[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\intercal}x_{\ell} \\ \beta[m']^{\intercal}x_{\ell} \end{pmatrix}  + \begin{pmatrix}
a_{\boldsymbol{i}(\ell)}[m]^{\intercal} \mathbf{1}_{|\mathbb{A}|} + \varepsilon_{\ell}[m] \\ a_{\boldsymbol{i}(\ell)}[m']^{\intercal} \mathbf{1}_{|\mathbb{A}|} + \varepsilon_{\ell}[m'] 
\end{pmatrix}\right\}   > \begin{pmatrix}
0 \\ 0
\end{pmatrix}\right) \\ 
&= \mathbb{P}\left(\begin{pmatrix}
\tilde{y}_{\ell}[m] \\ \tilde{y}_{\ell}[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\intercal}x_{\ell} \\ \beta[m']^{\intercal}x_{\ell} \end{pmatrix}  +  \begin{pmatrix}
\Sigma[m, m] & 0 \\ 0 & \Sigma[m', m']
\end{pmatrix} \xi_{r[m, m']}\right\}  > \begin{pmatrix}
0 \\ 0
\end{pmatrix}\right) \\ 
&= \mathbb{P}\left( \xi_{r[m, m']} >  -\begin{pmatrix}
\tilde{y}_{\ell}[m]\beta[m]^{\intercal}x_{\ell} / \Sigma[m, m] \\ \tilde{y}_{\ell}[m'] \beta [m']^{\intercal}x_{\ell} / \Sigma[m', m'] 
\end{pmatrix} \right) \\
&=: \mathbb{P}\left( \xi_{r[m, m']} >  -\begin{pmatrix}
\tilde{y}_{\ell}[m]\gamma[m]^{\intercal}x_{\ell}  \\ \tilde{y}_{\ell}[m'] \gamma [m']^{\intercal}x_{\ell} 
\end{pmatrix} \right) \\

&=: \Phi_{2}(\eta_{\ell}[m], \eta_{\ell}[m']; \tilde{y}_{\ell}[m] \tilde{y}_{\ell}[m']r[m, m']),
\end{align*}$$
where
$$\begin{align*} \gamma[m] = \frac{\beta[m]}{\Sigma[m, m]}, \qquad r[m, m'] = \frac{\Sigma[m, m']}{\Sigma[m, m] \Sigma[m', m']} , \qquad \eta_{\ell}[m] = \tilde{y}_{\ell}[m]\gamma[m]^{\intercal}x_{\ell}. \end{align*}$$
The conditional likelihood can be given by
$$\begin{align*} \mathbb{P}\left( Y_{\ell} [m] = y_{\ell} [m], Y_{\ell}[m'] = y_{\ell}[m'] \mid a_{\boldsymbol{i}(\ell)}^{\intercal}v_{\mathcal{K}} = a_{\boldsymbol{j}, (\mathcal{K})}\right)
&= \mathbb{P}\left(\begin{pmatrix}
\tilde{y}_{\ell}[m] \\ \tilde{y}_{\ell}[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\intercal}x_{\ell} \\ \beta[m']^{\intercal}x_{\ell} \end{pmatrix}  + \begin{pmatrix}
a_{\boldsymbol{i}(\ell)}[m]^{\intercal} \mathbf{1}_{|\mathbb{A}|} + \varepsilon_{\ell}[m] \\ a_{\boldsymbol{i}(\ell)}[m']^{\intercal} \mathbf{1}_{|\mathbb{A}|} + \varepsilon_{\ell}[m'] 
\end{pmatrix}\right\}   > \begin{pmatrix}
0 \\ 0
\end{pmatrix} \mid a_{\boldsymbol{i}(\ell)}^{\intercal} v_{\mathcal{K}} = a_{\boldsymbol{j}, (\mathcal{K})}\right) \\ 
&= \mathbb{P}\left(\begin{pmatrix}
\tilde{y}_{\ell}[m] \\ \tilde{y}_{\ell}[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\intercal}x_{\ell} + a_{\boldsymbol{j}, (\mathcal{K})}[m] \\ \beta[m']^{\intercal}x_{\ell} + a_{\boldsymbol{j}, (\mathcal{K})}[m'] \end{pmatrix}  + \begin{pmatrix}
a_{\boldsymbol{i}(\ell)}[m]^{\intercal} v_{\overline{\mathcal{K}}} + \varepsilon_{\ell}[m] \\ a_{\boldsymbol{i}(\ell)}[m']^{\intercal} v_{\overline{\mathcal{K}}} + \varepsilon_{\ell}[m'] 
\end{pmatrix}\right\}   > \begin{pmatrix}
0 \\ 0
\end{pmatrix} \right) \\ 
&= \mathbb{P}\left(\begin{pmatrix}
\tilde{y}_{\ell}[m] \\ \tilde{y}_{\ell}[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\intercal}x_{\ell} + a_{\boldsymbol{j}, \mathcal{K}}[m] \\ \beta[m']^{\intercal}x_{\ell} + a_{\boldsymbol{j}, \mathcal{K}}[m'] \end{pmatrix}  +  \begin{pmatrix}
\Sigma_{(\overline{\mathcal{K}})}[m, m] & 0 \\ 0 & \Sigma_{(\overline{\mathcal{K}})}[m', m']
\end{pmatrix} \xi_{r_{(\overline{\mathcal{K}})}[m, m']}\right\}  > \begin{pmatrix}
0 \\ 0
\end{pmatrix}\right) \\ &= \mathbb{P}\left( \xi_{r_{(\mathcal{K})}[m, m']} > -\begin{pmatrix}
\tilde{y}_{\ell}[m]\left(\beta[m]^{\intercal}x_{\ell} + a_{\boldsymbol{j}, \mathcal{K}}[m]\right) / \Sigma_{(\overline{\mathcal{K}})}[m, m] \\ \tilde{y}_{\ell}[m']\left(\beta[m']^{\intercal}x_{\ell} + a_{\boldsymbol{j}, \mathcal{K}}[m']\right) / \Sigma_{(\overline{\mathcal{K}})}[m', m']
\end{pmatrix} \right) \\
&=: \mathbb{P}\left( \xi_{r_{(\mathcal{K})}[m, m']} > -\begin{pmatrix}
\tilde{y}_{\ell}[m]\left(\gamma_{(\mathcal{K})}[m]^{\intercal}x_{\ell} + \alpha_{\boldsymbol{j}, (\mathcal{K})}[m]\right) \\ \tilde{y}_{\ell}[m']\left(\gamma_{(\mathcal{K})}[m']^{\intercal}x_{\ell} + \alpha_{\boldsymbol{j}, (\mathcal{K})}[m']\right)
\end{pmatrix} \right) \\
&=: \Phi_{2}\left(\eta_{\ell, (\mathcal{K})}[m], \eta_{\ell, (\mathcal{K})}[m']; \tilde{y}_{\ell}[m] \tilde{y}_{\ell}[m']r_{ (\mathcal{K})}[m, m']\right),
\end{align*}$$
where
$$\begin{align*} \gamma_{(\mathcal{K})}[m] = \frac{\beta[m]}{\Sigma_{(\mathcal{K})}[m, m]}, \qquad \alpha_{\boldsymbol{j}, (\mathcal{K})}[m] = \frac{a_{\boldsymbol{j}, \mathcal{K}}[m]}{\Sigma_{(\mathcal{K})}[m, m]}, \qquad r_{(\mathcal{K})}[m, m'] = \frac{\Sigma_{(\mathcal{K})}[m, m']}{\Sigma_{(\mathcal{K})}[m, m] \Sigma_{(\mathcal{K})}[m', m']}, \qquad \eta_{\ell, (\mathcal{K})}[m] = \tilde{y}_{\ell}[m]\left(\gamma_{(\mathcal{K})}[m]^{\intercal}x_{\ell} + \alpha_{\boldsymbol{j}, (\mathcal{K})}[m]\right). \end{align*}$$

Note the standard construction of $\tau$ applies: 
$$\begin{align*} \tau^{2}_{\mathcal{K}}[m] = \frac{\Sigma_{(\mathcal{K})}[m, m]}{\Sigma[m, m] - \Sigma_{(\mathcal{K})}[m, m]}, \qquad \gamma_{(\mathcal{K})}[m]= \gamma[m] \sqrt{ 1 + \tau^{2}_{\mathcal{K}} } .  \end{align*}$$
Further, we can write 
$$\begin{align*} \begin{pmatrix} \alpha_{\boldsymbol{j}, (\mathcal{K})}[m] \\ \alpha_{\boldsymbol{j}, (\mathcal{K})}[m'] \end{pmatrix} = \begin{pmatrix} \tau_{\mathcal{K}}[m] u_{\boldsymbol{j}, \mathcal{K}}[m] \\ \tau_{\mathcal{K}}[m'] u_{\boldsymbol{j}, \mathcal{K}}[m'] \end{pmatrix}, \qquad \begin{pmatrix} u_{\boldsymbol{j}, \mathcal{K}}[m] \\ u_{\boldsymbol{j}, \mathcal{K}}[m'] \end{pmatrix} \sim \mathcal{N}\left( \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 & \rho_{\mathcal{K}}[m, m'] \\ \rho_{\mathcal{K}}[m, m'] & 1 \end{pmatrix} \right), \end{align*}$$
where
$$\begin{align*} \tau^{2}_{(\mathcal{K})}[m, m'] = \frac{\Sigma_{(\mathcal{K})}[m, m']}{\sqrt{\left(\Sigma[m, m] - \Sigma_{(\mathcal{K})}[m, m]\right)\left(\Sigma[m', m'] - \Sigma_{(\mathcal{K})}[m', m']\right)}}, \qquad \rho_{\mathcal{K}}[m, m'] = \frac{\tau^{2}_{(\mathcal{K})}[m, m']}{\tau_{\mathcal{K}}[m] \tau_{\mathcal{K}}[m']}, \end{align*}$$
recovering $\tau^{2}_{(\mathcal{K})}[m, m] = \tau^{2}_{\mathcal{K}}[m]$ on the diagonal.
Note the introduced $(\mathcal{K})$ arguments for $\mathcal{K} = \emptyset$ map nicely to the [[All Likelihood|all likelihood]]; thus to avoid invoking the further $(\mathcal{K})$ subset, 