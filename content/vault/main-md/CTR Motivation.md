---
modified: 2026-07-13T11:24:06-07:00
created: 2026-02-14T18:37:13-08:00
---

# CTR 
We interrogate data structures that emerge in the case of 3 crossed random effects. Consider the domain of online advertising. Here, we let $(i, j, k)$ encode the cross $\text{user }\times \text{ site } \times \text{ advertiser}$. $Z_{ijk} = 1$ indicates that user $i$ was served advertisement $k$ on site $j$. $Y_{ijk} = 1 \mid Z_{ijk} = 1$ corresponds to the event that user $i$ clicked on the served advertisement. We note possible interpretations for $a_{i}$, $b_{j}$, and $c_{k}$ in this regime as, in order, a user's inclination to click on advertisements in general, a site's "trustworthiness" (the general userbase's belief that the site would not promote malware, e.g.), and the "clickability" of the advertisement %% (perhaps some measure of potential virality)%%. 

In considering the case of targeted advertising, it is clear that observation structures can be of great inconvenience to the proposed method. We start with a toy example. 

**(Perfect Diagonal Targeting)** Regardless of the visited site, user $i$ only ever observes advertisements from $R_{k}(i)$ advertisers. 

# Analogizing Consistency Statements
%% ## @lumleyAsymptoticsMarginalGeneralized Basic Alignment

First, we consider aligning with @lumleyAsymptoticsMarginalGeneralized on their definition of sparse correlation. Denote by $\mathcal{S}_{(i, j, k)}$ the set of (observed) indices that coincide with at least one coordinate of $(i, j, k)$. For $m$ the size of the largest possible set of (strictly) independent observations (in our setting, this can generally assumed to be $N^{\min \kappa}$)  ie. **TODO I THINK SHOULD BE A MAX INTERPRETATION BUT IF NOT PULL FROM SUPP**  **Sparse Correlation** is defined by 
$$\begin{aligned} \max_{(i, j, k) \in \mathcal{S}} |S_{(i, j, k)}| m = O(N).   \end{aligned}$$
Conservatively, we can write
$$\begin{aligned} \max_{(i, j, k) \in \mathcal{S}} |S_{(i, j, k)}| &\leq \max_{(i, j, k) \in \mathcal{S}} \left\{ N_{i \bullet \bullet } + N_{\bullet  j \bullet } + N_{\bullet  \bullet  k} \right\}  \leq \max_{i}N_{i \bullet  \bullet } + \max_{j} N_{\bullet  j \bullet } + \max_{k} N_{\bullet \bullet  k}  \\ &= O\left( \max\left\{ \max_{i} N_{i \bullet \bullet }, \max_{j} N_{\bullet j \bullet }, \max_{k} N_{\bullet  \bullet  k} \right\}  \right). \end{aligned}$$
I note that in the unbalanced case, I'd expect upper bounding by the sum to be fairly tight; if we extended the big row example to cross a big column and a big slice, then that the big row and the big column intersect would not be surprising. Since this is an order constraint, though, I don't expect the pairwise relationships to matter too much. 

Without loss of generality, let $\kappa_{1}$ be the smallest power. Then by standard Pigeonhole Principle, $m \leq N^{\kappa_{1}}$  (and in fact we generally believe $m = \Omega(N^{\kappa_{1}})$ under light balance conditions #TODO). A heuristic under balance is that $\max_{i} N_{i \bullet \bullet}$ will be the largest of the three, as (1) the total number of possible levels $N^{\kappa_{1} + \kappa_{2}}$ is larger and (2) because there are less levels of $i$ than $j$ or $k$, counts should be comparatively concentrated. Regardless, the sparse correlation condition is satisfied when 
$$\begin{aligned} \max\left\{ \max_{i} N_{i \bullet  \bullet }, \max_{j} N_{\bullet  j \bullet }, \max_{k} N_{\bullet  \bullet  k} \right\} = O(N^{1 - \kappa_{1}}); \end{aligned}$$
That's stronger than current S1.1, so perhaps being too strict in our starting point.  %%




# IPW Consistency Statements 
Force a CLT on (2) of S1.1
## Generic 2
Normalize $w_{ij} \leq 1$.
$$\begin{aligned} \mathbb{V}[\ell_{\text{all}}(\gamma)] &\leq \frac{B^{2}}{N^{2}} \sum_{ij} \sum_{rs} w_{ij}w_{rs}Z_{ij}Z_{rs} (\mathbf{1}\left[i = r \right]  + \mathbf{1}\left[j = s \right] - \mathbf{1}\left[i = r \right]\mathbf{1}\left[j = s \right]   ) \\ &= \frac{B^{2}}{N^{2}} \left( \sum_{ijs} w_{ij}w_{is} Z_{ij}Z_{is} + \sum_{ijr} w_{ij}w_{rj} Z_{ij}Z_{rj} - \sum_{ij}w_{ij}^{2}  \right) \\ &\leq \frac{B^{2}}{N^{2}} \left( \sum_{ijs} w_{ij}w_{is} Z_{ij}Z_{is} + \sum_{ijr} w_{ij}w_{rj} Z_{ij}Z_{rj} \right) \end{aligned}$$
## Row Weighting
### Gamma Consistency
#### Variance Vanishes
Normalize to keep the sum of the weights at the same scale as $N$. Let $w_{ij} \propto 1 / N_{i}$, $\sum_{i j} w_{ij}Z_{ij} = N$ so that $w_{ij} = \frac{N}{N_{i\bullet}}\left[ \sum_{ij} Z_{ij} / N_{i\bullet} \right]^{-1} = N^{1 - \kappa_{1}} / N_{i \bullet}$. Note we recover $w_{ij} \equiv 1$ under the case that $i$ and $j$ are only ever seen once (for all data).

$$\begin{aligned} \mathbb{V}[\ell_{\text{all}}(\gamma)] & \leq \frac{B^{2}}{N^{2}}\left( \sum_{ijs}  \frac{N^{-2\kappa_{1}} N^{2}}{N^{2}_{i \bullet }} Z_{ij}Z_{is} + \sum_{ijr} \frac{N^{2}N^{-2\kappa_{1}}}{N_{i \bullet  } N_{r \bullet }} Z_{ij}Z_{rj} \right) \\ &= \frac{B^{2}}{N^{2\kappa_{1}}} \left( \sum_{ijs} \frac{1}{N_{i \bullet }^{2}} Z_{ij}Z_{is} + \sum_{ijr}  \frac{1}{N_{i \bullet } N_{r \bullet }} Z_{ij}Z_{rj}\right) \\ &\leq \frac{B^{2}}{N^{2\kappa_{1}}} \left( N^{\kappa_{1}} + \sum_{ir} \frac{1}{N_{i \bullet }} \right) \\ &= \frac{B^{2}}{N^{2 \kappa_{1}}}\left( N^{\kappa_{1}} + N^{\kappa_{1}} \sum_{i} \frac{1}{N_{i \bullet }} \right) \\ &= \frac{B^{2}}{N^{\kappa_{1}}} + N^{\kappa_{1}} \sum_{i} \frac{1}{N_{i \bullet }}. \end{aligned}$$
A sufficient (but not necessary) condition would be to require $\sum_{i} N_{i \bullet}^{-1} = o(N^{\kappa_{1}})$ - Notice then though that the independent observation weights fail, since $\sum_{i} N_{i\bullet}^{-1}.  \sum_{i} 1 = N^{\kappa_{1}}$. So perhaps the simplification away from $Z_{ij}Z_{rj}$ is less dramatic. Is there a nicer story to write for the condition 
$$\begin{aligned} \sum_{ijr} \frac{1}{N_{i \bullet }N_{r\bullet }} Z_{ij}Z_{rj} = o(N^{2\kappa_{1}})? \end{aligned}$$
To sanity check, note that, since $N_{i\bullet}^{-1}N_{r\bullet}^{-1} \leq 1$, the column decay condition $\varepsilon_{C} \to 0$ is a sufficient condition. But information on the cross would be nice. Intuitively, for fixed $i$, $r$, the sum over $j$ collects the number of observations with shared $j$; 
$$\begin{aligned} \sum_{ijr} \frac{1}{N_{i \bullet } N_{r \bullet }}Z_{ij} Z_{rj} = \sum_{ir} \frac{|T_{i} \cap T_{r}|}{N_{i \bullet }N_{r\bullet }}. \end{aligned}$$
Surely we should have failure in the big column case. Let us assume that $N_{i \bullet}$ are otherwise perfectly balanced, so that $N_{i\bullet}N_{r\bullet} =N^{2} / N^{2\kappa}$. Then since we generally assume $\max_{j}N_{\bullet j} = \Omega(N^{\kappa_{1}})$ for the big column, ie. that basically every row sees as observation from $j^{*}$, 
$$\begin{aligned} \sum_{ir} \frac{|T_{i} \cap T_{r}|}{N_{i \bullet }N_{r\bullet }} \approx \frac{N^{2\kappa}}{N^{2}} N^{2\kappa} \end{aligned}$$
Not necessarily decaying. 
#### Convergence to a Concave Function
Note 
$$\begin{aligned} \frac{\ell_{\text{all}}(\gamma)}{N} \to  \frac{\mathbb{E}[\ell_{\text{all}}]}{N} &= \frac{1}{N^{\kappa_{1}}} \sum_{ij} \frac{1}{N_{i\bullet }} Z_{ij} \left[ \Phi\left( x_{ij}^{\intercal}\gamma_{0} \right) \log \Phi\left( x_{ij}^{\intercal}\gamma \right) + \Phi\left( -x_{ij}^{\intercal}\gamma_{0} \right)\log \Phi\left( -x_{ij}^{\intercal}\gamma \right) \right] \\ &=: g(\gamma) \end{aligned}$$
is clearly still a concave function, as is $\ell_{\text{all}}(\gamma) / N$. Further, 

$$\begin{aligned} \frac{ \partial g(\gamma_{0}) }{ \partial \gamma } = \frac{1}{N^{\kappa_{1}}} \sum_{ij} \frac{1}{N_{i \bullet }} Z_{ij}[x_{ij} - x_{ij}] = 0, \end{aligned}$$
so $\gamma_{0}$ is a maximizer of $g$. Thus it suffices to ensure $g$ is strictly concave; writing 
$$\begin{aligned} \frac{ \partial^{2} g(\gamma_{0}) }{ \partial \gamma \partial \gamma ^{\intercal} } = -\frac{1}{N^{\kappa_{1}}} \sum_{ij} \frac{1}{N_{i \bullet }} Z_{ij} \frac{\varphi \left( x_{ij}^{\intercal}\gamma_{0} \right)^{2}}{\Phi\left( x_{ij}^{\intercal}\gamma_{0} \right) \Phi\left( -x_{ij}^{\intercal}\gamma_{0} \right)}x_{ij}x_{ij}^{\intercal},  \end{aligned}$$
we recover the analogous Hessian except for the weighting; we can directly account for it with the below. 

Adjusting (S1.1) condition 2 with 

2. $N^{-\kappa_{1}} \sum_{ij} Z_{ij} N_{i\bullet}^{-1} x_{ij}x_{ij}^{\intercal} \to V$, where $V$ is positive definite,

Satisfies the desired properties. This should be a weaker condition than the original. 

**I See no issues with the $Z_{ij} \to N_{ij}$ domain difference here.** 
### Sigma Consistency 
Choose $\mathcal{S}_{1}$ as in the original ARC proof, with the added care for $N_{ij}$ replicates case that we only take one of the replicates. $\tilde{N}_{A}$ should grow in the same way. We have alignment up to

$$\begin{aligned} \text{Pr}\left\{P_{\tau^{2}_{A}}(y[1], y[2]) \mid y[1]\right\} \leq \frac{P_{\tau^{2}_{A} + \varepsilon}(y[1])}{P_{\tau^{2}_{A}}(y[1])};\end{aligned}$$
However, weighting makes the decay of this less immediate. We resort to the log scale to show that this properly decays. 

Abusing some notation, 
$$\begin{aligned} \log(P_{\tau^{2}_{A} + \varepsilon}(y[1]) / P_{\tau^{2}_{A}}(y[1])) &= \frac{R_{1}}{\left[ \sum \tilde{N}_{i \bullet } ^{-1} \right]}\sum_{i =1}^{R_{1}} \frac{1}{\tilde{N}_{i \bullet }} \log \frac{L_{i\bullet  }(\tau^{2}_{A} + \varepsilon)}{L_{i\bullet }(\tau^{2}_{A})} \\ \end{aligned}$$
which we need to go to $-\infty$
### Product Weighting
Let $w_{ij} \equiv 1 / [N_{i \bullet}N_{\bullet j}]$. 

$$\begin{aligned} \mathbb{V}[\ell_{\text{all}}(\gamma)] \leq \frac{B^{2}}{N^{2}} \left( \sum_{ijs} \frac{Z_{ij}Z_{is}}{N_{i\bullet }^{2}N_{\bullet  j}N_{\bullet  s}}  + \sum_{ijr} \frac{Z_{ij}Z_{rj}}{N_{\bullet  j}^{2}N_{i\bullet }N_{r\bullet }}\right) \end{aligned}$$

# Likelihood-Based Bashes
## All Likelihood
### Log Likelihood
$$\begin{aligned} \ell_{\text{all}} = \sum_{(i, j, k) \in \mathcal{S}} \log \Phi\left( y_{ijk}x_{ijk}^{\intercal}\gamma \right) \end{aligned}$$
### Score and Hessian
$$\begin{aligned} \nabla_{\gamma} \ell_{\text{all}} = \sum_{(i, j, k) \in \mathcal{S}} y_{ijk}x_{ijk}\cdot \varphi \left( y_{ijk}x_{ijk}^{\intercal}\gamma \right) = \sum_{(i, j, k) \in \mathcal{S}} y_{ijk}x_{ijk}\cdot \varphi \left( x_{ijk}^{\intercal}\gamma \right)\end{aligned}$$
$$\begin{aligned} \nabla^{2}_{\gamma} \ell_{\text{all}} = -\sum_{(i ,j , k) \in \mathcal{S}} y_{ijk}^{2} \varphi \left( x_{ijk}^{\intercal}\gamma \right) \left[ x_{ijk}x_{ijk}^{\intercal} \right]\end{aligned}$$
### Variance

$$\begin{aligned} \mathbb{V}[\nabla_{\gamma} \ell_{\text{all}}] = \mathbb{E}\left[ \nabla_{\gamma}\ell_{\text{all}} \nabla_{\gamma} \ell_{\text{all}}^{\intercal} \right] - \mathbb{E}[\nabla_{\gamma} \ell_{\text{all}}]\mathbb{E}[\nabla_{\gamma} \ell_{\text{all}}]^{\intercal};\end{aligned}$$
#### Expectation of Square
We deal with term $\mathbb{E}\left[ \nabla_{\gamma}\ell_{\text{all}}\nabla_{\gamma}\ell_{\text{all}}^{\intercal} \right]$ first. 
$$\begin{aligned} \nabla_{\gamma} \ell_{\text{all}} \nabla_{\gamma}\ell_{\text{all}}^{\intercal} =& \underbrace{ \sum_{ijk} \varphi^{2}\left( x_{ijk}^{\intercal}\gamma \right) x_{ijk}x_{ijk}^{\intercal} }_{ \text{I} } \\ & + \underbrace{ \sum_{ijkst} y_{ijk}y_{ist} \varphi \left( x_{ijk}^{\intercal}\gamma \right) \varphi \left( x_{ist}^{\intercal} \gamma \right) x_{ijk}x_{ist}^{\intercal} }_{ \text{II}(a) } + \text{II}(b) + \text{II}(c) \\ &+\underbrace{  \sum_{ijkr} y_{ijk}y_{rjk} \varphi \left(x_{ijk}^{\intercal}\gamma \right) \varphi \left(x_{rjk}^{\intercal}\gamma \right)x_{ijk}x_{rjk}^{\intercal} }_{ \text{III(a)} } + \text{III}(b) + \text{III}(c) \\ &+ \underbrace{ \sum_{ijkrst} y_{ijk}y_{rst} \varphi \left( x_{ijk}^{\intercal}\gamma \right)\varphi \left( x_{rst}^{\intercal}\gamma \right)x_{ijk}x_{rst}^{\intercal} }_{ \text{IV} } \end{aligned}$$
where we define the analogous $\text{II}(b)$ ($\text{II}(c)$) by the sum over all cross terms which share the second (third) index, and similarly $\text{III}(b)$ ($\text{III}(c)$) by the sum over all cross terms which share all but the second (third) index. Note as standard that $\varphi$ is symmetric, so the first term is actually deterministic, and only sign information contributes to the expectation for the other types of terms; 
$$\begin{aligned} \mathbb{E}[Y_{ijk}Y_{ist}] =& \mathbb{P}(Y_{ijk} = Y_{ist}) - \mathbb{P}(Y_{ijk} \neq Y_{ist}), \end{aligned}$$
with the first term expanded as 
$$\begin{aligned} \mathbb{P}(Y_{ijk} = Y_{ist})=& \mathbb{P}(Y_{ijk} = Y_{ist} = 1) + \mathbb{P}(Y_{ijk} = Y_{ist} = -1) \\ =& \mathbb{P}\left( X_{ijk}^{\intercal}\beta + a_{i} + b_{j} + c_{k} + \varepsilon_{ijk} \geq 0, X_{ist}^{\intercal}\beta + a_{i} + b_{s} + c_{t} + \varepsilon_{ist} \geq 0 \right) \\ &+ \mathbb{P}\left( X_{ijk}^{\intercal}\beta + a_{i} + b_{j}  + c_{k} + \varepsilon_{ijk} < 0, X_{ist}^{\intercal}\beta + a_{i} + b_{s} + c_{t} + \varepsilon_{ist} < 0\right). \end{aligned}$$
Writing with bivariate normal cdf (and scaling back to $\gamma$), we can say for $\rho_{A} = \sigma^{2}_{A}/ \sigma^{2}$ the intraclass correlation coefficient 
$$\begin{aligned} \mathbb{P}(Y_{ijk} = Y_{ist}) = \Phi_{2}\left( X_{ijk}^{\intercal}\gamma_{0}, X_{ist}^{\intercal}\gamma_{0}; \rho_{A} \right) + \Phi_{2}\left( -X_{ijk}^{\intercal}\gamma_{0}, -X_{ist}^{\intercal}\gamma_{0}; \rho_{A} \right).\end{aligned}$$
In turn, 
$$\begin{aligned} \mathbb{E}[Y_{ijk}Y_{ist}] &= 2 \left( \Phi_{2}\left( X_{ijk}^{\intercal}\gamma_{0}, X_{ist}^{\intercal}\gamma_{0}; \rho_{A} \right) + \Phi_{2}\left( -X_{ijk}^{\intercal}\gamma_{0}, -X_{ist}^{\intercal}\gamma_{0}; \rho_{A} \right)\right) - 1 \\ &= 4\Phi_{2}\left( X_{ijk}^{\intercal}\gamma_{0}, X_{ist}^{\intercal}\gamma_{0} ; \rho_{A}\right) - 2\Phi\left( X_{ijk}^{\intercal}\gamma_{0} \right) - 2\Phi\left( X_{ijk}^{\intercal}\gamma_{0} \right) + 1. \end{aligned}$$
Performing the analogous calculation on the $\text{III}$ term, and letting $\rho_{-A} = \sigma^{2}_{B} / \sigma^{2} + \sigma^{2}_{C} / \sigma^{2}$, #TODO (awkward with negation factorization keeping 1, but maybe fine? need to make a notation page) we have the same form with different ICC, 
$$\begin{aligned} \mathbb{E}[Y_{ijk}Y_{rjk}] = 4\Phi_{2} \left( X_{ijk}^{\intercal}\gamma_{0}, X_{rjk}^{\intercal}\gamma_{0}; \rho_{A} \right) -2\Phi\left( X_{ijk}^{\intercal}\gamma_{0} \right) - 2\Phi\left( X_{ijk}^{\intercal}\gamma_{0} \right) + 1. \end{aligned}$$
Finally,
$$\begin{aligned} \mathbb{E}[Y_{ijk}Y_{rst}] = 4\Phi\left( X_{ijk}^{\intercal}\gamma_{0} \right)\Phi\left( X_{rst}^{\intercal}\gamma_{0} \right) - 2\Phi\left( X_{ijk}^{\intercal}\gamma_{0} \right) - 2\Phi\left( X_{rst}^{\intercal}\gamma_{0} \right) + 1. \end{aligned}$$
#### Square of Expectation 
Now we consider $\mathbb{E}[\nabla_{\gamma}\ell_{\text{all}}]\mathbb{E}[\nabla_{\gamma}\ell_{\text{all}}]^{\intercal}$. First, 
$$\begin{aligned} \mathbb{E}[\nabla_{\gamma} \ell_{\text{all}}] =& \mathbb{E}\left[\sum_{(i, j, k) \in \mathcal{S}} y_{ijk}x_{ijk}\cdot \varphi \left( x_{ijk}^{\intercal}\gamma \right) \right]\\ =& \sum_{(i, j, k) \in \mathcal{S}} x_{ijk}\varphi \left( x_{ijk}^{\intercal}\gamma\right) \cdot \mathbb{E}[y_{ijk}] \\ =& \sum_{(i,j, k) \in \mathcal{S}} x_{ijk}\varphi \left( x_{ijk}^{\intercal}\gamma \right) \left(2\Phi\left( x_{ijk}^{\intercal}\gamma_{0} \right) - 1\right). \end{aligned}$$
Then 
$$\begin{aligned} \mathbb{E}[\nabla_{\gamma} \ell_{\text{all}}]\mathbb{E}[\nabla_{\gamma} \ell_{\text{all}}]^{\intercal} =& \underbrace{ \sum_{ijk} \varphi^{2}\left( x_{ijk}^{\intercal}\gamma \right) \left(2\Phi\left( x_{ijk}^{\intercal}\gamma_{0} \right) - 1\right)^{2} x_{ijk}x_{ijk}^{\intercal} }_{ \text{I}^{*} } \\ &+ \underbrace{ \sum_{ijkst} \varphi \left( x_{ijk}^{\intercal}\gamma \right) \varphi \left( x_{ist}^{\intercal}\gamma \right) \left(2\Phi\left( x_{ijk}^{\intercal}\gamma_{0} \right) - 1\right) \left(2\Phi\left( x_{ist}^{\intercal}\gamma_{0} \right) - 1\right)x_{ijk}x_{ist}^{\intercal} }_{ \text{II}^{*}(a) } + \text{II}^{*}(b) + \text{II}^{*}(c)  \\ &+ \underbrace{ \sum_{ijkr} \varphi \left( x_{ijk}^{\intercal}\gamma \right)\varphi \left( x_{rjk}^{\intercal}\gamma \right)\left(2\Phi\left( x_{ijk}^{\intercal}\gamma_{0} \right) - 1\right)\left(2\Phi\left( x_{rjk}^{\intercal}\gamma_{0} \right) - 1\right)x_{ijk}x_{rjk}^{\intercal} }_{ \text{III}^{*}(a) } + \text{III}^{*}(b) + \text{III}^{*}(c) \\ &+ \underbrace{ \sum_{ijkrst} \varphi\left( x_{ijk}^{\intercal}\gamma \right)\varphi \left( x_{rst}^{\intercal}\gamma \right)\left(2\Phi\left( x_{ijk}^{\intercal}\gamma_{0} \right) - 1\right)\left(2\Phi\left( x_{rst}^{\intercal}\gamma_{0} \right) - 1\right) x_{ijk}x_{rst}^{\intercal} }_{ \text{IV}^{*} }. \end{aligned}$$

#### All Together 
Recombining $\mathbb{E}\left[ \nabla_{\gamma}\ell_{\text{all}}\nabla_{\gamma}\ell_{\text{all}}^{\intercal} \right] - \mathbb{E}[\nabla_{\gamma}\ell_{\text{all}}]\mathbb{E}[\nabla_{\gamma}\ell_{\text{all}}]^{\intercal}$, note that we generally get cancellation for all but the $\Phi_{2}$ and $\Phi^{2}$ terms. In fact, both $\text{IV}$ terms completely cancel out. Recomposed, we net
$$\begin{aligned} \frac{\mathbb{V}[\nabla_{\gamma} \ell_{\text{all}}]}{4} =& \sum_{ijk} \varphi^{2}\left( x_{ijk}^{\intercal}\gamma \right) \left[ \Phi^{2}\left( x_{ijk}^{\intercal}\gamma \right) - \Phi\left( x_{ijk}^{\intercal}\gamma \right)\right]x_{ijk}x_{ijk}^{\intercal} \\ &+ \sum_{ijkst} \varphi \left( x_{ijk}^{\intercal}\gamma \right)\varphi \left( x_{ist}^{\intercal}\gamma \right)\left[ \Phi_{2}\left( x_{ijk}^{\intercal}\gamma, x_{ist}^{\intercal}\gamma; \rho_{A} \right) - \Phi\left( x_{ijk}^{\intercal}\gamma \right) \Phi\left( x_{ist}^{\intercal}\gamma \right)\right]x_{ijk}x_{ist}^{\intercal}  + \text{II}(b) + \text{II}(c) \\ &+ \sum_{ijkr} \varphi\left( x_{ijk}^{\intercal}\gamma \right) \varphi \left( x_{rjk}^{\intercal}\gamma \right)\left[ \Phi_{2}\left( x_{ijk}^{\intercal}\gamma, x_{rjk}^{\intercal}\gamma; \rho_{-A} \right) - \Phi\left( x_{ijk}^{\intercal}\gamma \right)\Phi\left( x_{rjk}^{\intercal}\gamma \right) \right] x_{ijk}x_{rjk}^{\intercal} + \text{III}(b) + \text{III}(c).  \end{aligned}$$


## Row (Standard)

## Row (Negation) 

$$\begin{aligned} \ell_{c}(\tau^{2}_{C}) &= \sum_{k} \log \int _{\mathbb{R}} \prod_{(i, j) \mid k} \Phi\left( y_{ijk}\left( x_{ijk}^{\intercal} \gamma + u_{i} \right) \right) \tau_{C}^{-1} \varphi (u_{i} / \tau_{C}) \, du_{i} \\ &= \sum_{k} \log \int _{\mathbb{R}} \prod_{(i, j) \mid k}\left[ \int  \, dx  \right] \, dx \end{aligned}$$