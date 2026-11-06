# Reproducible Research

## About this course

A reproducible project can be re-run, understood and shared by other people. It is also easier for you to return to months later.

This course introduces the practical habits that make this possible. It covers project structure, documentation, Quarto reports, virtual environments and sharing data.

The course takes about two hours. Each topic has a hands-on activity (together, your turn, then the answer), and sections 2 and 3 have a short demo, and attendees run no code. The notes are written so they can also be used for self-study.

## What is in this repository

| File or folder | What it is |
|---|---|
| `index.qmd` | The course home page, with the learning objectives, outline and download buttons |
| `slides.qmd` | The slides: two watch-only demos and one activity per topic (together, your turn, answer), with the steps in the speaker notes (press S), plus optional Q-FAIR slides at the end |
| `notes.qmd` | The notes. Reference for attendees, and written so they can be used for self-study, with a "Try it yourself" activity and answer for each section |
| `instructor.qmd` | A quick-glance guide for the instructor: timings, key messages, things not to forget and checkpoints |
| `example-project/` | The folder attendees download: `messy-project/` (bad structure and names), `tidy-project/` (the best practices), `one-document/` (one report, many formats) and `take-home/` (a checklist) |
| `build_example_zip.py` | Zips `example-project/` into `example-project.zip`, the download linked from the home page. The zip is built automatically, so it isn't committed |
| `_quarto.yml`, `custom.scss`, `_brand.yml` | Site settings, styles and branding |
| `assets/` | Images |
| `.github/workflows/publish.yml` | Renders the website and publishes it to the `gh-pages` branch on every push to `main` |

## Teaching the course

Read `instructor.qmd` first. Before teaching:

1. Download and unzip the example folder, and copy `tidy-project/` somewhere you can change it.
2. Check that **R** and **Quarto 1.4 or later** are installed on your machine (RStudio and Positron include Quarto), and run `tidy-project/code/run_all.R` once to check the demos work. Attendees need only Quarto, not R.
3. Prepare a small project with an environment (`renv` or `uv`) for the Section 3 demo.
4. Press Render on `one-document/report.qmd`.

## Building the course locally

You need [Quarto](https://quarto.org/docs/get-started/) (version 1.4 or later; RStudio and Positron include it) and the software from the course's setup instructions, plus `knitr` and `rmarkdown` for R code or `jupyter` for Python code.

Then:

```bash
git clone https://github.com/Bristol-Training/reproducible-research.git
cd reproducible-research
python3 build_example_zip.py
quarto preview
```

`build_example_zip.py` makes the example folder download, so the link on the home page works. `quarto preview` opens the course in your browser and reloads it whenever you save a `.qmd` file. The rendered site goes in `docs/`, which isn't committed.

## Publishing

The website is published automatically. Every push to `main` runs the GitHub Action in `.github/workflows/publish.yml`, which builds `example-project.zip`, renders the site and pushes it to the `gh-pages` branch. GitHub Pages serves the site from that branch. You can also run the Action by hand from the **Actions** tab.

## Contributing

Corrections and suggestions are welcome.

**Spotted a problem?** [Open an issue](https://github.com/Bristol-Training/reproducible-research/issues) saying which page and section it's in.

**Small fix, like a typo?** Open the `.qmd` file on GitHub, click the pencil icon (**Edit this file**), make the change and click **Propose changes**. GitHub makes a copy of the repository for you and opens a pull request.

**Bigger change?**

1. Fork the repository on GitHub and clone your fork.
2. Create a branch: `git checkout -b my-change`.
3. Edit the `.qmd` files and check the result with `quarto preview`.
4. Commit and push your branch, then open a pull request on GitHub describing what you changed and why.

Commit only the source files: the `.qmd` files, any new images in `assets/` and any changes to `example-project/`. Don't commit `docs/` or `example-project.zip`. They're ignored by git, and the website is rebuilt automatically after merging.

## Credits

Developed by the [Jean Golding Institute](https://www.bristol.ac.uk/golding/).

Jean Golding Institute © CC-BY 4.0
