---
modified: 2026-07-07T23:52:30-07:00
created: 2025-10-27T21:19:27-07:00
---
# Themes
- "treat as part of model"
- all is the ugliest
- i really want a slice/
- motivating question emerges in "if I only want to know direction…"

# Cases 
We have 6 cases of broad interest, defined by the dependence structures of $x_{A}$ and $x_{B}$. Written out, we have the following models: note we omit the natural symmetric cases of 4 and 5. 

## 1. General

$$\begin{align} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, i, j}^{\intercal}a_{i} + x_{B, i, j}^{\intercal}b_{j} + \varepsilon_{ij}  \end{align}$$
### All
$$\begin{align} \mathbb{P}(Y_{ij} = 1) = \Phi\left( \frac{x_{ij}^{\intercal}\beta}{\sqrt{ x_{A, i, j}^{\intercal}\Sigma_{A}x_{A, i,j} + x_{B, i, j}^{\intercal}\Sigma_{B}x_{B, ij} + 1 }} \right)  \end{align}$$
### Row
$$\begin{align} \mathbb{P}(Y_{ij} =1 \mid a) = \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{A, i, j}^{\intercal}a_{i}}{\sqrt{ x_{B, i, j}^{\intercal}\Sigma_{B}x_{B, i, j} + 1 }} \right) \end{align}$$
### Column
$$\begin{align} \mathbb{P}(Y_{ij} =1 \mid b) = \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{B, i, j}^{\intercal}b_{j}}{\sqrt{ x_{A, i, j}^{\intercal} \Sigma_{A}x_{A, i, j} + 1 }} \right) \end{align}$$

## 2. Matching
$$\begin{align} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, i}^{\intercal}a_{i} + x_{B, j}^{\intercal}b_{j} + \varepsilon_{ij}. \end{align}$$
### All
$$\begin{align} \mathbb{P}(Y_{ij} =1 ) = \Phi\left( \frac{x_{ij}^{\intercal}\beta}{\sqrt{ x_{A, i}^{\intercal}\Sigma_{A}x_{A, i} + x_{B, j}^{\intercal}\Sigma_{B}x_{B, j}  + 1}} \right) \end{align}$$

### Row
$$\begin{align} \mathbb{P}(Y_{ij} = 1\mid a) = \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{A, i}^{\intercal}a_{i}}{\sqrt{ x_{B, j}^{\intercal}\Sigma_{B}x_{B, j} + 1 }} \right) \end{align}$$
### Column
$$\begin{align} \mathbb{P}(Y_{ij} =1 \mid b) = \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{B, j}^{\intercal}b_{j}}{\sqrt{ x_{A, i}^{\intercal}\Sigma_{A}x_{A, i} + 1 }} \right) \end{align}$$
### Pairwise
$$\begin{align} \mathbb{P}(Y_{ij} = 1, Y_{ij'} = 1) &= \mathbb{P}\left( x_{ij}^{\intercal}\beta + x_{A, i}^{\intercal}a_{i} + x_{B, j}^{\intercal}b_{j} + \varepsilon_{ij} > 0, x_{ij}^{\intercal}\beta + x_{A, i}^{\intercal}a_{i} + x_{B, j'}^{\intercal}b_{j'} + \varepsilon_{ij'} > 0 \right) \\
&= \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{A, i}^{\intercal}a_{i}}{\sqrt{ x_{B, j}^{\intercal}\Sigma_{B}x_{B, j} + 1 }}, \frac{x_{ij}^{\intercal}\beta + x_{A, i}^{\intercal}a_{i}}{\sqrt{ x_{B, j'}^{\intercal}\Sigma_{B} x_{B, j'} + 1 }}\right). \end{align}$$


## 3. Shared-Fixed
$$\begin{align} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, j}^{\intercal}a_{i} + x_{B, j}^{\intercal}b_{j} + \varepsilon_{ij}, \end{align}$$

### All
$$\begin{align} \mathbb{P}(Y_{ij} = 1) = \Phi\left( \frac{x_{ij}^{\intercal}\beta}{\sqrt{ x_{A, j}^{\intercal} \Sigma_{A} x_{A, j} + x_{B, j}^{\intercal}\Sigma_{B}x_{B, j} + 1 }} \right) \end{align}$$
### Row
$$\begin{align} \mathbb{P}\left(Y_{ij} = 1 \mid a \right)  = \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{A, j}^{\intercal}a_{i}}{\sqrt{ x_{B, j}^{\intercal}\Sigma_{B}x_{B, j} + 1 }} \right)\end{align}$$
### Column

