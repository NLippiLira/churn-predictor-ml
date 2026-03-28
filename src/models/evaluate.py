import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

from src.data.preprocess import preprocess


def evaluate_model():
    # Ruta base
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    data_path = os.path.join(base_dir, "data", "churn.csv")
    model_path = os.path.join(base_dir, "models", "churn_model.pkl")

    # Cargar datos y modelo
    df = preprocess(data_path)
    model = joblib.load(model_path)

    # Variables
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Predicciones
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # Métricas
    print("\n📊 Classification Report:\n")
    print(classification_report(y_test, y_pred))

    print("\n📈 ROC-AUC:", roc_auc_score(y_test, y_proba))

    # Matriz de confusión
    cm = confusion_matrix(y_test, y_pred)
    print("\n🧱 Confusion Matrix:\n")
    print(cm)


if __name__ == "__main__":
    evaluate_model()