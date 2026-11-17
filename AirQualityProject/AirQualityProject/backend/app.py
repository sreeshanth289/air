import os, joblib, pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocessing import FEATURES

app = Flask(__name__)
CORS(app)
bundle = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))
model, medians = bundle["model"], bundle["medians"]

def category(co):
    # simple illustrative thresholds (mg/m^3) -- adjust for your project
    return "Good" if co < 2 else "Moderate" if co < 4 else "Poor" if co < 8 else "Pollution episode"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    row = pd.DataFrame([{f: data.get(f) for f in FEATURES}]).astype(float)
    row = row.fillna(medians)
    co = float(model.predict(row)[0])
    return jsonify({"CO_prediction": round(co, 2), "status": category(co)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
