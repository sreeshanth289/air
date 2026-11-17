import os, joblib
from sklearn.ensemble import RandomForestRegressor
from preprocessing import load_data, get_xy

HERE = os.path.dirname(__file__)
df = load_data(os.path.join(HERE, "..", "data", "AirQualityUCI.xlsx"))
X, y, medians = get_xy(df)
model = RandomForestRegressor(n_estimators=100, max_depth=12, min_samples_leaf=5, n_jobs=-1, random_state=0).fit(X, y)
joblib.dump({"model": model, "medians": medians}, os.path.join(HERE, "model.pkl"), compress=3)
print("Saved model.pkl")
