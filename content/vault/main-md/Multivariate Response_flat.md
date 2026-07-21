---
tags: [no-index]
up: "[[Multivariate Response]]"
modified: 2026-07-13T11:24:39-07:00
created: 2026-07-13T11:24:10-07:00
---

\section{Multivariate Response Form}
We consider the model given by $Y_{ij} = \mathbf{1}\left[W_{ij} > 0 \right]$, taken componentwise over $k = 1, \dots, K$, for 

\begin{align} W_{ij} = Bx_{ij} + a_{i} + b_{j} + \varepsilon_{ij}; \end{align}

simplifying to the bivariate case, we have $B \in \mathbb{R}^{2 \times p}$ a set of stacked coefficients $B:= \left( \beta_{1}^{\intercal} \, \, \beta_{2}^{\intercal}\right)^{\intercal}$, along with

\begin{align} a_{i} \sim \mathcal{N} \left(\begin{pmatrix}
0 \\
0
\end{pmatrix}, \begin{pmatrix}
\sigma^{2}_{A_{1}} & \rho_{A} \\ \rho_{A} & \sigma^{2}_{A_{2}}
\end{pmatrix}\right) , \,\,\, b_{j} \sim \mathcal{N} \left(\begin{pmatrix}
0 \\
0
\end{pmatrix}, \begin{pmatrix}
\sigma^{2}_{B_{1}} & \rho_{B} \\ \rho_{B} & \sigma^{2}_{B_{2}}
\end{pmatrix}\right), \,\,\,\,\,\,\varepsilon_{ij} \sim \mathcal{N} \left(\begin{pmatrix}
0 \\
0
\end{pmatrix}, \begin{pmatrix}
1 & \rho_{\varepsilon} \\ \rho_{\varepsilon} & 1
\end{pmatrix}\right). \end{align}

Under the standard ARC balance conditions, it is clear that we can get consistent estimates for $\sigma^{2}_{A_{1}}$, $\sigma^{2}_{A_{2}}$, $\sigma^{2}_{B_{1}}$, $\sigma^{2}_{B_{2}}$, and $B$, by applying standard ARC componentwise. A few different directions emerge for solving for $\rho$ terms; I was running into a wall for the second, but I outline both here.

\section{Component-wise Conditional Distributions}
\subsection{Derivation}
We motivate this with oracle knowledge of $W_{ij(2)}$ (vs. $Y_{ij(2)}$). Throughout, we assume no missing observations within components, ie. I observe $W_{ij(1)}$ if and only if I observe $W_{ij(2)}$. 

We have a closed form conditional distribution of components via Schur complementation; defining

\begin{align} \Sigma :=  \begin{pmatrix}
\sigma^{2}_{1} & \rho \\
\rho & \sigma^{2}_{2}
\end{pmatrix} &:= \begin{pmatrix}
\sigma^{2}_{A_{1}} + \sigma^{2}_{B_{1}} + 1 & \rho_{A} + \rho_{B} + \rho_{\varepsilon} \\
\rho_{A} + \rho_{B} + \rho_{\varepsilon} & \sigma^{2}_{A_{2}} + \sigma^{2}_{B_{2}} + 1
\end{pmatrix} \end{align}

the marginal covariance of the $W_{ij}$ vector, it emerges that

\begin{align} W_{ij(1)} \mid W_{ij(2)} \sim \mathcal{N}\left( x_{ij}^{\intercal}\beta_{1} + \frac{\rho}{\sigma_{2}^{2}}\left( W_{ij(2)} - x_{ij}^{\intercal} \beta_{2} \right),  \sigma^{2}_{1} - \frac{\rho^{2}}{\sigma^{2}_{2}} \right). \end{align}


It follows that

\begin{align} \mathbb{P}(Y_{ij(1)} = 1 \mid W_{ij(2)}) &= \mathbb{P}(W_{ij(1)} > 0 \mid W_{ij(2)}) \\
 &= \mathbb{P}\left( x_{ij}^{\intercal}\beta_{1} + \frac{\rho}{\sigma^{2}_{2}} \left( W_{ij(2)} - x_{ij}^{\intercal}\beta_{2} \right) + \tilde{Z}_{ij}\sqrt{ \sigma_{1}^{2} - \frac{\rho^{2}}{\sigma_{2}^{2}} } > 0 \mid W_{ij(2)}\right) \\
