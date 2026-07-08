---
modified: 2026-05-26
created: 2026-05-11T15:12:21-07:00
tags: [genai/claude]
---

# Notation and Model Definition

![[Multivariate Notation (realign)]]

Here, $\varepsilon_{\ell} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(\mathbf{0}_{M}, \Sigma_{E})$ and $a_{\boldsymbol{i}(\ell), \mathcal{K}} \sim \mathcal{N}(\mathbf{0}_{M}, \Sigma_{\mathcal{K}})$. With total covariance $\Sigma = \Sigma_{E} + \sum_{\mathcal{K} \in \mathbb{A}} \Sigma_{\mathcal{K}}$, the all likelihood *can* be written as a product of $N$ $M$-variate normal cdfs; since this is intractable for moderate $M$, we work pairwise across components.

# Pairwise Marginal Likelihood (the introducing step, in the cleaner tilde form)

The bivariate case below uses primes for the second component and tildes for the signed response, and is the cleaner rewrite of the introducing step. Vectorize $\boldsymbol{\tilde{\rho}}, \boldsymbol{\tilde{\sigma}^{2}}, \boldsymbol{\tilde{\sigma}'^{2}}$ as length-$\lvert\mathbb{A}\rvert$ vectors (same shape as $\boldsymbol{a}_{\boldsymbol{i}}$); the composite likelihood $L_{\text{all}}(\Gamma, r)$ at the end of the section generalizes to $M$ components directly.

![[Bivariate Tilde (realign)]]

# Pairwise Conditional Slice Likelihood (slice over $\mathcal{K}$)

![[Multivariate Conditional Slice Likelihood (realign)]]

# High Cardinality and Numerical Notes

%% reese: same place as in the K-crossed writeup — sparsity/high-cardinality discussion gets its own section once we have an opinion on the M-variate analogue of \tilde{\varepsilon}_k. %%

# Case Studies
%% reese: slot for the multivariate VPCV settings. %%
