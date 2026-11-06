# Example folder

Everything you need for the course activities. The activities don't need you to run any code: the only thing you run is **Render**.

| Folder | What it is | Used in |
|---|---|---|
| `messy-project/` | A project with a bad structure and bad names. Open it and see what you can work out | Sections 1 to 3 |
| `tidy-project/` | The same project with all the good habits: a README, a data dictionary, clear folders, and a report | Sections 1 to 3 |
| `python-project/` | A small Python project with no environment yet, for the uv demo. Its README has the steps | Section 3 |
| `r-project/` | The same project in R, for the renv demo. Its README has the steps | Section 3 |
| `one-document/` | A short report to turn into HTML, PDF and Word. Open `report.qmd` and press **Render** | Section 2 |
| `take-home/` | A one-page checklist to tick for your own project | Section 4 |

## One document, many formats

1. Open `one-document/report.qmd` in RStudio or Positron.
2. Press **Render**, and choose HTML, then Typst (PDF), then Word. Or run `quarto render report.qmd` in a terminal to make them all at once.
3. Change the title or a sentence, and render again. All the formats change.

If Render doesn't work, open the ready-made files in `one-document/finished/`.
