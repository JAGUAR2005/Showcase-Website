from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve plots as static files
os.makedirs('plots', exist_ok=True)
app.mount("/plots", StaticFiles(directory="plots"), name="plots")

print("Loading models and registry...")
pipeline = joblib.load('xgb_pipeline.pkl')
clf_pipeline = joblib.load('xgb_classifier_pipeline.pkl')
with open('models_registry.json', 'r') as f:
    models_registry = json.load(f)
print("Models and registry loaded.")

class CarFeatures(BaseModel):
    market: str
    brand: str
    model: str
    year: int
    mileage: int
    fuel_type: str
    transmission: str
    target_currency: str = "USD"

EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 83.50,
    "GBP": 0.79
}

CURRENCY_SYMBOLS = {
    "USD": "$",
    "EUR": "€",
    "INR": "₹",
    "GBP": "£"
}

@app.get('/config')
async def get_config():
    return models_registry

@app.get('/metrics')
async def get_metrics():
    # Updated metrics from latest run
    return {
        "regression": {"r2": 0.880, "mae": 3316.73, "rmse": 6145.14},
        "classification": {"accuracy": 0.814, "recall": 0.814, "precision": 0.815, "f1": 0.814},
        "dataset": {"records": 364062}
    }

@app.post('/predict')
async def predict(features: CarFeatures):
    data = {
        'brand': [features.brand.lower()],
        'model': [features.model.lower()],
        'car_age': [2024 - features.year],
        'mileage': [features.mileage],
        'km_per_year': [features.mileage / (2024 - features.year + 1)],
        'fuel_type': [features.fuel_type.lower()],
        'transmission': [features.transmission.lower()],
        'market': [features.market.lower()]
    }
    df = pd.DataFrame(data)
    
    # Predict continuous price (Base is USD)
    pred_price_usd = pipeline.predict(df)[0]
    
    # Predict segment
    pred_segment_idx = clf_pipeline.predict(df)[0]
    segments = ['Budget', 'Mid-Range', 'Premium', 'Luxury']
    pred_segment = segments[pred_segment_idx]
    
    # Currency Conversion
    rate = EXCHANGE_RATES.get(features.target_currency.upper(), 1.0)
    symbol = CURRENCY_SYMBOLS.get(features.target_currency.upper(), "$")
    converted_price = pred_price_usd * rate
    
    return {
        'predicted_price': round(float(converted_price), 2),
        'segment': pred_segment,
        'currency': features.target_currency.upper(),
        'symbol': symbol
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
