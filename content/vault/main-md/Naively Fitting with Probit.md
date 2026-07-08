---
modified: 2026-07-07T23:46:31-07:00
created: 2025-11-04T17:21:08-08:00
aliases:
  - Random slopes via Naive Probit
---
# Issues with the warmstart, etc. 
- when is it good/bad
- scale of covariance is what i really want 
- connection to [[Binary Response ARC - Generalizing|Binary Response ARC]] - I feel like there is something I can do with this "underlying distribution", something something [[Monte Carlo Sampling]]
# Naively Fitting with Probit
## Simulation Motivation
As discussed in the opportunities for per-column fits in random slopes, I think that some sort of all-likelihood is preferable. I start with a simulation observation; Consider as standard
$$\begin{align} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, ij}^{\intercal}a_{i} + x_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} \end{align}$$
and simulate the above with $x_{ij}$, $x_{A, ij}$, and $x_{B, ij}$ generated as normal with identity covariance. Here, I let `beta ← runif(p, -1, 1)` for $p = 4$, $p_{A} = 2$, $p_{B} = 2$. I let $b_{j}$ also have identity covariance and 
$$\begin{align} a_{i} \sim \mathcal{N}\left( 0, \begin{pmatrix}
0.5 & 0.3 \\
0.3 & 0.7
\end{pmatrix} \right) \end{align}$$
arbitrarily. I'll use a capital $S$ to describe the covariances of the data, in contrast to $\Sigma$ to the random effects themselves. Generating this data, I then fit probit naively over the augmented vector $\tilde{x} =\left( x_{ij}^{\intercal}, x_{A, ij}^{\intercal}, x_{B, ij}^{\intercal} \right)^{\intercal}$. We'll call this fit $\tilde{\gamma}$ for now. 

In this particular case, $\tilde{\gamma}$ had the following behavior. As might be desired, $x_{A, ij}$ and $x_{B, ij}$ had very small coefficients; in my test case, I have largest magnitude .0126 on any of the 4 (compared to .07 smallest magnitude of the rest). Further, doing a termwise $\tilde{\gamma} / \beta$, I have scale differences in $(1.85, 1.93)$, so it seems like there exists some exploitable shared scale that may be fruitful, and that we are actually learning directional information. Since I have desired behavior of zeroing out $x_{A}$ and $x_{B}$, I switch over back to a naive $\hat{\gamma}$ estimation over the non-augmented form. The fits were generally equivalent to 4 digits, though I do need to reassess under different $x$ regimes which may cause more strife. 
## Heuristics - independent $x_{A}$, $x_{B}$, $x$ setting
What's happening here? We're abusing distributional information $S$ of the $x$'s. Incorporating this (and also abusing some notations/interpretations),

$$\begin{align} \mathbb{P}(Y_{ij} = 1 \mid X_{ij}) &= \mathbb{P}\left( X_{ij}^{\intercal}\beta + X_{A, ij}^{\intercal} a_{i} + X_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} > 0 \mid X_{ij} \right) \\
&= \mathbb{P}\left( \varepsilon_{ij} + X_{A, ij}^{\intercal} a_{i} + X_{B, ij}^{\intercal}b_{j}  < X_{ij}^{\intercal}\beta | X_{ij}\right) \\
&\approx \mathbb{P}\left( Z\sqrt{ 1 +  \text{tr}(\Sigma_{A}S_{A}) + \text{tr}(\Sigma_{B}S_{B})} < X_{ij}^{\intercal}\beta \mid X_{ij} \right) \\
&= \Phi\left( \frac{X_{ij}^{\intercal}\beta}{\sqrt{ 1 + \text{tr}(\Sigma_{A}S_{A}) + \text{tr}(\Sigma_{B}S_{B}) }} \right).\end{align}$$
Since it appears so frequently, let's call $v := v_{A} + v_{B}:= \text{tr}(\Sigma_{A}S_{A}) + \text{tr}(\Sigma_{B}S_{B})$. In the simulation case, I have $v_{A} = 1.2$ and $v_{B} = 2$ so that $\sqrt{ 1 + v } = 2.04$; which isn't quite right, too large but in the ballpark. But I'm hoping this might wash away as a nice warm start for iteration. I think the theory might be ugly here, but maybe there's something that emerges as a first order approximation, eg; I really just want a direction that can start a $\Sigma_{A}$, $\Sigma_{B}$ estimation. 

