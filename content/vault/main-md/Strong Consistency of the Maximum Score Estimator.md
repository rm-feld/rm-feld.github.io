---
type: theorem
aliases: [strong consistency of the maximum score estimator]
tags: [crossed, research, stanford-stats/y2]
modified: 2026-04-03T17:31:56-07:00
created: 2026-04-03T16:59:26-07:00
---

> [!tip] Strong Consistency of the Maximum Score Estimator
> **Theorem 1, [[@manskiSemiparametricAnalysisDiscrete1985]].** Let [[Standard Assumptions for Maximum Score Estimation|assumptions 1, 2]], and [[Consistency of the Maximum Score Estimator#^assumption-3-manski-consistency|3]] hold. Further, let every component of $\beta$ be bounded away from zero, ie. there exists known $\eta > 0$ such that $\lvert \beta_{k} \rvert / \left\lvert\left\lvert \beta \right\rvert\right\rvert_{2} \geq \eta$ for all $k = 1, \dots, p$. The [[Maximum Score Estimator]] over the corresponding candidate set $B_{\eta} = \left\{ \beta: \left\lvert\left\lvert \beta \right\rvert\right\rvert_{2} = 1, \, |\beta_{k}|  \geq \eta \; \;\forall \, k = 1, \dots, p\right\}$ is [[Almost Sure Convergence|strongly consistent]] for $\beta_{0}$.

%% %%

> [!abstract]- Proof Sketch
> The proof follows a standard path of proving almost-sure convergence; with lemmas as labeled in [[@manskiSemiparametricAnalysisDiscrete1985]],
> 1. Show uniqueness of maxima over a candidate set (**Lemma 3**). 
> 2. Show [[Uniform Convergence]] of the sample score function $S_{n}(\beta)$ to its population limit $S(\beta)$ occurs [[Almost Sure Event|almost surely]] (**Lemma 4**, via a [[Glivenko-Cantelli]] type statement). 
> 3. Show the continuity in $\beta$ of $S(\beta)$ over $B_{\eta}$. (**Lemma 5**). 
> %% %%
> The above is sufficient to recover the desired. 

%% %%

%% 

> [!hint]- Intuition and Connections
> 


 %%