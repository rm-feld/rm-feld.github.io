---
type: setup
aliases: [k-crossed random effects model]
tags: [stanford-stats/y2]
modified: 2026-05-05T15:12:22-07:00
created: 2026-03-21T15:55:53-07:00
---

> [!attention] K-Crossed Random Effects Model
> Let $\mathcal{A} \subseteq 2^{[K]}\setminus \left\{ \emptyset \right\}$. The $K$-**crossed random effects model** is given by 
> $$\begin{align*} \mathbb{E}(Y_{\ell} \mid x_{\ell}, a_{\ell}) = g^{-1}\left( x_{\ell}^{\intercal}\beta + a_{\ell}^{\intercal}\mathbf{1} \right), \end{align*}$$
> where $a_{\ell} := a_{\boldsymbol{i}(\ell)}$ are a flattened vector encoding with components $a_{\boldsymbol{i}, \mathcal{K}}$, $\mathcal{K} \subseteq \mathbb{A}$. Components are i.i.d. within each slice, $a_{\boldsymbol{i}, \mathcal{K}} \sim \mathcal{N}(0, \sigma^{2}_{\mathcal{K}})$ over $\boldsymbol{i}[\mathcal{K}] \in \mathcal{S}[\mathcal{K}]$. As standard, random effects are shared when components are shared, so that $a_{\boldsymbol{i}, \mathcal{K}} = a_{\boldsymbol{i}', \mathcal{K}}$ when $\boldsymbol{i}[\mathcal{K}] = \boldsymbol{i}'[\mathcal{K}]$. Here and throughout, we use $a_{\ell}^{\intercal}\mathbf{1}$ as a shorthand for 
> $$\begin{align*} a_{\ell}^{\intercal}\mathbf{1} := \sum_{\mathcal{K} \in \mathcal{A}} a_{\boldsymbol{i}, \mathcal{K}} .\end{align*}$$

There is an expectation that $\mathcal{A}_{1} :=\left\{ \left\{ k \right\} \right\}_{k =1}^{K} \subseteq \mathcal{A}$. I am giving the subscript by cardinality, as might be preferred; that is, $\mathcal{A}_{m}= \left\{ \mathcal{K} \subseteq 2^{[K]} : |\mathcal{K}| = m\right\}$. We can then define interactions up to a desired depth, $\mathcal{A}_{\leq m} = \left\{ \mathcal{K} \subseteq 2^{[K]}: |\mathcal{K}| \leq m \right\}$. 