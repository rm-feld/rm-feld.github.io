---
modified: 2026-07-05T19:55:52-07:00
created: 2025-10-20T17:38:20-07:00
---
 ## Single Factorization
The 3-random effect Jacobian can be given by
$$\begin{align} D = \frac{1}{\sqrt{ \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C}  + 1}}\begin{bmatrix}
\mathbf{I}_{p} & \frac{-\beta / 2}{\sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} + 1} & \frac{-\beta / 2}{\sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} + 1} & \frac{-\beta / 2}{\sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} + 1} \\
\mathbf{0}_{p}^{\intercal} &  \frac{1}{\sigma^{2}_{B} + \sigma^{2}_{C} + 1} & -\frac{\sigma^{2}_{A}}{(\sigma^{2}_{B} + \sigma^{2}_{C} + 1)^{2}} & - \frac{\sigma^{2}_{A}}{(\sigma^{2}_{B} + \sigma^{2}_{C} + 1)^{2}}\\
\mathbf{0}_{p}^{\intercal} & -\frac{\sigma^{2}_{B}}{(\sigma^{2}_{A} + \sigma^{2}_{C} + 1)^{2}} & \frac{1}{\sigma^{2}_{A} + \sigma^{2}_{C} + 1} & - \frac{\sigma^{2}_{B}}{(\sigma^{2}_{A} + \sigma^{2}_{C} + 1)^{2}} \\
\mathbf{0}_{p}^{\intercal} & -\frac{\sigma^{2}_{C}}{(\sigma^{2}_{A} + \sigma^{2}_{B} + 1)^{2}} & -\frac{\sigma^{2}_{C}}{(\sigma^{2}_{A} + \sigma^{2}_{B} + 1)^{2}} & \frac{1}{\sigma^{2}_{A} + \sigma^{2}_{B} + 1}
\end{bmatrix} \end{align}$$
for which the generalization to $K$ random effects is decently natural; index by $k = 1, \dots, K$ the appropriate variance terms $\sigma^{2}_{1}, \dots, \sigma^{2}_{K}$, and write $S = \sum_{k = 1}^{K} \sigma^{2}_{k}$. Then
$$\begin{align} D = \frac{1}{\sqrt{ S + 1 }} \begin{bmatrix}
\mathbf{I}_{p} & -\mathbf{1}_{K}^{\intercal} \otimes \beta /[2(S + 1)]  \\
\mathbf{0}_{K\times p } & \mathbf{A}
\end{bmatrix} \end{align},$$
where $\mathbf{A}(K\times K)$ is defined by the relations
$$\begin{align} \mathbf{A}_{ii} &= \frac{1}{S + 1- \sigma^{2}_{i}}, \,\,\,\,\,\,\, \mathbf{A}_{ij}= -\frac{\sigma^{2}_{i}}{(S + 1 - \sigma^{2}_{i})^{2}}.\end{align}$$

## Negation Factorization
For 3 random effects, the Jacobian is given by 
$$\begin{align} D = \frac{1}{\sqrt{ \sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C}  + 1}}\begin{bmatrix}
I_{p} & \frac{-\beta / 2}{\sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} + 1} & \frac{-\beta / 2}{\sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} + 1} & \frac{-\beta / 2}{\sigma^{2}_{A} + \sigma^{2}_{B} + \sigma^{2}_{C} + 1} \\
\mathbf{0}_{p}^{\intercal} & -\frac{\sigma^{2}_{B} + \sigma^{2}_{C}}{(\sigma^{2}_{A} + 1)^{2}} & \frac{1}{\sigma^{2}_{A} + 1}  & \frac{1}{\sigma^{2}_{A} + 1} \\
\mathbf{0}_{p}^{\intercal} & \frac{1}{\sigma^{2}_{B} + 1} & -\frac{\sigma^{2}_{A} + \sigma^{2}_{C}}{(\sigma^{2}_{B} + 1)^{2}} & \frac{1}{\sigma^{2}_{B} + 1} \\
\mathbf{0}_{p}^{\intercal} & \frac{1}{\sigma^{2}_{C} + 1} & \frac{1}{\sigma^{2}_{C} + 1} & -\frac{\sigma^{2}_{A} + \sigma^{2}_{B}}{(\sigma^{2}_{C} +1 )^{2}}
\end{bmatrix} \end{align}$$
for the negation factorization. As with the single factorization, the 
