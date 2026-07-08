---
type: setup
aliases: [many-to-many matching problem]
tags: [crossed, research, stanford-stats/y2]
modified: 2026-04-03T21:24:54-07:00
created: 2026-04-03T19:02:43-07:00
---

> [!attention] Many-to-Many Matching Problem
> Following [[@foxToolkitMatchingMaximum]], we analyze a 'market' consisting of two distinct groups or entities, the 'upstream' and 'downstream'. We can for example label the upstream group a set of products and the downstream group a set of buyers. We can (as standard) let $i \in I$ index the upstream indices and $j \in J$. Under this analogy, the **many-to-many** case of the **Matching Problem** involves observation of each potential pairing, so that we see $\left\{ (X_{ij}, Y_{ij}) \right\}_{i \in I, j \in J}$ where we make the distributional assumption $Y_{ij} = \mathbf{1}\left[\text{product } i \text{ is bought by buyer } j  \right] = \mathbf{1}\left[X_{ij}^{\intercal}\beta + u_{ij} > 0  \right]$ for some unobservable latent $u_{i}$ satisfying the [[Median Independence|median independence]] condition. It is thus many-to-many in the sense that multiple buyers can buy the same product, and an individual buyer can buy multiple products. 