I think that it is not unreasonable to assume this will work for some good behavior of fourth moments and some limiting behavior
$$\begin{align} \frac{1}{N} \sum_{i, j} x_{A, ij}x_{A, ij}^{\intercal} \to  S_{A}, \,\,\,\,\,\,\,\, \frac{1}{N} \sum_{i, j} x_{B, ij}x_{B, ij}^{\intercal} \to  S_{B}, \, \, \, \,\, \,  \frac{1}{N} \sum_{i, j} x_{ij}x_{ij}^{\intercal} \to  S_{X}, \end{align}$$
which at least in the nonsequential case/etc. is probably a decent assumption (more philosophically, "when are we allowed to pool," maybe). The other strong assumption in this case is that $x_{A}$, $x_{B}$, $x$ are independent; which is much more concerning/strong/unreasonable of an assumption, probably. We'll come back to that later, but let's see some ways the iteration can shake out. 

### First Approach 
I'll whiten over flattened data, "columnwise;" looks like there might be some ambiguity/unclear best practices in this case for shared $i$, $j$ behavior, potentially to be explored. Obviously in this case we then have access to $\hat{S}_{A}$, $\hat{S}_{B}$, $\hat{S}_{X}$ sample covariances which we would plug in throughout.

$$\begin{align} \mathbb{P}(Y_{ij} = 1 \mid b) &= \mathbb{P}\left( X_{ij}^{\intercal}\beta + X_{A, ij}^{\intercal}a_{i} + X_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} > 0 \mid b \right) \\
&= \mathbb{P}\left( X_{ij}^{\intercal}\hat{\gamma}^{(0)}  + \frac{X_{B, ij}^{\intercal}b_{j}}{\sqrt{ 1 + v } } >\frac{X_{A, ij}^{\intercal}a_{i} + \varepsilon_{ij}}{\sqrt{ 1 + v }} |b\right) \\
&\approx \mathbb{P}\left( X_{ij}^{\intercal}\hat{\gamma}^{(0)} + \frac{X_{B, ij}^{\intercal}b_{j}}{\sqrt{ 1 + v }}  > \frac{Z\sqrt{ \text{tr}(\Sigma_{A}S_{A}) + 1 }}{\sqrt{ 1 + v }} \right) \\
&= \Phi\left( X_{ij}^{\intercal}\hat{\gamma}^{(0)}_{B} + \frac{X_{B, ij}^{\intercal}b_{j}}{\sqrt{ 1 + v_{A} }} \right)\end{align}$$
for
$$\begin{align} \hat{\gamma}_{B}^{(0)} &= \hat{\gamma}^{(0)}\sqrt{ \frac{1 + v_{A} + v_{B}}{1 + v_{A}}}  \\
&= \hat{\gamma}^{(0)} \sqrt{ 1 + \frac{v_{B}}{1 + v_{A}} };\end{align}$$
I'm still a little "conflicted" with this in the sense that, in order to get good behavior of probit matching, we kind of need to discard $x_{A, ij}$ and $x_{B, ij}$ information again in favor of $x_{B, ij}^{\intercal}b_{j} \sim \mathcal{N}(0, \text{tr}(\Sigma_{B}S_{B}))$ and $X_{A, ij}^{\intercal}a_{i} \sim \mathcal{N}(0, \text{tr}(\Sigma_{A}S_{A}))$ to get a solve that only depends on $v_{B} / (1 + v_{A})$. But in the warm-start regime, maybe this is fine and we just want something decently simple to start with. Marginally, I think this treatment is fine, but I think there might be something more principled we can do with replacing $\hat{S}_{A}$ with $\hat{S}_{A(j)}$, etc. and to actually incorporate $b_{j}$ information. regardless, discarding $x_{B, ij}$ in favor of the $\Sigma_{B}$ scaling gives us access to $\tau^{2}_B = v_{B} / (1 + v_{A})$ and analogously $\tau^{2}_{A} = v_{A} / (1 + v_{B})$ estimates via the standard optimization procedures. And once I have that, I've solved for global scale, and I have the standard explicit estimate of $\beta$. 

