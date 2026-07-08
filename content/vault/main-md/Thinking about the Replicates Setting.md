---
modified: 2025-10-29T01:46:13-07:00
created: 2025-10-27T19:03:39-07:00
---
# Replicates in the iid case 
I find parallels between replicates and the flattening relationships that we observe in the [[ARC Generalization - K Random Effects|k random effects]] model. We start with the standard two random effects model under replicates. We can probe the leave-one-out conditional distribution of the replicate. But I think in the ARC format this tends to be problematic pretty quickly; in particular, we can just sketch out the first few steps
$$\begin{align} \mathbb{P}(Y_{ij}^{(t)} = y_{ij}^{(t)} \mid Y_{ij}^{(-t)}) &= \mathbb{P}\left( X_{ij}^{\intercal}\beta + a_{i} + b_{j} + \varepsilon_{ij} > 0 \mid Y_{ij}^{(-t)} \right) \\
&= \mathbb{P}\left( \eta_{ij} + \frac{a_{i} + b_{j} + \varepsilon_{ij}}{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} } }   > 0 \mid Y_{ij}^{(-t)}\right),\end{align}$$
where it is clear that we would have to integrate over the latent region described by the sign information in $Y_{ij}^{(-t)}$. If we had $T$ replicates, then we would have a $T$-dimensional integral. Explicitly, we are trying to control the deviation in $(b_{j} + \varepsilon_{ij})/\sqrt{ 1 +\sigma^{2}_{A} + \sigma^{2}_{B} }$, when we assume knowledge of $a_{i}$ and we know $b_{j}$ is shared. 

But this kind of parceling is exactly what we do in the [[ARC Generalization - K Random Effects|singular factorization]]. There, our product is over 
$$\begin{align} \prod_{(j, k) \mid i}  \Phi\left( w_{ijk}(x_{ijk}^{\intercal}\gamma + u_{i}) \right),\end{align}$$
which inherently discards the events of marginal shared $j$ or shared $k$, since we only look at uniqueness of $(i, j, k)$ pairs. In the same way as above, we would additively gain integral order with the number of "replicates", or number of responses that share $j$ or share $k$. Here we also have an issue of hierarchical ambiguity, in that we can group over $j$ or over $k$ (or both) and get conflicting answers, even without replicates. It feels like we're trying to "correct the misspecification" of the simplified model, which I'm skeptical of given the driving computational desire. 

But perhaps there is something nested that I can be doing here? 

