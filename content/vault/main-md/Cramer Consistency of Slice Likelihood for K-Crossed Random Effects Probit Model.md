---
type: theorem
aliases: [cramer consistency of slice likelihood for k-crossed random effects probit model]
tags: [crossed, research, stanford/y2, STUB, todo, TODO]
modified: 2026-07-07T21:54:50-07:00
created: 2026-05-04T11:54:47-07:00
---

> [!tip] Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model
> 
> In addition to the assumptions of [[Consistency of All Likelihood for K-Crossed Random Effects Probit Model#^all-consistency|+]], let there exist a subset $\tilde{\mathcal{S}} \subseteq \mathcal{S}_{0}$ that satisfy the following:
> 1. $|\tilde{\mathcal{S}}[\mathcal{K}]| = |\mathcal{S}[k]|$ for $k \in \mathcal{K}$, 
> 2. $|\tilde{\mathcal{S}}[\overline{\mathcal{K}}]| = |\tilde{S}[k]|$ for $k \in \overline{\mathcal{K}}$, 
> 3. $\tilde{N}_{\boldsymbol{j}, \mathcal{K}} \geq 2$ for all $\boldsymbol{j} \in \tilde{S}[\mathcal{K}]$, and 
> 4. $|\tilde{S}| \to \infty$ with $N$. 
> Then there is a root of the $\mathcal{K}$-slice likelihood equation that is a consistent estimator for $\tau^{2}_{\mathcal{K}}$. 
> 
^slice-cramer-consistency

In words, conditions 1 and 2 can be interpreted as … see [[City Block Figures]] for visual intuition. 

%% %%

> [!success]- %% %%
> 
> We give the analogue of the subset argument of [[@jiangSubsetArgumentConsistency2013]] as utilized in [[@bellioSupplementaryMaterialConsistent]]. 
> 
> To show [[Cramer Consistency|Cramer consistency]] of the slice estimator $\hat{\tau}^{2}_{\mathcal{K}}$, we require that a subset of the data whose likelihood coincides with the misspecified likelihood grows with $N$ in the limit. That is, if there exists $\tilde{\mathcal{S}} \subseteq \mathcal{S}_{0}$ growing with $N$ for which the estimator that maximizes the slice likelihood [[K-Crossed Slice Probit Likelihood#^slice-likelihood|+]] is exactly the [[MLE]] of an equicorrelated probit model. Let $\tilde{N}$ be the analogue count object. In order to coincide with the MLE, we require the following:
> 1. $|\tilde{\mathcal{S}}[\mathcal{K}]| = |\mathcal{S}[k]|$ for $k \in \mathcal{K}$, 
> 2. $|\tilde{\mathcal{S}}[\overline{\mathcal{K}}]| = |\tilde{S}[k]|$ for $k \in \overline{\mathcal{K}}$, and
> 3. $\tilde{N}_{\boldsymbol{j}, \mathcal{K}} \geq 2$ for all $\boldsymbol{j} \in \tilde{S}[\mathcal{K}]$. 
> %% #TODO replicates control in the notation is unclear%%
> In words, 1 and 2 enforce that the only interaction between units is through $u_{\boldsymbol{j}}$; 1 an *inter-slice* restriction that helps enforce the independence of the outermost product, and 2 an *intra-slice* restriction that lets observations within each slice $\boldsymbol{j} \in \tilde{\mathcal{S}}[\mathcal{K}]$ correspond to an equicorrelated probit model (though we note that this must be persistent across slices). 3 is the standard observation threshold at which we include terms in the innermost product. 
> 
> If $|\tilde{S}| \to \infty$ with $N$, the exact argument of [[@bellioSupplementaryMaterialConsistent]] holds; reproducing it here for completeness, let decompose $\tilde{S}^{C} = \mathcal{S}_{0} \setminus \tilde{\mathcal{S}}$, and let $y_{[1]}$ be the $Y_{\ell}$ values for $\boldsymbol{i}(\ell) \in \tilde{\mathcal{S}}$, $y_{[2]} \in \tilde{S}^{C}$. for $Y_{[2]}$ the set of all possible values of $y_{[2]}$, 
> 
> $$\begin{align*} \mathbb{P}\left\{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]}, y_{[2]}) \leq P_{\tau^{2}_{\mathcal{K}} + \epsilon} (y_{[1]}, y_{[2]}) \mid y_{[1]}\right\} &= \mathbb{P}\left\{ \frac{P_{\tau^{2}_{\mathcal{K}} + \epsilon} (y_{[1]}, y_{[2]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]}, y_{[2]})} \geq 1 \mid y_{[1]} \right\} \\ 
> &\leq \mathbb{E}\left\{ \frac{P_{\tau^{2}_{\mathcal{K}} + \epsilon}(y_{[1]}, y_{[2]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]}, y_{[2]})} \mid y_{[1]}\right\} \\ 
> &= \sum_{y_{[2]} \in Y_{[2]}} \frac{P_{\tau^{2}_{\mathcal{K}} + \epsilon}(y_{[1]}, y_{[2]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]}, y_{[2]})}  p_{\tau^{2}_{\mathcal{K}}}(y_{[2]} \mid y_{[1]}) \\ 
> &= \sum_{y_{[2]} \in Y_{[2]}}\frac{P_{\tau^{2}_{\mathcal{K}} + \epsilon}(y_{[1]}, y_{[2]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]})} \\ 
> &= \frac{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]})}, 
> \end{align*}$$
> for $P_{\tau^{2}_{\mathcal{K}}}$ the slice likelihood statement evaluated at $\tau^{2}_{\mathcal{K}}$. Regularity %% check: correct phrase for "regular likelihood"? %% of the likelihood and $|\tilde{\mathcal{S}}| \to \infty$ allow us to conclude by the subset argument of [[@jiangSubsetArgumentConsistency2013]] that the final equality converges to zero in probability. Repeating the argument for $\tau^{2}_{\mathcal{K}} - \epsilon$ lets us conclude root consistency for $\tau^{2}_{\mathcal{K}}$. $\blacksquare$  



