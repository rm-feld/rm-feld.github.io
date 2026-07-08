---
type: setup
aliases: [crossed random effects model]
tags: [crossed, research, stanford-stats/y2]
modified: 2026-04-07T21:03:39-07:00
created: 2026-04-07T20:19:42-07:00
---

> [!attention] Crossed Random Effects Model
> Let $i$ and $j$ index levels of two categorical variables. For [[Link Function|link function]] $g$, consider data of the form $\left\{ (x_{ij}, Y_{ij}) \right\}$ for which 
> $$\begin{align*} \mathbb{E}(Y_{ij} \mid x_{ij}, a_{i}, b_{j}) = g^{-1}\left( x_{ij}^{\intercal}\beta + a_{i} + b_{j} \right),\end{align*}$$
> for $a_{i} \overset{\mathrm{iid}}{\sim} \mathcal{N}(0, \sigma^{2}_{A})$, and $b_{j} \overset{\mathrm{iid}}{\sim}\mathcal{N}(0, \sigma^{2}_{B})$.
> 
> We do not generally expect to see all possible crosses; we thus have $Z_{ij} \in \left\{ 0, 1 \right\}$ the observation indicator, where we only observe $(x_{ij}, Y_{ij})$ if $Z_{ij} = 1$. Thus it is convenient to define
> $$\begin{align*} \mathcal{S} = \left\{ (i, j) \mid Z_{ij} = 1 \right\}  \end{align*}$$
> over indices $i \in I$, $j \in J$. 

