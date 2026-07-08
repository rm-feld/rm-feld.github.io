---
modified: 2026-04-15T12:11:52-07:00
created: 2026-03-31T19:54:46-07:00
---

Maximum score estimation seems to be fairly confined to the econometrics literature, where it has evolved into usage for explicitly pairwise regimes. We outline some results and some potential opportunities. 
# Setup and Standard Approach

## Defining the Maximum Score Estimator
We are interested in the binary choice model, given by the following. 

![[Inference for Binary Choice Models]]

Notice we are allowed heteroskedasticity in the $U_{i}$'s in this regime. 

We give a few intermediate assumptions. 

![[Standard Assumptions for Maximum Score Estimation]]

[[@manskiMaximumScoreEstimation1975]] introduces the maximum score estimator. 

![[Maximum Score Estimator]]
## Asymptotics

### Consistency
![[Consistency of the Maximum Score Estimator]]

### Rate Results
![[Exploring Rate Properties of the Maximum Score Estimator]]

# "Crossed" Usage with the Matching Problem
The **(many-to-many) Matching Problem** seems to echo *some* of the setup of the $(K = 2)$ binary [[K-Crossed Random Effects Model|crossed random effects model]] where we "end up observing all pairs" (in the sense that we backfill zeros when a match is not observed). 

![[Many-to-Many Matching Problem]]

Towards this goal, [[@foxToolkitMatchingMaximum]] defines an objective which we simplify in the (linear response, one-market) case with the following logic. 

Let $x_{ij}$ be derivable as a function of $(i, j)$, and let $\mathcal{X}= \left\{ (i, j) \mid y_{ij} = 1 \right\}$ be the observed matches. The idea is that, because acceptance probability is supposed to agree in rank with the fixed predictor, we should be awarding choices of $\beta$ for which the "fixed-predictor" payout under the true observed matches is higher than some other candidate match. Let 
$$\begin{align*} \mathcal{X}_{i}^{C} = \left\{ j \in J: y_{ij} \neq 1 \right\}, \qquad \mathcal{X}_{i} = \left\{ j \in J: y_{ij} = 1 \right\}  . \end{align*}$$
and for ease of notation assume that all $i \in I$ participate in the market (every product $i$ is bought buy some $j$) so that $\left\{ \mathcal{X}_{i}^{C} \right\}_{i \in I}$ forms a partition over all counterfactual purchase events, and make the analogous statement for the natural $\mathcal{X}_{j}, \mathcal{X}_{j}^{C}$. The objective in this case can be written as 
$$\begin{align*} Q(\beta) = \sum_{i \in I} \sum_{j \in \mathcal{X}_{i}} \sum_{j' \in \mathcal{X}_{i}^{C}} \mathbf{1}\left[x_{ij}^{\intercal}\beta > x_{ij'}^{\intercal}\beta \right] + \sum_{j \in J} \sum_{i \in \mathcal{X}_{j}}\sum_{i' \in \mathcal{X}_{j}^{C}} \mathbf{1}\left[x_{ij}^{\intercal}\beta > x_{i'j}^{\intercal}\beta \right]  \end{align*}$$
*(though I think I may be introducing some double counting to be subtracted out here).*

# Extensions to Maximum Score
## Smoothed Maximum Score Estimation
If the cube-root asymptotics are not preferred, there exists a smoothed extension for which (almost) $\sqrt{ n }$-asymptotics are recovered. This is introduced by [[@horowitzSmoothedMaximumScore1992]]. The extension has natural motivation. 

![[Smoothed Maximum Score Estimator]]

Because of ambiguity in relative scale of $\sigma_{N}$ and $\beta$, [[@horowitzSmoothedMaximumScore1992]] makes explicit the implicit normalization statement of [[@manskiSemiparametricAnalysisDiscrete1985]].

![[Consistency of the Smoothed Maximum Score Estimator]]

Asymptotic normality in this regime is difficult and requires more fine-grained control. [[@horowitzSmoothedMaximumScore1992]] builds on top of the consistency assumptions. 

![[Asymptotic Normality Assumptions for the Smoothed Maximum Score Estimator]]

Under the above regime, the limiting distribution of $\tilde{\beta} - \tilde{\beta}_{0}$ which is normal. Following some standard patterns in [[Local Asymptotic Normality|LAN]] behavior, decay of $N\sigma_{N}^{2h +1}$ guides asymptotics. 

![[Limiting Distribution of the Smoothed Maximum Score Estimator]]

[[@horowitzSmoothedMaximumScore1992]] emphasizes the implication of the above that the fastes possible rate of convergence under this non-parametric regime for $\tilde{b}_{N}$ is $N^{-h / (2h + 1)}$. The paper gives implementation details on the estimation of $A$, $D$ and $Q$ in a consistent manner in **Theorem 3**. 

# (Some) Potential Opportunities

