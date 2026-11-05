# clean the data
d <- read.csv("data.csv")
d <- d[!is.na(d$body_mass), ]     # take out the NAs (i think this is right)
d$sex[is.na(d$sex)] <- "unknown"
write.csv(d, "data_final.csv")    # then I did the rest by hand in excel