$$\begin{align} \mathbb{P}\left( Y_{ij} = 1 \mid b \right)  &= \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{B, j}^{\intercal} b_{j} }{\sqrt{ x_{A, j}^{\intercal}\Sigma_{A}x_{A, j} + 1 }} \right)\end{align}$$

Over each column, both the effect $b_{j}$ and the scale are shared. Thus in each column, I can fit a probit model over the design matrix $\left( x_{i, j}^{\intercal}, x_{B, j}^{\intercal} \right)$ which will be a consistent estimator #TODO (under what conditions on $x$?) of  
$$\begin{align} \gamma_{j} =  \frac{\left( \beta ^{\intercal}, b_{j}^{\intercal} \right)}{\sqrt{ x_{A, j}^{\intercal} \Sigma_{A}x_{A, j} + 1} }. \end{align}$$
How do we combine these per-column estimates? Let's start with some rudimentary observations and directions. 

A first naturalistic estimator is this; I stack only the first $p$ coefficients of each $\hat{\gamma}_{j}$ fit, and take the max eigenvalue of the corresponding matrix. We can take the unit of each one. However, we have three sources of variance in the estimates that might cause us to downweight contributions. First is number of observations $N_{\bullet j}$, for which we can reasonably expect in the sparsity model that many of these have $N_{\bullet j} < p$. This makes me think of regularization. Secondly, larger $x_{A}$ induces larger uncertainty, though without knowledge of $\Sigma_{A}$, the correct scaling of components is unknown. Finally, especially in this lower rank setting, we can have unwieldy $\hat{b}_{j}$ estimation. We again branch into different treatments of this. We know $b_{j}$ is mean zero; I feel like regularization on only $b_{j}$ can be reasonable. Downweighting directions by all of these factors seems appropriate, but I'm not sure what the appropriate form of this is. I investigate a regularization interpretation later. 

Even if we do regularization, though, I'm skeptical of consistency or good behavior of the above. In the regime we can imagine here, penalizing $b_{j}$ fits, indeed forcing $b_{j} =0$ (which would be innapropriate in this regime, since we're not pooling $b_{j}$ as discussed in [[Naively Fitting with Probit]]), $N_{\bullet j} < p$ means that we'll have perfectly separating hyperplanes for basically all columns, and so either we blow up, or need to randomize reported solutions in some principled way, or return the space of solutions for each column, which seems expensive. I think there may still be something interesting here, but I'm skeptical of good behavior of ARC without the existence of some all likelihood/procedure/utilization that can provide $N \gg p$. Still, there may be something above; just not sure what theory I can utilize/what is possible, and under what conditions, etc. 

Also notice as in the column estimate of (4) that it is denominator variation that is of greatest worry; we have no issues with $x_{B}$ having dependence on $i$ as well, but we would have issues if $x_{A}$ did, Because we lose common scale. 

## 4. Contrast-General
$$\begin{align} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, j}^{\intercal}a_{i} + x_{B, i, j} ^{\intercal} b_{j} + \varepsilon_{ij}\end{align}$$
### All
$$\begin{align} \mathbb{P}(Y_{ij} =1 ) = \Phi\left( \frac{x_{ij}^{\intercal}\beta}{\sqrt{ x_{A, j}^{\intercal}\Sigma_{A} x_{A, j} + x_{B, ij}^{\intercal}\Sigma_{B}x_{B, ij} + 1 }} \right) \end{align}$$
### Row
$$\begin{align} \mathbb{P}(Y_{ij} = 1\mid a) = \Phi\left( \frac{x_{ij}^{\intercal}\beta +x_{A, j}^{\intercal}a_{i}}{\sqrt{ x_{B, ij}^{\intercal}\Sigma_{B} x_{B, ij} + 1 }} \right) \end{align}$$
### Column

$$\begin{align} \mathbb{P}\left( Y_{ij} = 1 \mid b \right) &= \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{B, i, j}^{\intercal}b_{j}}{\sqrt{ x_{A, j}^{\intercal}\Sigma_{A}x_{A,j} + 1 }} \right)\end{align}$$
As mentioned in (3), we have shared $b_{j}$ and scale per column, so we have column fits. 
## 5. Match-General

