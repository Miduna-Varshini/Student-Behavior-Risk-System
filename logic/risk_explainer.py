def explain_risk(row, anomaly_prediction, spikes):
    reasons = []

    if anomaly_prediction == -1:
        reasons.append("Behavior deviates from normal pattern")

    if row["login_hour"] < 5 or row["login_hour"] > 22:
        reasons.append("Abnormal login time")

    if row["day_type"] == 1 and row["session_duration"] > 80:
        reasons.append("Long session during weekend")

    reasons.extend(spikes)

    if not reasons:
        reasons.append("Normal behavior")

    return reasons

