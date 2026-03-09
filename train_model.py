import joblib
import pandas as pd
from db_connection import engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Cargar datos
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
riesgo_map = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
df["riesgo_num"] = df["riesgo"].map(riesgo_map)

X = df[["time_seconds", "amount", "riesgo_num"]]
y = df["is_fraud"]

# Train / Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Modelo
model = LogisticRegression(
    class_weight="balanced",
    max_iter=1000
)

model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

print("📊 Confusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\n📈 Classification Report")
print(classification_report(y_test, y_pred))

joblib.dump(model, "models/logreg_fraud_v1.pkl")
print("💾 Modelo guardado en models/logreg_fraud_v1.pkl")
