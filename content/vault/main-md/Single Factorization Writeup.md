---
modified: 2026-07-21T01:38:00-07:00
created: 2025-10-07T12:58:29-07:00
---
# Case $K$ = 3
We consider a model of the form 
$$\begin{aligned} Y_{ijk} = \mathbf{1}\left[X_{ijk}^{\intercal}\beta + a_{i} + b_{j} + c_{k} + \varepsilon_{ijk} > 0 \right]  .\end{aligned}$$
Though a little ugly, we omit the use of the title-$K$ and instead let $I$, $J$, $K$ be the size of each dimension, versus $R$ and $C$ for the row-column behavior of typical $(i, j)$. 

# Single Form
## Factorization
Analogizing [@bellioConsistentScalableComposite2025], we want to "noise out" the other terms. Looking at $a_{i}$, this can be accomplished by noticing that dividing by $\sqrt{ 1 + \sigma^{2}_{B} + \sigma^{2}_{C} }$,
$$\begin{aligned} Y_{ijk} = \mathbf{1}\left[\frac{1}{\sqrt{ 1 + \sigma^{2}_{B} + \sigma^{2}_{C} }} \left( X_{ijk}^{\intercal}\beta + a_{i} + (b_{j} + c_{k} + \varepsilon_{ijk})  \right) > 0\right].   \end{aligned}$$
Let
$$\begin{aligned} u_{i}= \frac{a_{i}}{\sqrt{ 1 + \sigma^{2}_{B} + \sigma^{2}_{C} }}  \sim \mathcal{N}\left( 0, \frac{\sigma^{2}_{A}}{1 +\sigma^{2}_{B} + \sigma^{2}_{C}} \right)\end{aligned}$$
*(defining $v_{j}$ and $w_{k}$ later in an analogous manner)* for which 
$$\begin{aligned} \tau^{2}_{A} := \frac{\sigma^{2}_{A}}{1 + \sigma^{2}_{B} + \sigma^{2}_{C}}, \end{aligned}$$
and notice
$$\begin{aligned} \eta_{ijk} := \frac{b_{j} + c_{k} + \varepsilon_{ijk}}{1 + \sigma^{2}_{B} + \sigma^{2}_{C}} \sim \mathcal{N}(0, 1).\end{aligned}$$
As in [@bellioConsistentScalableComposite2025], we recover the same form of $\gamma$,
$$\begin{aligned} \gamma = \frac{\beta}{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }}, \,\,\,\,\,  \end{aligned}$$
for which it turns out that the $\gamma_{A}$ analogue follows the same form; 
$$\begin{aligned} \frac{\beta}{\sqrt{ 1 + \sigma^{2}_{B} + \sigma^{2}_{C} }} &= \frac{\beta}{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }}  \cdot \frac{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }}{\sqrt{ 1 + \sigma^{2}_{B} + \sigma^{2}_{C} }} \\ &= \gamma \cdot \sqrt{ 1 + \frac{\sigma^{2}_{A}}{1 + \sigma^{2}_{B} + \sigma^{2}_{C}} } \\ &= \gamma \sqrt{ 1 + \tau^{2}_{A} }  \\ &=: \gamma_{A}.\end{aligned}$$

Taking the immediate analogous forms for $\tau^{2}_{B}$ and $\tau^{2}_{C}$, we arrive at the parametrization $$\begin{aligned} \psi = \left( \gamma ^{\intercal}, \tau^{2}_{A}, \tau^{2}_{B}, \tau^{2}_{C} \right)^{\intercal}. \end{aligned}$$

## Likelihood Maximization 
The key motivation of the factorization is a form of the marginal at various levels. In particular, we know that marginally,

$$\begin{aligned} \text{Pr}(Y_{ijk}= 1) = \Phi\left( X_{ijk}^{\intercal}\gamma \right); \end{aligned}$$
thus we still have the [@bellioConsistentScalableComposite2025] form 
$$\begin{aligned} L_{\text{all}}(\gamma) = \prod_{(i, j, k) \in \mathcal{S}} \Phi\left( X_{ijk}^{\intercal}\beta \right)^{Y_{ijk}} \Phi\left( -X_{ijk}^{\intercal}\beta \right)^{1 - Y_{ijk}},\end{aligned}$$
for which maximization is not particularly expensive. 

