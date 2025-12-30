def build_timeline(student_df):
    timeline = []

    for _, row in student_df.iterrows():
        entry = {
            "login_hour": row["login_hour"],
            "session_duration": row["session_duration"],
            "actions_per_minute": row["actions_per_minute"],
            "files_accessed": row["files_accessed"],
            "device_change": row["device_change"]
        }
        timeline.append(entry)

    return timeline

