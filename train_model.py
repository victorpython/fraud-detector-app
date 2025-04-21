import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Cargar datos
df = pd.read_csv("data/transactions.csv")
df['location'] = df['location'].str.replace('Cancún', 'Cancun')
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
df = df.drop(['timestamp'], axis=1)
df = pd.get_dummies(df, columns=['merchant_category', 'location'])

X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Guardar modelo y scaler
os.makedirs("app/model", exist_ok=True)
joblib.dump(model, "app/model/rf_model.pkl")
joblib.dump(scaler, "app/model/scaler.pkl")
