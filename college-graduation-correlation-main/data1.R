
library(vioplot)
library(ggplot2)
library(dplyr)

## Set the working directory to the root of your DSC 520 directory
setwd("C:\\Users\\headc\\Desktop\\DSC520\\Week 9")

## Load the datasets to
firstyear_df <- read.csv("FirstYear_data.csv")
college_df <- read.csv("collegegrad_data.csv")
highschool_df <- read.csv("HighSchool_data.csv")

## create usable data sets
firsttograd_df <- cbind(firstyear_df$Percentage, college_df$College, firstyear_df$state)
firsttograd_df <- as.data.frame(firsttograd_df)

hightocoll_df <- cbind(highschool_df$value, college_df$College, highschool_df$location, highschool_df$year)
hightocoll_df <- as.data.frame(hightocoll_df)

hightofirst_df <- cbind(firstyear_df$Percentage, highschool_df$value, firstyear_df$state)
hightofirst_df <- as.data.frame(hightofirst_df)

# Bar Charts on different data sets
ggplot(firstyear_df, aes(x = state, y = Percentage)) +
  geom_col() +
  geom_text(aes(label = Percentage), vjust = 1.5, colour = "white") + 
  labs(y= "Percentage of Graduates", x = "States") + ggtitle("First Year Students") + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

ggplot(highschool_df, aes(x = location, y = value)) +
  geom_col() +
  geom_text(aes(label = value), vjust = 5, colour = "white") + 
  labs(y= "Percentage of Graduates", x = "States") + ggtitle("High School Graduates") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
        
ggplot(college_df, aes(x = state, y = College)) +
  geom_col() +
  geom_text(aes(label = College), vjust = 5, colour = "white") + 
  labs(y= "Percentage of Graduates", x = "States") + ggtitle("College Graduates") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

ggplot(firsttograd_df, aes(x = V1, y = V2)) +
  geom_col() +
  geom_text(aes(label = V2), vjust = 5, colour = "white") + 
  labs(y= "Percentage of Graduates", x = "States") + ggtitle("College Graduates") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))


