# Dataset 1: Conditions contributing to COVID-19 Deaths

This dataset looks at the number of covid-19 deaths across the United States and categorizes them based on contributing factors. This analysis will look to see if we can predict the number of yearly deaths based on a given contributing factor and an associated age group.

## Data Preparing

I will be removing all columns except for 'Condition', 'Age Group', and 'COVID-19 Deaths'. I will be removing white space in all of the columns, as well as remvoving the rows in the age group column that are either all ages or not stated. I will finally be dropping any rows with empty columns.