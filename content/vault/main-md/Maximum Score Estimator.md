---
type: definition
aliases: [maximum score estimator]
tags: [for-crossed, research, stanford-stats/y2]
modified: 2026-04-03T17:24:58-07:00
created: 2026-04-01T22:47:02-07:00
---

> [!important] Maximum Score Estimator
> For recovering the direction $\gamma = \beta / \left\lvert\left\lvert \beta_{2} \right\rvert\right\rvert$ of the [[Inference for Binary Choice Models|binary choice model]], [[@manskiMaximumScoreEstimation1975]] suggests the **maximum score estimator** as the estimator that prioritizes sign alignment over the unit sphere:
> $$\begin{align*} \hat{\beta}= \text{argmax}_{\gamma \in \mathcal{S}^{p}} \left\{ n^{-1} \sum_{ i =1}^{n} \tilde{Y}_{i} \mathbf{1}\left[\gamma ^{\intercal}X_{i} \geq 0 \right] \right\}  \end{align*}$$
> where $\tilde{Y}_{i}:= 2Y_{i} - 1$ is the equivalent sign representation of $Y_{i}$ the observed response. 

Intuitively, we are penalizing events where threshold crossing from the observed component disagrees with the final sign of $\tilde{Y}_{i}$. 

As in [[@manskiSemiparametricAnalysisDiscrete1985]], we label the objective as the **sample score function**
$$\begin{align*} S_{n}(\beta) = \frac{1}{n} \sum_{i =1}^{n} \tilde{Y}_{i} \text{sign}\left( x_{i}^{\intercal}\beta \right), \end{align*}$$
with the corresponding **population score function**
$$\begin{align*} S(\beta) = \mathbb{E}\left[ \tilde{Y}\text{sign}\left( X^{\intercal}\beta \right) \right] .\end{align*}$$
