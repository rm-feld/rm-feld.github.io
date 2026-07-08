---
type: setup
aliases: [inference for binary choice models]
tags: [crossed, research, stanford-stats/y2]
modified: 2026-04-03T16:23:46-07:00
created: 2026-04-01T21:47:03-07:00
---

> [!attention] Inference for Binary Choice Models
> Let us observe pairs $(X_{i}, Y_{i})$ independently from a **binary choice model,**
> $$\begin{align*} Y_{i} = \mathbf{1}\left[X_{i}^{\intercal}\beta + U_{i} \geq 0 \right] . \end{align*}$$
> for $U_{i}$ some unobserved latent term. We enforce that 
> $$\begin{align*} \text{med}(U_{i} \mid X_{i} =x) = 0 \end{align*}$$
> for any $x$ in the support of $X$. 
> %% %%
> We are interested in estimations of $\beta$. This is sometimes not recoverable; in this case, we are often interested in identifying the direction, $\beta/\left\lvert\left\lvert \beta \right\rvert\right\rvert_{2}$. We say $X_{i} \overset{\mathrm{iid}}{\sim} F_{X}$ some distribution. 

This is also called the "threshold-crossing" model or the stochastic utility model of choice in the econometrics literature. 


