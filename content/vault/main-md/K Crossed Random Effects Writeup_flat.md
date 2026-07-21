---
tags:
  - no-index
up: "[[K Crossed Random Effects Writeup]]"
modified: 2026-07-13T11:28:32-07:00
created: 2026-07-13T11:05:41-07:00
---


# Notation and Model Definition 
Throughout, we use the notation of integer arrays from brackets, i.e. $[N] = \left\{ 1,\dots, N \right\}$. We also use $\xi \sim \mathcal{N}(0, 1)$ as the generic unit [[Normal Distribution|normal]] placeholder for likelihood calculations. 

We consider $N$ observations of the form $\left\{ (x_{\ell}, Y_{\ell}) \right\}_{\ell = 1}^{N}$ for $\boldsymbol{i} = (i_{1}, \dots, i_{K})$ a multi-index for the levels of the $K$ random effects. The number of unique levels in each category is expected to grow with $N$; in particular, there are $R_{k}:=N^{\kappa_{k}}$ unique levels of the $k$th random effects, $\mathcal{i} \in \mathcal{I}_{0} \subseteq \mathcal{I} :\equiv \otimes\left\{ [R_{k}] \right\}_{k=1}^{K}$ where $\mathcal{I}_{0}$ is the (unique set of) observed indices. Note we are letting $\ell$ be a unique index for each observation, so that we may have replicates. 

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

