---
type: code
tags:
  - code/function
  - code/language/r
found at: pkg/arcre/R/data/tensor_synth.R
---

# `extract_rows_by_index`

```r
extract_rows_by_index <- function(csv_file, idx, cols, chunk_size = 1e+06) {
    con <- file(csv_file, "r")
    on.exit(close(con), add = TRUE)
    out <- vector("list", length(idx))
    ptr <- 1L
    row_id <- 0L
    repeat {
        lines <- readLines(con, n = chunk_size)
        if (length(lines) == 0L) 
            break
        rows <- row_id + seq_along(lines)
        keep <- rows %in% idx[ptr:length(idx)]
        if (any(keep)) {
            dt <- fread(text = lines[keep], header = FALSE, select = cols, showProgress = FALSE)
            out[ptr:(ptr + nrow(dt) - 1L)] <- split(dt, seq_len(nrow(dt)))
            ptr <- ptr + nrow(dt)
        }
        row_id <- row_id + length(lines)
        if (ptr > length(idx)) 
            break
    }
    rbindlist(out)
}
```

%% begin persistent %%

%% end persistent %%

