import numpy as np
import pandas as pd

TARGET = "CO(GT)"
FEATURES = ["PT08.S1(CO)", "PT08.S2(NMHC)", "PT08.S3(NOx)", "PT08.S4(NO2)",
            "PT08.S5(O3)", "T", "RH", "AH", "hour", "month"]

def load_data(path):
    df = pd.read_excel(path)
    df = df.dropna(axis=1, how="all").replace(-200, np.nan)  # -200 = missing in UCI data
    df["hour"] = pd.to_datetime(df["Time"].astype(str)).dt.hour
    df["month"] = pd.to_datetime(df["Date"]).dt.month
    df = df[df[TARGET].notna()].copy()
    return df

def get_xy(df):
    X = df[FEATURES]
    medians = X.median()
    return X.fillna(medians), df[TARGET], medians
