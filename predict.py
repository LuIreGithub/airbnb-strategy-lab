import joblib

saved = joblib.load("model.pkl")

model = saved["model"]
columns = saved["columns"]

