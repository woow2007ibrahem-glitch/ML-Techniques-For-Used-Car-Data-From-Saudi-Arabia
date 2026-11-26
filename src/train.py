# to save model after train
import os
import joblib

os.makedirs("models", exist_ok=True)
joblib.dump(models, "models/used_car_price_model.joblib")