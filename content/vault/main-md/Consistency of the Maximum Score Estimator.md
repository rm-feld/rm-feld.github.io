---
modified: 2026-07-07T21:29:37-07:00
created: 2026-04-02T18:12:14-07:00
tags: [maximum-score]
---
We first consider the issue of identification. Our particular identification criteria is given by what Manski calls **Linear Median-Discrete Response (LMDR) Identification:**

![[Linear Median-Discrete Response (LMDR) Identification]]

**Lemma 2** of [[@manskiSemiparametricAnalysisDiscrete1985]] gives a particular identification of $\gamma$ (identification of $\beta$ up to scale).

![[Identification of the Maximum Score Estimator]]

If [[Asymptotic Consistency|strong consistency]] is of interest, we introduce a shared distributional assumption:

> [!attention] Assumption 3
> $\left\{ (X_{i}, Y_{i}) \right\}_{i =1}^{n} \overset{\mathrm{iid}}{\sim} F_{YX}$ some joint distribution.  
> ^assumption-3-manski-consistency

Using some standard machinery, Theorem 3 of [[@manskiSemiparametricAnalysisDiscrete1985]] gives the consistency proof under the three presented assumptions, though we unfortunately require nontriviality of each component. 

![[Strong Consistency of the Maximum Score Estimator]]

While the zero bounding result may be undesirable, the consistency result is reasonably robust to (random) misclassification. Consider the case where each observation is corrupted with probability $p$, where if the observation is corrupted, we observe $(X_{i}, 1)$ and $(X_{i}, -1)$ with equal probability; then **Corollary 1** of [[@manskiSemiparametricAnalysisDiscrete1985]] states that [[Strong Consistency of the Maximum Score Estimator|strong consistency]] still holds. 