---
modified: 2026-04-14T00:25:17-07:00
created: 2026-04-13T23:53:55-07:00
---

# se-sims

Replication pipeline for the Stack Exchange case study 

## Expected File Format

```
se-sims/
├── input/se_raw/          # raw XML
│   ├── Posts.xml
│   ├── Tags.xml
│   └── Users.xml
├── tmp_chunks/            
├── plots/                 # RE distribution PNGs written by 04_run_cre.R
├── parse_xml.py           # step 01 — extract CSVs from XML
├── 02_join_data.R         # step 02 — join posts + users, write chunks
├── 03_build_model_data.R  # step 03 — filter, build x/y/f, save RData
├── 04_run_cre.R           # step 04 — fit ARC probit, print results, plot REs
├── stackoverflow_joined.RData       # (RData) output of 02
├── stackoverflow_arc_data.RData     # output of 03
└── cre_results.RData                # output of 04
```

## Pipeline

**If you already have `stackoverflow_arc_data.RData`**, skip to step 04 and run `04_run_cre.R` from the `se-sims/` directory. Update path to `k_arc.R` on line 32. `k_arc.R` currently has the `k = 3` implementation. 

**If you already have `stackoverflow_joined.RData`**, set `INPUT_MODE <- "rdata"` in `03_build_model_data.R` and start at step 03.

---

**CAUTION ON INTERCEPT:** GLM is fit with intercept, which currently needs to be manually prepended to the design matrix; 

```r
x_arc <- cbind("(Intercept)" = 1, x)
```

### PROBIT EXAMPLE 
#### 3 random effects (asker × answerer × tag)
*Adjusting location of `k_arc` source,* run directly in `R` with the below. 

```r
library(arcProbit)
library(sandwich)
library(statmod)
source("../arc_sims/k_crossed/R/k_arc.R")

load("stackoverflow_arc_data.RData")   # x, y, f1, f2, f3, obj_glm
x_arc <- cbind("(Intercept)" = 1, x)

fit3 <- arcbin3s.fit(
  x           = x_arc,
  y           = y,
  f1          = f1,       # asker
  f2          = f2,       # answerer
  f3          = f3,       # tag
  obj_glm     = obj_glm,
  nq          = 10,
  niter       = 10,
  get_effects = TRUE,
  get_se      = TRUE
)
```

#### 2 random effects (asker × answerer)

```r
library(arcProbit)
library(sandwich)
library(statmod)

load("stackoverflow_arc_data.RData")
x_arc <- cbind("(Intercept)" = 1, x)

df_glm <- data.frame(y = y, x)
obj_glm2 <- glm(y ~ ., data = df_glm, family = binomial(link = "probit"))

fit2 <- arcbin.fit(
  x           = x_arc,
  y           = y,
  f1          = f1,       # asker
  f2          = f2,       # answerer
  obj_glm     = obj_glm2,
  nq          = 10,
  niter       = 10,
  get_effects = TRUE,
  get_se      = TRUE
)
```
