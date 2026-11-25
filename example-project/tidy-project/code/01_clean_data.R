# Reads the raw data, removes incomplete rows, and saves a clean copy.
# Run from the project folder (the one that contains `data/` and `code/`).

raw <- read.csv("data/raw/penguins.csv")

# drop any rows with missing values
clean <- na.omit(raw)

write.csv(clean, "data/processed/penguins_clean.csv", row.names = FALSE)
