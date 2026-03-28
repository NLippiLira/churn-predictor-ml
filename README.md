# 🚀 Churn Predictor ML App

Aplicación Full Stack de Machine Learning que predice la probabilidad de abandono de clientes (churn) utilizando un modelo entrenado con datos reales de telecomunicaciones.

Este proyecto implementa la metodología **CRISP-DM** de extremo a extremo: desde el entendimiento del negocio hasta el despliegue en producción con Docker y una API REST.

---

## 🌐 Live Demo

* 🔗 Frontend: *(agregar URL GitHub Pages)*
* 🔗 Backend API: *(agregar URL Render)*

---

## 🧠 Problemática de Negocio

Las empresas de telecomunicaciones enfrentan pérdidas debido al abandono de clientes (churn).

### 🎯 Objetivo

Predecir qué clientes tienen alta probabilidad de abandonar el servicio para:

* Aplicar estrategias de retención
* Reducir pérdidas
* Optimizar campañas comerciales

---

## 🧭 Metodología — CRISP-DM

### 1️⃣ Business Understanding

* Problema: alta tasa de churn
* Objetivo: predecir abandono
* Tipo: clasificación binaria

---

### 2️⃣ Data Understanding (EDA)

Dataset: Telco Customer Churn

#### 📊 Información general

* ~7.000 registros
* Variables demográficas y de servicio
* Target: `Churn`

#### 📈 Distribución del target

* No churn ≈ 73%
* Churn ≈ 27%

👉 Dataset desbalanceado

---

#### 🔍 Observaciones clave

* Variables categóricas predominantes
* `TotalCharges` contenía valores no numéricos
* Presencia de datos faltantes
* Clientes con menor antigüedad tienden a abandonar

---

#### 💡 Insights relevantes

* Contratos mensuales → mayor churn
* Fibra óptica → mayor churn (posible precio alto)
* Pagos electrónicos → mayor riesgo

---

### 3️⃣ Data Preparation

* Eliminación de `customerID`
* Conversión de `TotalCharges`
* Eliminación de nulos
* One-Hot Encoding
* Feature engineering:

  * `tenure_group`

---

### 4️⃣ Modeling

Modelo utilizado:

* 🌲 Random Forest Classifier

---

### 📊 Métricas obtenidas

* ROC-AUC: ~0.80+
* Buen recall en clase churn
* Balance entre precisión y recall

---

### 5️⃣ Evaluation

#### 🧱 Matriz de confusión

* Buen nivel de detección de churn
* Algunos falsos positivos

---

#### 🎯 Interpretación

* Se prioriza **recall** → detectar clientes en riesgo
* Falsos positivos aceptables en contexto de negocio

---

#### 🚀 Mejoras futuras

* Feature selection
* Balanceo de clases (SMOTE)
* Modelos más avanzados (XGBoost)

---

### 6️⃣ Deployment

✔ API con Flask
✔ Modelo serializado (`.pkl`)
✔ Dockerización
✔ Frontend interactivo
✔ Deploy en la nube

---

## 🏗️ Arquitectura

Frontend (HTML, CSS, JS)
↓
API REST (Flask)
↓
Modelo ML (Random Forest)

---

## ⚙️ Tecnologías

### Backend

* Python 3.10
* Flask
* Scikit-learn
* Pandas
* Joblib

### Frontend

* HTML5
* CSS3
* JavaScript

### DevOps

* Docker
* GitHub
* Render

---

## 🐳 Docker

```bash
docker build -t churn-api .
docker run -p 5000:5000 churn-api
```

---

## 🔌 API

### Endpoint

```bash
POST /predict
```

### Ejemplo

```json
{
  "tenure": 12,
  "MonthlyCharges": 70,
  "Contract": "Month-to-month",
  "InternetService": "Fiber optic",
  "PaymentMethod": "Electronic check"
}
```

---

### Respuesta

```json
{
  "prediction": 1,
  "probability": 0.82
}
```

---

## 📦 Instalación local

```bash
git clone https://github.com/TU-USUARIO/churn-predictor-ml.git
cd churn-predictor-ml

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Ejecutar

```bash
python -m src.api.app
```

---

## 📊 Estructura del proyecto

```
churn-predictor/
│
├── data/
├── models/
│   └── churn_model.pkl
│
├── notebooks/
├── src/
│   ├── data/
│   ├── models/
│   └── api/
│
├── frontend-churn/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Futuras mejoras

* CI/CD con GitHub Actions
* Deploy automático
* Autenticación
* Dashboard con métricas
* Pipeline MLOps

---

## 👨‍💻 Autor

**Nicolás Lippi**

* Full Stack Developer
* Machine Learning Engineer

---

## 📄 Licencia

MIT License
