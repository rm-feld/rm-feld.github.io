---
type: proposition
aliases: [godambe H for k-crossed composite estimator, sensitivity matrix H]
tags: [crossed, genai/claude, research, stanford/y2]
modified: 2026-07-01T00:00:00-07:00
created: 2026-07-01T00:00:00-07:00
---

> [!tip] Sensitivity Matrix $H$ for the $K$-Crossed Composite Estimator
>
> The sensitivity (Godambe "bread") $H(\psi)=\mathbb E[-\nabla_\psi U(\psi)]$ is additive over criteria,
> $$H=\omega_{\mathrm{all}}H_{\mathrm{all}}+\sum_{\mathcal K\in\mathbb A}\omega_{\mathcal K}H_{\mathcal K},$$
> with an **arrow** block structure over $\psi=(\gamma,\{\rho_{\mathcal K}\})$: the all-term contributes only the $\gamma\gamma$ block,
> $$H_{\mathrm{all},\gamma\gamma}=\sum_{\ell=1}^N \frac{\varphi(x_\ell^{\mathsf T}\gamma)^2}{\Phi(x_\ell^{\mathsf T}\gamma)\,\Phi(-x_\ell^{\mathsf T}\gamma)}\,x_\ell x_\ell^{\mathsf T},$$
> and each slice-$\mathcal K$ term contributes to the $\gamma\gamma$, $\gamma\rho_{\mathcal K}$ and $\rho_{\mathcal K}\rho_{\mathcal K}$ blocks only (no $\rho_{\mathcal K}\rho_{\mathcal K'}$ coupling for $\mathcal K\neq\mathcal K'$).

^sensitivity-H

> [!success]- Proof
>
> **All block.** From [[Composite Score and Unbiased Estimating Equations (K-Crossed Probit)#^composite-score|the score lemma]], $-\nabla_\gamma U_{\mathrm{all}}=\sum_\ell w_\ell\, x_\ell x_\ell^{\mathsf T}$ with $w_\ell=R(t_\ell)\big(t_\ell+R(t_\ell)\big)$, $t_\ell=\tilde y_\ell x_\ell^{\mathsf T}\gamma$, $R=\varphi/\Phi$ (this is $-(\log\Phi)''$, positive by log-concavity, [[Concavity of the All Log-Likelihood (K-Crossed Probit)#^all-concavity|concavity lemma]]). Taking expectation over $\tilde y_\ell$ at $\eta=x_\ell^{\mathsf T}\gamma$,
> $$\mathbb E[w_\ell]=\Phi(\eta)\,R(\eta)\big(\eta+R(\eta)\big)+\Phi(-\eta)\,R(-\eta)\big(-\eta+R(-\eta)\big)=\frac{\varphi(\eta)^2}{\Phi(\eta)\Phi(-\eta)},$$
> the classical probit information weight, giving $H_{\mathrm{all},\gamma\gamma}$. Since $U_{\mathrm{all}}$ has no $\rho$-dependence, all other blocks of $H_{\mathrm{all}}$ vanish.
>
> **Slice blocks.** $\mathcal L_{\mathcal K}$ depends on $\psi$ only through $\gamma_{\mathcal K}=\gamma/\sqrt{1-\rho_{\mathcal K}}$ and $\tau_{\mathcal K}=\sqrt{\rho_{\mathcal K}/(1-\rho_{\mathcal K})}$, i.e. on $(\gamma,\rho_{\mathcal K})$. Hence $\nabla^2_\psi\mathcal L_{\mathcal K}$ is supported on the $(\gamma,\rho_{\mathcal K})$ sub-block; there is no $\rho_{\mathcal K}\rho_{\mathcal K'}$ entry because $\rho_{\mathcal K'}$ ($\mathcal K'\neq\mathcal K$) does not appear in $\mathcal L_{\mathcal K}$. The block entries are cluster sums of posterior-covariance terms (differentiating Fisher's identity); they are finite and, for $\omega_{\mathcal K}>0$ and identified $\tau^2_{\mathcal K}$, make the $\rho_{\mathcal K}\rho_{\mathcal K}$ block strictly positive.
>
> **Nonsingularity.** The $\gamma\gamma$ block is $\succ0$ (probit weights $>0$, $\sum_\ell x_\ell x_\ell^{\mathsf T}\succ0$). With each $\rho_{\mathcal K}\rho_{\mathcal K}$ block $>0$ and the arrow (bordered) structure, $H$ is nonsingular provided the $\gamma$-block dominates the borrowed $\gamma\rho$ borders (a Schur-complement condition, satisfied when slices are informative). $\blacksquare$

> [!warning]- Remark — non-orthogonality (contrast with Varin linear)
> In the linear-Gaussian case the $\gamma\rho$ (mean–variance) border vanishes by information orthogonality, so $H$ is block-diagonal and $\mathrm{avar}(\hat\beta)$ decouples. **For probit the border $H_{\gamma\rho_{\mathcal K}}$ is generally nonzero**, so this decoupling fails; retain the full arrow $H$. Empirically checking $\|H_{\gamma\rho}\|$ relative to the diagonal blocks is a cheap, informative diagnostic — flagged as a to-verify in [[Godambe Sandwich for the K-Crossed Composite Estimator]].

> [!note]- Estimation
> In practice use the **observed** sensitivity $-\nabla_\psi U(\hat\psi)$ from a single dataset (no expectation needed); it is consistent for $H$. The all-block observed form is $\sum_\ell w_\ell(\hat\psi)x_\ell x_\ell^{\mathsf T}$, exactly the Newton Hessian already assembled when fitting $\hat\gamma$.

**Role in the paper.** Provides the "bread" of the [[Godambe Sandwich for the K-Crossed Composite Estimator#^godambe-sandwich|sandwich]]; the "meat" is [[Variability Matrix J for the K-Crossed Composite Estimator]].
