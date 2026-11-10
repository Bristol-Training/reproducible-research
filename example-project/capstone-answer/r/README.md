# Penguin body mass

Does body mass differ between male and female Gentoo penguins?
**Status:** complete.

## Quickstart

1. Open this folder in RStudio or Positron, and run `renv::restore()`
   in the R console to install the packages.
2. Run `Rscript code/01_clean_data.R` to make the clean data.
3. Run `quarto render report.qmd` to make the report, in `outputs/`.

## Setup

- R 4.3 or later. The packages are in `renv.lock`.
- Quarto 1.4 or later.

## Contents

- `data/raw/` the original data (never edited)
- `data/processed/` the clean data, made by `code/01_clean_data.R`,
  and `penguins_clean_dictionary.csv`, which explains each column
- `code/` the scripts
- `report.qmd` the report, and `references.bib` its references
- `_quarto.yml` settings for the report (it puts the results in `outputs/`)
- `outputs/` the rendered report. Safe to delete

## Data

Penguin measurements from near Palmer Station, Antarctica
(Gorman, Williams and Fraser, 2014).