Analogizing $L_{\text{row}}$ is less clear, but in this case we use the notation $L^{(i)}$ for $L_{\text{row}}$, trying to capture the idea that we are enforcing independence over each "row" $i$. Indeed,
$$\begin{aligned} \text{Pr}(Y_{ijk} = 1 \mid a) = \Phi\left( X_{ijk}^{\intercal}\gamma _{A} + u_{i} \right), \end{aligned}$$
#TODO confirm a little more rigorously
where both $\gamma_{A}$ and $u_{i}$ are operations with $\tau^{2}_{A}$ only, when $\hat{\gamma}$ is approximated independently - 
$$\begin{aligned} L^{(i)}(\tau^{2}_{A}) = \tau_{A}^{-I} \prod_{i = 1}^{I} \int  L_{i \bullet} (\hat{\gamma}_{A} \mid u_{i})\, \varphi\left( \frac{u_{i}}{\tau_{A}} \right) du_{i},\end{aligned}$$
for which 
$$\begin{aligned} L_{i \bullet} (\hat{\gamma}_{A} \mid u_{i}) = \prod_{(j, k) \mid i} \Phi\left( X_{ijk}^{\intercal} \hat{\gamma}_{A} + u_{i} \right)^{Y_{ijk}} \Phi\left( -X_{ijk}^{\intercal}\hat{\gamma}_{A} - u_{i} \right)^{1 - Y_{ijk}} \end{aligned}$$
is natural.

## Backsolving 
We want to recover $\hat{\theta}$ from $\hat{\psi} = \left( \hat{\gamma}^{\intercal}, \hat{\tau}^{2}_{A}, \hat{\tau}_{B}^{2}, \hat{\tau}_{C}^{2} \right)^{\intercal}$. To do so, the trick is to solve with respect to $S = \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C}$. In particular, it is immediate that
$$\begin{aligned} \sigma^{2}_{A} = \tau^{2}_{A}(1 + \sigma^{2}_{B} + \sigma^{2}_{C}), \,\,\,\, \sigma^{2}_{B} = \tau^{2}_{B}(1 + \sigma^{2}_{A} + \sigma^{2}_{C}), \,\,\,\, \sigma^{2}_{C} = \tau^{2}_{C}(1  + \sigma^{2}_{A} + \sigma^{2}_{B}). \end{aligned}$$
From here, notice we can also write 
$$\begin{aligned} & \sigma^{2}_{A} = \tau^{2}_{A}(1 + S - \sigma^{2}_{A}) \\ \implies & \sigma^{2}_{A} = \frac{\tau^{2}_{A}(1 + S)}{1 + \tau^{2}_{A}}. \end{aligned}$$
Combining these two forms together, we can write
$$\begin{aligned} S = (1 + S) \left( \frac{\tau^{2}_{A}}{1 + \tau^{2}_{A}} + \frac{\tau^{2}_{B}}{ 1 + \tau^{2}_{B}} + \frac{\tau^{2}_{C}}{1 + \tau^{2} _{C}} \right) =: (1 + S)T; \end{aligned}$$
Thus $S = \frac{T}{1 - T}$, and recovering 
#TODO this is $\rho _A / (1 - \rho_{A} - \rho_{B} - \rho_{C})$
$$\begin{aligned} \hat{\sigma}^{2}_{A} = \frac{\hat{\tau}^{2}_{A}}{1 + \hat{\tau}_{A}^{2}}\cdot \frac{1}{1 - \hat{T}}\end{aligned}$$
gives us the desired solution. Note that this form **immediately generalizes for larger values of $K$.** Finally, we recover
$$\begin{aligned} \hat{\beta} = \hat{\gamma}  \sqrt{ 1 + \hat{\sigma}^{2}_{A} + \hat{\sigma}^{2}_{B} + \hat{\sigma}^{2}_{C} } .\end{aligned}$$
## Optimization
Note we have no difference from [@bellioConsistentScalableComposite2025] in the solving for $\hat{\gamma}$. Changes to (9) and (10) solve the exact form as previous, where we make 
# Negation Form 
There is another conditioning trick we can do, which involves a clever pairwise behavior. We start from the top again, to show equivalence. 

