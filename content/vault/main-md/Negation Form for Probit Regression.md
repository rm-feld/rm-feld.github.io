---
modified: 2025-10-03T14:43:07-07:00
created: 2025-10-02T11:26:53-07:00
---

# Set Up
## Factorization
We are considering the model 
$$\begin{align} Y_{ijk} = \mathbf{1}\left[X_{ijk}^{\intercal}\beta + a_{i} + b_{j} + c_{k} + \varepsilon_{ijk} > 0 \right],  \end{align}$$
for which $a_{i} \sim \mathcal{N}(0, \sigma^{2}_{A})$, $b_{j} \sim \mathcal{N}(0, \sigma^{2}_{B})$, $c_{k} \sim \mathcal{N}(0, \sigma^{2}_{C})$, and $\varepsilon_{ijk} \sim \mathcal{N}(0, 1)$, all independently. As with [@bellioConsistentScalableComposite2025], we define 
$$\begin{align} \gamma = \frac{\beta}{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }} \end{align}$$
with corresponding marginal
$$\begin{align} \mathbb{P}(Y_{ijk} = 1) &= \mathbb{E}\left[ \mathbf{1}\left[X_{ijk}^{\intercal} \gamma + \frac{\varepsilon_{ijk} + a_{i} + b_{j} + c_{k}}{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }} > 0\right]  \right] \\
&=: \mathbb{P}\left( X_{ijk}^{\intercal}\gamma + \eta_{ijk} > 0 \right) \\
&= \Phi\left( X_{ijk}^{\intercal}\gamma \right), \end{align}$$
since $\eta_{ijk} \sim \mathcal{N}(0, 1)$. We make similar statements on conditioning over some slice of the random effects. In particular, notice that (*"factoring out everything except for $c$"*),
$$\begin{align} \mathbb{P}(Y_{ijk} = 1 \mid a_{i}, b_{j}) &= \mathbb{E}\left[ \mathbf{1}\left[X_{ijk}^{\intercal}\beta + a_{i} + b_{j} + c_{k} + \varepsilon_{ijk} > 0 \right]  \mid a_{i}, b_{j}\right]  \\
&= \mathbb{E}\left[ \mathbf{1}\left[\frac{X_{ijk}^{\intercal}\beta}{\sqrt{ 1 + \sigma^{2}_{C} }} + \frac{a_{i} + b_{j}}{\sqrt{ 1 + \sigma^{2}_{C} }} +\frac{\varepsilon_{ijk} + c_{k}}{\sqrt{ 1 + \sigma^{2}_{C} }} > 0 \right] \mid a_{i}, b_{j} \right] \\
&=: \mathbb{P}\left( X_{ijk}^{\intercal}\gamma_{\neg C} + u_{ij} + \eta_{ij(k)} > 0 \mid u_{ij}\right) \\
&= \Phi\left( X_{ijk}^{\intercal}\gamma_{\neg C} + u_{ij}\right),\end{align}$$
for which $\tau^{2}_{\neg C} = (\sigma^{2}_{A} + \sigma^{2}_{B}) / (1 + \sigma^{2}_{C})$, and
$$\begin{align} \gamma_{\neg C} &= \frac{\beta}{\sqrt{ 1 + \sigma^{2}_{C} }} \\
&= \frac{\beta}{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }} \cdot \frac{\sqrt{ 1 + \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} }}{\sqrt{ 1 + \sigma^{2}_{C} }} \\
&= \gamma\cdot \sqrt{ 1 + \frac{\sigma^{2}_{A} + \sigma^{2}_{B}}{1 + \sigma^{2}_{C}}} = \gamma\cdot \sqrt{ 1 + \tau^{2}_{\neg C} }.\end{align}$$
The definitions of $\tau^{2}_{ \neg B}$, $\gamma_{\neg A}$, etc. are obvious and immediate. We define $\psi = \left( \gamma ^{\intercal}, \tau^{2}_{\neg A}, \tau^{2}_{\neg B}, \tau^{2}_{\neg C} \right) ^{\intercal}$ as our parameter vector. 

## Backsolving
Define $S = \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C}$. From here,

