from sqlalchemy import create_engine

SERVER = r'Edu\SQLEXPRESS'
DATABASE = 'BankFraudDB'
DRIVER = 'ODBC Driver 17 for SQL Server'

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}&trusted_connection=yes"
)

engine = create_engine(connection_string)

import pandas as pd
from db_connection import engine

# 1. Leer CSV
ruta_csv = 'data/creditcard.csv'
df = pd.read_csv(ruta_csv)

print("📄 CSV cargado")
print(df.head())

# 2. Validaciones

print("📊 Registros:", len(df))
print("🚨 Fraudes:", df["Class"].sum())

# 2. Cargar a SQL Server
tabla = "transactions"

df.to_sql(
    name=tabla,
    con=engine,
    if_exists="append",   
    index=False,
    chunksize=5000
)

print(f"✅ Datos cargados en la tabla '{tabla}'")
print(f"🔢 Filas insertadas: {len(df)}")
