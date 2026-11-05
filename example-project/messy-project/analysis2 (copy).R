# analysis for paper (copy)
library(ggplot2)
setwd("C:/Users/jsmith/Desktop/PhD/stuff for paper")
d <- read.csv("data_FINAL_USE_THIS.csv")
# d <- d[d$Mass > 0, ]
mean(d$Mass)
ggplot(d, aes(Species, Mass)) + geom_boxplot() + theme_minimal()
ggsave("plot_new.png")
write.csv(aggregate(Mass ~ Species, d, mean), "results_v3.csv")
