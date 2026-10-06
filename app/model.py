import pickle
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "model" / "best_model_final.pkl"

_model = None
_threshold = None


def load_model():
    global _model, _threshold
    if _model is None:
        with open(MODEL_PATH, "rb") as f:
            data = pickle.load(f)
        _model = data["model"]
        _threshold = data["threshold"]
    return _model, _threshold


def predict(age, systolic_bp, diastolic_bp, bmi, heart_rate, body_temp_f, previous_complications):
    model, threshold = load_model()

    pulse_pressure = systolic_bp - diastolic_bp
    map_value = (systolic_bp + 2 * diastolic_bp) / 3
    is_fever = 1 if body_temp_f > 100.4 else 0

    X = np.array([[
        age, systolic_bp, diastolic_bp, bmi, heart_rate,
        pulse_pressure, map_value, int(previous_complications), is_fever,
    ]])

    proba = model.predict_proba(X)[0]
    prob_high = float(proba[1])
    prob_low = float(proba[0])
    is_high = prob_high >= threshold

    return {
        "risk_label": "high_risk" if is_high else "low_risk",
        "probability_high_risk": prob_high,
        "probability_low_risk": prob_low,
        "threshold_used": threshold,
    }