I don't have too much trust in this estimate, but I think that it's fine. We have to start our iterations in a weird place in the sense that we'll go back to row-column immediately, instead of starting our iterations with all. As a reminder, our information is now the following; I have estimates of $\beta$, $\text{tr}(\Sigma_{A}S_{A})$ (with access to $S_{A}$), and $\text{tr}(\Sigma_{B}S_{B})$ (with access to $S_{B}$). Maybe for this iteration I continue to discard $x_{A, ij}$ but this time I utilize variation in $x_{B}$; or do I do it termwise? First a naive direction;

$$\begin{align} \mathbb{P}(Y_{ij} = 1 \mid b) &= \mathbb{P}\left( X_{ij}^{\intercal}\beta + X_{A, ij}^{\intercal}a_{i} + X_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} > 0 \mid b \right)  \\
&\approx \mathbb{P}\left( X_{ij}^{\intercal}\beta  + X_{B, ij}^{\intercal}b_{j}  > \sqrt{ 1 +v_{A} } Z\mid b \right) \\
&= \Phi\left( \frac{X_{ij}^{\intercal}\beta + X_{B, ij}^{\intercal}b_{j}}{\sqrt{ 1 + v_{A} }}  \right)\end{align}$$
for which I have $v_{A}$ and $\beta$ so I can do integration over $p_{B}$ terms to optimize over the only unknown, $b_{j}$. An approach to this is refitting a probit with known offset $X_{ij}^{\intercal}\beta /\sqrt{ 1 + v_{A} }$ to solve for $b_{j}$, then take $\sum_{j} b_{j}b_{j}^{\intercal}$ the covariance matrix, with some regularization/reweighting on number of observations or variance sensitivity due to $X_{B, ij}$ magnitude. Or, we can optimize a likelihood over $b_{j}$, over all $p_{B}$. In simulations, this first $b_{j}b_{j}^{\intercal}$ approximation has been pretty stable, but its iteration has been poor. This is generally because things 

 
 Having identified I explicitly need to do something univariate. In that case, we still have a natural approach in the standard per-element decomposition. It's still unclear to me whether to use a global or local fit in this regime. But to get started, let $b_{j[k]}$ index components and take $b_{j[-k]}$ as the rest of them. Then with some ugly block notation, we can get
$$\begin{align} X_{B, ij[-k]}^{\intercal}b_{j[-k]} \mid X_{B, ij[k]}b_{j[k]} \sim \mathcal{N}\left( X_{B, ij}^{\intercal} \right) \end{align}$$

### Trying to be scale "agnostic"
The scaling is off. I think there's also variation in $x_{ij}$ and sensitivity in $\beta$ I need to worry about, because the scale differences persisted; while scale differences were concentrated in (1.899, 1.936), it's a little concerning that I didn't see particularly strong tightening for a tenfold increase in datapoints. So there is probably something more subtle going on that isn't quite right - need to assess some worst case behavior in this regime. I will say that $\beta$ scale seems directly related to difference in scale, so maybe wrong comparison? Need to probe worst case behavior as well, or maybe there's a second order adjustment in the variance.

## Correlation between $x_{A}$ and $x$
Chat seems to think that there's some principled rotation we can exploit. I think it's not impossible. 


# Writing Out Something Actionable
## Simulation Motivation
As discussed in the opportunities for per-column fits in random slopes, I think that some sort of all-likelihood is preferable. I start with a simulation observation; Consider as standard
$$\begin{align} W_{ij} = x_{ij}^{\intercal}\beta + x_{A, ij}^{\intercal}a_{i} + x_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} \end{align}$$
and simulate the above with $x_{ij}$, $x_{A, ij}$, and $x_{B, ij}$ generated as normal with identity covariance. Here, I let `beta ← runif(p, -1, 1)` for $p = 4$, $p_{A} = 2$, $p_{B} = 2$. I let $b_{j}$ also have identity covariance and 
$$\begin{align} a_{i} \sim \mathcal{N}\left( 0, \begin{pmatrix}
0.5 & 0.3 \\
0.3 & 0.7
\end{pmatrix} \right) \end{align}$$
arbitrarily. I'll use a capital $S$ to describe the covariances of the data, in contrast to $\Sigma$ to the random effects themselves. Generating this data, I then fit probit naively over the augmented vector $\tilde{x} =\left( x_{ij}^{\intercal}, x_{A, ij}^{\intercal}, x_{B, ij}^{\intercal} \right)^{\intercal}$. We'll call this fit $\tilde{\gamma}$ for now. 

