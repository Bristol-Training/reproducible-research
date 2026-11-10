# Penguin body mass (R)

The average body mass of each penguin species, as a table and a bar chart.

This project has **no environment yet**. It is for the Section 3 demo, where you set one up with [renv](https://rstudio.github.io/renv/).

## Contents

- `data/penguins.csv`: the penguin measurements
- `code/analysis.R`: prints the average body mass of each species, and saves a chart to `outputs/`. It uses the `ggplot2` package
- `finished/`: the lock file renv makes during the demo (`renv.lock`), in case the demo doesn't work

## Demo: set up an environment with renv

You need the `renv` package: `install.packages("renv")`. Copy this folder somewhere first, so the original stays without an environment. Then open the copy as a project: in RStudio, **File → New Project → Existing Directory**; in Positron, open the folder. In the R console:

1. **Run it.** `source("code/analysis.R")`. If `ggplot2` isn't installed, it fails: this is the "it works on my laptop" problem. If it is installed, it works, but nothing records which version it used.
2. **Make an environment:** `renv::init()`. renv looks through the code for the packages it uses (here, `ggplot2`), installs them into the project's own library (`renv/library/`), and records them, at those versions, in the lock file, `renv.lock`. It also adds a `.Rprofile` file, so the environment is switched on whenever you open the project. R restarts.
3. **Run it in the environment:** `source("code/analysis.R")`. It prints the results and saves `outputs/body_mass.png`.
4. **Delete the environment:** close the project (or quit R), delete the `renv/library/` folder, then open the project again. `library(ggplot2)` now fails, because the project can only see its own library, and that has gone. This is what a colleague sees when you send them the project.
5. **Rebuild it from the lock file:** `renv::restore()`. This is what a colleague runs when you send them the project. They get the same packages, at the same versions. Run the script again: it works.

Send the code, the data, this README, `renv.lock`, `.Rprofile`, `renv/activate.R` and `renv/settings.json`. Don't send `renv/library/`.

`renv.lock` records the version of R you used, but renv doesn't install R. Write the version of R in the README too.
