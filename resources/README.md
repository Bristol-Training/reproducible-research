# Course resources

Ready-made files for the live demos, so you don't have to type code during the session. Copy them into your demo project and change the locations if you like. The scripts assume they are **run from the project folder** (the one containing `data/`, `code/` and `outputs/`).

| File | Copy it to | Used in |
|---|---|---|
| `code/00_get_data.R` | `my_project/code/` | Demo 1 |
| `code/01_clean_data.R` | `my_project/code/` | Demos 1 and 3 |
| `README_template.md` | `my_project/README.md` | Demo 2 |
| `report_r.qmd` | `my_project/report.qmd` | Demo 3 |
| `data/penguins.csv` | `my_project/data/raw/penguins.csv` | Only if you can't use `00_get_data.R` |

The data is R's built-in `penguins` dataset (R 4.5.0 or later): 344 penguins, with species, island, bill, flipper, body mass, sex and year. `00_get_data.R` saves it as `data/raw/penguins.csv`, so the project has a raw data file to protect. `data/penguins.csv` is the same data saved as a file, for anyone on an older version of R, or using Python or Excel.

The data has some missing values (`NA`): 11 rows are incomplete. `01_clean_data.R` removes them and writes `data/processed/penguins_clean.csv` (333 rows). The report keeps one species (Gentoo), and mixes text, code, an inline number, a table and a plot. For demo 3, `01_clean_data.R` has a commented-out line that keeps only the later years: uncomment it, re-run the script and re-render, and the report updates.

Run order for the demos:

```
00_get_data  ->  01_clean_data  ->  report.qmd
```

The scripts need base R only, plus `knitr` and `rmarkdown` for the Quarto report.
