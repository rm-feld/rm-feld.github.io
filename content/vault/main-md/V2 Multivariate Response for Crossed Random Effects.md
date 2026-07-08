---
modified: 2025-12-03T10:28:18-08:00
created: 2025-11-29T18:08:44-08:00
---
Rewrite of [[Multivariate Response]]. 

**NB:** changed notation a little here. I think we'll sacrifice placeholder $Z$ standard normal in place of $Z_{ij}$ probit latent, so that $W_{ij}$ can be utilized for sign, in line with code implementation. 
# Bivariate Response
We begin by looking at the bivariate case, instead of the multivariate case. We will find later that this analysis is sufficient. 

Consider the model given by 
$$\begin{align} Z_{ij} = BX_{ij}+ a_{i} + b_{j} + \varepsilon_{ij} \end{align}$$
for which $X_{ij} \in \mathbb{R}^{p + 1}$ is known and
$$\begin{align} a_{i} \sim \mathcal{N}(\mathbf{0}, \Sigma_{A}), \,\,\, b_{j} \sim \mathcal{N}(\mathbf{0}, \Sigma_{B}), \,\,\,\, \varepsilon_{ij} \sim \mathcal{N}(\mathbf{0}, \Sigma_{\varepsilon}), \end{align}$$
where we further impose $\Sigma_{\varepsilon}$ unit homoskedastic with some correlation $\rho_{\varepsilon}$. We do not observe $Z_{ij}$ but instead $Y_{ij} = \mathbf{1}\left[Z_{ij} > 0 \right]$, and our goal is to recover $\Sigma_{A}$, $\Sigma_{B}$, $r_{\varepsilon}$, and $B:= (\beta_{1}, \beta_{2})^{\intercal} \in \mathbb{R}^{2 \times (p + 1)}$. We'll use $W_{ij} := \text{diag}(2Y_{ij} - 1)$ to deal with the easier signs. Here, we'll label
$$\begin{align} \Sigma_{A} := \begin{pmatrix}
\sigma^{2}_{A 1} & \sigma_{A 12} \\
\sigma_{A 12} & \sigma^{2}_{A 2}
\end{pmatrix} ,\end{align}$$
with $\Sigma_{B}$ analogous. 

Note that, in the spirit of marginal misspecification, $\beta_{1}$, $\beta_{2}$, $\sigma^{2}_{A 1}$, $\sigma^{2}_{A 2}$, $\sigma^{2}_{B 1}$, and $\sigma^{2}_{B 2}$ are all immediately recoverable by treating the bivariate response model as two independent univariate response models. That is, we can immediately employ vanilla `arcProbit` to recover these terms. 

Thus the parameters of interest are $\sigma_{A 12}$, $\sigma_{B 12}$, and $\rho_{\varepsilon}$, the cross-terms. Intuitively, these cross-covariance terms require information about both $Y_{ij}^{(1)}$ and $Y_{ij}^{(2)}$; thus we consider a generalization of `arcProbit` utilizing bivariate normals. 

## All Likelihood
Let us start with the all likelihood. With some careful attention to signs, we can find that, collecting $\sigma^{2}_{1} := 1 + \sigma^{2}_{A1} + \sigma^{2}_{B 1}$, $\sigma^{2}_{2}$ analogous, and $\sigma_{12}:= \rho_{\varepsilon} + \sigma_{A 12 } + \sigma_{B 12}$,

$$\begin{align*} \text{Pr}(Y_{ij} = y_{ij}) &=  \text{Pr}(W_{ij}Z_{ij} > \mathbf{0}) \\
&= \text{Pr}(W_{ij}(BX_{ij} + a_{i} + b_{j} + \varepsilon_{ij}) > \mathbf{0}) \\
&= \text{Pr}\left(\begin{pmatrix}
\sigma^{-1}_{1} & 0\\
0& \sigma^{-1}_{2}
\end{pmatrix}W_{ij}(BX_{ij} + a_{i} + b_{j} + \varepsilon_{ij}) > \mathbf{0}\right) \\
&= \Phi_{2}\left( \frac{w_{ij}^{(1)}\beta_{1}^{\intercal}x_{ij}}{\sigma_{1}},  \frac{w_{ij}^{(2)}\beta_{2}^{\intercal}x_{ij}}{\sigma_{2}};  \frac{\sigma_{12} |W_{ij}|}{\sigma_{1} \sigma_{2}}  \right)
\end{align*}$$
where we take $> \mathbf{0}$ in the rectangular sense, and we stress $|W_{ij}|$ as the signed determinant. Further, note that all but $\sigma_{12}$ is known (in the sense that we have [[ARC]] estimates for them), so we're solving for a standard bivariate probit with correlation (except we already know $B$? so more of a direct maximization). Clearly though, I can solve for $\sigma_{12}$ in this regime. 

