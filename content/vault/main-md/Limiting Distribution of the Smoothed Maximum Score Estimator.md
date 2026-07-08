---
type: theorem
aliases: [limiting distribution of the smoothed maximum score estimator]
tags: [crossed, research, stanford-stats/y2]
modified: 2026-04-06T08:55:54-07:00
created: 2026-04-04T23:59:00-07:00
---


> [!tip] Limiting Distribution of the Smoothed Maximum Score Estimator
> **([[@horowitzSmoothedMaximumScore1992]], Theorem 2).** Let the [[Consistency of the Maximum Score Estimator|consistency assumptions]] and assumptions [[Asymptotic Normality Assumptions for the Smoothed Maximum Score Estimator|N5 - N11]] hold. Further, define in addition to $Q$ the standard limiting objects
> $$\begin{align*} A = -2\alpha_{A} \sum_{i =1}^{h} \left\{ [i!(h - i)!]^{-1} \mathbb{E}[F^{(i)}(0 \mid 0, \tilde{x})p^{(h - i)}(0 \mid \tilde{x})] \tilde{x} \right\}  \end{align*}$$
> and
> $$\begin{align*} D = \alpha_{D} \mathbb{E}\left[ \tilde{x}\tilde{x}^{\intercal}p(0 \mid \tilde{x}) \right]\end{align*}$$
> for $\alpha_{A} = \int _{\mathbb{R}} v^{h}K'(v) \, dv$, $\alpha_{D} = \int _{\mathbb{R}} [K'(v)]^{2} \, dv$. $D$ is to be interpreted as an analogue of the outer product for the information matrix in quasi maximum likelihood, and $A$ behaves as a limiting mean for the [[Smoothed Maximum Score Estimator|smoothed maximum score estimator]].
> %% %%
> Let $\left\{ b_{N} \right\}$ be a sequence of maximizers. We have the following cases:
> 1. If $N\sigma_{N}^{2h + 1} \to \infty$, $\sigma_{N}^{-h}(\tilde{b}_N - \tilde{\beta})\overset{p}{\to} -Q^{-1}A.$
> 2. If $N\sigma^{2h + 1}\to \lambda$ finite, $$\begin{align*} \sqrt{ N\sigma_{N} } (\tilde{b}_{N} - \tilde{\beta}) \overset{d}{\to}  \text{MVN}(-\lambda^{1 / 2}Q^{-1}A, Q^{-1}DQ^{-1}) \end{align*}$$
> 3. If $\sigma_{N} = (\lambda / N)^{1 / (2h + 1)}$ for some $\lambda \in (0, \infty)$, then for any $\Omega$ nonstochastic and [[Positive Semidefinite|PSD]] such that $A^{\intercal}Q^{-1}\Omega Q^{-1}A \neq 0$, the MSE is given by $\mathbb{E}_{A}\left[ (\tilde{b}_{N} - \tilde{\beta})^{\intercal}\Omega(\tilde{\beta}_{N} - \beta) \right]$, where $\mathbb{E}_{A}[\cdot]$ denotes expectation under the asymptotic distribution. The MSE is minimized at some normalized trace term $$\begin{align*} \lambda^{\star} \equiv \frac{\text{tr}(Q^{-1}\Omega Q^{-1}D)}{2hA^{\intercal}Q^{-1}\Omega Q^{-1}A} \end{align*}$$ with corresponding limiting distribution $$\begin{align*} N^{h / (2h + 1)}(\tilde{b}_{N} - \tilde{\beta})\overset{d}{\to}  \text{MVN}(-(\lambda^{\star})^{h / (2h + 1)} Q^{-1}A, (\lambda^{\star})^{-1 / (2 h + 1)} Q^{-1}DQ^{-1}). \end{align*}$$
