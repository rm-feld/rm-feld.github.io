---
tags: []
up: "[[Multivariate Writeup 1]]"
modified: 2026-05-26T12:34:27-07:00
created: 2026-05-11T13:02:08-07:00
---
%% From preamble (define here for Obsidian; no-op if already loaded in LaTeX) %%
$\newcommand{\real}{\mathbb{R}}$
$\newcommand{\dnorm}{\mathcal{N}}$
$\newcommand{\err}{\varepsilon}$
$\newcommand{\tran}{\mathsf{T}}$
$\newcommand{\simiid}{\stackrel{\mathrm{iid}}{\sim}}$
%% ell-indexed objects (subscript \ell is essentially universal) %%
$\newcommand{\xl}{x_{\ell}}$
$\newcommand{\Yl}{Y_{\ell}}$
$\newcommand{\yl}{y_{\ell}}$
$\newcommand{\ytl}{\tilde{y}_{\ell}}$
$\newcommand{\errl}{\err_{\ell}}$
$\newcommand{\il}{\boldsymbol{i}(\ell)}$
$\newcommand{\ail}{a_{\il}}$
$\newcommand{\uil}{u_{\il}}$
%% Crossed-specific %%
$\newcommand{\bA}{\mathbb{A}}$
$\newcommand{\Kc}{\overline{\mathcal{K}}}$
$\newcommand{\onesA}{\mathbf{1}_{|\bA|}}$
%% Multivariate-specific %%
$\newcommand{\phii}{\Phi_{2}}$
$\newcommand{\SgK}{\Sigma_{(\mathcal{K})}}$
$\newcommand{\SgKc}{\Sigma_{(\Kc)}}$
$\newcommand{\tauk}{\tau_{\mathcal{K}}}$
$\newcommand{\taukp}{\tau_{(\mathcal{K})}}$
$\newcommand{\rhok}{\rho_{\mathcal{K}}}$
$\newcommand{\gamk}{\gamma_{(\mathcal{K})}}$
$\newcommand{\rck}{r_{(\mathcal{K})}}$
$\newcommand{\rckc}{r_{(\Kc)}}$
$\newcommand{\alk}{\alpha_{\boldsymbol{j},(\mathcal{K})}}$
$\newcommand{\etak}{\eta_{\ell,(\mathcal{K})}}$
$\newcommand{\ujk}{u_{\boldsymbol{j},\mathcal{K}}}$

The generalization from [[Initial Notation for K crossed random effects|the univariate case]] follows fairly naturally. Being explicit with shapes, let us have $m = 1, \dots, M$ components and $k = 1, \dots, K$ categories, and model definition $\bA \subseteq 2^{[K]}$. Then we can adopt the original notation almost wholesale, with $\Yl \in \real^{M}$ and $\ail \in \real^{|\bA| \times M}$, $\xl \in \real^{p}$, and $B \in \real^{M\times p}$, so that 
$$\begin{align*} \mathbb{E}(\Yl \mid \xl) = g^{-1} \left( B\xl + \ail^{\tran}\onesA \right) . \end{align*}$$

We work in the probit case: 

> [!attention] Multivariate Crossed Probit Model
> The **Multivariate Crossed Probit Model in Latent Variable Form** can be given by 
> $$\begin{align*} \Yl = \mathbf{1}\left[ B\xl + \ail^{\tran} \onesA + \errl > 0\right] .  \end{align*}$$

The indicator is applied component-wise.

Here, $\errl \simiid \dnorm(\mathbf{0}_{M}, \Sigma_{E})$, $a_{\il, \mathcal{K}} \sim \dnorm(\mathbf{0}_{M}, \Sigma_{\mathcal{K}})$. 

$$\begin{align*}  \mathbb{P}(\Yl = \yl) &= \mathbb{P}\left( \ytl \odot \left\{ B\xl + \ail^{\tran} \onesA + \errl\right\} > 0  \right) \\ 
&= \mathbb{P}\left(\ytl \odot \left\{ B\xl + (\Sigma^{1 / 2} \uil)^{\tran}\onesA  \right\} > 0 \right) \\ \end{align*}$$

for $\Sigma = \Sigma_{E} + \sum_{\mathcal{K} \in \bA}\Sigma_{\mathcal{K}}$. The corresponding all likelihood *can* be written as the product of $N$ $M$-variate normal cdfs; since this is generally intractable for even moderate $M$, we consider a procedure applied pairwise. 

%% the mixed comes back into vogue  %%

## Option A:

