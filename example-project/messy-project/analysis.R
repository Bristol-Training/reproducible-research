# analysis for paper
# TODO fix this!!
library(ggplot2)
library(dplyr)
setwd("C:/Users/jsmith/Desktop/PhD/stuff for paper")
d <- read.csv("data_final_v2.csv")
d <- d[d$Mass > 0, ]
mean(d$Mass)
ggplot(d, aes(Species, Mass)) + geom_boxplot()
ggsave("plot1.png")
