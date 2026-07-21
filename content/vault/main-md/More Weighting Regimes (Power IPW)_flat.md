---
tags: [no-index]
up: "[[More Weighting Regimes (Power IPW)]]"
modified: 2026-07-13T11:23:49-07:00
created: 2026-07-13T11:23:15-07:00
---

\section{Generic Normalization Structure}
\subsection{Reweighting}$\alpha$
We consider normalized powers of row weights $w_{ij} = \alpha N_{i \bullet}^{-\theta}$ for $\theta \in [0,1]$, maintaining the non-collapsing scale $\sum_{ij}w_{ij}Z_{ij} = N$. It is clear by $\alpha \sum_{i}N_{i \bullet}^{1 - \theta} = N$ that 

\begin{align\textit{} \frac{N}{R \cdot \max_{i}(N_{i \bullet }^{1 - \theta})} \leq \alpha \leq \frac{N}{R \cdot \min_{i}(N_{i \bullet }^{1 - \theta})} \end{align}}

so that, since we can reasonably assume $\min(N_{i \bullet}) = 2$ in the presented regimes, nets 


\begin{align\textit{} \frac{N^{1 - \kappa_{1}}}{[\max_{i}N_{i}]^{1 - \theta}} \leq \alpha \leq \frac{N^{1 - \kappa_{1}}}{2^{1 - \theta}}. \end{align}}

May be over-reading, but the $\theta = \kappa_{1}$ bound feels appealing in this context. 
\subsection{Weight relations and bound}

\begin{align\textit{} \frac{\min_{i}N_{i \bullet }}{\max_{i} N_{i \bullet }} \leq \frac{\alpha}{N_{i \bullet }} \leq \frac{\max_{i}N_{i \bullet }}{\min_{i} N_{i \bullet }} \end{align}}

Note a crude bound

\begin{align\textit{} N_{i\bullet }^{- \theta} \leq  \frac{1}{1 + \theta(x - 1)}. \end{align}}

we can also get 

\begin{align\textit{} N_{i \bullet }^{-\theta} \leq \exp\left( -\frac{\theta (N_{i \bullet } - 1)}{N_{i \bullet }} \right). \end{align}}

\section{Conditions}
\subsection{Only Row Weighting}

\begin{align*} \mathbb{V}\left[ \frac{\ell_{\text{all}}(\gamma)}{N} \right] &\leq \frac{B^{2}\alpha^{2}}{N^{2}} \left( \sum_{ijs} N_{i \bullet }^{- 2\theta} Z_{ij}Z_{is} + \sum_{ijr} N_{i \bullet}^{-\theta} N_{r \bullet }^{ - \theta} Z_{ij}Z_{rj}\right) \\ 
&= \frac{B^{2}\alpha^{2}}{N^{2}} \left( \sum_{i} N_{i \bullet }^{2 - 2\theta} + \sum_{ijr} N_{i \bullet }^{-\theta}N_{r \bullet }^{-\theta} Z_{ij}Z_{rj}\right) \\ 
&\leq \frac{B^{2}\alpha^{2}}{N^{2}} \left( \sum_{i} N_{i \bullet }^{2 - 2\theta} + \sum_{ijr} \exp \left\{ -\theta [(N_{i\bullet} - 1)/N_{i\bullet } + (N_{r \bullet } - 1) / N_{r \bullet }] \right\} Z_{ij}Z_{rj} \right).\end{align\textit{}


Column decay will always be an issue, but it looks like the standard always works as an upper bound. meanwhile, 


\begin{align}} \frac{B^{2}\alpha^{2}}{N^{2}} \sum_{i}N_{i \bullet }^{2 - 2\theta}\end{align*}
 
is satisfied for \red{STUB} 