> [!attention] K-Crossed Random Effects Model
> Let $\mathbb{A} \subseteq 2^{[K]}\setminus \left\{ \emptyset \right\}$. The $K$-**crossed random effects model** is given by 
> $$\begin{align*} \mathbb{E}(Y_{\ell} \mid x_{\ell}, a_{\ell}) = g^{-1}\left( x_{\ell}^{\intercal}\beta + a_{\ell}^{\intercal}\mathbf{1} \right), \end{align*}$$
> where $a_{\ell} := a_{\boldsymbol{i}(\ell)}$ are a flattened vector encoding with components $a_{\boldsymbol{i}, \mathcal{K}}$, $\mathcal{K} \subseteq \mathbb{A}$. Components are i.i.d. within each slice, $a_{\boldsymbol{i}, \mathcal{K}} \sim \mathcal{N}(0, \sigma^{2}_{\mathcal{K}})$ over $\boldsymbol{i}[\mathcal{K}] \in \mathcal{S}[\mathcal{K}]$. As standard, random effects are shared when components are shared, so that $a_{\boldsymbol{i}, \mathcal{K}} = a_{\boldsymbol{i}', \mathcal{K}}$ when $\boldsymbol{i}[\mathcal{K}] = \boldsymbol{i}'[\mathcal{K}]$. Here and throughout, we use $a_{\ell}^{\intercal}\mathbf{1}$ as a shorthand for 
> $$\begin{align*} a_{\ell}^{\intercal}\mathbf{1} := \sum_{\mathcal{K} \in \mathbb{A}} a_{\boldsymbol{i}, \mathcal{K}} .\end{align*}$$

There is an expectation that $\mathbb{A}_{1} :=\left\{ \left\{ k \right\} \right\}_{k =1}^{K} \subseteq \mathbb{A}$. I am giving the subscript by cardinality, as might be preferred; that is, $\mathbb{A}_{m}= \left\{ \mathcal{K} \subseteq 2^{[K]} : |\mathcal{K}| = m\right\}$. We can then define interactions up to a desired depth, $\mathbb{A}_{\leq m} = \left\{ \mathcal{K} \subseteq 2^{[K]}: |\mathcal{K}| \leq m \right\}$.

To be more direct, the choice of $\mathbb{A}$ coincides with the definition of the model with respect to the chosen set of interaction terms considered. 

$Y_{\boldsymbol{i}} \in \left\{ -1, +1 \right\}$ is $\pm 1$-valued by default (no separate tilde/signed transform needed — $\tilde{\cdot}$ is reserved for other objects, e.g. slice-decay terms and growth-rate exponents). 

We use $\ell$ to index individual observations, so that $a_{\ell} := a_{\boldsymbol{i}(\ell)} := (a_{i_{1}}, \dots, a_{i_{k}})^{\intercal}$, and $a_{\ell}[\mathcal{K}]:=a_{\boldsymbol{i}(\ell)}[\mathcal{K}]$. 

Finally, we consider counting via collapsing over indices. We subscript $N$ for observation subcounts, with analogous structure to the above. That is, 
$$\begin{align*} N_{\boldsymbol{i'}, \mathcal{K}} := \sum_{\ell = 1}^{N}  \prod_{k \in \mathcal{K}} \mathbf{1}\left[i'_{k} = i_{k}(\ell) \right] ,  \end{align*}$$
with the same caveat of conforming arguments and shortcuts $N_{i, k}:= N_{i, \left\{ k \right\}}$, $N_{\boldsymbol{i}, \neg k} = N_{\boldsymbol{i}, [K]\setminus \left\{ k \right\}}$. We further let $N_{\boldsymbol{i}}:= N_{\boldsymbol{i}, [K]}$. When there are no replicates, $N_{\boldsymbol{i}} = Z_{\boldsymbol{i}} = \mathbf{1}\left[\boldsymbol{i} \in \mathcal{I}_{0} \right]$. Note that $N_{i\bullet}$ of [[ARC]] is $N_{i, 1}$. In words, this is the number of observed data points which have $i$ as the level of the first category, as opposed to the number of unique indices $\boldsymbol{i}$ which share the level $i$ in their first category. The second referenced object can be obtained by $|\mathcal{I}_{i, 1}|$.

## Notation Alignment with ARC 
We give the logic heuristics and equivalent objects of interest between the new notation and the previous notation, for $K = 3$. We also include some preview of the interaction results, as relevant for $\mathbb{A}$. 

We motivate the notation by checking alignment with the objects of interest in standard [[ARC]], for the probit case under $K = 3$. We will be improper in the sense that we will temporarily disconnect $k$ as enumerating the categories, so that we can use $c_{k}$ as the third random effect. The given previews some of the results of the paper. 

We reiterate that $\mathbb{A}$ is in essence a model definition for interactions. The standard case without interactions coincides with $\mathbb{A} = \left\{ \left\{ 1 \right\} , \left\{ 2 \right\}, \left\{ 3 \right\}\right\}$, 
$$\begin{align*} Y_{ijk} &= \mathbf{1}\left[x_{ijk}^{\intercal}\beta + a_{i} + b_{j} + c_{k} + \varepsilon_{ijk} > 0 \right] ,  \end{align*}$$
while the model $\mathbb{A}_{\leq 2} := \left\{ \left\{ 1 \right\}, \left\{ 2 \right\}, \left\{ 1, 2 \right\}, \left\{ 2, 3 \right\}, \left\{ 1, 3\right\} \right\}$ corresponds to the model 
$$\begin{align*} Y_{ijk} = \mathbf{1}\left[x_{ijk}^{\intercal}\beta + a_{i} + b_{j} + (ab)_{ij} + (bc)_{jk} + (ac)_{ik} + \varepsilon_{ijk} > 0\right] . \end{align*}$$
If we have some prior knowledge about expected interactions, we may omit certain terms from the above; for example, if we do not expect to need the interaction between $a$ and $b$, we can assign  $\mathbb{A} = \left\{ \left\{ 1 \right\}, \left\{ 2 \right\}, \left\{ 3 \right\}, \left\{ 2, 3 \right\}, \left\{ 1, 3 \right\} \right\}$ as our model. We do not let $\emptyset \in \mathbb{A}$, and it is expected that $\left\{ 1 \right\}, \left\{ 2 \right\}, \left\{ 3 \right\} \in \mathbb{A}$, though such a statement should hold without loss of generality provided that interactions are only included when their (nontrivial) subsets are included. As an example $\mathbb{A} = \left\{ \left\{ 1 \right\}, \left\{ 3 \right\}, \left\{ 1, 3 \right\} \right\}$ implicitly indexes a $K = 2$ model with interaction term $(ac)_{ik}$. However, $\mathbb{A} = \left\{ \left\{ 1 \right\}, \left\{ 3 \right\}, \left\{ 1, 3 \right\}, \left\{ 2, 3 \right\} \right\}$ violates the subset rule as $\left\{ 2 \right\} \notin \mathbb{A}$ but $\left\{ 2, 3 \right\} \in \mathbb{A}$. 

If $\left\{ 1, 2, 3 \right\} \in \mathbb{A}$, then we are implicitly discussing interactions, which makes the $(i, j, k)$ index ambiguous; thus it seems natural to have a unique index $\ell = 1, \dots, N$ for observations, with $\boldsymbol{i}(\ell) := (i_{\ell}, j_{\ell}, k_{\ell})$ the multi-index; in that case, $Y_{\ell} = Y_{\boldsymbol{i}(\ell)} = Y_{(i_{\ell}, j_{\ell}, k_{\ell})}$ seems natural. Under this regime, though, the random effects and interaction terms, eg. $(ab)_{i_{\ell}j_{\ell}}$, start to be unwieldy. We can use two arguments in the subscript to simplify these relations; we collect all random effects (including interaction terms) with the index $\boldsymbol{i}$ and a selector $\mathcal{K}$, so that 
$$\begin{align*} a_{\boldsymbol{i}, \left\{ 1, 2 \right\} } := a_{(i, j, k), \left\{ 1, 2 \right\} }:= (ab)_{ij}. \end{align*}$$
Thus any term of the form $a_{\boldsymbol{i}, \mathcal{K}}$ can index either a main effect or an interaction term, with $a_{\boldsymbol{i}, 1} = a_{i}$, $a_{\boldsymbol{i}, 2} = b_{j}$, $a_{\boldsymbol{i}, 3} = c_{k}$. But this brings another source of tension in the notation; it is awkward to always associate, say, $a_{i}$ in the original notation with the whole multi-index $a_{\boldsymbol{i}, 1}$, as the second and third components of $\boldsymbol{i}$ are meaningless in this setting. Thus we overload notation to also let the first subscript argument be only a slice of the multi-index, when arguments conform; eg. $a_{(j), 2} = b_{j}$ (notice $j$ is unbolded). Similarly, we can let $a_{(i, j), \left\{ 1, 2 \right\}} = (ab)_{ij}$. To emphasize that the first argument is a slice and not the full multi-index, we use $\boldsymbol{j}$ in place of $\boldsymbol{i}$ for a generic slice. Following standard conventions in programming, we use brackets for multi-index component selection, so that, eg., $\boldsymbol{i}[\left\{ 1, 3 \right\}] = (i, k)$. 

Continuing the above thread, how do we actually iterate through the multi-index slices? It is helpful in this regime to return to the observation structure. We let $\mathcal{S}_{0}$ be the set of all observed triples $(i, j, k)$, out of all possible triples $\mathcal{S}:= [N_{1}] \times [N_{2}]\times [N_{3}]$. The set of all unique doubles $(i, k)$ can be given by $\mathcal{S}[\left\{ 1, 3 \right\}]$. It is also helpful to define slices; for example, the unique set of all triples whose second category is $j^{\star}$ can be given by $\mathcal{S}_{j^{\star}, \left\{ 2 \right\}}$. Note the interpretation that this is "all of the indices that agree with the first argument over the categories specified in the second argument." Further note that elements of $S_{j^{\star}, \left\{ 2 \right\}}$ are of the full multi-index, i.e. triples, as opposed to $\mathcal{S}[\cdot]$; thus we keep the convention of $\boldsymbol{j} \in \mathcal{S}[\cdot]$ and $\boldsymbol{i} \in \mathcal{S}_{\cdot, \cdot}$. We can index the actual observations by $\ell: \boldsymbol{i}(\ell) \in S_{j^{\star}, \left\{ 2 \right\}}$. 

What if we don't want a unique count, but a total count? The analogues of the above are natural; $N_{j^{\star}, \left\{ 2 \right\}}$ is the number of observations whose second category is $j^{\star}$. In ARC notation without replicates, this is exactly $N_{\bullet j^{\star} \bullet}$. With replicates, we can make the distinction between this and $|\mathcal{S}_{j^{\star}, \left\{ 2 \right\}}|$, which is again the uniquely observed indices (and in this case would coincide with $N^{\kappa_{2}}$). This is especially important when we encounter more complex observation structures under high cardinality. %% Take the catastrophic case where we only observe $i$ and $j$ under a diagonal, i.e., all of our observations are of the form $(i, i, k)$.  %%

Finally, we bring up one hanging ambiguity; it is taxing in the generic case to enumerate the set of all interactions, or the relevant selection therein. To be explicit, consider the conditional probability over "$i$ and $j$"; previewing later results,
$$\begin{align*} \mathbb{P}(Y_{ijk} = 1 \mid a_{i}, b_{j}, (ab)_{ij}) &= \Phi \left( x_{ijk}^{\intercal}\gamma \sqrt{ 1 + \tau^{2}_{\neg 3} } + \sigma ^{-1} (a_{i} + b_{j} + (ab)_{ij})\right). \end{align*}$$
The vector component sum $v^{\intercal}\mathbf{1} = \sum_{i =1}^{p} v_{i}$ is often helpful to clean up the notation, but how do we cleanly index $( a_{i}, b_{j}, (ab)_{ij}) := \otimes \left\{ a_{\boldsymbol{i}, \mathcal{K}}: \mathcal{K} \subseteq \left\{ 1, 2 \right\} \right\}$ (omitting $\emptyset$)? How do we distinguish it from $( a_{i}, b_{j} )$? It turns out that we don't often need the latter object, so for now, we have adopted the notation 

$$\begin{align*} a_{\boldsymbol{i}}[\mathcal{K}]^{\intercal}\mathbf{1} := \sum_{\mathcal{K}' \subseteq \mathcal{K} : \mathcal{K}' \subseteq \mathbb{A}} a_{\boldsymbol{i}, \mathcal{K'}}\end{align*}$$
to discuss the sum of such observations, so that the above probability can be written as 

$$\begin{align*} \mathbb{P}(Y_{ijk} = 1 \mid a_{\boldsymbol{i}}[\left\{ 1, 2 \right\} ]) &= \Phi\left( x_{ijk}^{\intercal}\gamma \sqrt{ 1 + \tau^{2}_{\neg 3} } + a_{\boldsymbol{i}}[\left\{ 1, 2 \right\} ]^{\intercal}\mathbf{1}\right).\end{align*}$$
But perhaps using a different symbol for the sum or the implicit vector representation is appropriate - very open to suggestions!


# Main Result
 
The latent variable form is helpful in this regime. 

> [!attention] K-Crossed Random Effects Probit Model 
> The **Standard K-Crossed Random Effects Probit Model** can be given in latent variable form by
> $$\begin{align*} Y_{\ell} := 2\cdot\mathbf{1}\left[x_{\ell}^{\intercal}\beta + a_{\ell}^{\intercal}\mathbf{1} + \varepsilon_{\ell} > 0 \right] - 1 \in \left\{ -1, +1 \right\},  \end{align*}$$
> for $\varepsilon_{\ell} \overset{\mathrm{i.i.d.}}{\sim}\mathcal{N}(0, \sigma^{2}_{E})$. 

In this case, it can be helpful to invoke $\sigma^{2} := \sigma^{2}_{E} + \sum_{k=1}^{K} \sigma^{2}_{k}$ the total variance. Our interest is in the estimation of $\theta = \left( \beta ^{\intercal}, \sigma_{1}^{2}, \dots, \sigma_{K}^{2} \right)^{\intercal}$.

Following the standard grooves of [[ARC]], we can compute marginal, and row (or "slice") likelihoods, in order to retrieve information about $\sigma^{2}_{K}$ components and $\beta$. 

## Marginal Likelihood 
The marginal likelihood for the [[K-Crossed Random Effects Probit Model|probit model]] can be given by
$$\begin{align*} \mathbb{P}(Y_{\ell} = y_{\ell} \mid x_{\ell}) &= \mathbb{P}\left( y_{\ell} \left[ x_{\ell}^{\intercal}\beta + a_{\ell}^{\intercal}\mathbf{1} + \varepsilon_{\ell} \right] > 0 \right) \\ 
&= \mathbb{P}\left( y_{\ell} \left[x_{\ell}^{\intercal}\beta + \sigma\xi \right] > 0 \right) \\ 
&= \mathbb{P}\left( \frac{y_{\ell}x_{\ell}^{\intercal}\beta}{\sigma } > -\xi\right) \\
&:= \Phi\left( y_{\ell}x_{\ell}^{\intercal}\gamma \right)
\end{align*}$$
for $\gamma = \sigma^{-1 / 2} \beta$. 

In turn, it is natural to define the all likelihood as 

$$\begin{align*} L_{\text{all}}(\gamma) := \prod_{\ell = 1}^{N} \Phi\left( y_{\ell}x_{\ell}^{\intercal}\gamma \right) \end{align*}$$
and corresponding log-likelihood 
$$\begin{align*} \mathcal{L}_{\text{all}}(\gamma) := \sum_{\ell = 1}^{N} \log \Phi\left( y_{\ell} x_{\ell}^{\intercal} \gamma \right)  .\end{align*}$$
> [!tip] Consistency of All Likelihood for K-Crossed Random Effects Probit Model
> 
> 
> Let $\left\{ (x_{\ell}, Y_{\ell}) \right\}_{\ell =1}^{N}$ follow the $k$-crossed random effects probit model with true parameter $\gamma_{0} = \beta / \sigma$. Let $N \to \infty$, while $\max_{k \in [K]} \epsilon_{k} \to 0$. Further, let us satisfy the following: 
> 1. **(Uniform Boundedness of $x_{\ell}$)** $\left\lvert\left\lvert x_{\ell} \right\rvert\right\rvert \leq B < \infty$, 
> 2. **(Nondegeneracy of $x_{\ell}$)** $N^{-1} \sum_{\ell=1}^{N} x_{\ell}x_{\ell}^{\intercal} \to V \in \mathbb{R}^{p\times p}$ [[Positive Semidefinite|positive definite]], 
> 3. **(No Linear Subspace)** there does not exist $v \in \mathbb{R}^{p}$ such that $v^{\intercal}x_{\ell} \geq 0$ for all $Y_{\ell} = 1$ and $v^{\intercal}x \leq 0$ for all $Y_{\ell} = 0$. 
> If $\hat{\gamma}$ is any maximizer of the [[K-Crossed Marginal Probit Likelihood|all likelihood]], Then we have [[Convergence in Probability|convergence in probability]] of $\hat{\gamma}$ to $\gamma_{0}$,
> $$\begin{align*} \mathbb{P}(\left\lvert\left\lvert \hat{\gamma} - \gamma_{0} \right\rvert\right\rvert  > \epsilon) \to  0 \end{align*}$$
> as $N \to \infty$. 
^all-consistency

> [!success]- %% %%
>
> 
> We follow the proof of $\gamma$ consistency as given in [[@bellioConsistentScalableComposite2025]]. Letting 
> $$\begin{align*} \eta_{\ell}(\gamma) := Y_{\ell} \log \Phi\left( x_{\ell}^{\intercal}\gamma  \right) + (1 - Y_{\ell}) \log \Phi\left( -x_{\ell}^{\intercal}\gamma \right),\end{align*}$$
> we have $\eta_{\ell}(\gamma) < B$ for some $B$ by the uniform boundedness condition on $x_{\ell}$. In this case
> $$\begin{align*} \text{Var}\left( \frac{\mathcal{L}_{\text{all}}(\gamma)}{N} \right)  &\leq \frac{B^{2}}{N^{2}} \sum_{\ell = 1}^{N} \sum_{\ell' = 1}^{N} \left\{ \sum_{\emptyset \neq \mathcal{K} \subseteq [K]} (-1)^{|\mathcal{K}|} \prod_{k \in \mathcal{K}} \mathbf{1}\left[i_{k}(\ell) = i_{k}(\ell')\right]  \right\}. \\
> 
> \end{align*}$$
> Note that the expansion of the incluson-exclusion nets at most $2^{K} -1$ terms (some negative); by the fact that $\mathbf{1}\left[i_{k} = i'_{k} \right] \geq \prod_{k'\in \mathcal{K}} \mathbf{1}\left[i_{k'} =i'_{k'} \right]$ when $k \in \mathcal{K}$, we can upper bound the inclusion-exclusion expansion. Following the logic, 
> 
> $$\begin{align*} \text{Var}\left( \frac{\mathcal{L}_{\text{all}}(\gamma)}{N} \right) &\leq \frac{B^{2}2^{K-1}}{N^{2}} \sum_{\ell =1}^{N} \sum_{\ell' =1}^{N}  \left\{ \sum_{k =1}^{K} \mathbf{1}\left[i_{k}(\ell) = i_{k}(\ell') \right]  \right\} \\ 
> &= \frac{B_{1}^{2}}{N^{2}} \sum_{k =1}^{K}\sum_{i_{k} =1}^{R_{k}} N_{i_{k}, k}^{2} \\
> &\leq \frac{B_{1}^{2}}{N^{2}} \sum_{k =1}^{K} \sum_{i_{k} =1}^{R_{k}} N_{i_{k}, k}N\epsilon_{k} \\ 
> &\leq B^{2} \left\{ \sum_{k=1}^{K}\epsilon_{k} \right\} \to  0. 
> \end{align*}$$
> Again by the proof in [[@bellioConsistentScalableComposite2025]], both sides of the limiting log likelihood statement are concave in $\gamma$, and $\gamma_{0}$ is a maximizer the limiting log-likelihood. We thus get that $\gamma$ is a unique maximizer. $\blacksquare$
## Slice Likelihood 
There is much ambiguity in what might be the slice of interest in this regime. We give the generic one, then what might be the natural standard one. 

Let $\mathcal{K}, \overline{\mathcal{K}}$ be disjoint with $\mathcal{K}\cup \overline{\mathcal{K}} = [K]$.  By component independence, we can decompose variance as $\sigma^{2} = \sigma^{2}_{(\mathcal{K})} + \sigma^{2}_{(\overline{\mathcal{K}})}$, for 

$$\begin{align*} \sigma_{(\mathcal{K})}^{2} := \sum_{\mathcal{K}' \subseteq \mathcal{K}, \mathcal{K} \in \mathbb{A}} \sigma^{2}_{\mathcal{K'}}. \end{align*}$$
Note the use of parentheses to differentiate from the interaction terms indexed by $\mathcal{K}$.

Throughout, we use the shortand 
$$\begin{align*} a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} = \sum_{\mathcal{K}' \subseteq \mathcal{K}, \mathcal{K}' \in \mathbb{A}} a_{\ell, \mathcal{K}'}. \end{align*}$$


$$\begin{align*} \mathbb{P}(Y_{\ell} = y_{\ell} \mid x_{\ell}, a_{\ell}[\mathcal{K}]) &= \mathbb{P}\left( y_{\ell}\left[ x_{\ell}^{\intercal}\beta + a_{\ell}^{\intercal}\mathbf{1} + \varepsilon_{\ell} > 0 \right] \right) \\ 
&= \mathbb{P}\left( y_{\ell}\left[ x_{\ell}^{\intercal}\beta + a_{\ell}[\mathcal{K}]^{\intercal} \mathbf{1} + a_{\ell}[\overline{\mathcal{K}}]^{\intercal} \mathbf{1} + \varepsilon_{\ell}  \right] > 0\right) \\ 
&= \mathbb{P}\left( y_{\ell} \left[ x_{\ell}^{\intercal}\beta + a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} + \xi \sqrt{ \sigma^{2}_{(\overline{\mathcal{K}})} +  \sigma^{2}_{E}} \right] > 0\right) \\ 
&= \Phi\left( \frac{y_{\ell}\left[ x_{\ell}^{\intercal}\beta + a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} \right]}{\sqrt{ \sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E} }}  \right) \\ 
&= \Phi\left( \frac{y_{\ell}\left[ x_{\ell}^{\intercal}\beta + a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} \right]}{\sqrt{\sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E} }} \cdot \frac{\sqrt{ \sigma^{2}_{(\mathcal{K})} + \sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E} }}{\sqrt{ \sigma^{2}_{(\mathcal{K})} + \sigma^{2}_{(\overline{\mathcal{K}})}+ \sigma^{2}_{E}  }} \right) \\ 
&:= \Phi\left(y_{\ell}x_{\ell}^{\intercal}\gamma \sqrt{ 1 + \tau^{2}_{\mathcal{K}} } + \frac{a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1}}{\sqrt{ \sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E} }} \right) \\
&:= \Phi\left( y_{\ell}x_{\ell}^{\intercal}\gamma_{\mathcal{K}} + \tau_{\mathcal{K}} u_{\boldsymbol{j}}\right),
\end{align*}$$

