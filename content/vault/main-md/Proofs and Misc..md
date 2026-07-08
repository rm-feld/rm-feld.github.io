---
modified: 2026-03-16T11:53:39-07:00
created: 2026-03-13T20:53:31-07:00
---

# $K$-arc model, generic 

> [!attention] K-Crossed Random Effects Model 
> The binary $K$-crossed random effects model with mean function $g$ is given by 
> 
> $$\begin{align*} \mathbb{P}(Y_{\mathbf{i}} = 1) = g\left( x_{\mathbf{i}}^{\intercal}\beta + \sum_{k = 1}^{K} a_{k, \mathbf{i}} \right), \end{align*}$$
> For $a_{k, \mathbf{i}} \sim \mathcal{N}(0, \sigma^{2}_{k})$ the random effect from the $k$th random effect with index $\mathbf{i}[k]$. Note $a_{\mathbf{i}} := (a_{1, \mathbf{i}}, \dots , a_{k, \mathbf{i}})$ the vector of random effects for index $\mathbf{i}$ is assumed independent in each entry. 


# Weighting Proofs 
## Concentration Step Under Bounded Marginal Log-Likelihood Contributions

> [!lemma] Concentration of Weighted All Likelihood via Slice Decay
> 
> Letting $w_{\mathbf{i}}$ be any non-negative weights, normalized such that $\sum_{\mathbf{i}}w_{\mathbf{i}}Z_{\mathbf{i}} = N$. Define the per-level slice contributions $$\begin{align*} h_k(i_k) := \sum_{\mathbf{i} \in \mathcal{S}:, \mathbf{i}_k = i_k} w_{\mathbf{i}} Z_{\mathbf{i}}, \end{align*}$$ and let $\tilde{\varepsilon}_{k} := \max_{i_{k}} h_{k}(i_{k}) / N$. Suppose termwise marginal log likelihood $\eta_{\mathbf{i}}$ is uniformly bounded, and $\max_{k} \tilde{\varepsilon}_{k} \to 0$. Then for the weighted all log-likelihood $\ell_{\text{all}}(\gamma;w) = \sum_{\mathbf{i}}w_{\mathbf{i}}\eta_{\mathbf{i}}Z_{\mathbf{i}}$,
> $$\begin{align*} \mathrm{Var}\left( \frac{\ell_{\text{all}}(\gamma; w)}{N} \right) \leq B^{2} \sum_{k=1}^{K} \tilde{\varepsilon}_{k} \to 0. \end{align*}$$

**Proof.**

