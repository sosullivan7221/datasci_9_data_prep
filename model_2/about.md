# Dataset: Washington State Breach Notifications

This dataset looks at all breach notification instances in the state of Washington. This analysis will look to see if we can predict the number of Washington residents affected based on the cause of the data breach and the industry affected.

## Data Preparing

I will be putting all column names in lowercase. I will be only keeping the rows named 'DataBreachCause', 'WashingtoniansAffected', and 'IndustryType'. I will be remvoving all rows that contain missing values within these three columns.