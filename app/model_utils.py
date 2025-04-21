import joblib
import numpy as np
import pandas as pd

# Cargar modelo y scaler
model = joblib.load("app/model/rf_model.pkl")
scaler = joblib.load("app/model/scaler.pkl")

# Columnas que espera el modelo (ajustadas al entrenamiento)
columns = [
    'amount', 'hour',
    'merchant_category_electronics', 'merchant_category_fashion',
    'merchant_category_grocery', 'merchant_category_restaurants', 'merchant_category_travel',
    'location_CDMX', 'location_Cancun', 'location_Guadalajara', 'location_Monterrey'
]

def predecir_fraude(data_dict):
    # Convertir input a DataFrame
    df = pd.DataFrame([data_dict])
    
    # One-hot encoding manual
    for col in columns:
        if col not in df.columns:
            df[col] = 0
    
    df = df[columns]  # Reordenar
    scaled = scaler.transform(df)
    pred = model.predict(scaled)[0]
    
    return "⚠️ Transacción Fraudulenta" if pred == 1 else "✅ Transacción Segura"
