import pandas as pd
from db_connection import engine

# Cargar datos finales
query = """
SELECT
    time_seconds,
    amount,
    riesgo,
    is_fraud
FROM Fraud_Detected
"""

df = pd.read_sql(query, engine)

# Codificar riesgo
riesgo_map = {
    "LOW": 0,
    "MEDIUM": 1,
    "HIGH": 2
}

df["riesgo_num"] = df["riesgo"].map(riesgo_map)

# Features y target
X = df[["time_seconds", "amount", "riesgo_num"]]
y = df["is_fraud"]

print("📐 X shape:", X.shape)
print("🎯 y shape:", y.shape)
print("\n🚨 Distribución del target:")
print(y.value_counts())
