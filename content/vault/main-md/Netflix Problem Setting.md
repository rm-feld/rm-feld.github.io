---
type: setup
aliases: [netflix problem setting]
tags: [research, stats/bg, y1/t/b]
modified: 2026-04-07T20:53:34-07:00
created: 2026-04-07T20:39:13-07:00
---

> [!attention] Netflix Problem Setting
> The [Netflix prize](https://en.wikipedia.org/wiki/Netflix_Prize) was a competition hosted by Netflix to uncover censored ratings, as in [[Matrix Completion|matrix completion]]. 
> %% %%
> More colloquially, the Netflix problem refers to issues in inference under crosses of high cardinality categorical variables (in this case $\text{user }\times \text{ movie}$), where two problems are generally highlighted:
> 1. **Sparsity of Crossed Observations.** It is generally the case that an individual user has not seen most movies, and an individual movie has not been seen by most people. Thus observations over the whole cross of users and movies is sparse. 
> 2. **Meaningful Variance between Categories.** Some users have a propensity to rate things higher (or lower) independent of their observed covariates. Similarly, some movies may encourage higher or lower ratings. Thus we may want to choose a modeling procedure that meaningfully accounts for this variance. 