$$\begin{align*}  \mathbb{P}(\Yl = \yl) &= \mathbb{P}\left( \ytl \odot \left\{ B\xl + \ail^{\tran} \onesA + \errl\right\} > 0  \right) \\ 
&= \mathbb{P}\left(\ytl \odot \left\{ B\xl + (\Sigma^{1 / 2} \uil)^{\tran}\onesA  \right\} > 0 \right) \\ 
\end{align*}$$
Let 
$$\begin{align*} \xi_{r} \sim \dnorm\left(\begin{pmatrix}
0 \\ 0
\end{pmatrix}, \begin{pmatrix}
 1 & r \\ r & 1
\end{pmatrix}\right).  \end{align*}$$
The likelihood for a single data point can be given by 
$$\begin{align*} \mathbb{P}(\Yl[m] = \yl[m], \Yl[m'] = \yl[m'])
&= \mathbb{P}\left(\begin{pmatrix}
\ytl[m] \\ \ytl[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\tran}\xl \\ \beta[m']^{\tran}\xl \end{pmatrix}  + \begin{pmatrix}
\ail[m]^{\tran} \onesA + \errl[m] \\ \ail[m']^{\tran} \onesA + \errl[m'] 
\end{pmatrix}\right\}   > \begin{pmatrix}
0 \\ 0
\end{pmatrix}\right) \\ 
&= \mathbb{P}\left(\begin{pmatrix}
\ytl[m] \\ \ytl[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\tran}\xl \\ \beta[m']^{\tran}\xl \end{pmatrix}  +  \begin{pmatrix}
\sqrt{\Sigma[m, m]} & 0 \\ 0 & \sqrt{\Sigma[m', m']}
\end{pmatrix} \xi_{r[m, m']}\right\}  > \begin{pmatrix}
0 \\ 0
\end{pmatrix}\right) \\ 
&= \mathbb{P}\left( \xi_{r[m, m']} >  -\begin{pmatrix}
\ytl[m]\beta[m]^{\tran}\xl / \sqrt{\Sigma[m, m] } \\ \ytl[m'] \beta [m']^{\tran}\xl / \sqrt{\Sigma[m', m']}
\end{pmatrix} \right) \\
&=: \mathbb{P}\left( \xi_{r[m, m']} >  -\begin{pmatrix}
\ytl[m]\gamma[m]^{\tran}\xl  \\ \ytl[m'] \gamma [m']^{\tran}\xl 
\end{pmatrix} \right) \\

&=: \phii(\eta_{\ell}[m], \eta_{\ell}[m']; \ytl[m] \ytl[m']r[m, m']),
\end{align*}$$
where
$$\begin{align*} \gamma[m] = \frac{\beta[m]}{\sqrt{\Sigma[m, m]}}, \qquad r[m, m'] = \frac{\Sigma[m, m']}{\sqrt{\Sigma[m, m] \Sigma[m', m']}}, \qquad \eta_{\ell}[m] = \ytl[m]\gamma[m]^{\tran}\xl. \end{align*}$$

$$\begin{align*} L_{m, m'} (\gamma[m], \gamma[m'], r[m, m']) = \prod_{\ell =1}^{N} \Phi_{2} (\eta_{\ell}[m], \eta_{\ell}[m']; \tilde{y}_{\ell}[m] \tilde{y}_{\ell}[m']r[m, m']), \end{align*}$$
so we can give a pairwise optimization from  
$$\begin{align*} L_{\text{all}} (\Gamma, \boldsymbol{r}) = \prod_{m, m': m > m'} L_{m, m'}(\gamma[m], \gamma[m'], r[m, m']). \end{align*}$$
The conditional likelihood can be given by
$$\begin{align*} \mathbb{P}\left( \Yl[m] = \yl[m], \Yl[m'] = \yl[m'] \mid \ail^{\tran}v_{\mathcal{K}} = a_{\boldsymbol{j}, (\mathcal{K})}\right)
&= \mathbb{P}\left(\begin{pmatrix}
\ytl[m] \\ \ytl[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\tran}\xl \\ \beta[m']^{\tran}\xl \end{pmatrix}  + \begin{pmatrix}
\ail[m]^{\tran} \onesA + \errl[m] \\ \ail[m']^{\tran} \onesA + \errl[m'] 
\end{pmatrix}\right\}   > \begin{pmatrix}
0 \\ 0
\end{pmatrix} \mid \ail^{\tran} v_{\mathcal{K}} = a_{\boldsymbol{j}, (\mathcal{K})}\right) \\ 
&= \mathbb{P}\left(\begin{pmatrix}
\ytl[m] \\ \ytl[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\tran}\xl + a_{\boldsymbol{j}, (\mathcal{K})}[m] \\ \beta[m']^{\tran}\xl + a_{\boldsymbol{j}, (\mathcal{K})}[m'] \end{pmatrix}  + \begin{pmatrix}
\ail[m]^{\tran} v_{\Kc} + \errl[m] \\ \ail[m']^{\tran} v_{\Kc} + \errl[m'] 
\end{pmatrix}\right\}   > \begin{pmatrix}
0 \\ 0
\end{pmatrix} \right) \\ 
&= \mathbb{P}\left(\begin{pmatrix}
\ytl[m] \\ \ytl[m']
\end{pmatrix} \odot  \left\{ \begin{pmatrix}
\beta[m]^{\tran}\xl + a_{\boldsymbol{j}, \mathcal{K}}[m] \\ \beta[m']^{\tran}\xl + a_{\boldsymbol{j}, \mathcal{K}}[m'] \end{pmatrix}  +  \begin{pmatrix}
\sqrt{ \SgKc[m, m] } & 0 \\ 0 & \sqrt{ \SgKc[m', m'] }
\end{pmatrix} \xi_{\rckc[m, m']}\right\}  > \begin{pmatrix}
0 \\ 0
\end{pmatrix}\right) \\ &= \mathbb{P}\left( \xi_{\rck[m, m']} > -\begin{pmatrix}
\ytl[m]\left(\beta[m]^{\tran}\xl + a_{\boldsymbol{j}, \mathcal{K}}[m]\right) / \sqrt{\SgKc[m, m]}\\ \ytl[m']\left(\beta[m']^{\tran}\xl + a_{\boldsymbol{j}, \mathcal{K}}[m']\right) / \sqrt{ \SgKc[m', m']}
\end{pmatrix} \right) \\
&=: \mathbb{P}\left( \xi_{\rck[m, m']} > -\begin{pmatrix}
\ytl[m]\left(\gamk[m]^{\tran}\xl + \alk[m]\right) \\ \ytl[m']\left(\gamk[m']^{\tran}\xl + \alk[m']\right)
\end{pmatrix} \right) \\
&=: \phii\left(\etak[m], \etak[m']; \ytl[m] \ytl[m']\rck[m, m']\right),
\end{align*}$$
where
$$\begin{align*} \gamk[m] = \frac{\beta[m]}{\sqrt{\SgKc[m, m]}}, \qquad \alk[m] = \frac{a_{\boldsymbol{j}, \mathcal{K}}[m]}{\sqrt{\SgKc[m, m]}}, \qquad \rck[m, m'] = \frac{\SgK[m, m']}{\sqrt{\SgK[m, m] \SgK[m', m']}}, \qquad \etak[m] = \ytl[m]\left(\gamk[m]^{\tran}\xl + \alk[m]\right). \end{align*}$$

Note the standard construction of $\tau$ applies: 
$$\begin{align*} \tauk^{2}[m] = \frac{\SgK[m, m]}{\Sigma[m, m] - \SgK[m, m]}, \qquad \gamk[m]= \gamma[m] \sqrt{ 1 + \tauk^{2} } .  \end{align*}$$
Further, we can write 
$$\begin{align*} \begin{pmatrix} \alk[m] \\ \alk[m'] \end{pmatrix} = \begin{pmatrix} \tauk[m] \ujk[m] \\ \tauk[m'] \ujk[m'] \end{pmatrix}, \qquad \begin{pmatrix} \ujk[m] \\ \ujk[m'] \end{pmatrix} \sim \dnorm\left( \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 & \rhok[m, m'] \\ \rhok[m, m'] & 1 \end{pmatrix} \right), \end{align*}$$
where
$$\begin{align*} \taukp^{2}[m, m'] = \frac{\SgK[m, m']}{\sqrt{\left(\Sigma[m, m] - \SgK[m, m]\right)\left(\Sigma[m', m'] - \SgK[m', m']\right)}}, \qquad \rhok[m, m'] = \frac{\taukp^{2}[m, m']}{\tauk[m] \tauk[m']}, \end{align*}$$
recovering $\taukp^{2}[m, m] = \tauk^{2}[m]$ on the diagonal.
Note the introduced $(\mathcal{K})$ arguments for $\mathcal{K} = \emptyset$ map nicely to the [[All Likelihood|all likelihood]]; thus to avoid invoking the further $\mathcal{K}$ subset, we let $\mathcal{K}$ be implicit; in particular, we can think 

$$\begin{align*} L_{m, m'}(\gamma, \gamma', \tau^{2}, \tau'^{2}, t ; \mathcal{K}) &= \prod_{\boldsymbol{j} \in \pi_{\mathcal{K}}(\mathcal{S}_{0})} \int_{\mathbb{R}^{2}} \left[ \prod_{\il \mid \boldsymbol{j}} \Phi_{2}\left( \eta_{\ell}[m], \eta_{\ell}[m']; \tilde{y}_{\ell}[m] \tilde{y}_{\ell}[m']t\right) \right] \text{diag}(\tau, \tau') \varphi _{2}(\ujk[m], \ujk[m']; \rho_{\mathcal{K}}) \left[ 2\pi \sqrt{ 1 - \rho_{\mathcal{K}}^{2} } \right]^{-1} \, d\boldsymbol{u}_{j} \end{align*}$$

and then the slice likelihood can be given in the same joint optimization form; we end up with an optimization problem over all $Mp$ additional variables, with 

$$\begin{align*} L_{\mathcal{K}}(\Sigma_{\mathcal{K}};\gamma) := \sum_{m > m'} w_{mm'} L_{mm'}(\gamma[m], \gamma[m]', \tau^{2}[m], \tau^{2}[m'];\mathcal{K}).  \end{align*}$$



