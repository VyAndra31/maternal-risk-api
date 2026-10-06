from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    age: float = Field(..., ge=10, le=60)
    systolic_bp: float = Field(..., ge=50, le=250)
    diastolic_bp: float = Field(..., ge=30, le=180)
    bmi: float = Field(..., ge=10, le=60)
    heart_rate: float = Field(..., ge=40, le=200)
    body_temp_f: float = Field(..., ge=95.0, le=108.0)
    previous_complications: bool


class PredictionOutput(BaseModel):
    risk_label: str
    probability_high_risk: float
    probability_low_risk: float
    threshold_used: float
