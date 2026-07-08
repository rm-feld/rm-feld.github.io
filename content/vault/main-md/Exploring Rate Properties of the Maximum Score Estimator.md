---
modified: 2026-04-04T19:05:17-07:00
created: 2026-04-02T16:25:55-07:00
---
Despite [[Consistency of the Maximum Score Estimator|consistency]], maximum score estimation is fairly unwieldy in the sense that its asymptotics are not particularly standard, and in fact follow $O_{p}(n^{-1/3})$ (cube-root) decay. We give the below results without proof. 

**Example 6.4** of [[@kimCubeRootAsymptotics1990]] states the desired result.  

![[Rate Assumptions for Maximum Score Estimation]]

Summarizing the above, when we have the above assumptions + some nice regularity condition, we will satisfy **Theorem 1.1** of [[@kimCubeRootAsymptotics1990]], which says that the objective under cube-root scaling is asymptotically normal, 

$$\begin{align*} n^{2 / 3} S_{n}(\beta_{0} + tn^{- 1/3}) \overset{d}{\to} Z \end{align*}$$
which, if it is nondegenerate, corresponds to the ([[Almost Sure Event|almost surely]] unique) [[Convergence in Distribution|convergence in distribution]] of the parameter $n^{ 1/ 3}(\hat{\beta}_{n} - \beta_{0})$ to the random vector that maximimizes $Z$. The distribution of $Z$ is not generally understood. 

%% 
### actual proof stuff
Consider the following class of functions $\mathcal{G}$ described by 
$$\begin{align*} g(x, u, \beta) = h(x, u) \left[ \left\{ x^{\intercal}\beta \geq 0 \right\} - \left\{ x^{\intercal}\beta_{0} \geq 0 \right\}  \right] ,\end{align*}$$
where $h(x, u)$ encodes the true signed label (under known $u$)
$$\begin{align*} h(x, u) = \left\{ u + x^{\intercal}\beta_{0} \geq 0\right\} - \left\{ u+ x^{\intercal}\beta_{0} < 0 \right\}.  \end{align*}$$
The corresponding [[Subgraph Class (of a Function Space)|subgraph class]] turns out to have a finite [[VC Dimension]], so that 

 %%