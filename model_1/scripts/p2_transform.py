import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

# Load dataset
df = pd.read_pickle('/home/sean_osullivan/datasci_9_data_prep/model_1/data/raw/Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.pkl')

# Clean column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Select only needed columns
to_keep = [
    'condition_group',
    'condition',
    'age_group',
    'covid-19_deaths'
]

df = df[to_keep]
df.dropna(inplace = True)

# Remove rows with invalid values

df = df[~df['age_group'].isin(['All Ages', 'Not stated'])]


# Ordinal Encoding on condition_group
enc = OrdinalEncoder()
enc.fit(df[['condition_group']])
df['condition_group'] = enc.transform(df[['condition_group']])

# Dataframe with mapping on condition_group
df_mapping_condition_group = pd.DataFrame(enc.categories_[0], columns=['condition_group'])
df_mapping_condition_group['condition_group_ordinal'] = df_mapping_condition_group.index
df_mapping_condition_group.to_csv('/home/sean_osullivan/datasci_9_data_prep/model_1/data/processed/mapping_condition_group.csv', index=False)

# Ordinal Encoding on condition
enc = OrdinalEncoder()
enc.fit(df[['condition']])
df['condition'] = enc.transform(df[['condition']])

# Dataframe with mapping on condition
df_mapping_condition = pd.DataFrame(enc.categories_[0], columns=['condition'])
df_mapping_condition['condition_ordinal'] = df_mapping_condition.index
df_mapping_condition.to_csv('/home/sean_osullivan/datasci_9_data_prep/model_1/data/processed/mapping_condition.csv', index=False)

# Ordinal Encoding on condition_group
enc = OrdinalEncoder()
enc.fit(df[['age_group']])
df['age_group'] = enc.transform(df[['age_group']])

# Dataframe with mapping on condition_group
df_mapping_age_group = pd.DataFrame(enc.categories_[0], columns=['age_group'])
df_mapping_age_group['age_group_ordinal'] = df_mapping_age_group.index
df_mapping_age_group.to_csv('/home/sean_osullivan/datasci_9_data_prep/model_1/data/processed/mapping_age_group.csv', index=False)

# Save entire mapping to a csv

df.to_csv('/home/sean_osullivan/datasci_9_data_prep/model_1/data/processed/processed_covid_19_death_data.csv', index=False)