## Factorization
We are considering the model 
$$\begin{aligned} Y_{ijk} = \mathbf{1}\left[X_{ijk}^{\intercal}\beta + a_{i} + b_{j} + c_{k} + \varepsilon_{ijk} > 0 \right],  \end{aligned}$$
for which $a_{i} \sim \mathcal{N}(0, \sigma^{2}_{A})$, $b_{j} \sim \mathcal{N}(0, \sigma^{2}_{B})$, $c_{k} \sim \mathcal{N}(0, \sigma^{2}_{C})$, and $\varepsilon_{ijk} \sim \mathcal{N}(0, 1)$, all independently. As with [@bellioConsistentScalableComposite2025], we define 
$$\begin{aligned} \gamma = \frac{\beta}{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }} \end{aligned}$$
with corresponding marginal
$$\begin{aligned} \mathbb{P}(Y_{ijk} = 1) &= \mathbb{E}\left[ \mathbf{1}\left[X_{ijk}^{\intercal} \gamma + \frac{\varepsilon_{ijk} + a_{i} + b_{j} + c_{k}}{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }} > 0\right]  \right] \\ &=: \mathbb{P}\left( X_{ijk}^{\intercal}\gamma + \eta_{ijk} > 0 \right) \\ &= \Phi\left( X_{ijk}^{\intercal}\gamma \right), \end{aligned}$$
since $\eta_{ijk} \sim \mathcal{N}(0, 1)$. We make similar statements on conditioning over some slice of the random effects. In particular, notice that (*"factoring out everything except for $c$"*),
$$\begin{aligned} \mathbb{P}(Y_{ijk} = 1 \mid a_{i}, b_{j}) &= \mathbb{E}\left[ \mathbf{1}\left[X_{ijk}^{\intercal}\beta + a_{i} + b_{j} + c_{k} + \varepsilon_{ijk} > 0 \right]  \mid a_{i}, b_{j}\right]  \\ &= \mathbb{E}\left[ \mathbf{1}\left[\frac{X_{ijk}^{\intercal}\beta}{\sqrt{ 1 + \sigma^{2}_{C} }} + \frac{a_{i} + b_{j}}{\sqrt{ 1 + \sigma^{2}_{C} }} +\frac{\varepsilon_{ijk} + c_{k}}{\sqrt{ 1 + \sigma^{2}_{C} }} > 0 \right] \mid a_{i}, b_{j} \right] \\ &=: \mathbb{P}\left( X_{ijk}^{\intercal}\gamma_{\neg C} + u_{ij} + \eta_{ij(k)} > 0 \mid u_{ij}\right) \\ &= \Phi\left( X_{ijk}^{\intercal}\gamma_{\neg C} + u_{ij}\right),\end{aligned}$$
for which $\tau^{2}_{\neg C} = (\sigma^{2}_{A} + \sigma^{2}_{B}) / (1 + \sigma^{2}_{C})$, and
$$\begin{aligned} \gamma_{\neg C} &= \frac{\beta}{\sqrt{ 1 + \sigma^{2}_{C} }} \\ &= \frac{\beta}{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }} \cdot \frac{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }}{\sqrt{ 1 + \sigma^{2}_{C} }} \\ &= \gamma\cdot \sqrt{ 1 + \frac{\sigma^{2}_{A} + \sigma^{2}_{B}}{1 + \sigma^{2}_{C}}} = \gamma\cdot \sqrt{ 1 + \tau^{2}_{\neg C} }.\end{aligned}$$
The definitions of $\tau^{2}_{ \neg B}$, $\gamma_{\neg A}$, etc. are obvious and immediate. We define $\psi = \left( \gamma ^{\intercal}, \tau^{2}_{\neg A}, \tau^{2}_{\neg B}, \tau^{2}_{\neg C} \right) ^{\intercal}$ as our parameter vector. 

## Backsolving
Define $S = \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C}$. From here,

