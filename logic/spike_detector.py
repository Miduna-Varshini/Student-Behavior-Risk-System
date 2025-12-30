def detect_activity_spike(row):
    spikes = []

    if row["actions_per_minute"] > 40:
        spikes.append("High activity spike detected")

    if row["session_duration"] > 90:
        spikes.append("Unusually long session")

    if row["files_accessed"] > 7:
        spikes.append("Excessive file access")

    if row["device_change"] == 1:
        spikes.append("Device change during session")

    return spikes

