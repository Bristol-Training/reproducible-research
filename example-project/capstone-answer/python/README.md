# Penguin body mass

Does body mass differ between male and female Gentoo penguins?
**Status:** complete.

## Quickstart

1. Install [uv](https://docs.astral.sh/uv/), then run `uv sync` in this
   folder to install Python and the packages.
2. Run `uv run code/01_clean_data.py` to make the clean data.
3. Run `uv run quarto render report.qmd` to make the report, in `outputs/`.

## Setup

- Python 3.12 or later (uv installs it). The packages are in `uv.lock`.
- Quarto 1.4 or later.

## Contents

- `data/raw/` the original data (never edited)
- `data/processed/` the clean data, made by `code/01_clean_data.py`,
  and `penguins_clean_dictionary.csv`, which explains each column
- `code/` the scripts
- `report.qmd` the report, and `references.bib` its references
- `_quarto.yml` settings for the report (it puts the results in `outputs/`)
- `outputs/` the rendered report. Safe to delete

## Data

Penguin measurements from near Palmer Station, Antarctica
(Gorman, Williams and Fraser, 2014).