The misspecified all log-likelihood $\mathcal{L}_{\text{all}}$ for parameter $\rho:= \sigma_{12} / (\sigma_{1} \sigma_{2})$ can be written
$$\begin{align*} \mathcal{L}_{\text{all}}(\rho) &= \sum_{(i, j) \in \mathcal{S}} \log  \Phi_{2} \left( \frac{w_{ij}^{(1)}\beta_{1}^{\intercal} x_{ij}}{\sigma_{1}}, \frac{w_{ij}^{(2)}\beta_{2}^{\intercal}x_{ij}}{\sigma_{2}}; \rho|W_{ij}| \right) \\
&=: \sum_{(i, j) \in \mathcal{S}} \log \Phi_{2}(\eta_{ij}^{(1)}, \eta_{ij}^{(2)}; \rho |W_{ij}|)
\end{align*}$$
The score emerges as
$$\begin{align*} \frac{ \partial  }{ \partial \rho } \mathcal{L}_{\text{all}}(\rho) = \sum_{(i, j) \in \mathcal{S}} |W_{ij}| \frac{\varphi_{2}\left( \cdot \right)}{\Phi_{2}(\cdot)}
 \end{align*}$$
 where for sanity we truncate the terms in the parentheses (the per-$ij$ arguments are the same across). The Hessian can be given by %% writing analogous to the mode search update %%
$$\begin{align*} \frac{ \partial^{2}  }{ \partial \rho^{2} }  \mathcal{L}_{\text{all}}(\rho) = \sum_{(i, j) \in \mathcal{S}} \frac{\varphi_{2}(\cdot)}{\Phi_{2}^{2}(\cdot)}\left[ \Phi_{2} (\cdot)\cdot h_{ij} - \varphi_{2}(\cdot) \right] \end{align*}$$
where $h_{ij}$ deriving from $\varphi_{2}'(\cdot) = \varphi_{2}(\cdot)\cdot h_{ij}$ is given explicitly by 
$$\begin{align*} h_{ij} = \frac{(1 + \rho^{2})\eta_{ij}^{(1)}\eta_{ij}^{(2)} - |W_{ij}|\rho([\eta_{ij}^{(1)}]^{2} + [\eta_{ij}^{(2)}]^{2}) + |W_{ij}|\rho(1 - \rho^{2})}{(1 - \rho^{2})^{2}}; \end{align*}$$
thus we can root-search via [[Newton-Raphson]], eg., with the above closed form (precomputing $\Phi_{2}$, $\varphi_{2}$ to use standard implementations). Thus we have access to $\rho$ if it is unimodal. #TODO 
## Row Likelihood
We also have the standard analogues. Skipping some steps, notice we can write
$$\begin{align*} \text{Pr}(Y_{ij} = y_{ij}\mid a) &= \text{Pr}\left(\begin{pmatrix}
1 / \sqrt{ \sigma^{2}_{B 1} + 1 } & 0 \\
0 & 1 / \sqrt{ \sigma^{2}_{B 2} + 1 }
\end{pmatrix} W_{ij} (B X_{ij} + a_{i} + b_{j} + \varepsilon_{ij}) > \mathbf{0} \mid a\right) \\
&= \Phi_{2}\left( \frac{w_{ij}^{(1)}(\beta_{1}^{\intercal}x_{ij} + a_{i}^{(1)})}{\sqrt{ \sigma^{2}_{B 1} + 1 }} , \frac{w_{ij}^{(2)}(\beta_{2}^{\intercal}x_{ij} + a_{i}^{(2)})}{\sqrt{ \sigma^{2}_{B 2} + 1 }}; |W_{ij}|\frac{\rho_{\varepsilon} + \sigma_{B 12}}{\sqrt{ (\sigma^{2}_{B 1}  + 1) (\sigma^{2}_{B 2} + 1)}} \right) \\
&= \Phi_{2}\left( \frac{w_{ij}^{(1)}(\beta_{1}^{\intercal}x_{ij} + a_{i}^{(1)})}{\sqrt{ \sigma^{2}_{B 1} + 1 }} , \frac{w_{ij}^{(2)}(\beta_{2}^{\intercal}x_{ij} + a_{i}^{(2)})}{\sqrt{ \sigma^{2}_{B 2} + 1 }}; |W_{ij}|\frac{\rho \sigma_{1}\sigma_{2} - \sigma_{A 12}}{\sqrt{ (\sigma^{2}_{B 1}  + 1) (\sigma^{2}_{B 2} + 1)}} \right)
\end{align*}$$

