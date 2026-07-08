---
type: setup
aliases: [rate assumptions for maximum score estimation]
tags: [crossed, research, stanford-stats/y2]
modified: 2026-04-05T00:10:10-07:00
created: 2026-04-03T17:48:36-07:00
---

> [!attention] Rate Assumptions for Maximum Score Estimation
> [[@kimCubeRootAsymptotics1990]] Add the following assumptions (in addition to [[Standard Assumptions for Maximum Score Estimation|those of]] [[@manskiSemiparametricAnalysisDiscrete1985]] such that $\hat{\beta}_{n}\to \beta_{0}$ up to scale) towards convergence rate of the maximum score estimator:
> - **R1.** $X$ has a continuously differentiable density $p(\cdot)$
> - **R2.** The angular component of $X$ (ie. the corresponding distribution over the unit sphere) has a bounded, continuous density with respect to the surface measure on $S$. 
> ^manski-rate-main-assumptions


In addition to the above, there is in the natural course of derivation a fairly natural need for a regularity condition which can be chosen based on the domain of interest; letting $\kappa(x) = \mathbb{E}[\tilde{Y} \mid X = x]$ the expected signed response, the corresponding [[Hessian]] of the corresponding semi-parametric likelihood can be given by 
$$\begin{align*} \frac{ \partial^{2} }{ \partial \beta^{2} } \Gamma(\beta_{0}) &= -\int \mathbf{1}\left[x^{\intercal}\beta_{0} = 0 \right] \dot{\kappa}(x) ^{\intercal}\beta_{0} \; p(x) xx^{\intercal}  \, d\sigma \end{align*}$$
for $\sigma$ the image of the surface measure under the transformation 
$$\begin{align*} T_{\beta} = \left(  I - \left\lvert\left\lvert \beta \right\rvert\right\rvert ^{-2}_{2} \beta \beta ^{\intercal}  \right)\left( I - \beta_{0}\beta_{0}^{\intercal} \right) + \left\lvert\left\lvert \beta \right\rvert\right\rvert _{2}^{-1} \beta \beta_{0} ^{\intercal}.\end{align*}$$

Some standard regularity condition for which the above Hessian is well behaved is sufficient. [[@kimCubeRootAsymptotics1990]] suggest for the special case of $U\perp X$ the regularity assumption 
$$\begin{align*} \sigma \left\{ x: x^{\intercal}\beta_{0} = 0\text{ and } \dot{\kappa}(x)^{\intercal}\beta_{0} \, p(x) > 0\right\} > 0  \end{align*}$$
which is sufficient for the described asymptotics. 
^manski-regularity-assumptions



%% presumably surface measure is the natural one over the sphere.%%