In this particular case, $\tilde{\gamma}$ had the following behavior. As might be desired, $x_{A, ij}$ and $x_{B, ij}$ had very small coefficients; in my test case, I have largest magnitude .0126 on any of the 4 (compared to .07 smallest magnitude of the rest). Further, doing a termwise $\tilde{\gamma} / \beta$, I have scale differences in $(1.85, 1.93)$, so it seems like there exists some exploitable shared scale that may be fruitful, and that we are actually learning directional information. Since I have desired behavior of zeroing out $x_{A}$ and $x_{B}$, I switch over back to a naive $\hat{\gamma}$ estimation over the non-augmented form. The fits were generally equivalent to 4 digits, though I do need to reassess under different $x$ regimes which may cause more strife. 

## Algorithm Under Independence of $x$, $x_{A}$, and $x_{B}$. 
I still need to formalize an approximation, but here's something actionable. We have the standard setup. Then I have the following operation. 

1. Derive $\hat{\gamma}^{(0)}$ via application of naive probit. It is assumed that $\hat{\gamma}^{(0)} \approx \beta / \sqrt{ 1 + v }$ for $v := v_{A} + v_{B} := \text{tr}(\Sigma _{A}\Gamma_{A}) + \text{tr}(\Sigma_{B}\Gamma_{B})$. 
2. Continue to use global scale, this time only on partials. Use machinery of `likAGH` and global incorporation to solve, ie. we ignore $x_{A, ij}$ in favor of global incoporation $\Gamma_{A}$. I'll say we're still on iteration 0, which will be different. Here, what I'd like to do is to get some access to $b_{j}$ directly; but instead, what we're going to do is take our integrals over a purported normal $X_{B, ij}^{\intercal}b_{j} / \sqrt{ 1 + v_{A} }$ which will have the appropriate scaling to get our $\tau^{2}_{B}$ analogue. get $\tau^{2}_{A}$ the same way, and thus recover $v$, $v_{A}$, $v_{B}$, and in turn $\hat{\beta}^{(0)}$. 
3. A few directions here, for this final setup step. 
**(A - Assumption of Decent Observation)** Having recovered $v$, notice

$$\begin{align} \mathbb{P}(Y_{ij} = 1 \mid b) &= \mathbb{P}\left( X_{ij}^{\intercal}\beta + X_{A, ij}^{\intercal}a_{i} + X_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} > 0 \mid b \right) \\
&= \mathbb{P}\left( X_{ij}^{\intercal}\hat{\gamma}^{(0)}  + \frac{X_{B, ij}^{\intercal}b_{j}}{\sqrt{ 1 + v } } >\frac{X_{A, ij}^{\intercal}a_{i} + \varepsilon_{ij}}{\sqrt{ 1 + v }} |b\right) \\
&\approx \mathbb{P}\left( X_{ij}^{\intercal}\hat{\gamma}^{(0)} + \frac{X_{B, ij}^{\intercal}b_{j}}{\sqrt{ 1 + v }}  > \frac{Z\sqrt{ \text{tr}(\Sigma_{A}S_{A}) + 1 }}{\sqrt{ 1 + v }} \right) \\
&= \Phi\left( X_{ij}^{\intercal}\hat{\gamma}^{(0)}_{B} + \frac{X_{B, ij}^{\intercal}b_{j}}{\sqrt{ 1 + v_{A} }} \right)\end{align}$$
for
$$\begin{align} \hat{\gamma}_{B}^{(0)} &= \hat{\gamma}^{(0)}\sqrt{ \frac{1 + v_{A} + v_{B}}{1 + v_{A}}}  \\
&= \hat{\gamma}^{(0)} \sqrt{ 1 + \frac{v_{B}}{1 + v_{A}} }.\end{align}$$
So now I know $\hat{\gamma}^{(0)}_{B}$. This means I can solve for $b_{j}$ by fitting naive probit with known offset $X_{ij}^{\intercal}\hat{\gamma}_{B}^{(0)}$ and correcting by multiplying $\sqrt{ 1 + v_{A} }$. I inverse weight (or not) and get a covariance estimate via $S_{B} \propto \sum_{j} b_{j}b_{j}^{\intercal}$. Clearly I can do the same for $a_{i}$. This nets me an estimate of $\hat{\Sigma}_{A}^{(0)}$ and $\hat{\Sigma}_{B}^{(0)}$. 

