import pandas as pd 

#dataset
df = pd.read_csv('/home/sean_osullivan/datasci_9_data_prep/model_2/data/raw/Data_Breach_Notifications_Affecting_Washington_Residents__Personal_Information_Breakdown_.csv')

#Turn dataset into pickle file
df.to_pickle('/home/sean_osullivan/datasci_9_data_prep/model_2/data/raw/Data_Breach_Notifications_Affecting_Washington_Residents__Personal_Information_Breakdown_.pkl')