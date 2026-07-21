---
modified: 2026-07-09
created: 2026-04-24T11:27:42-07:00
tags: [genai/claude]
---

Note for reparametrization $\rho_{\mathcal{K}} = \tau^{2}_{\mathcal{K}} /  [1 + \tau^{2}_{\mathcal{K}}]$ we have the same nice form as the singular form [[K-Crossed Slice Probit (Singular)#^singular-rho|+]],
$$\begin{align*} \rho_{\mathcal{K}} = \frac{\sigma^{2}_{(\mathcal{K})}}{\sigma^{2}}.  \end{align*}$$

The issue in this regime is double counting, since $\sigma^{2}_{(\mathcal{K})}$ sums over all $\mathcal{K}' \in \mathbb{A}$ for which $\mathcal{K}' \subseteq \mathcal{K}$. In the case where $\mathbb{A} =\mathbb{A}_{1}$, we have single terms so this is not an issue. 

If we consider the case of $\mathbb{A} = \mathbb{A}_{1} \cup \mathbb{A}_{2}$, we get a fairly clean statement:
$$\begin{align*} \sum_{\mathcal{K} \in \mathbb{A}} \rho_{\mathcal{K}} - (K - 1)\sum_{\mathcal{K} \in \mathbb{A}_{1}} \rho_{\mathcal{K}} = 1 - \frac{\sigma^{2}_{E}}{\sigma^{2}},   \end{align*}$$
so 
$$\begin{align*} \sigma^{2} = \frac{\sigma^{2}_{E}}{1 - \sum_{\mathcal{K} \in \mathbb{A}} \rho_{\mathcal{K}} + (K -1) \sum_{\mathcal{K} \in \mathbb{A}_{1}} \rho_{\mathcal{K}}}, \qquad \sigma^{2}_{k} = \rho_{k}\sigma^{2}, \qquad \sigma^{2}_{\left\{ k, k' \right\} } = \sigma^{2}(\rho_{\left\{ k, k' \right\}  } - \rho_{k} - \rho_{k'}). \end{align*}$$

Extending this to the generic case, Möbius inversion gives

$$\begin{align*} \tilde{\rho}_{\mathcal{K}} := \frac{\sigma^{2}_{\mathcal{K}}}{\sigma^{2}} = \sum_{\mathcal{K}' \subseteq \mathcal{K}, \mathcal{K}' \in \mathbb{A}} (-1)^{|\mathcal{K}| - |\mathcal{K}'|} \rho_{\mathcal{K'}}, \end{align*}$$
from which 
$$\begin{align*} \sigma^{2} = \frac{\sigma^{2}_{E}}{1 - \sum_{\mathcal{K} \in \mathbb{A}} \tilde{\rho}_{\mathcal{K}} }, \qquad \sigma^{2}_{\mathcal{K}} = \tilde{\rho}_{\mathcal{K}} \sigma^{2}_{\mathcal{K}}, \qquad \beta = \sigma \gamma.  \end{align*}$$
We reiterate that we require that all (nontrivial) subsets of $\mathcal{K}$ are extant in $\mathbb{A}$, in order for the decomposition to hold. 
