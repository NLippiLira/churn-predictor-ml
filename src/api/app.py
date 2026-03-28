import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta base
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
model_path = os.path.join(base_dir, "models", "churn_model.pkl")

# Cargar modelo
model = joblib.load(model_path)
print("✅ Modelo cargado correctamente")


@app.route("/")
def home():
    return "Churn Predictor API funcionando 🚀"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Convertir a DataFrame
        df = pd.DataFrame([data])

        # ⚠️ IMPORTANTE: mismo formato que entrenamiento
        df = pd.get_dummies(df)
        
        # Alinear columnas con modelo (esto evita errores)
        model_columns = model.feature_names_in_
        df = df.reindex(columns=model_columns, fill_value=0)

        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        return jsonify({
            "prediction": int(prediction),
            "probability": float(probability)
        })

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)