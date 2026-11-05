# Saves R's built-in `penguins` data (R 4.5.0 or later) as the raw data for the project.
# Run once, from the project folder (the one that contains `data/` and `code/`).
#
# On an older version of R, copy `penguins.csv` from the resources folder into
# `data/raw/` instead.

write.csv(penguins, "data/raw/penguins.csv", row.names = FALSE)
