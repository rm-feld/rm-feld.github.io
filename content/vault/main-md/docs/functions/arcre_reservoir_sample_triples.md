---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/data/tensor_synth.R
---

# `reservoir_sample_triples`

```r
reservoir_sample_triples <- function(csv_file, cols, k, chunk_size = 1e+06) {
    stopifnot(length(cols) == 3)
    con <- file(csv_file, "r")
    on.exit(close(con), add = TRUE)
    reservoir <- vector("list", k)
    n_valid <- 0L
    repeat {
        lines <- readLines(con, n = chunk_size)
        if (length(lines) == 0L) 
            break
        dt <- fread(text = lines, header = FALSE, select = cols, fill = TRUE, showProgress = FALSE)
        ok <- complete.cases(dt)
        if (!any(ok)) 
            next
        dt <- dt[ok]
        for (i in seq_len(nrow(dt))) {
            n_valid <- n_valid + 1L
            row <- dt[i]
            if (n_valid <= k) {
                reservoir[[n_valid]] <- row
            }
            else {
                j <- sample.int(n_valid, 1L)
                if (j <= k) 
                  reservoir[[j]] <- row
            }
        }
        rm(dt)
        gc(FALSE)
    }
    if (n_valid < k) {
        reservoir <- reservoir[seq_len(n_valid)]
    }
    rbindlist(reservoir)
}
```

%% begin persistent %%

%% end persistent %%

