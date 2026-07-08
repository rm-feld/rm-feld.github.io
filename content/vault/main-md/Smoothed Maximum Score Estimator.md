---
type: definition
aliases: [smoothed maximum score estimator]
tags: [crossed, research, stanford-stats/y2]
modified: 2026-04-04T22:00:14-07:00
created: 2026-04-04T19:07:43-07:00
---

> [!important] Smoothed Maximum Score Estimator
> Per [[@horowitzSmoothedMaximumScore1992]], let $K:\mathbb{R} \to \mathbb{R}$ be continuous and satisfy the following conditions:
> - **K1 (Uniform Boundedness).** There exists finite $M \geq 0$ such that $\geq 0$ such that $|K(v)| < M$  for all $v \in \mathbb{R}$. 
> - **K2 ([[cdf]] Behavior).** $\lim_{ v \to -\infty } K(v) = 0$, and $\lim_{ v \to \infty } K(v) = 1$. 
> %% %%
> Now, let $\sigma_{N}$ be a sequence of positive reals that converges to zero in $N$. The **smoothed maximum score estimator** is given by 
> $$\begin{align*} S_{N}(\beta; \sigma_{N}) = N^{-1} \sum_{n = 1}^{N} \tilde{Y}_{n}\cdot K\left( x_{n}^{\intercal}\beta / \sigma_{N} \right).  \end{align*}$$

Morally, we are performing the standard trick of approximating a step function with some smoothed version. 