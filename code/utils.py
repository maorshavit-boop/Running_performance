import datetime
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,precision_score,recall_score, f1_score

def filter_columns(dfs, columns, names=None):
    new_dfs = []
    for i, df in enumerate(dfs):
        keep = [c for c in columns if c in df.columns]
        if names:
            missing = [c for c in columns if c not in df.columns]
            if missing:
                print(f"{names[i]} is missing columns: {missing}")
        new_dfs.append(df[keep])
    return new_dfs
#Converts pace to float
def pace_to_float(pace):
    if isinstance(pace, str) and ":" in pace:
        minutes, seconds = pace.split(":")
        return int(minutes) + int(seconds)/60
    if isinstance(pace, datetime.time):
        return pace.minute + pace.second / 60
    if isinstance(pace, datetime.timedelta):
        return pace.total_seconds() / 60
    try:
        return float(pace)
    except:
        return None
#Converts time to float
def time_to_minutes(t):
    if isinstance(t, str) and ":" in t:
        parts = t.split(":")
        try:
            if len(parts) == 3:  # hh:mm:ss
                h, m, s = parts
                return int(h) * 60 + int(m) + float(s) / 60
            elif len(parts) == 2:  # mm:ss
                m, s = parts
                return int(m) + float(s) / 60
            else:
                return float(t)
        except ValueError:
            return None
    if isinstance(t, datetime.timedelta):
        return t.total_seconds() / 60
    if isinstance(t, datetime.time):
        return t.hour*60 + t.minute + t.second / 60
    else:
        return float(t)
#GRPS calculation fuction
def calculate_grps(df):
    required_cols = ["Time", "Distance", "Avg HR"]
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"Input DataFrame must contain the following columns: {required_cols}")
    df["T2"] = df["Time"] * (10 / df["Distance"]) ** 1.06 # Calculate T2
    df["Normalized_HR"] = df["Avg HR"] / 195 # Calculate Normalized_HR
    # Calculate GRPS
    # To avoid division by zero or large numbers, we add a small epsilon to "T2"
    # This is good practice for numerical stability, especially if "T2" can be zero.
    epsilon = 1e-9
    df["GRPS"] = ((10 / (df["T2"] + epsilon)) / df["Normalized_HR"]) * 100
    return df

def eval_model(pipe, X_train, X_test, y_train, y_test, model_name):
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    return {
        "Model": model_name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Macro F1": f1_score(y_test, y_pred, average="macro"),
        "Macro Precision": precision_score(y_test, y_pred, average="macro"),
        "Macro Recall": recall_score(y_test, y_pred, average="macro"),
    }