for which $a_{i}$ is known up to cross-correlation, and for which the last line rewrites the given so that we only have unknown $\sigma_{A 12}$. From here, there are two ways that we can rewrite $a_{i}$ for ease of calculation. At this point, we can either make $a_{i}$ a product of a "proper" uncorrelated univariate normal, or we can do a termwise normalization and keep an underlying $u_{i}$ correlated bivariate unit normal. let's see what terms come out of each. 

### Latent Correlated Unit
**NOTATION BAD I THINK $\lambda$ for under the hood full argument (original code uses `arg`)**

If I let $u_{i}$ correlated bivariate unit normal, then my correlation emerges as $\rho_{A}:= \sigma_{A 12 } /(\sigma_{A 1} \sigma_{A 2})$ %% bad bad bad notation oops %% and 

$$\begin{align*} G_{A} :=  \begin{pmatrix}
\sigma_{A 1 } / \sqrt{ \sigma_{B 1}^{2} + 1 } & 0 \\
0 & \sigma_{A 2} / \sqrt{ \sigma^{2}_{B 2} + 1 }
\end{pmatrix} \end{align*}$$
is a *known* matrix for which we can now write the scaled $a_{i}$ with $G_{A}$. Collecting $\eta_{ij}^{(1)} = w_{ij}^{(1)}\left( \beta_{1}^{\intercal}x_{ij} \right) / \sqrt{ \sigma^{2}_{B1} + 1 }$, $\eta_{ij}^{(2)} = w_{ij}^{(2)}\left( \beta_{2}^{\intercal}x_{ij} \right) / \sqrt{ \sigma^{2}_{B 2} + 1 }$, $\eta_{ij} := (\eta_{ij}^{(1)}, \eta_{ij}^{(2)})$we have

$$\begin{align*} \text{Pr}(Y_{ij} = y_{ij} \mid a) = \Phi_{2}\left(\eta_{ij} + G_{A}u_{i}; |W_{ij}| \frac{\rho \sigma_{1}\sigma_{2} - \rho_{A}\sigma_{A 1}{\sigma_{A 2}}}{\sqrt{ (\sigma^{2}_{B 1} + 1) (\sigma^{2}_{B 2} + 1)}} \right)\end{align*}$$
Where the only unknown we have dependence on is $\rho_{A}$. The corresponding likelihood is given by 
$$\begin{align*} \mathcal{L}_{\text{row}}(\rho_{A}) &:= \prod_{i = 1}^{I} \int_{\mathbb{R}^{2}} \prod_{(i, j) \in \mathcal{S}_{i}} \Phi_{2}\left( \eta_{ij} + G_{A} u_{i}; |W_{ij} | \frac{\rho \sigma_{1} \sigma_{2} - \rho_{A}\sigma_{A 1} \sigma_{A 2}}{\sqrt{ (\sigma^{2}_{B 1} + 1)(\sigma^{2}_{B 2} + 1) }} \right) \varphi_{2}(u_{i}; \rho_{A}) \, du_{i} \\
&=: \prod_{i = 1}^{I} \int_{\mathbb{R}^{2}} \prod_{(i, j) \in \mathcal{S}_{i}} \Phi_{2}\left( \eta_{ij} + G_{A} u_{i}; \tilde{\rho}_{ij} \right) \, \varphi_{2}(u_{i}; \rho_{A}) \, du_{i} \\
&=: \prod_{i =1}^{I} \int _{\mathbb{R}^{2}}   L_{i\bullet }(\rho_{A}) \varphi_{2}(u_{i}; \rho_{A}) \, du_{i}. 
\end{align*}$$
#### Implementation Notes
[[The Standard Bashes|The standard fact]] 
$$\begin{align*} \frac{ \partial  }{ \partial x_{1} } \Phi_{2}(x_{1}, x_{2}; r) = \varphi(x_{1})\Phi\left( \frac{x_{2} - rx_{1}}{\sqrt{ 1 - r^{2} }} \right) \end{align*}$$

Lets us arrive at 
$$\begin{align*} \frac{ \partial  }{ \partial u_{i}^{(1)} } \log \left\{ L_{i\bullet }(\rho _{A})  \right\} &= \sum_{(i, j) \in \mathcal{S}_{i}} \frac{\varphi(\lambda_{ij}^{(1)})\Phi\left( (\lambda_{ij}^{(2)} - \rho_{ij}\lambda_{ij}^{(1)})  / \sqrt{ 1 - \rho_{ij}^{2} } \right) }{\Phi_{2}(\cdot)} \cdot \frac{\sigma_{A 1}}{\sqrt{ \sigma^{2}_{B 1 } + 1 }}; \end{align*}$$