**(B - Something Termwise Because Low Rank)** Above is fine if $p_{B}$ is decently small, things don't blow up. Maybe that's not the case, or I just care more about avoiding low rank behavior. I don't think this is the best option, but it's a good start on the correlated case. In this regime, perhaps I continue to use something more termwise and integrate across. Then I analogize cross terms in the same way. #STUB


**(C - Regularization)** Something something only learn the diagonal. I think given that the low-rank fit works with naive probit, we should also be fine with **A**. I have something explicit to write up at this point. 

4. Thus begins the iteration. I have access to $\hat{\Sigma}_{A}^{(t)}$ and $\hat{\Sigma}_{B}^{(t)}$. $\hat{\beta}^{(t + 1)}$ is then recovered naturally;
$$\begin{align} \mathbb{P}(Y_{ij} = 1) &= \mathbb{P}\left( X_{ij}^{\intercal}\beta + X_{A, ij}^{\intercal}a_{i} + X_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} > 0\right)  \\
&= \Phi\left( \frac{X_{ij}^{\intercal}\beta}{\sqrt{ 1 + X_{A, ij}^{\intercal}\Sigma_{A} X_{A, ij} + X_{B, ij}^{\intercal}\Sigma_{B} X_{B, ij} }} \right)\end{align}$$
for which we can explicitly scale $X_{ij}$ by the now-estimated denominator to recover the $\beta$ estimate.  

5. Now, how do we recover $\Sigma$ estimates given $\beta$? I just have more specific offsets. I run naive probit on the appropriately scaled $\beta$ term that scales (for $b_{j}$) with $\hat{\Sigma}_{A}$, and then do the same with $\hat{\Sigma}_{B}$. Iterate, done. 

*Really need to figure out some worst case behavior, but to start with, maybe the correlated case first. This should force some pairwise analysis, maybe. very obviously cheap though, but really interested in where this fails.*


### Iteration Step 
We have as an initialization $\hat{\Sigma}_{A}$, $\hat{\Sigma}_{B}$. Then we can rescale $X$ immediately without resorting to global; 

$$\begin{align} \mathbb{P}(Y_{ij} = 1) &= \mathbb{P}\left( X_{ij}^{\intercal}\beta + X_{A,ij}^{\intercal}a_{i} + X_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} > 0 \right) \\
&\approx \Phi\left( \frac{X_{ij}^{\intercal}\beta}{\sqrt{ 1 + X_{A, ij}^{\intercal}\hat{\Sigma}_{A}X_{A, ij} + X_{B, ij}^{\intercal}\hat{\Sigma}_{B}X_{B, ij} }} \right); \end{align}$$
so let 
$$\begin{align} V_{ij} = \frac{X_{ij}}{\sqrt{ 1 + X_{A, ij}^{\intercal}\hat{\Sigma}_{A}X_{A, ij} + X_{B, ij}^{\intercal}\hat{\Sigma}_{B}X_{B, ij} }} \end{align}$$
for which I can now fit probit directly and recover $\beta$. 

Now let us go from $\hat{\beta}$ to approximation of $\hat{\Sigma}_{B}$; note that we will use $\hat{\Sigma}_{A}$, and that the update there will be analogous. What we will do is fit per $j$ (when $N_{\bullet j}\geq n_{\text{min}}$ some minimum number of observations, as needed) a $b_{j}$ fit. This can be done in the following manner. We can do 

$$\begin{align} \mathbb{P}(Y_{ij} = 1 \mid b_{j}) &= \mathbb{P}\left( X_{ij}^{\intercal}\beta + X_{A, ij}^{\intercal}a_{i} + X_{B, ij}^{\intercal}b_{j} + \varepsilon_{ij} > 0 \right) \\
&= \Phi\left( \frac{X_{ij}^{\intercal}\beta + X_{B, ij}^{\intercal}b_{j}}{\sqrt{ 1 + X_{A, ij}^{\intercal}\hat{\Sigma}_{A}X_{A, ij} }} \right). \end{align}$$
Note by the approximation of $\hat{\beta}$ that $X_{ij}^{\intercal}\hat{\beta}$ is already known. The denominator is also fully known. Thus we fit a glm with offset $X_{ij}^{\intercal}\beta / \sqrt{ 1 + X_{A, ij}^{\intercal}\hat{\Sigma}_{A}X_{A, ij} }$ and input data $X_{B, ij} / \sqrt{ 1 + X_{A, ij}^{\intercal}\hat{\Sigma}_{A}X_{A, ij} }$. This should recover a shared $b_{j}$ estimate in each column (satisfying $N_{\bullet j} \geq n_{\text{min}}$). averaging over the observed $b_{j}b_{j}^{\intercal}$ estimates should be a reasonable estimate of $\Sigma_{B}$. 

