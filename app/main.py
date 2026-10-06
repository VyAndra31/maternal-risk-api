from fastapi import FastAPI, HTTPException
from app.schemas import PredictionInput, PredictionOutput
from app.model import predict

app = FastAPI(
    title="Maternal Risk Prediction API",
    description="API prediksi risiko ibu hamil berdasarkan tanda vital dan riwayat klinis.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Maternal Risk Prediction API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOutput)
def predict_risk(payload: PredictionInput):
    if payload.diastolic_bp >= payload.systolic_bp:
        raise HTTPException(
            status_code=422,
            detail="Diastolic BP tidak boleh lebih besar atau sama dengan Systolic BP.",
        )

    result = predict(
        age=payload.age,
        systolic_bp=payload.systolic_bp,
        diastolic_bp=payload.diastolic_bp,
        bmi=payload.bmi,
        heart_rate=payload.heart_rate,
        body_temp_f=payload.body_temp_f,
        previous_complications=payload.previous_complications,
    )

    return result
