---
type: setup
aliases: [asymptotic normality assumptions for the smoothed maximum score estimator]
tags: [crossed, research, stanford-stats/y2]
modified: 2026-04-05T00:11:07-07:00
created: 2026-04-04T22:20:52-07:00
---

> [!attention] Asymptotic Normality Assumptions for the Smoothed Maximum Score Estimator
> [[@horowitzSmoothedMaximumScore1992]] poses the following additional conditions. Throughout, let $\tilde{x} := (x_{2}, \dots, x_{p})$ and $z = x^{\intercal}\beta$ (so that $\left( z, \tilde{x}^{\intercal} \right)^{\intercal}$ is one-to-one with $x$ for fixed $\beta$).
> - **N5.** Components of $\tilde{x}$, $\tilde{x}\tilde{x}^{\intercal}$, and $\tilde{x}\tilde{x}^{\intercal}\tilde{x}\tilde{x}^{\intercal}$ have finite first (absolute) moments
> - **N6.** (In addition to asymptotic triviality), $\sigma_{N}$ obeys 
> $$\begin{align*} \frac{\log N}{N\cdot \sigma_{N}^{4}} \to  0. \end{align*}$$
> - **N7.** The kernel $K$ has the following (additional) properties:
> 	- $K$ is twice differentiable everywhere
> 	- $|K'(\cdot)|$, $|K''(\cdot)|$ are uniformly bounded
> 	- Integrals over the whole line with the following integrands are finite: $(K'(v))^{4}$, $K''(v)$, $v^{2}K''(v)$. 
> 	- For some $h \geq 2$ and any $i \in [h]$, $\int |v^{i} K'(v)| \, dv < \infty$ and $$\begin{align*} \int_{-\infty}^{\infty} v^{i}K'(v)  \, dv = \begin{cases} 0 & \text{ if } i< h, \\ d & \text{ if } i = h,\end{cases}  \end{align*}$$ where $d$ is strictly nonzero. 
> 	- For $i \in [h] \cup 0$, $\eta > 0$, and any sequence $\sigma_{N}$ which converges to zero, $$\begin{align*} \lim_{ N \to \infty } \sigma_{N}^{i -h} \int _{|\sigma_{N}v| > \eta} |v^{i} K'(v)| \, dv = 0  \end{align*}$$ and $$\begin{align*} \lim_{ N \to \infty } \sigma_{N}^{-1} \int _{|\sigma_{N}v| > \eta} |K''(v)| \, dv = 0.  \end{align*}$$
> - **N8.** %% Fairly unchanged wording %% For $i \in [h - 1]$, all $z$ in a neighborhood of $0$, almost every $\tilde{x}$, and some $M < \infty$, the $i$th partial in $z$ of the conditional density $p(z \mid \tilde{x})$, denoted by $p^{(i)}(z \mid \tilde{x})$, exists, is continuous in $z$, and is uniformly bounded by $M$. $M$ further bounds the conditional density itself, i.e. $p(x\mid \tilde{x}) < M$ for all $z$ and almost every $\tilde{x}$. 
> - **N9.** For $i \in [h]$ and all $z$ in a neighborhood of 0, almost every $\tilde{x}$, and some finite $M$, let $F(\cdot \mid z, \tilde{x})$ be the cumulative distribution of $u$ conditional on $z$, $\tilde{x}$. $F^{(i)}(-z \mid z, \tilde{x})$ exists and is uniformly bounded by $M$. 
> - **N10.** $\tilde{\beta}$ is an interior point of the candidate set $\tilde{B}$. 
> - **N11.** The (quasi maximum likelihood) Hessian analogue $$\begin{align*} Q:= 2\mathbb{E}\left[ \tilde{x}\tilde{x}^{\intercal} F^{(1)}(0 \mid 0, \tilde{x})p(0\mid \tilde{x}) \right] \end{align*}$$ exists and is negative definite. 


 