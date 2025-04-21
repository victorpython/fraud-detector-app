# 🏦 Fraud Detector App – QA en Inteligencia Artificial

**Proyecto de QA + IA para detección de fraude en transacciones bancarias**  
Una aplicación Flask con interfaz web donde puedes ingresar datos de una transacción y un modelo de `RandomForest` entrenado detecta si es segura o fraudulenta.

---

## 📁 Estructura del proyecto
   ```bash
   fraud-detector-app/
    ├── app/                            # Código de la aplicación
    │   ├── __init__.py
    │   ├── app.py                      # Servidor Flask principal
    │   ├── model_utils.py              # Carga del modelo y predicción
    │   ├── model/
    │   │   ├── rf_model.pkl            # Modelo entrenado
    │   │   └── scaler.pkl              # Scaler usado al entrenar
    │   └── templates/
    │       └── index.html              # Interfaz web de usuario
    │
    ├── data/                           # Datos de ejemplo
    │   ├── __init__.py
    │   └── transactions.csv            # Dataset sintético
    │
    ├── train_model.py                  # Script para entrenar y guardar el modelo
    ├── requirements.txt                # Lista de dependencias
    └── README.md                       # Este archivo
   ```

## 🚀 Instrucciones de uso

1. Clona el repositorio y entra al proyecto
   ```bash
   git clone https://github.com/victorpython/fraud-detector-app.git
   cd fraud-detector-app
   ```

2. Instala las dependencias
   ```bash
   pip install -r requirements.txt
   ```
      
3. Genera el modelo (Solo la primera vez o tras cambiar el dataset)
   ```bash
   python train_model.py
   ```

   Esto creará ```app/model/rf_model.pkl``` y ```app/model/scaler.pkl```

4. Arranca la aplicación Flask
   ```bash
   python app/app.py
   ```

   Abre tu navegador en ```http://127.0.0.1:5000```.

## 🧠 ¿Qué hace esta app?
🔹 Toma como entrada los siguientes datos:

- Monto de la transacción

- Hora del día

- Categoría del comercio

- Ubicación

🔹 Preprocesa los datos con un StandardScaler

🔹 Evalúa la transacción usando un modelo RandomForestClassifier

🔹 Muestra si la transacción es segura o potencialmente fraudulenta.

## 🛠️ Tecnologías utilizadas
- Python 3.9+

- Flask

- scikit-learn

- pandas

- HTML5

## 📬 Contacto
Víctor Cardoso
📧 victorcf.92@gmail.com
🔗 [linkedin.com/in/victorpython](https://www.linkedin.com/in/victor-cardoso-datascientist/)
