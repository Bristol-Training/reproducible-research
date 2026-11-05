# Example project

Files for following along with the course. You will use them to build up a small project: tidy it, document it, and report on it.

## What is here

| File | What it is | Used for |
|---|---|---|
| `penguins.csv` | The raw data (344 penguins, some rows incomplete) | Cycles 1 and 2 |
| `01_clean_data.R` | A short script that removes incomplete rows and saves a clean copy | Cycle 2 |
| `README_template.md` | A starting point for a README | Cycle 3 |
| `report.qmd` | A Quarto report that uses the clean data | Cycles 5 and 6 |
| `finished/` | The finished, tidy project, if you get stuck | Any time |

## If something doesn't work

Open the matching file in `finished/` and carry on from there. For example, if the cleaning script fails, use `finished/data/processed/penguins_clean.csv`.

## About the data

The penguins data (344 penguins, with species, island, bill and flipper measurements, body mass, sex and year) is also built into R 4.5 and later as `penguins`. Here it is provided as a CSV file, so everyone starts from the same file.