&= \Phi\left( \frac{x_{ij}^{\intercal}\beta_{1} + \rho \sigma_{2}^{-2}\left( W_{ij(2)} - x_{ij}^{\intercal}\beta_{2} \right)}{\sqrt{ \sigma_{1}^{2} - \rho^{2} / \sigma _{2}^{2} }} \right);\end{align}

thus in the marginal case, we can evaluate the integral 

\begin{align} \mathbb{P}(Y_{ij(1)} = 1 \mid Y_{ij(2)}) &= \int _{\tilde{A}_{ij(2)}}  \Phi\left( \frac{x_{ij}^{\intercal}\beta_{1} + \rho \sigma_{2}^{-2}\left( W_{ij(2)} - x_{ij}^{\intercal}\beta_{2} \right)}{\sqrt{ \sigma_{1}^{2} - \rho^{2} / \sigma _{2}^{2} }} \right)  \, dP(W_{ij(2)}) \\
&= \int _{A_{ij(2)}}  \Phi\left( \frac{x_{ij}^{\intercal}\beta_{1} + \rho \sigma_{2}^{-2}\left( \sigma_{2} u \right)}{\sqrt{ \sigma_{1}^{2} - \rho^{2} / \sigma _{2}^{2} }} \right) \varphi(u)\, du  \\
&:= \ell_{ij, 1\mid 2}.  \end{align}

for $A_{ij(2)}$ the appropriate domain of integration based on the value of $Y_{ij(2)}$; ie.

\begin{align} W_{ij(2)} > 0 \implies x_{ij}^{\intercal}\beta_{2} + \sigma_{2} u > 0 \implies u > - \frac{x_{ij}^{\intercal}\beta_{2}}{\sigma_{2}} \end{align}

so that $A_{ij(2)} = [-x_{ij}^{\intercal}\beta_{2} / \sigma_{2}, \infty)$ when $Y_{ij(2)} = 1$, and by symmetry we recover the opposite $A_{ij(2)} = (-\infty, -x_{ij}^{\intercal}\beta_{2} / \sigma_{2})$ for $Y_{ij(1)} = 0$. Thus maximization can be performed over a corresponding log likelihood, respecting a constraint of integral complexity to the single-dimension case. To be explicit, let

\begin{align} \hat{\ell}_{ij, 1 \mid 2}(\rho) = \int _{\hat{A}_{ij(2)}} \Phi\left( \frac{x_{ij}^{\intercal}\hat{\beta}_{1} + \rho \hat{\sigma}^{-1}_{2} u}{\sqrt{ \hat{\sigma}_{1}^{2} - \rho^{2} / \hat{\sigma}^{2}_{2}}}\right) \varphi(u)\, du, \end{align}

inheriting the estimates from the original solve, and maximize 

\begin{align} L_{1 \mid 2}(\rho) = \sum_{i, j \in \mathcal{S}} y_{ij} \log \hat{\ell}_{ij, 1 \mid 2}(\rho) + (1 - y_{ij}) \log (1 - \hat{\ell}_{ij, 1 \mid 2}(\rho)).  \end{align}

The marginal $W_{ij(2)}$ will have no $\rho$ contribution, and can thus be omitted from the above. 

There are of course some concerns with the above; I highlight two. First, we are fairly reliant on $\beta$, and $\sigma$ estimates; while this is also a feature of the ARC solve, reliance on a larger body of estimates (especially correlated ones) may accrue undesired error. Additionally, while the derivation of $\ell_{ij, 2 \mid 1}$ the symmetric case is clear from the above, it is unclear how and when $1 \mid 2$ would be preferable over $2 \mid 1$, or some mixture of both (sample, partition, sum, etc.), or how we could incorporate both. We have in our data domain that 0 is more common than 1 - perhaps there is some choice condition there that is appropriate. Thus we might want to do something direct with the 4 (or more generally $2^{k}$) potential responses, working directly with the bivariate distribution. Since we always have component-wise access to conditional normals, I note that the above does generalize fairly naturally. 

We now consider solving for $\rho_{A}$; $\rho_{B}$ will be a symmetric solve, and then we have recovered everything with $\rho$ identified above (backsolve for $\rho_{\varepsilon}$ is trivial). Doing the same complementation strategy, this time with just $a_{i(2)}$, use that

\begin{align} a_{i(1)} \mid a_{i(2)} \sim \mathcal{N}\left( \frac{\rho_{A}}{\sigma^{2}_{A_{2}}}a_{i(2)}, \sigma^{2}_{A_{1}} - \frac{\rho_{A}^{2}}{\sigma_{A_{1}}^{2}} \right) \end{align}