where $\gamma_{\mathcal{K}_0} = \gamma \sqrt{ 1 + \tau^{2}_{\mathcal{K}} }$ and $u_{\boldsymbol{j}} = a_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} / \tau_{\mathcal{K}}$ ($\boldsymbol{j}:= \boldsymbol{i}_{\ell}[\mathcal{K}]$) for 
$$\begin{align*} \tau^{2}_{\mathcal{K}} = \frac{\sigma_{(\mathcal{K})}^{2}}{\sigma^{2}_{(\overline{\mathcal{K}})} + \sigma^{2}_{E}} = \frac{\sigma^{2}_{(\mathcal{K})}}{\sigma^{2} - \sigma _{(\mathcal{K})}^{2}}.   \end{align*}$$
Note $u_{\ell}[\mathcal{K}]^{\intercal}\mathbf{1} \sim \mathcal{N}(0, 1)$. 

The corresponding **slice likelihood** in this case can be given by 
$$\begin{align*} L_{\mathcal{K}}(\tau^{2}_{\mathcal{K}}) &:= \prod_{\boldsymbol{j} \in \mathcal{S}[\mathcal{K}]} \int _{\mathbb{R}} L_{\boldsymbol{j}}(\gamma_{\mathcal{K}} \mid u_{\boldsymbol{j}}) \,\tau_{\mathcal{K}}^{-1}  \varphi \left( \frac{u_{\boldsymbol{j}}}{\tau_{\mathcal{K}}} \right) \, du_{\boldsymbol{j}} \\ 
&= \tau_{\mathcal{K}}^{-|\mathcal{S}[\mathcal{K}]|} \prod_{\boldsymbol{j} \in \mathcal{S}[\mathcal{K}]} \int _{\mathbb{R}} L_{\boldsymbol{j}}(\gamma_{\mathcal{K}} \mid u_{j}) \, \varphi \left( \frac{u_{\boldsymbol{j}}}{\tau_{\mathcal{K}}} \right) \, du_{\boldsymbol{j}}, \end{align*}$$
^slice-likelihood

