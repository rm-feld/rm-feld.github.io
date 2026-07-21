---
modified: 2026-07-09
created: 2026-05-04T14:33:21-07:00
tags: [genai/claude]
---

> [!info] Update (2026-07-01)
> The notes below are now largely formalized: the tree-crawl / degeneracy thoughts in [[Observation Richness for K-Crossed Designs]] (the pairwise cardinality-gap statistic provably catches the $(i,i,k)$ case), and the saturation / high-cardinality existence question in [[Existence of Isolating Subsets in the Near-Balanced Regime]] (greedy-off-a-matching construction; near-balanced regime covered under a weakened inter-slice condition).

The [[Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model|consistency statement for slice likelihoods]] keeps conditions for $|\tilde{\mathcal{S}}| \to \infty$ vague as we have found empirically that high order categorical random variables exhibit more complex structure than can be captured by the category-wise decay $\max_{k \in [K]} \epsilon_{k} \to 0$, or even the extended case. 


%% -- BEGIN NOTES TO EXPAND -- %%
**MIX OF SUFFICIENT CONDITION + MORE GENERAL THOUGHTS ON HIGH CARDINALITY REGIME**
- I'm not sure $\max_{\mathcal{K} \in \mathbb{A}} \epsilon_{k} \to 0$ for $\epsilon_{\mathcal{K}} = \max_{\boldsymbol{j} \in \mathcal{S}[\mathcal{K}]} N_{\boldsymbol{j}, \mathcal{K}} / N$ is sufficient, since this is a regime where we need more observations
- I think (like the big rows thing) there's going to be a saturation of some estimands if $\kappa_{k} < \kappa_{k'}$ by a sufficiently large margin; eg. if there are just many less levels of category $k$ then $k'$, then perhaps there are enough observations for direct reasonable estimability of the corresponding effects 
- Big issue 1 is curse of dimensionality-type "crosses make everything small"; under a uniformity in sampling over $\mathcal{S}$ (not $\mathcal{S}_{0}$), in $K = 3$, the expected number of observations, 
	- a slice over $(i, j)$ should expect $\sim N^{\kappa_{1} + \kappa_{2} - \kappa_{3}}$ unique observations, a slice over $k$ should expect $N^{\kappa_{3}  - \kappa_{2} - \kappa_{1}}$, but not sure if i'm delineating between $i$ and $j$ here 
	- I really can't tell if that makes things better or worse for us - curse of dimensionality in the traditional notion is "everything is orthogonal" just because there are so many opportunities to be orthogonal, but that's in some ways better for us because we need to be able to extract out the nice subset - but it seems like we need a different characterization for sufficient numbers of $\tilde{N}_{\boldsymbol{j}, \mathcal{K}} \geq 2$.
	- it seems like if one works, the others usually won't and we have to make the saturation case. 
- note upper bound on $|\tilde{S}|$ by $\max_{k \in [K]}N^{\kappa_{1}}$. 
- More generally, want to think about excluding catastrophic cases/difficult regimes: if we observe only "diagonals" $(i, i, k)$ in $K = 3$, then we never observe $a_{i}$ or $b_{j}$ separately, and thus it is impossible to make an estimate of $\sigma^{2}_{A}$ or $\sigma^{2}_{B}$. 
- maybe there's a tree-based crawl through the distributions of the $N_{\boldsymbol{j}, \mathcal{K}}$ distributions; my thought was that we check distribution of $N_{\boldsymbol{\boldsymbol{i}}, [K]}:= N_{\boldsymbol{i}}$ for $\boldsymbol{i} \in \mathcal{S}_{0}$ first, because spikes are replicates, then $N_{\boldsymbol{i}, \neg k}$ for $k \in [K]$, then naturally down cardinality of $\mathcal{K}$s. supposed to catch the $(i, i, k)$ case, but don't know if it's doing that or if it's working a different observation - maybe we need to get to within slices, which would be a pain and also computationally expensive. 
%% -- END NOTES TO EXPAND -- %%