Many of the approaches we have considered seem to support an iterative or otherwise alternating scheme in which a choice of direction makes estimating variance feasible, or where variance information supports a better estimate of $\beta$. In general, the $\beta$ direction information seems to be the more difficult of the two - if we can coerce an all likelihood statement from the given, **we may be able to at the very least warm start the iterative method with a consistent estimator**. Since the extension results have generally yielded non-concave results in maximization over $\sigma$, only learning $\beta$ up to unit value may not be particularly different from our current treatments under some scale information. 

We also have opportunties for heteroskedastic or non-normal random effects, as long as the median condition is satisfied. These differences can be incidental from an underlying normal (eg. random slopes) or more explicitly through the choice of a different link function. 

Random slopes is perhaps the immediate one that comes to mind…

## Random Slopes 
If we are not in the crossed regime, then 

$$\begin{align*} Y_{i} = \mathbf{1}\left[x_{i}^{\intercal}\beta + x_{i, A}^{\intercal}a_{i} + \varepsilon_{i} > 0\right]  \end{align*}$$
for $\varepsilon_{i} \sim \mathcal{N}(0, \sigma^{2}_{E})$, $a_{i} \sim \mathcal{N}(0, \Sigma_{A})$ has %% if $x_{i}$ has $x_{i, A}$ as components %%
$$\begin{align*} u_{i} = \mathcal{N}\left( 0, x_{i, A}^{\intercal}\Sigma_{A} x_{i, A} + \varepsilon_{i} \right) \end{align*}$$
for which, since the **normal median coincides with its mean, satisfies the [[Median Independence|median independence]] condition**. Thus the non-parametric [[All Likelihood|all likelihood]] in this regime may yield a consistency result if we can follow the subset or maximum variance arguments of the composite likelihood modification. **When $\beta$ direction is recovered, row likelihood and column likelihood analogues can be calculated, and we can warmstart the current iterative approach to the solve.** 

## Coercing a Crossed Maximum Score Estimator
The pairwise extensions of [[@foxToolkitMatchingMaximum]] and the generality of the median-independence of the [[Maximum Score Estimator|maximum score estimator]] makes the formulation of a formal crossed structure intriguing. Indeed, the pairwise maximum score estimator stated in generality in [[@foxToolkitMatchingMaximum]] allows for nonlinear functions of $(x_{ij}, i , j)$ (focused on a price interpretation) so some sort of statement may be available to us. 

**[[@foxEstimatingMatchingGames2018]] extends analysis of the pairwise extension with a particular eye for computational/[[Curse of Dimensionality|curse of dimensionality]] issues that emerge in the limit of agents**. Though its assumptions (particularly **Assumption 1**, for which Fox stresses that the evaluation may not encode unobserved components) seem to preclude modeling with crossed random effects, examples are in regimes where the crossed model may be more than reasonable, and **so at the very least we may be able to benchmark/compare behavior**. As an example of potentially comparable structure (and pitfalls thereof), I give in full **Example 2** of the paper which is of most immediate interest. 

> [!quote] **Example 2, [[@foxEstimatingMatchingGames2018]]**
> 
> Say an agent is defined to be either a buyer or a seller ex ante, as in the empirical work on the car parts industry later in this paper. Then this is an example of two-sided many-to-many matching. Define $\pi^{j}(\Phi, \Psi)$ to be $-\infty$ if an agent whose observable type $j \in J$ corresponds to a buyer conducts trades as a seller, and similarly for a seller type. A trade $\omega$ specifies the buyer observable type $b(\omega)$ and the seller observable type $s(\omega)$ in addition to other possible attributes, such as the quantity and quality of goods to deliver (if quantity and quality are specified on a finite grid and observable in the data for actual matches). A buyer of full type $i$ or $(j, k)$ then has profits of  
> 
> $$\begin{align*} \pi^{j}(\Phi) + \varepsilon_{\Phi}^{k} + \sum_{w \in \Phi} p_{\omega} \end{align*}$$
> As in marriage, the buyer’s unobservable valuation component $\varepsilon_{\Phi}^{k}$ depends on the trades and hence on the observable types $s(\omega) \in J$ of the seller partners. Similarly, a seller full type $i$ or $(j, k)$ has profits of 
> $$\begin{align*} \pi^{j}(\Psi) + \varepsilon_{\Psi}^{k} + \sum_{\omega \in \Psi} p_{\omega}. \end{align*}$$
> Recall that a competitive equilibrium exists without ruling out empirically relevant cases, such as a function $\pi^{j}(\Phi)$ exhibiting complementarities across multiple trades involving the same agent (e.g., Hatfield and Milgrom (2005)). Complementarities across multiple trades involving the same agent are vital to the empirical application to the car parts industry. 
> 
> An agent’s valuation is directly a function of only the trades where that particular agent is a buyer or a seller. The model assumes away externalities: valuations defined over trades to which the agent does not participate. Competition for trades certainly affects the price vector for trades, $p_{\Omega}$, although such competition for trades is not a valuation defined over trades to which the agent does not participate. True externalities could be important in applications; for example, if buyers are retailers and sellers are wholesalers, and buyers compete with each other for retail customers (outside of the matching game) after matching to sellers. Baccara, Imrohoroglu, Wilson and Yariv (2012) use the matching maximum score estimator introduced in this paper to estimate a matching game with externalities.