where
$$\begin{align*} L_{\boldsymbol{j}}(\gamma_{\mathcal{K}} \mid u_{\boldsymbol{j}}) &:= \prod_{\ell \in [N]: \boldsymbol{i}_{\ell}[\mathcal{K}] = \boldsymbol{j}} \Phi\left( x_{\ell}^{\intercal}\gamma_{\mathcal{K}} + \tau_{\mathcal{K}} u_{\boldsymbol{j}} \right) \\ 
&:= \prod_{\boldsymbol{i}_{\ell} \mid \boldsymbol{j}} \Phi\left( x_{\ell}^{\intercal} \gamma_{\mathcal{K}} + \tau_{\mathcal{K}} u_{\boldsymbol{j}} \right).  \end{align*}$$
As standard in our regime, we generally restrict likelihood to be over only terms with at least two terms in the inner product, $N_{\boldsymbol{j}, \mathcal{K}} \geq 2$.


### Singular Factorization 
We now work more specifically on the classical no-interactions subcase, so that $\mathbb{A} = \mathbb{A}_{1}$. 

Under the structure of [[K-Crossed Slice Probit (Singular)|the derived slice likelihood]], we can take in particular $\mathcal{K} = \left\{ k \right\}$. In this case, 

$$\begin{align*} L_{k}(\tau^{2}_{k}) := \tau^{-R_{k}}\prod_{j=1}^{R_{k}} \int _{\mathbb{R}}  L_{j} (\gamma_{k}\mid u_{j})\,  \varphi \left( \frac{u_{j}}{\tau_{k}} \right) \, du_{j} \end{align*}$$
for
$$\begin{align*} L_{j} (\gamma_{k} \mid u_{j}) &= \prod_{\boldsymbol{i}_{\ell} \mid j} \Phi\left( x_{\ell}^{\intercal}\gamma_{k} + \tau_{k}u_{j} \right).  \end{align*}$$
In this formulation, we can write 
$$\begin{align*} \tau_{k}^{2} = \frac{\sigma^{2}_{k}}{\sigma^{2} - \sigma^{2}_{k}} \in [0, 1] .  \end{align*}$$
In implementation, we often invoke the one-to-one transformation $\rho_{k} = \tau^{2}_{k} / [1 + \tau^{2}_{k}]$, inverted by $\tau^{2}_{k} = \rho_{k} / [1 - \rho_{k}]$. What is nice in this case is that  ^c05d20
$$\begin{align*} \rho_{k} &= \frac{\sigma^{2}_{k} / [\sigma^{2} - \sigma^{2}_{k}]}{1 + \sigma^{2}_{k} / [\sigma^{2} - \sigma^{2}_{k}]} \\ 
&= \frac{\sigma^{2}_{k}}{\sigma^{2} - \sigma^{2}_{k} + \sigma^{2}_{k}} \\
&= \sigma^{2}_{k} / \sigma^{2}
. \end{align*}$$
^singular-rho

