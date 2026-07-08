---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/data/tensor_synth.R
---

# `scan_valid_rows`

```r
scan_valid_rows <- function(csv_file, cat_cols, chunk_size = 1e+06) {
    con <- file(csv_file, "r")
    row_id <- 0L
    valid_rows <- integer()
    repeat {
        lines <- readLines(con, n = chunk_size)
        if (length(lines) == 0) 
            break
        dt <- fread(text = lines, header = FALSE, select = cat_cols, fill = TRUE)
        ok <- complete.cases(dt)
        valid_rows <- c(valid_rows, row_id + which(ok))
        row_id <- row_id + nrow(dt)
    }
    close(con)
    valid_rows
}
```

%% begin persistent %%

%% end persistent %%

