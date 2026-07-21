---
modified: 2025-10-29T09:33:44-07:00
created: 2025-10-29T00:51:04-07:00
---
Random slopes, in our construction, are of particular difficulty given that we lose even the $\gamma$ estimate. To be direct, we consider
$$\begin{aligned} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, ij}^{\intercal}a_{i} + x_{B, ij}^{\intercal}b_{j} + \varepsilon _{ij} \end{aligned}$$
with $Y_{ij} = \mathbf{1}\left[W_{ij} > 0 \right]$ as standard. The issue is that since the variance term will contain $x_{A, ij}$ and $x_{B, ij}$ dependence, so that we do not have a shared marginal variance to utilize. 

Perhaps an aggressive simplification is to force both $x_{A, ij}$ and $x_{B, ij}$ to only depend on $i$ or $j$. There are a few cases for this; it does not seem to be unreasonable in some case to have $(x_{A, j}, x_{B, j})$ (fixed terms only depend on the item: $a_{i}$ price sensitivity, $x_{A, j}$ item price, $b_{j}$ rate of item quality decay/depreciation, $x_{B_{j}}$ days since arrival), $(x_{A, i}, x_{B, j})$ ($x_{A, i}$ tax bracket $a_{i}$ price sensitivity), or $(x_{A, j}, x_{B, i})$ as subcases capturing $(i, j)$ shared or contrasting at different levels. We start with the first case; we can share a normalization within $i \mid j$,

$$\begin{aligned} \mathbb{P}(W_{ij} > 0) &= \mathbb{P}\left( x_{ij}^{\intercal}\beta + x_{A, j}^{\intercal}a_{i}  + x_{B, j}^{\intercal} b_{j} + \varepsilon_{ij} \right) \\ &= \Phi\left( \frac{x_{ij}^{\intercal}\beta }{\sqrt{ x_{A, j}^{\intercal} \Sigma_{A} x_{A, j} + x_{B, j}^{\intercal} \Sigma_{B} x_{B, j} + 1}} \right),\end{aligned}$$
and we can combine (eg. max of the sum of the log likelihoods) a per-$j$ fit. 

In the above, as long as the indexing of $x_{A}$ and $x_{B}$ are shared, there is a slice direction in which we can fit it. That is, we can recover the "interaction" of $x_{A, j}^{\intercal}a_{i}$; but we cannot recover $x_{A, j}^{\intercal}a_{i}$ and $x_{B, i}^{\intercal}b_{j}$ at the same time. I feel like I can do some theory for this, but I don't have anything written up yet. 

## Shared Single
Per-$j$ implicitly requires sharing $b_{j}$, so we would have
$$\begin{aligned} \mathbb{P}(Y_{i j} = y_{ij} \mid b) &= \mathbb{P}\left( x_{ij}^{\intercal}\beta + x_{A , j}a_{i} + x_{B, j}b_{j} + \varepsilon_{ij}  > 0 \mid b\right) \\ &= \Phi\left( \frac{x_{ij}^{\intercal}\beta  + x_{B, j}b_{j}}{\sqrt{ x_{A, j}^{2}\sigma^{2}_{A} + 1 }} \right).\end{aligned}$$
There is perhaps an interesting question here again about how we consider an optimization of $\beta$ scaled. Note (unintentionally suggestively, as presented above) that the natural fit of this is to feed the $(x_{ij}, x_{B, j})$ extended vector into a probit regression, and then $b_{j}$ is estimated as a model parameter. But then our optimal direction needs to take into account the normality of $b_{j}$, and the direction of $\beta$ also needs to be primarily driven by care of the $x_{ij}$ coefficients (and the intercept). 

Here is where we branch - it seems to me as though there are many ways we solve for the effective $\gamma$ here. What may also be interesting is that if I solve for $\gamma$, then this immediately induces an estimate of $b_{j} / \sqrt{ x_{A, j}^{2} \sigma^{2}_{A} + 1 }$, since we'd have $J$ (filtered by number of observations greater than two); $b_{j}$'s are normal with different variances, but because I don't know $\sigma^{2}_{A}$ yet, the corresponding scale is unclear. What kind of interpretations can I get out of this?

If I have an estimate of $b_{j} / \sqrt{ x_{A, j}^{2} \sigma^{2}_{A} + 1 }$, then I have access to its norm in $\mathbb{R}^{\tilde{J}}$, 
$$\begin{aligned}  \left\lvert\left\lvert b \right\rvert\right\rvert ^{2} = \sum_{j = 1}^{\tilde{J}} \frac{b_{j}^{2}}{x_{A, j}^{2} \sigma^{2}_{A} + 1} = \sum_{j =1 }^{\tilde{J}} \frac{\sigma_{B}^{2}}{x_{A, j}^{2} \sigma^{2}_{A} + 1} Z_j^{2},\end{aligned}$$
some weighted sum of normals. 

It seems like everything needs to stay per-$j$ in this case, which is unfortunate. Some sort of nonlinear optimization jointly of $(\sigma^{2}_{A}, \sigma^{2}_{B})$, and I can't figure out how to use the $A$ slice. 

## Some Additional Observations
I was trying to iterate over simpler and simpler models. The minimal informative one with full expression of random effects is to model 
$$\begin{aligned} W_{ij} = \beta_{0} + x_{A, ij} a_{i} + x_{B, ij}b_{j} + \varepsilon_{ij}, \end{aligned}$$
so that marginally,
$$\begin{aligned} \mathbb{P}(Y_{ij} = 1) &= \Phi\left( \frac{\beta_{0}}{\sqrt{ x_{A_{i, j}}^{2} \sigma^{2}_{A} + x_{B_{i, j}}^{2} \sigma^{2}_{B}  + 1} } \right).\end{aligned}$$
This makes me feel that the nonlinearity issues emerge immediately, in a way that will cause problems every time for the $\gamma$ estimation, since we have even for a single $\beta$ this structure. However, a strategy does seem to be explicitly learning $b_{j}$, etc. in these regimes. Let's work this out and see what we need. 
$$\begin{aligned} W_{ij} \mid a_{i} \sim \mathcal{N}(\beta_{0} + x_{A, ij} a_{i} , \sigma^{2}_{B, ij} x_{B, ij}^{2} + 1), \end{aligned}$$
so if $x_{B, ij}$ is only dependent on $i$, then 
$$\begin{aligned} \mathbb{P}(Y_{ij} =1 \mid a_{i}) = \Phi\left( \frac{\beta_{0} + x_{A, ij} a_{i}}{\sqrt{ \sigma^{2}_{B} x_{B, i} ^{2} + 1} } \right) \end{aligned}$$
and now we have a per-$i$ fit. So I actually only need to have one $(i,j)$ dependence structure and one $i$- or $j$- dependence structure, and that nets me direction information, even in the general $\beta$ case. Nothing immediately pops out to me about solving for the scale. 