What is important in this regime is that $\psi = \left( \gamma ^{\intercal}, \rho_{1}, \dots, \rho_{K} \right)^{\intercal}$ is a valid reparameterization of $\theta$. From $\sum_{k=1}^{K} \rho_{k} = 1 - \sigma^{2}_{E} / \sigma^{2}$, we can recover $\theta$ by 
$$\begin{align*} \sigma^{2} = \frac{\sigma^{2}_{E}}{1 - \sum_{k=1}^{K} \rho_{k}}, \qquad \sigma^{2}_{k} = \rho_{k} \sigma^{2}, \qquad \beta =\gamma / \sigma.  \end{align*}$$

Thus we can evaluate slice likelihoods over $\mathcal{K} \in \mathbb{A}_{1}$ to determine component-wise variances.
### Interaction Terms 
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

### Consistency of the Slice Likelihood 
I think that there are opportunities to make this tighter, but the immediate statement available to us is given by the following. 

> [!tip] Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model
> 
> In addition to the assumptions of [[Consistency of All Likelihood for K-Crossed Random Effects Probit Model#^all-consistency|+]], let there exist a subset $\tilde{\mathcal{S}} \subseteq \mathcal{S}_{0}$ that satisfy the following:
> 1. $|\tilde{\mathcal{S}}[\mathcal{K}]| = |\mathcal{S}[k]|$ for $k \in \mathcal{K}$, 
> 2. $|\tilde{\mathcal{S}}[\overline{\mathcal{K}}]| = |\tilde{S}[k]|$ for $k \in \overline{\mathcal{K}}$, 
> 3. $\tilde{N}_{\boldsymbol{j}, \mathcal{K}} \geq 2$ for all $\boldsymbol{j} \in \tilde{S}[\mathcal{K}]$, and 
> 4. $|\tilde{S}| \to \infty$ with $N$. 
> Then there is a root of the $\mathcal{K}$-slice likelihood equation that is a consistent estimator for $\tau^{2}_{\mathcal{K}}$. 
> 
^slice-cramer-consistency

In words, conditions 1 and 2 can be interpreted as … see [[City Block Figures]] for visual intuition. 

%% %%

> [!success]- %% %%
> 
> We give the analogue of the subset argument of [[@jiangSubsetArgumentConsistency2013]] as utilized in [[@bellioSupplementaryMaterialConsistent]]. 
> 
> To show [[Cramer Consistency|Cramer consistency]] of the slice estimator $\hat{\tau}^{2}_{\mathcal{K}}$, we require that a subset of the data whose likelihood coincides with the misspecified likelihood grows with $N$ in the limit. That is, if there exists $\tilde{\mathcal{S}} \subseteq \mathcal{S}_{0}$ growing with $N$ for which the estimator that maximizes the slice likelihood [[K-Crossed Slice Probit Likelihood#^slice-likelihood|+]] is exactly the [[MLE]] of an equicorrelated probit model. Let $\tilde{N}$ be the analogue count object. In order to coincide with the MLE, we require the following:
> 1. $|\tilde{\mathcal{S}}[\mathcal{K}]| = |\mathcal{S}[k]|$ for $k \in \mathcal{K}$, 
> 2. $|\tilde{\mathcal{S}}[\overline{\mathcal{K}}]| = |\tilde{S}[k]|$ for $k \in \overline{\mathcal{K}}$, and
> 3. $\tilde{N}_{\boldsymbol{j}, \mathcal{K}} \geq 2$ for all $\boldsymbol{j} \in \tilde{S}[\mathcal{K}]$. 
> %% #TODO replicates control in the notation is unclear%%
> In words, 1 and 2 enforce that the only interaction between units is through $u_{\boldsymbol{j}}$; 1 an *inter-slice* restriction that helps enforce the independence of the outermost product, and 2 an *intra-slice* restriction that lets observations within each slice $\boldsymbol{j} \in \tilde{\mathcal{S}}[\mathcal{K}]$ correspond to an equicorrelated probit model (though we note that this must be persistent across slices). 3 is the standard observation threshold at which we include terms in the innermost product. 
> 
> If $|\tilde{S}| \to \infty$ with $N$, the exact argument of [[@bellioSupplementaryMaterialConsistent]] holds; reproducing it here for completeness, let decompose $\tilde{S}^{C} = \mathcal{S}_{0} \setminus \tilde{\mathcal{S}}$, and let $y_{[1]}$ be the $Y_{\ell}$ values for $\boldsymbol{i}(\ell) \in \tilde{\mathcal{S}}$, $y_{[2]} \in \tilde{S}^{C}$. for $Y_{[2]}$ the set of all possible values of $y_{[2]}$, 
> 
> $$\begin{align*} \mathbb{P}\left\{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]}, y_{[2]}) \leq P_{\tau^{2}_{\mathcal{K}} + \epsilon} (y_{[1]}, y_{[2]}) \mid y_{[1]}\right\} &= \mathbb{P}\left\{ \frac{P_{\tau^{2}_{\mathcal{K}} + \epsilon} (y_{[1]}, y_{[2]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]}, y_{[2]})} \geq 1 \mid y_{[1]} \right\} \\ 
> &\leq \mathbb{E}\left\{ \frac{P_{\tau^{2}_{\mathcal{K}} + \epsilon}(y_{[1]}, y_{[2]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]}, y_{[2]})} \mid y_{[1]}\right\} \\ 
> &= \sum_{y_{[2]} \in Y_{[2]}} \frac{P_{\tau^{2}_{\mathcal{K}} + \epsilon}(y_{[1]}, y_{[2]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]}, y_{[2]})}  p_{\tau^{2}_{\mathcal{K}}}(y_{[2]} \mid y_{[1]}) \\ 
> &= \sum_{y_{[2]} \in Y_{[2]}}\frac{P_{\tau^{2}_{\mathcal{K}} + \epsilon}(y_{[1]}, y_{[2]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]})} \\ 
> &= \frac{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]})}{P_{\tau^{2}_{\mathcal{K}}}(y_{[1]})}, 
> \end{align*}$$
> for $P_{\tau^{2}_{\mathcal{K}}}$ the slice likelihood statement evaluated at $\tau^{2}_{\mathcal{K}}$. Regularity %% check: correct phrase for "regular likelihood"? %% of the likelihood and $|\tilde{\mathcal{S}}| \to \infty$ allow us to conclude by the subset argument of [[@jiangSubsetArgumentConsistency2013]] that the final equality converges to zero in probability. Repeating the argument for $\tau^{2}_{\mathcal{K}} - \epsilon$ lets us conclude root consistency for $\tau^{2}_{\mathcal{K}}$. $\blacksquare$

