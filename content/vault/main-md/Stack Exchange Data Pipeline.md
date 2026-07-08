---
modified: 2026-04-14T00:10:33-07:00
created: 2026-03-14T10:11:49-07:00
---
# Raw Download For Full Dataset 
**Very Large Files - Recording Here for Full Replication And Further Data**

I'm using the [September 2025 Stack Exchange Data Dump](https://archive.org/details/stackexchange_20250930) since data schema is clear - there are some anti-AI data spoiling measures that seem to be unimplemented in this version, though it may be worth checking and adding to preprocessing. 

You can find the full dataset for Stack Overflow [here](https://ia800800.us.archive.org/view_archive.php?archive=/9/items/stackexchange_20250930/stackexchange_20250930/stackoverflow.com.7z). Download:
- `Posts.xml` (~30GB zipped, ~200G unzipped)
- `Tags.xml` (1.3MB zipped, 16.9MB unzipped)
- `Users.xml` (~1GB zipped, ~11GB unzipped)

Clearly we can get other covariates from some of the other files, but for brevity we leave it here. `sede-and-data-dump` gives further information on data structure and tracked covariates. 

# Preprocessing Pipeline
## `parse_xml.py`
Derive covariates from text data and XML files. 

**INPUT:** `Posts.xml`, `Tags.xml`, `Users.xml`
**OUTPUT:** CSV files with saved covariates:
- `users.csv` (1.53GB)
	- `user_id`
	- `reputation`: SE "user score." 
	- `creation_date`: Account creation date. 
	- `last_access_date`
	- `up_votes`: Lifetime upvotes on questions and answers. 
	- `down_votes`
	- `views`: Number of times *profile* has been viewed. 
	- `about_me_length`: Character count of *'About Me'* profile 
- `questions.csv` (3.43GB)
	- `question_id`
	- `asker_id`
	- `accepted_answer_id`: id of accepted answer, *not* accepted answerer. Empty if no answer was accepted. 
	- `creation_date`
	- `score`: Net upvotes - downvotes on question
	- `view_count`
	- `answer_count`
	- `comment_count`
	- `favorite_count`
	- `body_length`: character count of question text 
	- `has_code`: binary encoding of having a code block in the question 
	- `n_code_blocks`
	- `n_links`
	- `n_images`
	- `title_length`
	- `raw_tags`
	- `n_tags`
	- `language_tags`: pipe-joined language tags from prespecified list 
	- `first_language_tag`
	- `first_topic_tag`: first non-language tag
- `answers.csv` (2.27GB) 
	- `answer_id`
	- `question_id`
	- `answerer_id`
	- `creation_date`
	- `score`: Net upvotes - downvotes on answer 
	- `comment_count`
	- `body_length`
	- `has_code`
	- `n_code_blocks`
	- `n_links`
- `tags.csv` (1.2MB)
	- `tag_name`
	- `tag_count`: total number of questions which had tag 
	- `is_language`

To clarify tag behavior in `questions.csv` and `tags.csv`, we reasonably expect very high counts with regards to tags for things like major programming languages, so we take the categorical variable of interest as "the first non-language tag," and treat language as a covariate of the question. The implementation doesn't quite grab everything, but the largest group takes up 5% of question volume, which doesn't seem too bad. 

**Note Time Leakage, Since Changing Covariates Record Snapshot at Time of Data Dump (September 2025).** 
## `02_join_data.R`
Join data across `asker_id x question_id x answer_id x answerer_id x question_tag`. 

*Because of the size of these objects, memory issues are frequent. This implementation employs lots of read in redundancies to reduce memory load, and returns chunked CSV files that can be read in separately.* 

**INPUT:** `users.csv`, `questions.csv`, `answers.csv`, `tags.csv` 
**OUTPUT:** chunked csv files with joined covariates (joined on answers). Chunks are broadly in ascending order of dates *on questions*, but don't quite divide cleanly. 

Broadly categorized (while keeping order):
- CATEGORICAL LEVELS:
	- `first_topic_tag`
	- `answerer_id` 
	- `asker_id`
	- `question_id`
	- `answer_id`
- ANSWER COVARIATES:
	- `score`: answer score
	- `comment_count`
	- `body_length`
	- `has_code`
	- `n_code_blocks`
	- `n_links` 
	- `a_date` 
	- `accepted_answer_id`: empty if no accepted answer (our $Y = 0$ case). 
- QUESTION COVARIATES:
	- `q_score`
	- `view_count`
	- `answer_count`
	- `q_comment_count` 
	- `favorite_count`: deprecated past ~2018(?), another "like" proxy 
	- `q_body_length`
	- `q_has_code`
	- `q_n_code_blocks`
	- `q_n_links` 
	- `n_images`
	- `title_length`
	- `n_tags`
	- `first_language_tag`
	- `q_date`
	- `y`: **RESPONSE** (whether or not the answer was accepted). 
	- `answer_order`: Among the answers that the question received, what number answer (in time) this question was
	- `answer_lag_min`: Among the answers that the question received, time in minutes between the question posted and the first answer posted 
- ASKER COVARIATES:
	- `asker_rep` 
	- `asker_upvotes`
	- `asker_downvotes`
	- `asker_views`
	- `asker_aboutme_len`
- ANSWERER COVARIATES:
	- `answerer_rep`
	- `answerer_upvotes`
	- `answerer_downvotes`
	- `answerer_views`
	- `answerer_about_me_len`
- `asker_age_days`
- `answerer_age_days`

**Date Boundaries for Reference:**
*Sizes range from 254.9 MB (12) to 995.8 MB (1)*. 
```text
=== chunk_001.csv ===
  a_date: 2008-08-01T12:16:22.167Z → 2024-03-31T22:37:18.990Z
  q_date: 2008-08-01T00:42:38.903Z → 2011-11-07T09:55:15.523Z
=== chunk_002.csv ===
  a_date: 2009-07-23T16:37:15.710Z → 2024-03-31T19:25:37.807Z
  q_date: 2010-08-03T09:14:22.303Z → 2013-02-13T19:55:35.323Z
=== chunk_003.csv ===
  a_date: 2009-07-28T10:34:57.403Z → 2024-03-31T22:47:39.760Z
  q_date: 2013-01-23T14:53:27.257Z → 2014-02-08T14:42:04.497Z
=== chunk_004.csv ===
  a_date: 2011-08-17T11:24:41.493Z → 2024-03-31T23:01:45.757Z
  q_date: 2014-01-02T04:11:32.187Z → 2015-01-28T16:18:48.703Z
=== chunk_005.csv ===
  a_date: 2013-09-05T14:32:37.387Z → 2024-03-31T20:54:49.527Z
  q_date: 2014-12-31T06:45:09.223Z → 2015-12-30T20:34:40.460Z
=== chunk_006.csv ===
  a_date: 2013-11-17T21:54:37.193Z → 2024-03-31T22:27:18.490Z
  q_date: 2015-12-30T20:35:07.753Z → 2016-12-01T10:49:38.783Z
=== chunk_007.csv ===
  a_date: 2011-06-08T15:44:29.540Z → 2024-03-31T22:24:24.640Z
  q_date: 2016-11-28T12:01:58.793Z → 2017-11-16T20:00:51.550Z
=== chunk_008.csv ===
  a_date: 2017-11-16T20:09:29.087Z → 2024-03-31T21:50:53.927Z
  q_date: 2017-11-16T07:58:43.113Z → 2018-12-16T00:36:57.833Z
=== chunk_009.csv ===
  a_date: 2015-10-20T19:43:04.230Z → 2024-03-31T23:52:01.587Z
  q_date: 2018-11-24T04:20:44.263Z → 2020-02-16T18:34:12.737Z
=== chunk_010.csv ===
  a_date: 2015-10-08T19:24:37.287Z → 2024-03-31T23:19:41.050Z
  q_date: 2020-02-12T10:55:44.027Z → 2021-03-28T22:31:13.353Z
=== chunk_011.csv ===
  a_date: 2021-03-16T08:57:55.413Z → 2024-03-31T23:51:41.710Z
  q_date: 2021-03-08T07:26:41.623Z → 2022-08-23T15:18:24.917Z
=== chunk_012.csv ===
  a_date: 2022-08-23T15:23:18.617Z → 2024-03-31T23:59:37.970Z
  q_date: 2022-08-19T23:01:56.917Z → 2024-03-31T23:56:47.153Z
```

## `03_build_model_data.R` 
Choose covariate subset to define $\beta$ and perform initial naïve probit fit 

**INPUT:** joined data (chunks, though joined CSV with appropriate covariates or RData can be utilized)
**OUTPUT:** RData saved via `save(x, y, f1, f2, f3, obj_glm, x_scale)` - `f3` is tag levels, so can be omitted for two levels. 

Implementation prioritizes filtering for the following:
- date range (specify `DATE_MIN` and `DATE_MAX`)
- `ANSWER_CT`: number of answers the question received. 
	- `1` = all questions with exactly one answer (*first* answer, via `answer_order`, can also retain nice binary interpretation)
	- `NULL` = all (multinomial opportunity)
	- `c(1, k)` = top $k$ (multinomial opportunity, avoid worst-case time tails)
- `MIN_OBS` 

**CURRENTLY SAVED COVARIATES (NO STANDARDIZING/DEMEANING FOR CURRENT DATA):** $\beta \in \mathbb{R}^{6}$, 
- `log_answer_lag` (minutes)
- `log_a_bodylen`
- `answer_has_code` (natural intercept term)
- `q_has_code` 
- `log_asker_rep`
- `log_answerer_rep`