#### Likelihood Version - Diagonal Term
I think the above fails predominantly because of perfectly separating hyperplanes. But then I lose a lot of data, so that's bad too. The solution is to do one at a time and then pairwise, then. What does that look like?

Generally, it seems like the initialization is reasonably stable. So we'll use that as a starting point. My goal is to solve for, say, $b_{j}[1]$ the first component. Then
$$\begin{align} \mathbb{P}(Y_{ij} = 1 \mid b_{j}[1]) &= \mathbb{P}(W_{ij} > 0 \mid b_{j}[1]) \\
&= \mathbb{P}\left( X_{ij}^{\intercal}\beta + X_{A, ij}^{\intercal}a_{i} + X_{B, ij}^{\intercal}b_{j}  + \varepsilon_{ij} > 0 \mid b_{j} [1]\right) \\
&= \mathbb{P}\left( X_{ij}^{\intercal} \beta + X_{A, ij}^{\intercal}a_{i} + X_{B, ij}[1]^{\intercal}b_{j}[1] + X_{B ,ij}[-1]^{\intercal}b_{j} [-1] + \varepsilon_{ij} > 0 \mid b_{j} [1] \right) \\
&= \Phi\left( \frac{X_{ij}^{\intercal}\beta + X_{B, ij}[1]^{\intercal}b_{j}[1] + X_{B, ij}[-1]^{\intercal}\Sigma_{B, [1, -1]}\sigma^{-2}_{B 1}b_{j}[1]}{\sqrt{ 1 + X_{A, ij}^{\intercal}\hat{\Sigma}_{A}X_{A, ij} + \text{Var}\left( X_{B, ij} [-1]^{\intercal}b_{j}[-1] \mid b_{j} [1] \right)  }} \right)  \end{align}$$

for which
$$\begin{align} \text{Var}\left( X_{B, ij}[-1]^{\intercal}b_{j}[-1]\mid b_{j}[1] \right) &= X_{B, ij}[-1]^{\intercal}\text{Var}(b_{j}[-1] \mid b_{j} [1]) X_{B, ij}   \\
&= X_{B, ij}[-1]^{\intercal}\left( \Sigma_{B, -1} - \sigma^{-2}_{B, 1}\Sigma_{B, 1, -1} \Sigma_{B, 1, -1}^{\intercal} \right).\end{align}$$
A starting point for some algorithm that might work - maybe I only update a term at a time, in which case I assume I have $\hat{\Sigma}_{B, 1,-1}$ and $\hat{\Sigma}_{B, -1}$ available to me. In that case, my likelihood maximization is over 

$$\begin{align} \frac{1}{\sigma_{B_{1}}^{-C}}\prod_{j = 1}^{C} \int \left[ \prod_{(i, j) \in \mathcal{S}_{i}} \Phi\left( \frac{w_{ij}\left( X_{ij}^{\intercal}\beta   + \left\{  X_{B, ij}[1] + X_{B, ij}[-1]^{\intercal}\Sigma_{B, [1, -1]}\sigma^{-2}_{B 1} \right\}b_{j}[1] \right)}{\sqrt{ 1 + X_{A, ij}^{\intercal}\Sigma_{A} X_{A, ij} + X_{B, ij}[-1]^{\intercal} \left\{ \Sigma_{B, -1} - \sigma^{-2}_{B 1} \Sigma_{B, [1, -1]}\Sigma_{B, [1, -1]}^{\intercal} \right\}X_{B, ij}[-1] }} \right) \right] \, \varphi\left( \frac{b_{j}[1]}{\sigma_{B_{1}} } \right) d b_{j}.   \end{align}$$
##### Posterior Mode for AGH

We need to adjust [[Gauss-Hermite Quadrature]] starting point by posterior for $b_{j}[1]$. In particular, we want the posterior mode of $b_{j}[1] \mid w_{ij}$, where this operation is carried out in each column. So here I'm just minimizing the inside likelihood. 

I think this will be an ugly component-wise bash, but hopefully there's some immediate schur complementation. Okay, let's start with just differentiation of the log likelihood of the inner sum. This is sufficient. Rewrite with respect to unit $u_{i}$; 

