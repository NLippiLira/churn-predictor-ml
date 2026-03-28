import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib

from src.data.preprocess import preprocess


def train_model():
    # Ruta dinámica
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_path = os.path.join(base_dir, "data", "churn.csv")

    # Cargar y procesar datos
    df = preprocess(data_path)

    # Separar variables
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Entrenar
    model.fit(X_train, y_train)

    # Predicción
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # Evaluación
    print("\n📊 Classification Report:\n")
    print(classification_report(y_test, y_pred))

    print("\n📈 ROC-AUC:", roc_auc_score(y_test, y_proba))

    # Guardar modelo
    model_path = os.path.join(base_dir, "models")
    os.makedirs(model_path, exist_ok=True)

    joblib.dump(model, os.path.join(model_path, "churn_model.pkl"))

    print("\n✅ Modelo guardado correctamente")


if __name__ == "__main__":
    train_model()