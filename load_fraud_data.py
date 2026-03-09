import pandas as pd
from db_connection import engine

query = """
SELECT
    transaccion_id,
    time_seconds,
    amount,
    is_fraud,
    riesgo
FROM Fraud_Detected
"""

df = pd.read_sql(query, engine)

print("✅ Datos cargados desde SQL Server")
print(df.head())

print("\n📐 Shape:", df.shape)

print("\n🚨 Fraudes reales:")
print(df["is_fraud"].value_counts())

print("\n⚠️ Distribución de riesgo:")
print(df["riesgo"].value_counts())