$$\begin{align} & \tau^{2}_{\neg  A} = \frac{\sigma^{2}_{B} + \sigma^{2}_{C}}{1 + \sigma^{2}_{A}}  \\
\implies & 1+ \sigma^{2}_{A} = \frac{\sigma^{2}_{B} + \sigma^{2}_{C}}{\tau^{2}_{\neg A}} \\
\implies & \sigma^{2}_{A} = \frac{S - \sigma^{2}_{A}}{\tau^{2}_{\neg A} } - 1  \\
\implies & \left( 1 + \frac{1}{\tau^{2}_{\neg A}} \right)\sigma^{2}_{A} = \frac{S}{\tau^{2}_{\neg A}} - 1 \\
\implies & \sigma^{2}_{A}  = \frac{S - \tau^{2}_{\neg A}}{1 + \tau^{2}_{\neg  A}}; \end{align}$$
in turn,
$$\begin{align} & S = \left( \frac{1}{1 + \tau^{2}_{\neg A}} + \frac{1}{1 + \tau^{2}_{\neg B}} + \frac{1}{1 + \tau^{2}_{\neg C}} \right)S - \left( \frac{\tau^{2}_{\neg A}}{1 + \tau^{2}_{\neg A}} + \frac{\tau^{2}_{\neg B}}{1 + \tau^{2}_{\neg B}} + \frac{\tau^{2}_{\neg C}}{1 + \tau^{2}_{\neg C}} \right) \\
\implies & S = \left(\frac{1}{1 + \tau^{2}_{\neg A}} + \frac{1}{1 + \tau^{2}_{\neg B}} + \frac{1}{1 + \tau^{2}_{\neg C}}  - 1\right)^{-1}\left( \frac{\tau^{2}_{\neg A}}{1 + \tau^{2}_{\neg A}} + \frac{\tau^{2}_{\neg B}}{1 + \tau^{2}_{\neg B}} + \frac{\tau^{2}_{\neg C}}{1 + \tau^{2}_{\neg C}} \right).  \end{align}$$
Let $t_{A} = 1 + \tau^{2}_{\neg A}$ to simplify some clutter. Then since we have the same denominator,
$$\begin{align} S &= \frac{t_{B}t_{C}(t_{A} - 1) + t_{A}t_{C}(t_{B} - 1) + t_{A}t_{B}(t_{C} - 1)}{t_{B}t_{C} + t_{A}t_{C} + t_{B}t_{A} - t_{A}t_{B}t_{C}} = \frac{2(t_{A}t_{B}t_{C})}{t_{B}t_{C} + t_{A}t_{C} +t_{B}t_{A} - t_{A}t_{B} t_{C}} - 1.  \end{align}$$
# Estimating $\psi$
There are many directions of generalization for ARC with three crossed random effects. We list a few below and provide some commentary. 

## 1
We can define the $(i,j)$-slice-wise misspecified model likelihood by (N.1.8)
$$\begin{align} L_{(i, j)}(\tau^{2}_{\neg C}) = \prod_{i = 1}^{I} \prod_{j = 1}^{J} \int _{\mathbb{R}} L_{ij\bullet} (\hat{\gamma}_{\neg C} \mid u_{ij}) \, du_{ij}, \end{align}$$
for (N.1.9)
$$\begin{align} L_{ij\bullet} (\hat{\gamma}_{\neg C} \mid u_{ij}) = \prod_{k \mid (i, j)} \Phi\left( x_{ijk}^{\intercal} \hat{\gamma}_{\neg C} + u_{ij} \right)^{y_{ijk} } \Phi\left( -x_{ijk}^{\intercal}\hat{\gamma}_{\neg C} - u_{ij}\right)^{1 - y_{ijk}},\end{align}$$
taking $k \mid (i, j) = \left\{ k:(i, j, k) \in \mathcal{S} \right\}$ the natural observed set of indices. 

## 2 Too Big one

## 3
Maybe we solve for a $\gamma_{i(j)}$ instead, in the intermediate sense; fit an augmenetation
$$\begin{align} X_{ijk}^{\intercal}\beta + a_{i} \end{align}$$




We highlight the above negation form as easily generalizable to an arbitrary fixed number of random effects, #TODO though we are interested in different submodels, and though the slice-wise number of values can become very small (which, from the [[Shihao Comment]], seems to generally perform worse)

In what other ways can we consider and fit the misspecified model? A direction of motivation is the following goal. A primary interest is in reducing the use of high-dimensional integrals to many smaller low-dimensional integrals. It seems natural to be able to "take a hit" of two-dimensional integrals vs. one-dimensional integrals, in exchange for some benefit; how could we do such a thing?