$$\begin{align} \mathcal{L}_{j} &:=\log \prod_{(i, j) \in \mathcal{S}_{i}} \Phi\left( \frac{w_{ij}\left( X_{ij}^{\intercal}\beta   + \left\{  X_{B, ij}[1] + X_{B, ij}[-1]^{\intercal}\Sigma_{B, [1, -1]}\sigma^{-2}_{B 1} \right\}b_{j}[1] \right)}{\sqrt{ 1 + X_{A, ij}^{\intercal}\Sigma_{A} X_{A, ij} + X_{B, ij}[-1]^{\intercal} \left\{ \Sigma_{B, -1} - \sigma^{-2}_{B 1} \Sigma_{B, [1, -1]}\Sigma_{B, [1, -1]}^{\intercal} \right\}X_{B, ij}[-1] }} \right)  \\
&=: \sum_{(i, j) \in \mathcal{S}_{i}} \log \Phi\left( \frac{w_{ij}\left( \eta_{ij} + X_{B, ij}[-1]^{\intercal}\Sigma_{B, [1, -1]}\sigma_{B 1}^{-1} \right)u_{j}}{\sqrt{ 1 + v_{A, ij} + v_{B, ij}^{(-1)} }} \right) \\
&=: \sum_{(i, j) \in \mathcal{S}_{i}} \log \Phi\left( \frac{w_{ij}(\eta_{ij} + \psi_{ij}^{(-1)}u_{j})}{\sqrt{ 1 + v_{A, ij} + v_{B, ij}^{(-1)} }} \right);\end{align}$$
In turn, calling the inner term $\text{arg}_{\text{ij}}$, 
$$\begin{align} g:= \frac{ \partial  }{ \partial u_{j} } \mathcal{L}_{j} = -u_{j} + \sum_{(i, j) \in \mathcal{S}_{i}}  \frac{\varphi(\text{arg}_{ij})}{\Phi(\text{arg}_{ij})}\cdot \frac{w_{ij}\psi_{ij}^{(-1)}}{\sqrt{ 1 + v_{A, ij} + v_{B, ij}^{(-1)} }}, \end{align}$$
$$\begin{align} H = 1 - \sum_{(i, j) \in \mathcal{S}_{i}} \frac{\varphi(\text{arg}_{ij})}{\Phi^{2}[\text{arg}_{ij}]} \frac{[\psi_{ij}^{(-1)}]^{2}}{1 + v_{A, ij} + v_{B, ij}^{(-1)}}\left\{ \varphi(\text{arg}_{ij}) + \text{arg}_{ij} \cdot \Phi(\text{arg}_{ij}) \right\}.  \end{align}$$
As a per-term update, this should be sufficient for optimization. Might need to borrow some theory from alternating mazimization, EM, Gibbs sampling for justification?

> [!faq]- Chat Rewrite to Check
> ![[Chat Rewrite for Consistent Notation]]

#### Likelihood Version - Cross Term
First pass will get us access to the diagonal. Once we have the diagonal, the natural instinct is to go two-at-a-time to reconstitute the crossterms.

