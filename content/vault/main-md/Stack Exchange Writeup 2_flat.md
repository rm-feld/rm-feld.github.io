---
tags:
  - no-index
up: "[[Stack Exchange Writeup 2]]"
modified: 2026-07-13T11:28:21-07:00
created: 2026-07-13T11:20:28-07:00
---

\subsubsection{Model Setup}

We are interested in covariate-rich opportunities for the crossed random effects model which mimic the sparse cross structure. 

\textbf{Stack Exchange Data Setting}
We consider the question-answer site \href{https://stackexchange.com}{Stack Exchange (SE)}. On SE, some users (who we will call \textbf{askers}) will pose a question that other users (who we will call \textbf{answerers}) can give answers to. Questions can receive no or many answers, and other users can upvote or downvote both the question and (some or all) answers. Askers are generally expected to tag questions with relevant keywords in order to encourage their question reaching the right experts. 

By far the most active subset of SE is \href{https://stackoverflow.com/questions}{Stack Overflow}.

Stack Exchange is liberal in its sharing of data with a cc-by-sa 4.0 license and a Data Dump to \href{https://archive.org/search?query=creator%3A%22Stack+Exchange%2C+Inc.%22}{archive.org} which encodes large amounts of user and post information. \textit{Anti-AI protective measures have been put into place in recent years, so some care may need to be taken for more recent data dumps.} 

For binary response, \textbf{question acceptance} serves as an interesting starting point for potential deployment of the crossed random effects model. 

An interesting feature of SE is that the asker can "accept" at most one answer that they receive for a question, which is meant to be an indication of the "best" of the received answers. If there is no best answer, or the asker abandons the question, there may not be an accepted answer. This may motivate the question: \textbf{what types of question-answer pairs are viable acceptance targets?}

Let $i \in I$ index the asker, $j \in J$ index the answerer, and $k \in K$ index the tag. For covariates $x_{ijk}$ to be derived, we can imagine a binary crossed random effects model defined by pairs $(x_{ijk}, Y_{ijk})$ for which

\begin{align\textit{} Y_{ijk} = \mathbf{1}\left[ \text{answerer } i \text{ accepted the answer of answerer } j \text{ on the question with tag } k \text{ with covariates } x_{ijk}\right]  \end{align}}

with 

\begin{align\textit{} \mathbb{P}(Y_{ijk} = 1) = g^{-1}\left( x_{ijk}^{\intercal}\beta + a_{i} + b_{j} + c_{k} + \varepsilon_{ijk} \right) \end{align}}

given link function $g$. 

We note first that natural interpretations exist for the random effects:
\begin{itemize}
\item $a_{i}$ indicates some inclination of asker $i$ towards or against accepting answers. Some askers will always accept the first provided answer ($a_{i}$ 'large' and positive), while some askers are either disinclined to follow up on answers ($a_{i}$ negative). 
\item $b_{j}$ indicates some inclination of acceptability of answers from answerer $j$; perhaps answerer $j$ uses language particularly popular in the forum, which increases its likelihood to be accepted. In the opposite case, the user themselves may be unpopular so that answerers are less likely to accept an answer from them. 
\item $c_{k}$ can be a notion of ease or difficulty in communicating answers in a particular subdomain. Questions about \texttt{collision-detection} may be harder to answer in a way that an asker would prefer compared to a question about \texttt{pandas}. 
\end{itemize}

$x_{ijk}$ can be fairly rich with respect to potential covariates. In particular:
\begin{itemize}
\item \textbf{User covariates.} Both the asker $i$ and the answerer $j$ have user profiles which contain information as to the number of questions they have asked, the number of questions they have answered, a "reputation" score of contributions, their last sign on time, and the date on which their account was created, among others. 
\item \textbf{Question covariates.} Since posts contain text data, we can derive many covariates of varying granularity. Focusing on Stack Overflow, some potential linearly contributing covariates are the following:
\end{itemize}
	- \texttt{question_length}: questions with too many words may not be friendly to answer or may imply desiderata not achieved by answers. 
	- \texttt{has_code}/\texttt{num_code_blocks}: questions that clearly describe a bug or a use case may have a clearer answer that is easier to accept. 
	- \texttt{num_question_comments}/\texttt{num_question_edits}: questions that require significant follow-up before being answered may be detrimental to ultimate acceptance. 
	- \texttt{question_views}/\texttt{question_votes}: community popularity of a question, or proxies thereof, may encourage answerers who write acceptable answers. \texttt{question_votes} can also be negative, which may indicate 
\begin{itemize}
\item \textbf{Answer covariates.} We can use the analogous post covariates along with the same text processing from the question text for the answer text (or some superset/subset thereof). Additionally, of interest may be:
\end{itemize}
	- \texttt{response_time_gap}: answers posted closer to the initial creation of the question may be more likely to be accepted. 
	- \texttt{num_other_answers}: having more options of answers to accept will of course be negatively correlated with acceptance of an answer. 

The last covariate highlighted may be an uncomfortable structure to include, in that we may not appreciate the zero-sum competitive nature of choosing \textit{between} presented answers. While this competition isn't necessarily uncommon in our settings (if our response $Y$ is the act of \textit{choosing} a movie, for example, in the Netflix Problem setting, then the user naturally observes some subset of competitors), we can perhaps only look at acceptance behavior from the \textit{first answer}.

$x_{ijk}$ for the crossed random effects model can be fairly rich with respect to potential covariates. In particular:
\begin{itemize}
\item \textbf{User covariates.} Both the asker $i$ and the answerer $j$ have user profiles which contain information as to the number of questions they have asked, the number of questions they have answered, a "reputation" score of contributions, their last sign on time, and the date on which their account was created, among others. 
\item \textbf{Question covariates.} Since posts contain text data, we can derive many covariates of varying granularity. Focusing on Stack Overflow, some potential linearly contributing covariates are the following:
\end{itemize}
	- \texttt{question_length}: questions with too many words may not be friendly to answer or may imply desiderata not achieved by answers. 
	- \texttt{has_code}/\texttt{num_code_blocks}: questions that clearly describe a bug or a use case may have a clearer answer that is easier to accept. 
	- \texttt{num_question_comments}/\texttt{num_question_edits}: questions that require significant follow-up before being answered may be detrimental to ultimate acceptance. 
	- \texttt{question_views}/\texttt{question_votes}: community popularity of a question, or proxies thereof, may encourage answerers who write acceptable answers. \texttt{question_votes} can also be negative, which may indicate 
\begin{itemize}
\item \textbf{Answer covariates.} We can use the analogous post covariates along with the same text processing from the question text for the answer text (or some superset/subset thereof). Additionally, of interest may be:
\end{itemize}
	- \texttt{response_time_gap}: answers posted closer to the initial creation of the question may be more likely to be accepted. 
	- \texttt{num_external_links}: questions which reference other sources or information may be seen as more trustworthy or well-researched. 
	- \texttt{num_other_answers}: answers competing with other answers will make acceptance of an answer less likely. 

The last covariate highlighted may be an uncomfortable structure to include, in that we may not appreciate the zero-sum competitive nature of choosing \textit{between} presented answers. While this competition isn't necessarily uncommon in our settings (if our response $Y$ is the act of \textit{choosing} a movie, for example, in the Netflix Problem setting, then the user naturally observes some subset of competitors), we can perhaps only look at acceptance behavior from the \textit{first answer}.

\subsubsection{Some Details + First Run}
\subsection{Background}
The archived data helpfully includes a schema file sede-and-data-dump-schema-se which is fairly comprehensive in structure. Using the \href{https://archive.org/details/stackexchange_20250930}{September 2025 snapshot}, some preprocessing to question-answer pairs from 2018 - 2022 nets the following: 

\textbf{Data Set Size/Structure:}
\begin{lstlisting}
=== FULL JOINED DATASET ===
Rows: 27,127,190 
Unique askers: 3,893,885 
Unique answerers: 2,374,567 
Unique topic tags: 39,532 
Y=1 rate: 0.3453 
Columns: 43 
first_topic_tag, answerer_id, asker_id, question_id, answer_id, score, comment_count, body_length, has_code, n_code_blocks, n_links, a_date, accepted_answer_id, q_score, view_count, answer_count, q_comment_count, favorite_count, q_body_length, q_has_code, q_n_code_blocks, q_n_links, n_images, title_length, n_tags, first_language_tag, q_date, y, answer_order, answer_lag_min, asker_rep, asker_upvotes, asker_downvotes, asker_views, asker_aboutme_len, answerer_rep, answerer_upvotes, answerer_downvotes, answerer_views, answerer_aboutme_len, asker_age_days, answerer_age_days, tag_total_count 

Answer count distribution:
    answer_count       N
           <int>   <int>
 1:            1 9755912
 2:            2 7578665
 3:            3 4130200
 4:            4 2138515
 5:            5 1143869
 6:            6  650482
 7:            7  400108
 8:            8  263395
 9:            9  186157
10:           10  138855

Object size in memory: 9.65 GB

\end{lstlisting}

Most questions only receive one answer, with some exceptionally popular questions receiving many answers. I also note that answerers are less prevalent than askers, which makes sense. 

\paragraph{Second Pass Filtering and Naive Probit}

Let us look only at 2018. With some heavier filtering (and cutting down on covariates), we get some additional information (and first step ARC recovery of $\gamma$) the below:

\begin{lstlisting}
=== Dataset ===
  N: 386,243 
  Askers: 108,723 
  Answerers: 45,628 
  Tags: 6,355 
  Y=1 rate: 0.6205 

=== Balance ===
  eps_asker:    0.000360  (max 139)
  eps_answerer: 0.005719  (max 2,209)
  eps_tag:      0.052679  (max 20,347)

  Top 10 tags:
    first_topic_tag     N   share
             <char> <int>   <num>
 1:         android 20347 0.05268
 2:         reactjs 10690 0.02768
 3:      python-3.x 10651 0.02758
 4:           mysql  9888 0.02560
 5:             ios  9401 0.02434
 6:          pandas  7701 0.01994
 7:          arrays  6253 0.01619
 8:           excel  6248 0.01618
 9:            json  5880 0.01522
10:      sql-server  5721 0.01481

=== Building x ===
  Covariates:
    log_answer_lag            = log1p(answer_lag_min)
    log_a_bodylen             = log1p(body_length)
    answer_has_code           = has_code
    log_q_bodylen             = log1p(q_body_length)
    q_has_code                = q_has_code
    log_asker_rep             = log1p(asker_rep)
    log_answerer_rep          = log1p(answerer_rep)
  x: 386243 x 7 
  Columns: log_answer_lag, log_a_bodylen, answer_has_code, log_q_bodylen, q_has_code, log_asker_rep, log_answerer_rep 

  y: 386,243 (62.1% = 1)

=== Fitting probit GLM ===
  Converged: TRUE [ 4 sec ]
  Coefficients:
    (Intercept)               -1.68780
    log_answer_lag            -0.07829
    log_a_bodylen             +0.11769
    answer_has_code           +0.21971
    log_q_bodylen             +0.01693
    q_has_code                +0.10725
    log_asker_rep             +0.07468
    log_answerer_rep          +0.08045

=== Saved: stackoverflow_arc_data.RData ===
  x: 386,243 x 7
  f1 (asker):    108,723 levels
  f2 (answerer): 45,628 levels
  f3 (tag):      6,355 levels
\end{lstlisting}

This is supposed to be a weighting free setting, and I don't think the tag distribution looks \textit{too} bad (a heuristic already encoded is to take the first non-language tag, because commonly the first tag is \texttt{python} or \texttt{R} or \texttt{html} in significant quantities) but we may need to either be more aggressive (and get rid of \texttt{android}/\texttt{ios}, etc.). I think it would also be reasonable to pick top 10 languages and split between \texttt{popular_language} and \texttt{unpopular_language} or otherwise bin, which might be fine. 

The derived coefficients also seem to be reasonable. \texttt{log_answer_lag} the logged time it takes to receive an answer after a question is posted being negatively correlated with acceptance, and putting lots of weight on the answer having code seems very reasonable to me in this regime. 

\paragraph{K-ARC Fit}
We have done sufficient preprocessing to pass our data to K-ARC. We get the below summary:

\begin{lstlisting}
=== Sourcing k_arc.R ===
  Path: ../arc_sims/k_crossed/R/k_arc.R 

=== Fitting 3-crossed ARC probit ===
  nq=10  niter=10  get_se=TRUE
  (rho optimisation runs three separate 1-D optimisations)
  Done [ 48.1 sec ]

=== Variance / ICC estimates ===
  rho_asker    (rhoa) : 0.332927
  rho_answerer (rhob) : 0.076812
  rho_tag      (rhoc) : 0.026596
  denom (1-a-b-c)     : 0.563665

  sigma_asker    : 0.768536
  sigma_answerer : 0.369152
  sigma_tag      : 0.217217

=== Coefficients (scaled to latent-variable metric) ===
  Term                        Estimate    Std.Err        z   
  ----------------------------------------------------------
  (Intercept)                 -2.24807    0.06366  -35.311  ***
  log_answer_lag              -0.10428    0.00351  -29.715  ***
  log_a_bodylen               +0.15676    0.00577   27.185  ***
  answer_has_code             +0.29264    0.01311   22.321  ***
  log_q_bodylen               +0.02255    0.00816    2.763  **
  q_has_code                  +0.14285    0.01090   13.102  ***
  log_asker_rep               +0.09947    0.00326   30.494  ***
  log_answerer_rep            +0.10716    0.00660   16.245  ***
  Signif. codes: *** p<0.001  ** p<0.01  * p<0.05  . p<0.1

=== Random effects summary ===
  Asker (f1)  (n=108,723)
    mean=-0.0127  sd=0.4725  min=-2.2745  max=1.8344
  Answerer (f2)  (n=45,628)
    mean=-0.0035  sd=0.1652  min=-1.3851  max=1.0658
  Tag (f3)  (n=6,355)
    mean=0.0103  sd=0.0916  min=-0.4526  max=0.9563
\end{lstlisting}

Variance is well within the expected regime, though it's interesting that $\sigma_{A}$ is so much larger than either of the other ones. My guess is that it's a consequence of abandoning behavior (since the asker is the only person who can accept an answer, we can get noisier swings when very good answers are not accepted). 

A natural sanity check is to look at the derived random effects. Mixed efficacy here: tags distribution looks great, but some interesting behavior in \texttt{answerer} and \texttt{asker}.
