import pandas as pd
import joblib
from db_connection import engine



# 1️⃣ Cargar modelo
model = joblib.load("models/logreg_fraud_v1.pkl")
print("✅ Modelo cargado correctamente")

# 2️⃣ Query SQL
query = """
SELECT
    transaccion_id,
    time_seconds,
    amount,
    riesgo,
    is_fraud
FROM Fraud_Detected
"""


# 3️⃣ Leer desde SQL
df = pd.read_sql(query, engine)

print("📊 Transacciones cargadas:", df.shape)
print("Columnas:", df.columns.tolist())

# 4️⃣ Normalizar nombres de columnas (PRO)
df.columns = df.columns.str.strip().str.lower()

# 5️⃣ Convertir riesgo a numérico
df["riesgo"] = df["riesgo"].str.strip().str.upper()

riesgo_map = {
    "LOW": 0,
    "MEDIUM": 1,
    "HIGH": 2
}

df["riesgo_num"] = df["riesgo"].map(riesgo_map)

print("Valores únicos riesgo_num:", df["riesgo_num"].unique())

# 6️⃣ Crear X
X = df[["time_seconds", "amount", "riesgo_num"]]

# 7️⃣ Calcular probabilidad
df["fraud_probability"] = model.predict_proba(X)[:, 1]

# 8️⃣ Clasificación
# Definimos porcentaje a revisar
porcentaje_alertas = 0.005   # 0.5%

# Calculamos threshold dinámico
threshold = df["fraud_probability"].quantile(1 - porcentaje_alertas)

# Generamos predicción
df["fraud_prediction"] = df["fraud_probability"] >= threshold

print(f" Threshold dinámico usado: {threshold}")
print(" Alertas generadas:", df["fraud_prediction"].sum())

print(df.head())

df_to_save = df[[
    "transaccion_id",
    "fraud_probability",
    "fraud_prediction"
]]

print(df["fraud_probability"].describe())
from sklearn.metrics import confusion_matrix, classification_report

print("\n📊 MATRIZ DE CONFUSIÓN")
print(confusion_matrix(df["is_fraud"], df["fraud_prediction"]))

print("\n📈 REPORTE DE CLASIFICACIÓN")
print(classification_report(df["is_fraud"], df["fraud_prediction"]))
df_to_save.to_sql(
    "Fraud_Scored",
    engine,
    if_exists="append",   
    index=False
)

print("💾 Scoring guardado en SQL (Fraud_Scored)")