Writing in gradient form, a score for $u_{i}$ can be written by 
$$\begin{align*} \nabla_{u} \log \left\{ L_{i\bullet }(\rho_{A}) \varphi_{2}(u_{i}; \rho_{A}) \right\} = \sum_{(i, j) \in \mathcal{S}_{i}} \frac{1}{\Phi_{2}(\cdot)}G_{A}^{\intercal} \begin{pmatrix}
\varphi(\lambda_{ij}^{(1)})\Phi\left( (\lambda_{ij}^{(2)} - \rho_{ij}\lambda_{ij}^{(1)}) / \sqrt{ 1 - \rho_{ij}^{2} } \right) \\
\varphi(\lambda_{ij}^{(2)})\Phi\left( (\lambda_{ij}^{(1)} - \rho_{ij}\lambda_{ij}^{(2)})  / \sqrt{ 1 - \rho_{ij}^{2} } \right) 
\end{pmatrix} - \Sigma_{A}^{-1} u_{i}. \end{align*}$$

The Hessian is uglier; but writing it with respect to the Hessian $H_{\lambda}$ of $L_{i}(\rho_{A})$ that ignores the scaling, we can write

$$\begin{align*} H_{u} = \sum_{(i, j) \in \mathcal{S}_{i}} G_{A}^{\intercal}\left\{ H_{\lambda} -  \frac{\nabla_{\lambda}\Phi_{2}(\cdot)\nabla_{\lambda}\Phi_{2}(\cdot)^{\intercal}}{\Phi_{2}(\cdot)^{2}} \right\} G_{A} - \Sigma_{A}^{-1}.  \end{align*}$$
Clearly we can write all of this with respect to $\rho_{A}$, and so we have the information needed for an [[Adaptive Gauss Hermite Quadrature|AGH]] implementation. 


### Latent Standard Bivariate Normal
But perhaps we'd prefer $u_{i}$ uncorrelated. 

$$\begin{align*} G_{A}:= \frac{1}{\sqrt{ \sigma^{2}_{A 1} + \sigma^{2}_{A 2} + 2\sqrt{ \sigma^{2}_{A 1}\sigma^{2}_{A 2} - \sigma_{A 12} ^{2} }} } \begin{pmatrix}
\left( \sigma^{2}_{A 1} + \sqrt{ \sigma^{2}_{A 1} \sigma^{2}_{A 2} - \sigma^{2}_{A 12} }  \right) / \sqrt{ \sigma^{2}_{B 1} + 1 } & \sigma_{A 12} / \sqrt{ \sigma^{2}_{B1} + 1 } \\
\sigma_{A 12} / \sqrt{ \sigma^{2}_{B 2} + 1 } & \left( \sigma^{2}_{A 1} + \sqrt{ \sigma^{2}_{A 1} \sigma^{2}_{A 2} - \sigma^{2}_{A 12} } \right) / \sqrt{  \sigma^{2}_{B 2} + 1 }
\end{pmatrix}.   \end{align*}$$
I'm a little skeptical of this one - with our only unknown being $\sigma_{A 12}$, it seems unwieldy to try to solve for it "as separated", which $\sigma_{A 12}$ dependence in each term. This $G_{A}$ isn't calculable, whereas the former one is. But we probably will have to bash out the likelihood as well. 

Okay, so with this, the row likelihood is given by 

$$\begin{align*} \mathcal{L}_{\text{row}}() \end{align*}$$



$$\begin{align*} \text{Pr}(Y_{ij} = y_{ij}\mid b) &= \text{Pr}\left(\begin{pmatrix}
1 / \sqrt{ \sigma^{2}_{A 1} + 1 } & 0 \\
0 & 1 / \sqrt{ \sigma^{2}_{A 2} + 1 }
\end{pmatrix} W_{ij} (B X_{ij} + a_{i} + b_{j} + \varepsilon_{ij}) > \mathbf{0} \mid b\right) \\
&= \Phi_{2}\left( \frac{w_{ij}^{(1)}(\beta_{1}^{\intercal}x_{ij} + b_{j}^{(1)})}{\sqrt{ \sigma^{2}_{A 1} + 1 }}, \frac{w_{ij}^{(2)}(\beta_{2}^{\intercal}x_{ij} + b_{j}^{(2)})}{\sqrt{ \sigma^{2}_{A 2} + 1 }}; |W_{ij}|\frac{\rho_{\varepsilon} + \sigma_{A 12}}{\sqrt{ (\sigma^{2}_{A 1}  + 1) (\sigma^{2}_{A 2} + 1)}} \right)\end{align*},$$

