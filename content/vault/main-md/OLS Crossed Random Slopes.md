---
modified: 2025-12-03T09:41:50-08:00
created: 2025-12-03T09:41:16-08:00
---
# OLS Crossed Random Slopes 
%% THIS IS NOT A SPARSE MODEL %%
$$\begin{align} Y_{ij} = X_{ij}^{\intercal}\beta + X_{A, j}^{\intercal}a_{i} + X_{B, i}^{\intercal} b_{j} + \varepsilon_{ij}, \end{align}$$
for $\varepsilon_{ij} \sim \mathcal{N}(0, \sigma^{2}_{\varepsilon})$, $a_{i} \sim \mathcal{N}(0, \Sigma_{A})$, $b_{j} \sim \mathcal{N}(0, \Sigma_{B})$. Doing OLS, I have some closed form access now. %% Bayesian interpretation of regularization-as-prior; apply to only a subset of components? %%

What happens if I do a naïve fit? This needs to be done over slices, ie. $i$ or $j$, otherwise I have an unbalanced variance contribution. Let's say we're doing this over $i$. Then I'm interested in the outcome of solving for an augmented setup
$$\begin{align} \beta_{i} := \left( \beta ^{\intercal} \, \,  a_{i}^{\intercal}\right)^{\intercal} \in \mathbb{R}^{p + p_{A}},  \end{align}$$
where in essence I treat $b_{j}$ as an extended set of fixed coefficients. Let's keep it one-dimensional for now %% also keep coming back to some pairwise behavior %% for $a_{i}$, $b_{j}$, $x_{A, j}$, and $x_{B, i}$. 

Under fixed $i$, $a_{i}$ is shared. Further, $b_{j}$ is random but with fixed variance, defined by $x_{B, i}^{2}\sigma^{2}_{B}$. So under some balance conditions, I'd be solving for 
$$\begin{align} \hat{\beta}_{i} = \left( \tilde{X}^{\intercal}_{i} \tilde{X}_{i} \right)^{-1} \tilde{X}^{\intercal}_{i} Y_{i} \end{align}$$
for $\tilde{X}_{i}$ the augmented $[X_{ij} \, \, \, X_{A, j}]$ design matrix. 


What does this look like? my instinct is something ridge regression-esque with a component-wise requirement. But let's do the block inversion first. We'll simplify notation to drop indices, so write
$$\begin{align} \left( \tilde{X}_{i}^{\intercal}\tilde{X}_{i} \right)^{-1} &=: \begin{pmatrix}
X'X & X'X_{A} \\
X_{A}'X &X_{A}'X_{A}

\end{pmatrix}^{-1}, \end{align}$$
for which we let $X = UDV^{\intercal}$ and $X_{A} = U_{A}D_{A}V_{A}^{\intercal}$ for the full SVD, eg. $D_{A} \in\mathbb{R}^{n \times p_{A}}$ with many zero terms. Note the common terms $(X_{A}'X_{A})^{-1} = V_{A}D_{A}^{-2}V_{A}'$ and $(X'X)^{-1} = VD^{-2}V'$, where we abuse notation for $D^{-2} \in \mathbb{R}^{p\times p}$ since we're really doing $D^{\intercal}D$ multiplication. 

Block inversion nets us

$$\begin{align} \begin{pmatrix}
X'X & X'X_{A} \\
X_{A}'X &X_{A}'X_{A}

\end{pmatrix}^{-1} &= \begin{pmatrix}
(X'X - X'X_{A}(X_{A}'X_{A})^{-1}X_{A}'X)^{-1} & 0 \\
0 & (X_{A}'X_{A} - X_{A}'X(X'X)^{-1}X'X_{A})^{-1}
\end{pmatrix} \begin{pmatrix}
I & -X'X_{A}(X_{A}'X_{A})^{-1} \\
-X_{A}'X(X'X)^{-1} & I
\end{pmatrix}  \end{align}$$


for which we recover with the SVD
$$\begin{align} \hat{\beta_{i}} = [X_{i}'(I - P_{X_{A}})^{-1} X_{i}]^{-1} X_{i}'(I - P_{X_{A}})(X'\beta + X_{A, j}'a_{i} + X_{B, i}'b + \varepsilon_{i}). \end{align}$$

