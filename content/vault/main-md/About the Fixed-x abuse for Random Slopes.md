---
modified: 2026-07-07T19:35:34-07:00
created: 2026-01-05T11:27:15-08:00
tags: [random-slopes]
---

Our current approach to [[Random Slopes]] is fundamentally guided by an initial treatment of known-$x$ as random; looking at 

$$\begin{align*} y_{ij} = \mathbf{1}\left[x_{ij}^{\intercal}\beta + x_{A, ij}^{\intercal}a_{i} + x_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} > 0 \right], \end{align*}$$
we treat $x_{A, ij}^{\intercal}a_{i}$ and $x_{B, ij}^{\intercal}b_{j}$ as random (normal) quantities in and of themselves (mostly thinking about simplifying case $x_{ij} \perp x_{A, ij}, x_{B, ij}$), temporarily discarding knowledge of $x_{A, ij}$ and $x_{B, ij}$. Then, crudely, 


A few thoughts here. Firstly, as a direction for later, maybe we can somehow use a bootstrapped version of $x_{A, ij}$, $x_{B, ij}$ to get something - would be nice to incorporate this information earlier. Secondly, $\text{tr}(\Sigma_{B}G_{B})$, for example, might somehow serve as regularization information for current drifting by perfect separation. 


# Regularization using 