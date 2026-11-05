# Reproducible Research

## About this course

A reproducible project can be re-run, understood and shared by other people. It is also easier for you to return to months later.

This course introduces the practical habits that make this possible. It covers project structure, documentation, Quarto reports, virtual environments and sharing data.

The course takes about two hours. You follow along with short live demos on your own copy of an example folder, and then try each idea yourself. Notes are provided for reference.

| File | What it is |
|---|---|
| `slides.qmd` | The slides, with five live demos and four exercises |
| `notes.qmd` | Reference notes for attendees, with tabs for different ways of working |
| `instructor.qmd` | Instructor notes: timings, demo scripts and pitfalls |
| `example-project/` | The example folder that attendees download, with a ready-made `finished/` copy |
| `example-project.zip` | The same folder as a zip, linked from the home page. Rebuild it with `python3 build_example_zip.py` after any change |

## Building the course locally

You need [Quarto](https://quarto.org/docs/get-started/) and the software from the course's setup instructions, plus `knitr` and `rmarkdown` for R code or `jupyter` for Python code.

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