$$\begin{align} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, i}^{\intercal}a_{i} + x_{B, i, j}^{\intercal}b_{j} + \varepsilon_{ij} \end{align}$$
### All
$$\begin{align} \mathbb{P}(Y_{ij} =1 ) = \Phi\left( \frac{x_{ij}^{\intercal}\beta}{\sqrt{ x_{A, i}^{\intercal}\Sigma_{A}x_{A, i} + x_{B, ij}^{\intercal}\Sigma_{B}x_{B, ij} + 1 }} \right) \end{align}$$
### Row
$$\begin{align}\mathbb{P}(Y_{ij} = 1 \mid b) = \Phi\left( \frac{x_{ij}^{\intercal}\beta  + x_{B , i ,j}^{\intercal}b_{j}}{\sqrt{ x_{A, i}^{\intercal}\Sigma_{A}x_{A, i} + 1}} \right) \end{align}$$
### Column
$$\begin{align} \mathbb{P}(Y_{ij} =1\mid a) = \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{A, i}^{\intercal}a_{i}}{\sqrt{ x_{B, ij}^{\intercal}\Sigma_{B}x_{B, ij} + 1 }} \right) \end{align}$$

## 6. Contrasting
This is perhaps the one of strongest interest. 
$$\begin{align} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, j}^{\intercal}a_{i} + x_{B, i}^{\intercal}b_{j} + \varepsilon_{ij} \end{align}$$

$$\begin{align} \mathbb{P}(Y_{ij} = 1) = \Phi\left( \frac{x_{ij}^{\intercal}\beta}{\sqrt{  x_{A, j}^{\intercal}\Sigma_{A}x_{A, j} + x_{B, i}^{\intercal}\Sigma_{B}x_{B, i} + 1 }} \right) \end{align}$$

$$\begin{align} \mathbb{P}(Y_{ij} =1 \mid a) = \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{A, j}^{\intercal}a_{i}}{\sqrt{ x_{B, i}^{\intercal}\Sigma_{B}x_{B, i} + 1 }} \right) \end{align}$$

$$\begin{align} \mathbb{P}(Y_{ij} =1 \mid b) = \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{B, i}^{\intercal}b_{j}}{\sqrt{ x_{A, j}^{\intercal}\Sigma_{A}x_{A, j} + 1 }} \right) \end{align}$$



# Case of Interest
Of strong interest is the case where random effects define an interaction in both direction; we consider the underlying latent 
$$\begin{align} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, j}^{\intercal}a_{i} + x_{B, i}^{\intercal}b_{j} + \varepsilon_{ij} \end{align}$$
for which the indexing indicates that $x_{A, j}$ depends only on the column, and $x_{B, i}$ depends only on the rows. 

%% "Treat as coefficient vs. scale fuckery" %%

In the fixed-$x$ case, is there an orthogonality condition that I can apply to ignore $x_{B, i}^{\intercal}b_{j}$ when I solve?

$$\begin{align} \mathbb{P}(Y_{ij} = 1\mid b) &= \mathbb{P}\left( x_{ij}^{\intercal}\beta + x_{B, i}^{\intercal}b_{j} + x_{A, j}^{\intercal}a_{i} + \varepsilon_{ij} > 0 \right) \\
&= \mathbb{P}\left( \frac{x_{ij}^{\intercal}\beta + x_{B, i}^{\intercal}b_{j}}{\sqrt{ x_{A, j}^{\intercal}\Sigma_{A} x_{A, j} + 1}} + \tilde{Z} > 0\right) \\
&= \Phi\left( \frac{x_{ij}^{\intercal}\beta + x_{B, i}^{\intercal}b_{j}}{\sqrt{ x_{A, j}^{\intercal}\Sigma_{A} x_{A, j} + 1 }} \right); \end{align}$$
do i have a slice? yes, if i'm willing to treat $b_{j}$ as a coefficient, which i'm not super sure about. is there a nicer way to downweight a probit result by $b_{j}$ discrepancy? 
- i feel like there's actually a picture for that; but it keeps coming back to a piecewise regime. 

let's say i have a fit per $i$. then we have shared $a_{i}$, $x_{B, i}$; *in what regime can i say that it's reasonable to treat $a_{i}$ as a "fixed unknown" coefficient?* Under independence of $a_{i}$ and the covariate values, 

- interested in behavior of the naïve fit. 