so that 

\begin{align} W_{ij(1)} \mid a_{i(2)} \sim \mathcal{N}\left(x_{ij}^{\intercal}\beta_{1} + \frac{\rho_{A}}{\sigma^{2}_{A_{2}}}a_{i(2)} , \sigma^{2}_{A_{1}} + \sigma^{2}_{B_{1}} + 1 - \frac{\rho_{A}^{2}}{\sigma^{2}_{A_{1}}} \right) \end{align}


\begin{align} \mathbb{P}(W_{ij(1)} > 0 \mid a_{i(2)}) &= \mathbb{P}\left( x_{ij}^{\intercal}\beta_{1} + a_{i(1)} + b_{j(1)} + \varepsilon_{ij(1)} > 0 \mid a_{i(2)}\right)  \\
&= \Phi\left(\frac{x_{ij}^{\intercal} \beta_{1} + \rho_{A}\sigma_{A_{2}}^{-2} a_{i(2)}}{\sqrt{ \sigma_{A_{1}}^{2} + \sigma_{B_{1}}^{2} + 1 - \rho_{A}^{2} / \sigma^{2}_{A_{1}} }}  \right).\end{align}

Since our composite likelihoods are inherently misspecified, it can be natural to use knowledge of marginal $a_{i(2)} \sim \mathcal{N}(0, \sigma^{2}_{A_{2}})$ to recover $\mathbb{P}(W_{ij(1)} > 0)$. Then we would get a natural notion of $\ell_{ij, 1 \mid 2}$ as previous, for $\rho_{A}$, and an analogous maximization. But it may be possible to nudge the $a_{i(2)}$ with currently unused $W_{ij(2)}$. We can try to incorporate this information in the following way; use that $(a_{i(2)}, W_{ij(2)})$ is normally distributed. Deriving the cross term, we find that 

\begin{align} \text{Cov}(a_{i(2)}, W_{ij(2)}) &= \mathbb{E}\left[ a_{i(2)}\left( x_{ij}^{\intercal}\beta_{2} + a_{i(2)} + b_{j(2)} + \varepsilon_{ij(2)} - x_{ij}^{\intercal}\beta_{2} \right) \right] = \sigma^{2}_{A_{2}}, \end{align}

which nets us that 

\begin{align} & a_{i(2)} \mid W_{ij(2)} \sim \mathcal{N}\left( \frac{\sigma^{2}_{A_{2}}}{\sigma_{2}^{2}}\left( W_{ij(2)} - x_{ij}^{\intercal}\beta_{2} \right) , \sigma^{2}_{A_{2}} - \frac{\sigma^{4}_{A_{2}}}{\sigma^{2}_{2}}\right);  \end{align}

having access only to $W_{ij(2)} > 0$, we'd be integrating over the positive domain of $W_{ij(2)}$; with an obvious lack of independence in $W_{ij(2)}$ and $a_{i(2)}$, it seems as though the ultimate integration is indeed bivariate.
\subsection{Formal Optimization Statement}


\subsection{Implementation}
Applying Adaptive Gauss Hermite Quadrature requires that we recover the posterior mode of the latent. 




\section{Bivariate Integration}
Perhaps bivariate integration is a cost we are willing to take; though we of course also care about growth of the number of integrations, our concern is generally in avoiding (very) high dimensional integrals, and \cite{jackelNoteMultivariateGaussHermite2005} has some notes on adapting Gauss-Hermite Quadrature to higher dimensions, so implementation is perhaps not terrible. 

In this case, our interest is in the tuple of sign information. A first (wrong) instinct is to normalize with the marginal covariance of $W_{ij}$; this degrades sign information, so cannot be used. Instead, we might keep to something still applied termwise, 

\begin{align} \begin{pmatrix}
\sigma_{1}^{-1} & 0 \\
0 & \sigma_{2}^{-1}
\end{pmatrix} W_{ij}  \sim \mathcal{N}\left( \begin{pmatrix}
x_{ij}^{\intercal}\beta_{1} / \sigma_{1} \\
x_{ij}^{\intercal}\beta_{2} / \sigma_{2}
\end{pmatrix}, \begin{pmatrix}
1 & \rho \\
\rho & 1
\end{pmatrix} \right)   . \end{align}

