# Reads the raw data, removes incomplete rows, and saves a clean copy.
# Run from the project folder (the one that contains `data/` and `code/`).

raw <- read.csv("data/raw/penguins.csv")

# drop any rows with missing values
clean <- na.omit(raw)

# Optional (cycle 6): uncomment the next line to keep only the later years, then
# re-run this script and render the report again. The numbers will change.
# clean <- clean[clean$year >= 2008, ]

write.csv(clean, "data/processed/penguins_clean.csv", row.names = FALSE)
