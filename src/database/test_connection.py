from db_connection import engine

try:
    with engine.connect() as connection:
        print("✅ Conexión exitosa a SQL Server")
except Exception as e:
    print("❌ Error de conexión")
    print(e)
