x <- read.csv("data.csv")
head(x)
summary(x)
table(x$species)
# why is this empty??
x[x$Island == "Torgersn", ]
