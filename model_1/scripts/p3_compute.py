import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Import processed data

df = pd.read_csv('/home/sean_osullivan/datasci_9_data_prep/model_1/data/processed/processed_covid_19_death_data.csv')

# Define Variables

X = df.drop('covid-19_deaths', axis=1) # Independent variables, all except covid-19 deaths
y = df['covid-19_deaths'] # Dependent variable

# Fit the scalar
scaler = StandardScaler()
scaler.fit(X)
pickle.dump(scaler, open('/home/sean_osullivan/datasci_9_data_prep/model_1/models/scaler_cov19.sav', 'wb'))

# Fit the scaler to the features and transform
X_scaled = scaler.transform(X)

# Split the scaled data into training, validation, and testing sets (70%, 15%, 15%)
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Pickle the X_train
pickle.dump(X_train, open('/home/sean_osullivan/datasci_9_data_prep/model_1/models/X_train_cov19_.sav', 'wb'))

# Pickle X.columns
pickle.dump(X.columns, open('/home/sean_osullivan/datasci_9_data_prep/model_1/models/X_columns_cov19.sav', 'wb'))