Since we still have estimates of $\sigma_{1}$, $\sigma_{2}$, $\beta_{1}$, and $\beta_{2}$, this is integration over the correct domain (of the $2^{k}$ responses, for the correct sign relations) for bivariate normal with correlation $\rho$. log likelihood is natural. In the standard manner, we can also consider

\begin{align} W_{ij} \mid a_{i} \sim \mathcal{N}\left( \begin{pmatrix}
x_{ij}^{\intercal}\beta_{1} + a_{i(1)}\\
x_{ij}^{\intercal} \beta_{2} + a_{i(2)}
\end{pmatrix}, \begin{pmatrix}
\sigma^{2}_{B_{1}} + 1 & \rho_{B} + \rho_{\varepsilon} \\
\rho_{B} + \rho_{E} & \sigma^{2}_{B_{2}} + 1 
\end{pmatrix} \right)  \end{align}

so that (rewriting $\rho_{B} + \rho_{E} = \rho - \rho_{A}$), 

\begin{align} \begin{pmatrix}
(\sigma^{2}_{B_{1}} + 1)^{- 1 / 2} & 0 \\
0 & (\sigma^{2}_{B_{2}} + 1)^{ - 1/ 2}
\end{pmatrix}W_{ij} \mid a_{i} \sim \mathcal{N}\left(  \begin{pmatrix}
x_{ij}^{\intercal}\beta_{1} + a_{i(1)}/\sqrt{ \sigma^{2}_{B_{1}} + 1 }  \\
x_{ij}^{\intercal}\beta_{2} + a_{i(2)} / \sqrt{ \sigma^{2}_{B_{2}} + 1 }
\end{pmatrix} , \begin{pmatrix}
1 & 1 - \rho_{A} \\
1 - \rho_{A} & 1
\end{pmatrix}\right).  \end{align}

Then with the appropriate thresholds to match signs, we can use the bivariate normal cdf and integrate over $a_{i}$. Clearly the distribution of $a_{i}$ does not depend on $\rho_{B}$ or $\rho_{\varepsilon}$, so estimation is only over $\rho_{A}$ or estimated quantities. It should be noted that we are calculating a bivariate cdf within a bivariate integration. 

\subsection{Formal Statement}
Let us be more direct with the final form of the above. We have for the below $Z$ placeholders being distributed standard normal with correlation $\rho$ that


\begin{align} \text{Pr}\left(Y_{ij} = \begin{pmatrix}
1 \\
1
\end{pmatrix}\right) &= \text{Pr}(W_{ij}^{(1)} > 0, W_{ij}^{(2)} > 0)  \\
&= \text{Pr}\left( x_{ij}^{\intercal}\beta_{1} / \sigma_{1} + Z^{(1)} > 0, x_{ij}^{\intercal}\beta_{2} + Z^{(2) } > 0\right) \\
&= \text{Pr}\left( Z > -x_{ij}^{\intercal}\gamma \right) \\
&= \text{Pr}\left( Z < x_{ij}^{\intercal}\gamma \right)\\
&= \Phi_{2}\left( x_{ij}^{\intercal}\beta_{1}/\sigma_{1}, x_{ij}^{\intercal}\beta_{2} / \sigma_{2}; \rho \right). \end{align}



\begin{align} \text{Pr}\left( Y_{ij} = \begin{pmatrix}
1 \\
0
\end{pmatrix} \right) &= \text{Pr}(W_{ij}^{(1)} > 0, W_{ij}^{(2)} \leq 0) \\
&= \text{Pr}\left( x_{ij}^{\intercal}\beta_{1} / \sigma_{1} + Z^{(1)} > 0, x_{ij}^{\intercal}\beta_{2} + Z^{(2)} \leq 0 \right)  \\
&= \text{Pr}\left( Z ^{(1)} > -x_{ij}^{\intercal}\beta_{1} / \sigma_{1}, -Z^{(2)} > x_{ij}^{\intercal}\beta_{1} / \sigma_{1} \right) \\
&= \text{Pr}\left( -Z^{(1)} < x_{ij}^{\intercal}\beta_{1} , Z^{(2)} < -x_{ij}^{\intercal}\beta_{1} / \sigma_{1}\right) \\
&= \Phi_{2} \left( x_{ij}^{\intercal}\beta_{1} / \sigma_{1}, -x_{ij}^{\intercal}\beta_{2} / \sigma_{2}; -\rho \right) .\end{align}


It turns out that we can collect all of this with 