$$\begin{aligned} & \tau^{2}_{\neg  A} = \frac{\sigma^{2}_{B} + \sigma^{2}_{C}}{1 + \sigma^{2}_{A}}  \\ \implies & 1+ \sigma^{2}_{A} = \frac{\sigma^{2}_{B} + \sigma^{2}_{C}}{\tau^{2}_{\neg A}} \\ \implies & \sigma^{2}_{A} = \frac{S - \sigma^{2}_{A}}{\tau^{2}_{\neg A} } - 1  \\ \implies & \left( 1 + \frac{1}{\tau^{2}_{\neg A}} \right)\sigma^{2}_{A} = \frac{S}{\tau^{2}_{\neg A}} - 1 \\ \implies & \sigma^{2}_{A}  = \frac{S - \tau^{2}_{\neg A}}{1 + \tau^{2}_{\neg  A}}; \end{aligned}$$
in turn,
$$\begin{aligned} & S = \left( \frac{1}{1 + \tau^{2}_{\neg A}} + \frac{1}{1 + \tau^{2}_{\neg B}} + \frac{1}{1 + \tau^{2}_{\neg C}} \right)S - \left( \frac{\tau^{2}_{\neg A}}{1 + \tau^{2}_{\neg A}} + \frac{\tau^{2}_{\neg B}}{1 + \tau^{2}_{\neg B}} + \frac{\tau^{2}_{\neg C}}{1 + \tau^{2}_{\neg C}} \right) \\ \implies & S = \left(\frac{1}{1 + \tau^{2}_{\neg A}} + \frac{1}{1 + \tau^{2}_{\neg B}} + \frac{1}{1 + \tau^{2}_{\neg C}}  - 1\right)^{-1}\left( \frac{\tau^{2}_{\neg A}}{1 + \tau^{2}_{\neg A}} + \frac{\tau^{2}_{\neg B}}{1 + \tau^{2}_{\neg B}} + \frac{\tau^{2}_{\neg C}}{1 + \tau^{2}_{\neg C}} \right).  \end{aligned}$$
Let $t_{A} = 1 + \tau^{2}_{\neg A}$ to simplify some clutter. Then since we have the same denominator,
$$\begin{aligned} S &= \frac{t_{B}t_{C}(t_{A} - 1) + t_{A}t_{C}(t_{B} - 1) + t_{A}t_{B}(t_{C} - 1)}{t_{B}t_{C} + t_{A}t_{C} + t_{B}t_{A} - t_{A}t_{B}t_{C}} = \frac{2(t_{A}t_{B}t_{C})}{t_{B}t_{C} + t_{A}t_{C} +t_{B}t_{A} - t_{A}t_{B} t_{C}} - 1.  \end{aligned}$$

Letting $\rho_{\neg A} = \tau^{2}_{\neg A} / (1 + \tau^{2}_{\neg A})$, we can also write this as 
$$\begin{aligned} S = (2 - \rho _{\neg  A} - \rho_{\neg  B} - \rho_{\neg  C}) ^{-1} (\rho_{A} + \rho_{B} + \rho_{C}). \end{aligned}$$
## Misspecified Likelihood 
Note $\hat{\gamma}$ will be derived in the analogous way. For $\hat{\tau}^{2}_{\neg A}$, $\hat{\tau}^{2}_{\neg B}$, $\hat{\tau}_{\neg C}^{2}$, the corresponding misspecified likelihood is given by (taking $\hat{\tau}^{2}_{\neg C}$ as our representative example),
$$\begin{aligned} L_{(i ,j)}(\hat{\tau}^{2}_{\neg  C}) = \prod_{i = 1}^{I} \prod_{j = 1}^{J} \int  _{\mathbb{R}} L_{ij \bullet}(\hat{\gamma}_{\neg  C} \mid u_{ij}) \tau_{\neg  C}^{-1} \varphi\left( \frac{u_{ij}}{\tau_{\neg C}} \right)\, du_{ij}.  \end{aligned}$$


$$\begin{aligned} \frac{\tau^{2}_{A}}{1 + \tau^{2}_{A}} + \frac{\tau^{2}_{B}}{1 + \tau^{2}_{B}} + \frac{\tau^{2}_{C}}{1 + \tau^{2}_{C}} < 1 \end{aligned}$$