# Rebuilds everything from the raw data.
# Run it from the project folder:   Rscript code/run_all.R

unlink("data/processed/penguins_clean.csv")   # delete the cleaned data
unlink("outputs", recursive = TRUE)           # delete the report
dir.create("outputs")

source("code/01_clean_data.R")                # make the cleaned data again
system2("quarto", c("render", "report.qmd", "--output-dir", "outputs"))   # make the report again
