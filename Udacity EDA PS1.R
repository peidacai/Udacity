library(ggplot2)
install.packages("swirl") 
library(swirl) 
swirl()

install.packages('knitr', dependencies = T) 
library(knitr)

install.packages('devtools', dependencies = T) 
library(devtools) 
install_version("colorspace","1.2-4") 


install.packages('ggplot2', dependencies = T) 
library(ggplot2) 

data("diamonds")
summary(diamonds)
?diamonds
str(diamonds)

names(diamonds)
qplot(x = cut, data = diamonds)
qplot(x = price, data = diamonds)