- explicit hierarchical
- estimate $a_{i}$ etc.
- pairwise 
	- ordering?
- the 'i only care about $S$' thing
- 99% 1% thing

A natural notion is to split $u_{ij}$; define
$$\begin{align} u_{i} = \frac{a_{i}}{\sqrt{ 1 + \sigma^{2}_{C} }} \sim \mathcal{N}\left( 0, \frac{\sigma^{2}_{A}}{1 + \sigma^{2}_{C}} \right) , \,\,\,\, v_{j} = \frac{b_{j}}{\sqrt{ 1 + \sigma^{2}_{C} }} \sim \mathcal{N}\left( 0, \frac{\sigma^{2}_{B}}{1 + \sigma^{2}_{C}} \right).\end{align}$$
- model class balances as random draw?

The issue that emerges is that shared $i$ or $j$ induces the "necessity" of integration over slice dependence. **treat as replicates?** estimate term?
- an idea - with replicates we can do binomial integration, which might be nicer.

$$\begin{align} L_{[i,j]} () = \prod_{i = 1}^{I} \int \prod_{j = 1}^{J}  \, dx  \end{align}$$

$$\begin{align} L_{[i, j]} () = \prod_{i = 1}^{I} \end{align}$$

# Iterations of Likelihood Form Under Negation Factorization - Throwing Things at the Wall

## (0) Misc. Misspecifications and middle steps
- 
## (1)
**Motivation:** marginal of the negation factorization
$$\begin{align} L_{(i, j)}(\tau^{2}_{\neg C}) = \prod_{i = 1}^{I} \prod_{j = 1}^{J} \int _{\mathbb{R}} L_{ij\bullet} (\hat{\gamma}_{\neg C} \mid u_{ij}) \, du_{ij}, \end{align}$$

$$\begin{align} L_{ij\bullet} (\hat{\gamma}_{\neg C} \mid u_{ij}) = \prod_{k \mid (i, j)} \Phi\left( x_{ijk}^{\intercal} \hat{\gamma}_{\neg C} + u_{ij} \right)^{y_{ijk} } \Phi\left( -x_{ijk}^{\intercal}\hat{\gamma}_{\neg C} - u_{ij}\right)^{1 - y_{ijk}},\end{align}$$


## (2)
- **Motivation:** a naive way of dealing with levels is an "inconsequential" approximation of some nuisance term
$$\begin{align} L_{(i, j)}(\tau^{2}_{\neg C}) &= \prod_{i = 1}^{I} \int \prod_{j = 1}^{J}  \, dx \end{align}$$

## (3)
$$\begin{align} L_{(i,j)} (\tau^{2}_{\neg C}) = \prod_{i =1 }^{I} \prod_{j = 1} ^{J} \end{align}$$

## (4) 
$$\begin{align} L_{(i, j)} = \prod_{i =1 }^{I} \prod_{j = 1}^{J} \int _{\mathbb{R}^{2}} L_{ij\bullet}\, dx \end{align}$$

- explicit likelihood under misspec

$$\begin{align} L_{(i, j)} = \prod_{i = 1}^{I} \int_{\mathbb{R}^{| J_{i}| + 1}}  \varphi\left( \frac{u_{i}}{ \sigma_{A} / \sqrt{ 1  + \sigma^{2}_{C} }}\right)\prod_{j \mid i} \left[ \prod_{k\mid (i, j)} \Phi\left( X_{ijk}^{\intercal}\beta + u_{i} + v_{j} \right)^{y_{ijk}}\Phi\left( -X_{ijk}^{\intercal}\beta - u_{i} - v_{j} \right)^{1 - y_{ijk}}  \right]  (1 + \sigma^{2}_{C}) \frac{1}{\sqrt{ \sigma_{A} \sigma_{B} }} \varphi \left( \frac{v_{j}}{\sigma_{B} / \sqrt{ 1 + \sigma^{2}_{C} }} \right)\, d\left\{ v_{J \mid i} \right\} du_{i}    \end{align}$$

# How Can I Misspecify My Models in a Nice Way
## Throwing Things at the Wall
- as replicates formulation
	- the marginal with shared $i$ can be seen as a 
- repeat procedure nested
	- issues with ordering - $i$ then $j$ vs. $j$ then $i$
- estimate an intermediate $u_{i}$ or $v_{j}$
- if interaction term, integral over $\mathbb{R}^{2}$ seems natural; otherwise less so
	- also multiple

okay, if I have 
