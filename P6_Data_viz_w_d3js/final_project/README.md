## Summary

### Introduction

This project focuses on creating a visualization to illustrate the differences in number of TripAdvisor reviews for two competing hotel brands for selected locations. Actual hotel brands were anonymised (hotel A and hotel B).

### Data source

The data was obtained via webscraping TripAdvisor website for number of reviews as well as reviewers' location.

### Findings

Hotel A started to get TripAdvisor reviews about a year earlier than hotel B. This headstart was maintained from about 2006 till 2012 where hotel B saw a surge in number of reviews and overtook hotel A by almost a factor of three.

The intention of the visualization is to highlight this difference (through the use of animation, especially when the two lines split in 2012).

The split from 2012 onwards was the result of more than 4-fold increase in number of reviews from Asian countries in 2013 for hotel B. This was in contrast to the slight reduction in Asian reviews for hotel A.

## Design

Since this was a plot of yearly user reviews, a line chart was chosen to demonstrate the trends. The main message was the stark differences start from mid-2012 onwards.

User can then select the options to investigate this phenomenon further via examining user reviews based on continents of origin.

For distribution by continents, I chose a stack bar chart to highlight that Asia was the main reason behind the difference, starting from mid-2012. All other continents were greyed out to highlight the effects of reviews from Asia.

The martini glass approach was adopted. Initial author-driven portion of the visualization used animated line charts to illustrate the yearly growth trend of the number of reviews for both hotels. The animation served to highlight the split in growth trend from 2012 onwards.

User interactive portion occurs at the end of the animation, allowing the user to dive deeper into the locations of reviewers for each hotel.

## Feedback

Feedback was solicited from three different persons, who had chosen to remain anonymous.

Person A: "The animation really did highlight the split in the trend lines. It would be better if the user can see the breakdown of the reviewers."

Person B: "While it is helpful to be able to compare both hotels on the same map, it may be better if we can see each one individually as the overlapping circles can be quite confusing."

Person C: "Some of the smaller circles in the maps are obscured by the dark colors."

## Resources

Example of d3 line charts
https://bl.ocks.org/mbostock/3883245

Animating d3 line charts
http://bl.ocks.org/duopixel/4063326

Filtering data in d3.js based on columnd
http://stackoverflow.com/questions/23156864/d3-js-filter-from-csv-file-using-multiple-columns

Adding gridlines
http://www.d3noob.org/2013/01/adding-grid-lines-to-d3js-graph.html

Stacked bar with tooltips
http://bl.ocks.org/mstanaland/6100713