> [!info] Update (2026-07-01)
> The notes below are now largely formalized: the tree-crawl / degeneracy thoughts in [[Observation Richness for K-Crossed Designs]] (the pairwise cardinality-gap statistic provably catches the $(i,i,k)$ case), and the saturation / high-cardinality existence question in [[Existence of Isolating Subsets in the Near-Balanced Regime]] (greedy-off-a-matching construction; near-balanced regime covered under a weakened inter-slice condition).

The [[Cramer Consistency of Slice Likelihood for K-Crossed Random Effects Probit Model|consistency statement for slice likelihoods]] keeps conditions for $|\tilde{\mathcal{S}}| \to \infty$ vague as we have found empirically that high order categorical random variables exhibit more complex structure than can be captured by the category-wise decay $\max_{k \in [K]} \epsilon_{k} \to 0$, or even the extended case. 


%% -- BEGIN NOTES TO EXPAND -- %%
**MIX OF SUFFICIENT CONDITION + MORE GENERAL THOUGHTS ON HIGH CARDINALITY REGIME**
- I'm not sure $\max_{\mathcal{K} \in \mathbb{A}} \epsilon_{k} \to 0$ for $\epsilon_{\mathcal{K}} = \max_{\boldsymbol{j} \in \mathcal{S}[\mathcal{K}]} N_{\boldsymbol{j}, \mathcal{K}} / N$ is sufficient, since this is a regime where we need more observations
- I think (like the big rows thing) there's going to be a saturation of some estimands if $\kappa_{k} < \kappa_{k'}$ by a sufficiently large margin; eg. if there are just many less levels of category $k$ then $k'$, then perhaps there are enough observations for direct reasonable estimability of the corresponding effects 
- Big issue 1 is curse of dimensionality-type "crosses make everything small"; under a uniformity in sampling over $\mathcal{S}$ (not $\mathcal{S}_{0}$), in $K = 3$, the expected number of observations, 
	- a slice over $(i, j)$ should expect $\sim N^{\kappa_{1} + \kappa_{2} - \kappa_{3}}$ unique observations, a slice over $k$ should expect $N^{\kappa_{3}  - \kappa_{2} - \kappa_{1}}$, but not sure if i'm delineating between $i$ and $j$ here 
	- I really can't tell if that makes things better or worse for us - curse of dimensionality in the traditional notion is "everything is orthogonal" just because there are so many opportunities to be orthogonal, but that's in some ways better for us because we need to be able to extract out the nice subset - but it seems like we need a different characterization for sufficient numbers of $\tilde{N}_{\boldsymbol{j}, \mathcal{K}} \geq 2$.
	- it seems like if one works, the others usually won't and we have to make the saturation case. 
- note upper bound on $|\tilde{S}|$ by $\max_{k \in [K]}N^{\kappa_{1}}$. 
- More generally, want to think about excluding catastrophic cases/difficult regimes: if we observe only "diagonals" $(i, i, k)$ in $K = 3$, then we never observe $a_{i}$ or $b_{j}$ separately, and thus it is impossible to make an estimate of $\sigma^{2}_{A}$ or $\sigma^{2}_{B}$. 
- maybe there's a tree-based crawl through the distributions of the $N_{\boldsymbol{j}, \mathcal{K}}$ distributions; my thought was that we check distribution of $N_{\boldsymbol{\boldsymbol{i}}, [K]}:= N_{\boldsymbol{i}}$ for $\boldsymbol{i} \in \mathcal{S}_{0}$ first, because spikes are replicates, then $N_{\boldsymbol{i}, \neg k}$ for $k \in [K]$, then naturally down cardinality of $\mathcal{K}$s. supposed to catch the $(i, i, k)$ case, but don't know if it's doing that or if it's working a different observation - maybe we need to get to within slices, which would be a pain and also computationally expensive. 
%% -- END NOTES TO EXPAND -- %%
