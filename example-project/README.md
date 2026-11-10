# Example folder

Everything you need for the course activities. The activities don't need you to run any code: the only thing you run is **Render**.

| Folder or file | What it is | Used in |
|---|---|---|
| `messy-project/` | A project with a bad structure and bad names. Open it and see what you can work out | Sections 1 to 3 |
| `tidy-project/` | The same project with all the good habits: a README, a data dictionary, clear folders, and a report | Sections 1 to 3 |
| `one-document/` | A short report to turn into HTML, PDF and Word. Open `report.qmd` and press **Render** | Section 2 |
| `environment-demo/` | A small project with no environment yet, in R (`r/`, for the renv demo) and Python (`python/`, for the uv demo). Each README has the steps | Section 3 |
| `checklist.pdf`, `checklist.docx` | A one-page checklist to tick for your own project | Section 4 |
| `capstone-answer/` | A finished answer to the capstone exercise, in R (`r/`) and Python (`python/`), with the rendered report in `outputs/`. Try the exercise first! | After the course |

## One document, many formats

1. Open `one-document/report.qmd` in RStudio or Positron.
2. Press **Render**, and choose HTML, then Typst (PDF), then Word. Or run `quarto render report.qmd` in a terminal to make them all at once.
3. Change the title or a sentence, and render again. All the formats change.

If Render doesn't work, open the ready-made files in `one-document/finished/`.