\begin{align} \text{Pr}(Y_{ij} = y_{ij}) = \Phi_{2}\left( w_{ij}^{(1)}x_{ij}^{\intercal}\beta_{1}  / \sigma_{1}, w_{ij}^{(2)}x_{ij}^{\intercal}\beta_{2} / \sigma_{2}; w_{ij}^{(1)}w_{ij}^{(2)}\rho\right) \end{align}

for $w_{ij} = 2y_{ij} - 1$ as standard. 

Then the corresponding all likelihood can be given by 


\begin{align} L_{\text{all}}(\rho) = \prod_{(i, j) \in \mathcal{S}}  \Phi_{2}\left( w_{ij}^{(1)}x_{ij}^{\intercal}\beta_{1}  / \sigma_{1}, w_{ij}^{(2)}x_{ij}^{\intercal}\beta_{2} / \sigma_{2}; w_{ij}^{(1)}w_{ij}^{(2)}\rho\right). \end{align}


We have similar structures for the slice likelihoods. Write

\begin{align} \text{Pr}(Y_{ij} = y_{ij} \mid a_{i}) &= \text{Pr}\left(\frac{w_{ij}^{(1)}\left( x_{ij}^{\intercal}\beta_{1}  + a_{i}^{(1)}  +Z^{(1)}\right)}{\sqrt{ \sigma^{2}_{B_{1}} + 1 }} > 0, \frac{w_{ij}^{(2)}\left( x_{ij}^{\intercal}\beta_{2} + a_{i}^{(2)} + Z^{(2)} \right)}{\sqrt{ \sigma^{2}_{B_{2}} + 1 }} > 0\right)  \\
&= \Phi_{2}\left( w_{ij}^{(1)} \frac{ x_{ij}^{\intercal}\beta_{1}  + a_{i}^{(1)}}{\sqrt{ \sigma^{2}_{B_{1}} + 1 }} , w_{ij}^{(2)} \frac{x_{ij}^{\intercal}\beta_{2} + a_{i}^{(2)}}{\sqrt{ \sigma^{2}_{B_{2}} + 1 }}; w_{ij}^{(1)}w_{ij}^{(2)}(\rho - \rho_{A})\right).\end{align}

Let $r_{A} := \rho- \rho_{A}$. Then for $\gamma_{B} = \left( \beta_{1} ^{\intercal}/ \sqrt{ \sigma^{2}_{B_{1}} + 1 }, \beta_{2}^{\intercal} / \sqrt{ \sigma^{2}_{B_{2}} + 1 } \right)^{\intercal}$, along with

\begin{align} \tilde{\Sigma}_{A} = \begin{pmatrix}
\frac{\sigma^{2}_{A_{1}}}{\sigma^{2}_{B_{1}} + 1} & \tilde{\rho} \\
 \tilde{\rho}& \frac{\sigma^{2}_{A_{2}}}{\sigma^{2}_{B_{2}} + 1}
\end{pmatrix}, \, \, \, \tilde{\rho} = \frac{\rho_{A}\sigma_{A_{1}}\sigma_{A_{2}}}{\sqrt{ (\sigma^{2}_{B_{1}} + 1)(\sigma^{2}_{B_{2}} + 1) }},  \end{align}

we can write

\begin{align} L_{\text{row}}(r_{A}) = \prod_{i = 1}^{I} \int _{\mathbb{R}^{2}} L_{i\bullet } (\hat{r}_{A} \mid u_{i}) \, p(u_{i}) du_{i}  \end{align}

for $u_{i} \sim \mathcal{N}(0, \tilde{\Sigma}_{A})$ and

\begin{align} L_{i\bullet }(r_{A} \mid u_{i}) = \prod_{j \mid i} \Phi_{2}\left( w_{ij}\otimes  \left( \gamma_{B}^{\intercal} x_{ij} + u_{i}\right); w_{ij}^{(1)}w_{ij}^{(2)} r_{A}\right) . \end{align}

The column likelihood is of course analogous. 

\subsection{Implementation Notes}


\begin{align} L_{\text{all}}(\rho) = \prod_{(i, j) \in \mathcal{S}}  \Phi_{2}\left( w_{ij}^{(1)}x_{ij}^{\intercal}\beta_{1}  / \sigma_{1}, w_{ij}^{(2)}x_{ij}^{\intercal}\beta_{2} / \sigma_{2}; w_{ij}^{(1)}w_{ij}^{(2)}\rho\right). \end{align}

Then mode finding is ugly, but we should do it anyway. See The Standard Bashes. 