By $|\eta_{\mathbf{i}}| \leq B$ uniformly bounded, covariate contributions can be bounded via a coordinate-wise union bound, $$\begin{align*} \lvert \mathrm{Cov}(\eta_{\mathbf{i}}, \eta_{\mathbf{i}'}) \rvert \leq B^{2}\cdot \mathbf{1}\left[\exists, k: i_{k} = i'_{k} \right] \leq B^{2}\sum_{k =1}^{K} \mathbf{1}\left[i_{k} = i'_{k} \right]. \end{align*}$$ Thus $$\begin{align*} \mathrm{Var}\left( \frac{\ell_{\text{all}}(\gamma; w)}{N} \right) &\leq \frac{B^{2}}{N^{2}} \sum_{\mathbf{i}} \sum_{\mathbf{i}'} Z_{\mathbf{i}}Z_{\mathbf{i}'}w_{\mathbf{i}}w_{\mathbf{i}'} \sum_{k = 1}^{K} \mathbf{1}\left[i_{k} = i_{k}' \right] \\ &= \frac{B^{2}}{N^{2}} \sum_{k=1}^{K} \sum_{\mathbf{i}}\sum_{\mathbf{i}'} w_{\mathbf{i}} w_{\mathbf{i}'} Z_{\mathbf{i}}Z_{\mathbf{i}'} \mathbf{1}\left[i_{k} = i_{k}' \right]. \end{align*}$$ Each of the outer summands can be written exactly in terms of $h_k$: 
$$\begin{align*} \frac{B^{2}}{N^{2}} \sum_{\mathbf{i}} \sum_{\mathbf{i}'} w_{\mathbf{i}} w_{\mathbf{i}'}Z_{\mathbf{i}}Z_{\mathbf{i}'} \mathbf{1}\left[i_{k} = i_{k}' \right] &= \frac{B^{2}}{N^{2}} \sum_{j= 1}^{R_{k}} \left(\sum_{\mathbf{i}:, i_k = j} w_{\mathbf{i}}Z_{\mathbf{i}}\right)^{2} \\ 
&= B^{2} \sum_{j = 1}^{R_{k}}\left(\frac{h_{k}(j)}{N}\right)^{2} \\ 
& \leq B^{2} \tilde{\varepsilon}_{k} \sum_{j =1}^{R_{k}} \frac{h_{k}(j)}{N} \\
&= B^{2}\tilde{\varepsilon}_{k}, \end{align*}$$ where the third line emerges from maximum bounding, and the last equality uses $\sum_{j} h_k(j) = N$. Summing over $k$, $$\begin{align*} \mathrm{Var}\left( \frac{\ell_{\text{all}}(\gamma; w)}{N} \right) \leq B^{2} \sum_{k=1}^{K} \tilde{\varepsilon}_{k} \to 0 \end{align*}$$ under $\max_{k}\tilde{\varepsilon}_{k} \to 0$. $\blacksquare$

**Remark.** Besides observation structure, the lemma requires only uniformly bounded marginal log-likelihood, and is otherwise agnostic to the link. Thus after verifying the new slice decay conditions $\max_{k}\tilde{\varepsilon}_{k}\to 0$, we need only consider if the maximizer of $\ell_{\text{all}}(\gamma;w)$ is unique and identifiable to conclude weak consistency of $\hat{\gamma}$. This argument also holds if $\gamma$ is unavailable; our uniqueness statements simply shift to that of $(\beta, \sigma)$. $\square$ 

---
## K-Probit Consistency for All Likelihood

> [!corollary] Consistency of Probit $\hat{\gamma}$ Under Row-IPW
> 
> Let $\hat{\gamma}$ be any maximizer of $\ell_{\mathrm{all}}(\gamma; w_{\mathbf{i}})$ with row-IPW weights $w_{\mathbf{i}} = N/ [R_{1}N_{1, \mathbf{i}}]$. In addition to the [[Base Assumptions for K-crossed Random Effects with Symmetric Binary Link|base assumptions for the probit $k$-arc model]], assume $\max_{k \neq 1} \tilde{\varepsilon}_{k} \to 0$, where $$\begin{align*} h_k(i_k) = \frac{N}{R_{1}} \sum_{\mathbf{i}:, \mathbf{i}_k = i_k} \frac{Z_{\mathbf{i}}}{N_{1, i_1}}, \qquad \tilde\varepsilon_k = \max_{i_k} h_k(i_k)/N. \end{align*}$$ Then $\hat{\gamma}$ is weakly consistent; that is, $\forall\epsilon > 0$, $$\begin{align*} \mathbb{P}(\left\lvert\left\lvert \hat{\gamma} - \gamma_{0} \right\rvert\right\rvert > \epsilon) \to 0 \end{align*}$$ as $N \to \infty$.

> [!success]- %% %%
> The proof follows a standard pattern: (1) concentration of the all likelihood, (2) confirming that $\gamma_{0}$ is a maximizer, and (3) ensuring the maximizer is unique.
> 
> We first validate concentration with the #cite Lemma. By our assumptions, we clearly need only confirm decay of $h_{1}(i_{1})$ and the appropriate reweighting. Intuitively, $w_{\mathbf{i}}$ weights levels of the first random effect equally; 
> 
> $$\begin{align*} h_{1}(i_{1}) &= \frac{N}{R_{1}}\sum_{\mathbf{i}: \mathbf{i}_{1}  = i_{1}} \frac{Z_{\mathbf{i}}}{N_{1, i_{1}}} \\ 
> &= \frac{N}{R_{1}} \cdot \frac{N_{1, i_{1}}}{N_{1, i_{1}}} \\
> &= \frac{N}{R_{1}}; \end{align*}$$
> Thus $\sum_{i =1}^{R_{1}} h_{1}(i) = N / R_{1} \cdot R_{1} = N$, and $\max_{i}h_{1}(i) / N = 1/R_{1} \to 0$, so the lemma holds. 
> 
> We now show that $\gamma_{0}$ is the unique maximizer of the all likelihood. Note that both $g(\gamma; w) := \lim_{N\to\infty} \mathbb{E}[\ell_{\text{all}}(\gamma;w)/N]$ and $\ell_{\text{all}}(\gamma;w)/N$ are concave in $\gamma$, and we can directly follow the proof of $\gamma$ consistency as given in the original ARC paper [@bellioSupplementaryMaterialConsistent]. In particular, $\nabla_\gamma g(\gamma_0) = 0$ and the Hessian 
> $$\begin{align*} H := \frac{\partial^{2} g(\gamma_0)}{\partial\gamma,\partial\gamma^\intercal} = -\frac{1}{N}\sum_{\mathbf{i}} w_{\mathbf{i}} x_{\mathbf{i}} x_{\mathbf{i}}^\intercal Z_{\mathbf{i}} ,\mathbb{E}\left\{\frac{\varphi(x_{\mathbf{i}}^\intercal\gamma_0)^2}{\Phi(x_{\mathbf{i}}^\intercal\gamma_0),\Phi(-x_{\mathbf{i}}^\intercal\gamma_0)}\right\} \end{align*}$$ is nontrivially negative definite by the limiting assumption on the $x_{\mathbf{i}}$ structure. Thus $\gamma_0$ is the unique maximizer of a strictly concave function, and we conclude $\hat\gamma \xrightarrow{p} \gamma_0$. $\blacksquare$

---
## Conditions Under which weighting conditions hold.
We consider some sufficient conditions and worst case behavior of $\tilde{\varepsilon}_{k}$. $\tilde{\varepsilon}_{k}$ is easy to check and reasonably okay to interpret, though we may prefer some digging. 
### Sufficient Conditions 
We first note that $\tilde{\varepsilon}_{k}$ coincides with $\varepsilon_{k}$ when $w_{\mathbf{i}} \equiv 1$. 
#### Row-IPW 
We first look at what needs to be true (in addition to standard slice decay condition $\varepsilon_{k\neq 1}\to 0$) in order for $\tilde{\varepsilon}_{k}\to 0$ for all $k$ under first slice inverse-proportion weighting. It is easy to see that the above is not sufficient. We have already shown that this implies $\tilde{\varepsilon}_{1} \to 0$. Let us look at $\tilde{\varepsilon}_{2}$ without loss of generality. 

Written explicity, we have
$$\begin{align*} \frac{h_{2}(j)}{N} &= \frac{1}{R_{1}} \sum_{\mathbf{i}: \mathbf{i}[2] = j} N_{1, \mathbf{i}[1]}^{-1} \\
&= \frac{1}{R_{1}} \sum_{i =1 }^{R_{1}} \sum_{\mathbf{i}: \mathbf{i}[2] = j} N_{1, i}^{-1} \mathbf{1}\left[\mathbf{i}[1] = i \right] 
\end{align*}$$
a candidate of the $\tilde{\varepsilon}_{2}$ maximum. Note by definition of $N_{1,i}$ that the inner sum is at most 1, since there can be at most $N_{1, i}$ observations whose first index is $i$. 

Here is some logic to follow. If $j$ is completely nested under some $i$, then 
$$\begin{align*} \frac{h_{2}(j)}{N} = \frac{1}{R_{1}} \cdot \frac{N_{2, j}}{N_{1, i}} \leq \frac{1}{R_{1}}, \end{align*}$$
with equality when we only ever see $(i, j)$ together - note this implicitly means $N_{2, j} \leq N_{1, i}$. This clearly does not violate the decay condition. If $j$ only appears in the data with $i$ or $i'$, say, each exactly half of the time, then 

$$\begin{align*} \frac{h_{2}(j)}{N} = \frac{1}{R_{1}}\cdot \left[ \frac{1}{2}\cdot \frac{N_{2, j}}{N_{1, i}} + \frac{1}{2}\cdot \frac{N_{2, j}}{N_{1, i'}} \right]. \end{align*}$$
The implicit inequality is now that $N_{2, j}/2 \leq N_{1, i}, N_{1, i'}$. 

The above motivates a counterexample when $\kappa_{2} > \kappa_{1}$. 

> [!example] Catastrophic Weighting Outcome Under Row IPW - Big Row.
> 
> Let half of our observations come from one level $i^{\star}$ of the first random effect, and let all other levels see exactly two observations. When $\kappa_{2} > \kappa_{1}$, we are able to observe a "large" level $j^{\star}$ which can grow as $N^{\tilde{\kappa}}$, which clearly satisfies the slice decay condition $\varepsilon_{2} \to 0$. For large $N$, $N^{\tilde{\kappa}} > 2N^{\kappa_{1}}$, so $j^{\star}$ can eventually always "fill" all of the non-$i^{\star}$ rows. When we let such a thing occur, then 
> $$\begin{align*} \frac{h_{2}(j^{\star})}{N} \leq \frac{1}{R_{1}}\sum_{i \neq i^{\star}} \sum_{\mathbf{i}: \mathbf{i}[2] = j^{\star}} N_{1, i}^{-1} \mathbf{1}\left[\mathbf{i}[1] = i \right]  = \frac{R_{1} - 1}{R_{1}} \to  1,  \end{align*}$$
> which clearly violates the decay condition for $\tilde{\varepsilon}_{2}$. 

It is informative that the above counterexample fails for uniform levels; if rows are of uniform size, ie. $N_{1, i} = N^{1 - \kappa_{1}}$ for all $i$, then $j^{\star}$ can "fill" $N^{\tilde{\kappa} + \kappa_{1} - 1}$ levels so that
$$\begin{align*} \frac{h_{2}(j^{\star})}{N} \approx \frac{1}{N^{\kappa_{1}}}\cdot N^{\tilde{\kappa} + \kappa_{1} - 1} = N^{\tilde{\kappa} - 1} \to  0, \end{align*}$$
since implicitly $\tilde{\kappa} < 1$.

For the latex conversion test - note $N_{1, i} = N_{i\bullet}$. 

An observation to make from the above is that our preference is for big rows to co-occur with big slices, when they exist; we have asymptotically nontrivial contribution of an index whenever it appears in many of the small rows. 

This seems to be a bad sign, in the sense that, in our data regime, it is reasonable that a level of $k = 2$ grows as $N^{\tilde{\kappa}}$, and that it is common over the smaller row-levels. As an example, we can think of e-commerce (eg. Amazon) where we allow people purchasing for industrial purposes as part of the users for a cross of users $\times$ products; if there exists some individual user (eg. a large company) that buys a nontrivial proportion of the products, and a very popular product that a nontrivial proportion of users buy (but that this company doesn't), then we may see that many of the people who nontrivially buy this item will hike up the $h_{2}(j^{\star})$ contribution. Obviously many caveats, but I'm thinking about something like Amazon Prime; nontrivial proportion of users have it, but the number of products is much bigger than the number of users, and number of products sold is also much larger than number of Amazon Prime memberships sold, so we have that Amazon Prime memberships satisfy the column decay condition, but that co-occurrence over each user is non-trivial. 

I believe that the above is a failure that emerges from the row-IPW, and not in the general case. In particular, we interpret the row-weighted all likelihood of the above as treating users equally, in which case Amazon Prime encompasses a nontrivial proportion of a user's purchase history; whereas without row weighting, Amazon prime encompasses a trivial proportion of total purchase volume.  









