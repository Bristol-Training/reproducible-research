# Reads the raw data, removes incomplete rows, and saves a clean copy.
# Run from the project folder: Rscript code/01_clean_data.R

raw <- read.csv("data/raw/penguins.csv")
clean <- na.omit(raw)
write.csv(clean, "data/processed/penguins_clean.csv", row.names = FALSE)
