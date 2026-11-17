# Air Quality Prediction & Pollution Episode Detection

Predicts CO(GT) from the UCI Air Quality dataset using a Random Forest regressor.

## Run
```
cd backend
pip install -r requirements.txt
python train_model.py     # regenerates model.pkl
python app.py             # starts API on http://127.0.0.1:5000
```
Then open `frontend/index.html` in a browser.
