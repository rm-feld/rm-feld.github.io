---
type: definition
aliases: [LMDR-identification, LMDR-identified]
tags: [crossed, research, stanford-stats/y2]
modified: 2026-04-03T16:43:48-07:00
created: 2026-04-03T16:30:58-07:00
---

> [!important] Linear Median-Discrete Response (LMDR) Identification
> Consider the set of $X \sim F_{x}$ whose sign disagrees with that of the true linear parameter $\beta_{0}$, given by 
> $$\begin{align*}  \mathcal{X}_{\beta} = \left\{ x \in \mathbb{R}^{k} \mid \text{sign}\left( x^{\intercal}\beta\right)  \neq \text{sign}\left( x^{\intercal}\beta_{0} \right)\right\}.  \end{align*}$$
> In turn, we can define a loss 
> $$\begin{align*} R(\beta) = \int _{\mathcal{X}_{\beta}}  \, dF_{x}.  \end{align*}$$
> For $B \subseteq \mathbb{R}^{p}$ such that $B \ni \beta$, [[@manskiSemiparametricAnalysisDiscrete1985]] says that $g(\beta)$ is **LMDR-identified with respect to $B$** if and only if $R(\beta) > 0$ for every $\beta \in B: \beta \neq \beta_{0}$. 

