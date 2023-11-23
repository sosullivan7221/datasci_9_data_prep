import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

# Load dataset
df = pd.read_pickle('/home/sean_osullivan/datasci_9_data_prep/model_2/data/raw/Data_Breach_Notifications_Affecting_Washington_Residents__Personal_Information_Breakdown_.pkl')

# Clean column names
df.columns = df.columns.str.lower()

# Select only needed columns
to_keep = [
    'databreachcause',
    'washingtoniansaffected',
    'industrytype',
]

df = df[to_keep]
df.dropna(inplace = True)

# Ordinal Encoding on databreachcause
enc = OrdinalEncoder()
enc.fit(df[['databreachcause']])
df['databreachcause'] = enc.transform(df[['databreachcause']])

# Dataframe with mapping on databreachcause
df_mapping_databreachcause = pd.DataFrame(enc.categories_[0], columns=['databreachcause'])
df_mapping_databreachcause['databreachcause_ordinal'] = df_mapping_databreachcause.index
df_mapping_databreachcause.to_csv('/home/sean_osullivan/datasci_9_data_prep/model_2/data/processed/mapping_databreachcause.csv', index=False)

# Ordinal Encoding on industrytype
enc = OrdinalEncoder()
enc.fit(df[['industrytype']])
df['industrytype'] = enc.transform(df[['industrytype']])

# Dataframe with mapping on industrytype
df_mapping_industrytype = pd.DataFrame(enc.categories_[0], columns=['industrytype'])
df_mapping_industrytype['industrytype_ordinal'] = df_mapping_industrytype.index
df_mapping_industrytype.to_csv('/home/sean_osullivan/datasci_9_data_prep/model_2/data/processed/mapping_industrytype.csv', index=False)

df.to_csv('/home/sean_osullivan/datasci_9_data_prep/model_2/data/processed/processed_washington_breach_notification_data.csv', index=False)