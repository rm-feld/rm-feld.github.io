---
type: setup
aliases: [standard assumptions for maximum score estimation]
tags: [crossed, manski-type, research, stanford-stats/y2]
modified: 2026-04-03T17:39:23-07:00
created: 2026-04-02T16:28:29-07:00
---

> [!attention] Standard Assumptions for Maximum Score Estimation
> Towards [[Identifiability..def|identifiability]] and [[Asymptotic Consistency|consistency]] of the [[Maximum Score Estimator|maximum score estimator]], we assume the following, as given by [[@manskiSemiparametricAnalysisDiscrete1985]]:
> 1. **Linear Median Regression.** There exists $\beta \in \mathbb{R}^{p}$ unique, such that $\text{med}(y \mid x) = x^{\intercal}\beta$. 
> ^max-score-a1
> 2. **Nondegenerate Support Condition.** 
> 	- The support of $X$ is not contained in any proper linear subspace $K \subset \mathbb{R}^{p}$.
> 	- $0 < \mathbb{P}(Y \geq 0 \mid X) < 1$ a.e. $F_{X}$. 
> 	- $\beta \not\equiv 0$; that is, there exists at least one $k = 1,\dots, p$ such that $\beta_{k} \neq 0$. 

We are also sometimes interested in a weaker moment assumption, labeled **(1')** in [[@manskiSemiparametricAnalysisDiscrete1985]], given by
$$\begin{align*} x^{\intercal}\beta \geq 0 \iff \mathbb{E}[\tilde{Y} \mid X = x] \geq 0, \qquad x^{\intercal}\beta < 0 \iff \mathbb{E}[\tilde{Y}|X = x] < 0, \end{align*}$$
or equivalently the sign agreement given by $\text{sign}([\mathbb{E}(\tilde{Y} \mid X = x)]) = \text{sign}\left( x^{\intercal}\beta \right)$. 
^one-prime-sign-condition