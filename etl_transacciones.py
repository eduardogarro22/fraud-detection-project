import pandas as pd
from db_connection import engine
from sqlalchemy import text
from datetime import datetime, timedelta

# 1. Leer datos crudos (limitamos para prueba)
query = """
SELECT TOP 100
    Time,
    Amount,
    Class
FROM Fraud_Transactions_Raw
ORDER BY Time
"""

df = pd.read_sql(query, engine)

# 2. Transformaciones
start_date = datetime(2024, 1, 1)

df["fecha"] = df["Time"].apply(
    lambda x: start_date + timedelta(seconds=float(x))
)

df["monto"] = df["Amount"]
df["es_fraude"] = df["Class"]

df["cuenta_id"] = 1  # simulamos una cuenta
df["tipo_transaccion"] = "compra"
df["canal"] = "online"

df_final = df[
    ["cuenta_id", "fecha", "monto", "tipo_transaccion", "canal", "es_fraude"]
]

# 3. Insertar en SQL Server
df_final.to_sql(
    "transacciones",
    con=engine,
    if_exists="append",
    index=False
)

print("✅ ETL completado: transacciones insertadas correctamente")
