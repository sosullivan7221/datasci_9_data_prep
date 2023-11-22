import pandas as pd 

#dataset
df = pd.read_csv('/home/sean_osullivan/datasci_9_data_prep/model_1/data/raw/Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv')

#Turn dataset into pickle file
df.to_pickle('/home/sean_osullivan/datasci_9_data_prep/model_1/data/raw/Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.pkl')