Let's keep going with bad notation. I'm just going to give new random effect coefficients; we'll let $c$ and $d$ take the place of the natural block matrix that comes out of this process, so that ("shuffled") $b_{j} = \left( c_{j}^{\intercal}, d_{j}^{\intercal} \right)^{\intercal}$ and we have ("shuffled") block covariance matrix
$$\begin{align*} \Sigma_{B} = \begin{pmatrix}
\Sigma_{C} & \Sigma_{CD} \\
\Sigma_{DC} & \Sigma_{D}
\end{pmatrix} \end{align*}$$
For $\Sigma_{CD} = \Sigma_{DC}^{\intercal}$, $\Sigma_{C} \in \mathbb{R}^{2\times 2}$, $\Sigma_{D} \in \mathbb{R}^{(p_{B} - 2) \times (p_{B} - 2)}$, and 
$$\begin{align*} \Sigma_{C} = \begin{pmatrix}
\sigma^{2}_{C 1} & \sigma_{C 12} \\
\sigma_{C 12} & \sigma^{2}_{C 2}
\end{pmatrix} \end{align*}$$
for which $\sigma_{C 12}$ is functionally our renaming of the crossterm between some chosen pair of the $p_{B}$ components. Then by standard Schur complementation, we arrive at
$$\begin{align*} \mathbb{P}(Y_{ij} = y_{ij} \mid c) &= \mathbb{P}\left( X_{ij}^{\intercal}\beta + X_{A, ij}^{\intercal}a_{i} + X_{C, ij}^{\intercal}c_{j} + X_{D, ij}^{\intercal}d_{j} + \varepsilon > 0 \mid c \right) \\
&= \Phi \left\{  \frac{X_{ij}^{\intercal}\beta + X_{C, ij}^{\intercal}c_{j} + X_{D, ij}^{\intercal}\Sigma_{DC}\Sigma_{C}^{-1} c_{j}}{\sqrt{ 1 + X_{A, ij}^{\intercal}\Sigma_{A}X_{A, ij} + X_{D, ij}^{\intercal}\left\{ \Sigma_{D} - \Sigma_{DC} \Sigma_{C}^{-1} \Sigma_{CD} \right\} X_{D, ij} }}  \right\}, 
\end{align*}$$
where $c_{j}$ is bivariate normal with covariance $\Sigma_{C}$. We maintain a concept of row and column likelihood, and our single-update scheme means that it is clearly dependent on only $\sigma_{C 12}$ since everything is known. 
##### Posterior Mode Search for AGH
The posterior mode derivation is a combined analogue of [[V2 Multivariate Response for Crossed Random Effects]] and the above main term cases. With [[Chat Random Slopes Cross Term Bash|some chat help]], we get

Let  
$$M := \Sigma_C^{-1/2}, \qquad c_j = M u_j.$$

Define  
$$\eta_{ij} := X_{ij}^\top \beta, \,\, \, \psi_{ij} := M^\top (X_{C,ij} + \Sigma_C^{-1}\Sigma_{CD} X_{D,ij}),$$
$$v_{A,ij} := X_{A,ij}^\top \Sigma_A X_{A,ij}, \, \, \, \, v_{D,ij}^{(\text{cond})} := X_{D,ij}^\top\big(\Sigma_D - \Sigma_{DC}\Sigma_C^{-1}\Sigma_{CD}\big)X_{D,ij},$$
$$S_{ij} := 1 + v_{A,ij} + v_{D,ij}^{(\text{cond})}, \,\,\,\,
\mathrm{arg}_{ij}
=
\frac{ w_{ij}\big(\eta_{ij} + \psi_{ij}^\top u_j\big) }
     { \sqrt{S_{ij}} }.
$$

Then the [[The Standard Bashes]] provide us with 
$$
\nabla_{u_j}\ell(u_j)
=
-\,u_j
+
\sum_{(i,j)\in\mathcal S_j}
\frac{\varphi(\mathrm{arg}_{ij})}{\Phi(\mathrm{arg}_{ij})}\,
\frac{ w_{ij} }{ \sqrt{S_{ij}} }\,
\psi_{ij},
$$
$$
\nabla^2_{u_j}\ell(u_j)
=
- I
-
\sum_{(i,j)\in\mathcal S_j}
\frac{
\varphi(\mathrm{arg}_{ij})\big( \varphi(\mathrm{arg}_{ij}) + \mathrm{arg}_{ij}\,\Phi(\mathrm{arg}_{ij}) \big)
}{
\Phi(\mathrm{arg}_{ij})^2
}
\cdot
\frac{ w_{ij}^2 }{ S_{ij} }
\cdot
\psi_{ij}\psi_{ij}^\top.
$$


## Working on the case without independence.

~~The idea should be the same, but we'll have earlier scaling because of $\Gamma$ relations. Note (4) and (5) of the above should remain completely unchanged, as we return to the fixed-$x$ setting in that regime. ~~
$$\begin{align} \Gamma = \begin{pmatrix}
\Gamma_{X} & \Gamma_{XA} &\Gamma_{XB} \\
\Gamma_{AX} & \Gamma_{A} & \Gamma_{AB} \\
\Gamma_{BX} & \Gamma_{BA} & \Gamma_{B}
\end{pmatrix} \end{align}$$
is immediately estimable,%%  and further denote by $\Gamma_{R}$, $\Gamma_{XR}$, $\Gamma_{RX} \equiv \Gamma_{XR}^{\intercal}$ the block matrix that shoves $\Gamma_{A}$ and $\Gamma_{B}$ together.  %%

Oof gaussian requirement gets much stronger. We'll try with and without it. 

With it, 











