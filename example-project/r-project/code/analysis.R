# Average body mass of each penguin species, as a table and a chart.
# Run from the project folder (the one that contains `data/` and `code/`):
#     Rscript code/analysis.R

library(ggplot2)

penguins <- na.omit(read.csv("data/penguins.csv"))

# average body mass (grams) of each species
mass <- aggregate(body_mass ~ species, data = penguins, FUN = mean)
mass$body_mass <- round(mass$body_mass)
cat(nrow(penguins), "penguins\n")
print(mass, row.names = FALSE)

dir.create("outputs", showWarnings = FALSE)
chart <- ggplot(mass, aes(x = species, y = body_mass)) +
  geom_col(fill = "#3b6ea5") +
  labs(x = "Species", y = "Average body mass (g)")
ggsave("outputs/body_mass.png", chart, width = 6, height = 4, dpi = 150)
cat("Saved outputs/body_mass.png\n")
