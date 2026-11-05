# Reproducible Research

## About this course

A reproducible project can be re-run, understood and shared by other people. It is also easier for you to return to months later.

This course introduces the practical habits that make this possible. It covers project structure, documentation, Quarto reports, virtual environments and sharing data.

The course takes about two hours. You follow along with short live demos on your own copy of an example folder, and then try each idea yourself. Notes are provided for reference.

## What is in this repository

| File or folder | What it is |
|---|---|
| `index.qmd` | The course home page, with the learning objectives, outline and download buttons |
| `slides.qmd` | The slides. Six "I do, you do" cycles, one instructor demo and four exercises, with the steps for each in the speaker notes (press S) |
| `notes.qmd` | Reference notes for attendees, with tabs for different ways of working |
| `instructor.qmd` | A quick-glance guide for the instructor: timings, key messages, things not to forget and checkpoints |
| `example-project/` | The example folder that attendees download and follow along with. `finished/` inside it holds the ready-made result, in case a step doesn't work |
| `example-project.zip` | The same folder as a zip, linked from the home page. Rebuild it with `python3 build_example_zip.py` after any change to `example-project/` |
| `_quarto.yml`, `custom.scss`, `_brand.yml` | Site settings, styles and branding |
| `assets/` | Images |
| `docs/` | The rendered website (generated, so don't edit it) |

## Teaching the course

Read `instructor.qmd` first. Before teaching:

1. Download and unzip the example folder, and rehearse each cycle once.
2. Render `example-project/finished/report.qmd`, and save the resulting `report.html` next to it. This is the fallback for anyone whose Render fails. Then rebuild the zip.
3. Check that Quarto 1.4 or later is installed (RStudio and Positron include it).

## Building the course locally

You need [Quarto](https://quarto.org/docs/get-started/) (version 1.4 or later; RStudio and Positron include it) and the software from the course's setup instructions, plus `knitr` and `rmarkdown` for R code or `jupyter` for Python code.

Then:

```bash
git clone https://github.com/Bristol-Training/reproducible-research.git
cd <repo>
quarto preview
```

`quarto preview` opens the course in your browser and reloads it whenever you save a `.qmd` file.

## Contributing

Corrections and suggestions are welcome.

**Spotted a problem?** [Open an issue](https://github.com/Bristol-Training/reproducible-research/issues) saying which page and section it's in.

**Small fix, like a typo?** Open the `.qmd` file on GitHub, click the pencil icon (**Edit this file**), make the change and click **Propose changes**. GitHub makes a copy of the repository for you and opens a pull request.

**Bigger change?**

1. Fork the repository on GitHub and clone your fork.
2. Create a branch: `git checkout -b my-change`.
3. Edit the `.qmd` files and check the result with `quarto preview`.
4. Commit and push your branch, then open a pull request on GitHub describing what you changed and why.

Only commit the `.qmd` files (and any new images in `assets/`, and the files in `example-project/` with the rebuilt `example-project.zip`), not the `docs/` folder. The maintainer re-renders the website after merging.

## Credits

Developed by the [Jean Golding Institute](https://www.bristol.ac.uk/golding/).

Jean Golding Institute © CC-BY 4.0
