import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("models/isolation_forest.pkl")
scaler = joblib.load("models/scaler.pkl")

FEATURE_COLUMNS = [
    "login_hour",
    "day_type",
    "session_duration",
    "actions_per_minute",
    "time_between_actions",
    "files_accessed",
    "device_change"
]

def detect_anomaly(row):
    """
    Returns:
    - prediction (-1 = anomaly, 1 = normal)
    - anomaly_score (confidence)
    """

    features = row[FEATURE_COLUMNS].values.reshape(1, -1)
    scaled = scaler.transform(features)

    prediction = model.predict(scaled)[0]
    score = model.decision_function(scaled)[0]

    return prediction, round(score, 3)

