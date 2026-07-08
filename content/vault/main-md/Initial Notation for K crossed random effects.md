---
modified: 2026-05-28T10:15:41-07:00
created: 2026-02-16T15:20:19-08:00
---
Throughout, we use the notation of integer arrays from brackets, i.e. $[N] = \left\{ 1,\dots, N \right\}$. We also use $\xi \sim \mathcal{N}(0, 1)$ as the generic unit [[Normal Distribution|normal]] placeholder for likelihood calculations. 

We consider $N$ observations of the form $\left\{ (x_{\boldsymbol{i_{\ell}}}, Y_{\boldsymbol{i}_{\ell}}) \right\}_{\ell = 1}^{N}$ for $\boldsymbol{i} = (i_{1}, \dots, i_{K})$ a multi-index for the levels of the $K$ random effects. The number of unique levels in each category is expected to grow with $N$; in particular, there are $R_{k}:=N^{\kappa_{k}}$ unique levels of the $k$th random effects, $\mathcal{i} \in \mathcal{I}_{0} \subseteq \mathcal{I} :\equiv \otimes\left\{ [R_{k}] \right\}_{k=1}^{K}$ where $\mathcal{I}_{0}$ is the (unique set of) observed indices. Note we are letting $\ell$ be a unique index for each observation, so that we may have replicates. 

We are often interested in subgroupings which share indices. In particular, we are often interested in subsets of $\mathcal{I}_{0}$ of the form 
$$\begin{align*} \mathcal{I}_{\boldsymbol{i}, \mathcal{K}}= \left\{\boldsymbol{i} \in \mathcal{I}_{0}: i_{k} := i_{k} \text{ for } k \in \mathcal{K} \subseteq [K]  \right\} . \end{align*}$$
We simplify notation in the singular cases $\mathcal{I}_{\boldsymbol{i}, \left\{ k \right\}} = \mathcal{I}_{\boldsymbol{i}, k}$, $\mathcal{I}_{\boldsymbol{i}, [K]\setminus \left\{ k \right\}} = \mathcal{I}_{\boldsymbol{i}, \neg k}$. 

It is also often the case that we are indexing through some (ordered wlog) subset $\mathcal{K} = \left\{ k_{1}, \dots, k_{\lvert \mathcal{K} \rvert} \right\}$ of the random effects. We let
$$\begin{align*} \mathcal{I}[\mathcal{K}] := \left\{ \boldsymbol{j} \in \otimes \left\{ [N^{\kappa_{k}}]  \right\} _{k \in \mathcal{K}} : \exists \, \boldsymbol{i} \in \mathcal{I}_{0} \text{ such that } i_{k} = j_{k} \; \forall k \in \mathcal{K} \right\},   \end{align*}$$
$\boldsymbol{i}[\mathcal{K}] := (i_{k_{1}}, \dots, i_{k_{\lvert \mathcal{K} \rvert}})$. In words, $\mathcal{I}[\mathcal{K}]$ is the unique set of observed indices *over only the categories indexed by $\mathcal{K}$.*

We emphasize here that $\boldsymbol{j}$ is a slice of the indices not generally of the same shape as $\boldsymbol{i}$. This is to emphasize operations over a category or set of categories, and to disentangle the events $\boldsymbol{i}_{\ell}[\mathcal{K}] = \boldsymbol{i}_{\ell'}[\mathcal{K}]$ and $\boldsymbol{i}_{\ell} = \boldsymbol{i}_{\ell'}$. As an example, $\mathcal{I}[\left\{ 1 \right\}] = [R_{1}]$ is the set of all unique observed levels of the first category, and $S[\left\{ 1, 2 \right\}] \subseteq [R_{1}]\times [R_{2}]$ is the set of all observed pairs of the first two categories (not the whole cartesian product). The number of indices indexed by $\boldsymbol{j}$ is $|\mathcal{K}|$. 

It is reasonable here to overload notation so that the first argument of $\mathcal{I}$ can take subsets of the indices when arguments conform. That is, we let 
$$\begin{align*} \mathcal{I}_{\boldsymbol{j}, \mathcal{K}} := \left\{ \boldsymbol{i} \in \mathcal{I}_{0}: \boldsymbol{i}[\mathcal{K}] =  \boldsymbol{j}  \right\}.   \end{align*}$$


Generically, we give the $K$-crossed random effects model by the following. 

![[K-Crossed Random Effects Model]]

To be more direct, the choice of $\mathbb{A}$ coincides with the definition of the model with respect to the chosen set of interaction terms considered. 

We let $\tilde{Y}_{\boldsymbol{i}}:= 2Y_{i} - 1 \in\left\{ -1, 1 \right\}$, which is convenient for simplifying likelihoods. 

We use $\ell$ to index individual observations, so that $a_{\ell} := a_{\boldsymbol{i}(\ell)} := (a_{i_{1}}, \dots, a_{i_{k}})^{\intercal}$, and $a_{\ell}[\mathcal{K}]:=a_{\boldsymbol{i}(\ell)}[\mathcal{K}]$. 

Finally, we consider counting via collapsing over indices. We subscript $N$ for observation subcounts, with analogous structure to the above. That is, 
$$\begin{align*} N_{\boldsymbol{i'}, \mathcal{K}} := \sum_{\ell = 1}^{N}  \prod_{k \in \mathcal{K}} \mathbf{1}\left[i'_{k} = i_{k}(\ell) \right] ,  \end{align*}$$
with the same caveat of conforming arguments and shortcuts $N_{i, k}:= N_{i, \left\{ k \right\}}$, $N_{\boldsymbol{i}, \neg k} = N_{\boldsymbol{i}, [K]\setminus \left\{ k \right\}}$. We further let $N_{\boldsymbol{i}}:= N_{\boldsymbol{i}, [K]}$. When there are no replicates, $N_{\boldsymbol{i}} = Z_{\boldsymbol{i}} = \mathbf{1}\left[\boldsymbol{i} \in \mathcal{I}_{0} \right]$. Note that $N_{i\bullet}$ of [[ARC]] is $N_{i, 1}$. In words, this is the number of observed data points which have $i$ as the level of the first category, as opposed to the number of unique indices $\boldsymbol{i}$ which share the level $i$ in their first category. The second referenced object can be obtained by $|\mathcal{I}_{i, 1}|$. 