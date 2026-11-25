# Penguin body mass analysis

Body measurements of 333 penguins on three islands. **Status:** complete.

## Quickstart

1. Open this folder in RStudio or Positron (or a terminal).
2. Run `code/run_all.R`. It cleans the data and builds the report (HTML, PDF and Word) in `outputs/`.
3. Try opening `report.qmd`, changing `chosen_species <- "Gentoo"` to `"Chinstrap"` or `"Adelie"`, and rendering again: every number, table and figure updates across all three formats.

## Setup

- R 4.3 or later (uses `knitr` and `rmarkdown` for Quarto rendering)
- Quarto 1.4 or later (to make the report)

## Contents

- `data/raw/` the original data (never edited)
- `data/processed/` the cleaned data, and `penguins_clean_dictionary.csv`, which explains each column
- `code/` the scripts (`01_clean_data.R` and `run_all.R`)
- `report.qmd` the report, which makes HTML, PDF and Word versions from one file
- `_quarto.yml` settings for the report (it puts the results in `outputs/`)
- `outputs/` made by `run_all.R`. Safe to delete

## Data

Penguin measurements from near Palmer Station, Antarctica (Gorman, Williams and Fraser, 2014). The same data is built into R 4.5 and later as `penguins`: see `?penguins` for the source and licence.
