# Maternal Risk Prediction API

A REST API that serves a machine learning model to predict maternal health risk levels based on patient vital signs. Containerized with Docker so it runs on any machine without additional setup.

> This system is a screening tool only, not a substitute for medical diagnosis.

---

## Model

| Attribute | Details |
|---|---|
| Algorithm | Gradient Boosting Classifier |
| Dataset | Maternal Health Risk (UCI / Kaggle) |
| Target | Binary — `high_risk` / `low_risk` |
| Custom threshold | 0.42 (optimized to maximize recall on high risk class) |

---

## How to Run

The only requirement is Docker. No Python, no library installation needed.

**1. Clone the repository**

```bash
git clone https://github.com/VyAndra31/maternal-risk-api.git
cd maternal-risk-api
```

**2. Build the image**

```bash
docker build -t maternal-risk-api .
```

**3. Run the container**

```bash
docker run -p 8000:8000 maternal-risk-api
```

API is now running at `http://localhost:8000`.

---

## Endpoints

### `GET /health`
Check if the API is running.

### `POST /predict`
Send patient data, get risk prediction.

**Request body:**
```json
{
  "age": 30,
  "systolic_bp": 140,
  "diastolic_bp": 95,
  "bmi": 28.0,
  "heart_rate": 88,
  "body_temp_f": 101.0,
  "previous_complications": true
}
```

**Response:**
```json
{
  "risk_label": "high_risk",
  "probability_high_risk": 0.998,
  "probability_low_risk": 0.001,
  "threshold_used": 0.42
}
```

### Interactive docs
Open `http://localhost:8000/docs` for Swagger UI.

---

## Project Structure

```
maternal-risk-api/
├── app/
│   ├── main.py        # FastAPI routes
│   ├── model.py       # Model loading and prediction logic
│   └── schemas.py     # Input/output schema validation
├── model/
│   └── best_model_final.pkl
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Stack
- FastAPI
- Uvicorn
- scikit-learn 1.6.1
- Docker
