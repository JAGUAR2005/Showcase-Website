# Feature: Multi-Currency Support and Model-Specific Valuations

## Objective
Enhance the valuation engine to support specific car models (for accurate depreciation modeling) and allow users to view predicted prices in multiple currencies dynamically.

## Key Files & Context
- `train_pipeline.py`: Needs to extract 'model' from datasets and train the ML models with it. Needs to generate a dynamic registry of markets -> brands -> models.
- `main.py`: Needs a new endpoint to serve the hierarchy configuration, and updates to the prediction endpoint to accept the `model` feature and handle currency conversions.
- `frontend/src/App.tsx`: Needs UI updates for cascading dropdowns (Brand -> Model) and a toggle/selector for the display currency.

## Implementation Steps

### 1. Data Pipeline Updates (`train_pipeline.py`)
- Modify `clean_india`, `clean_europe`, and `clean_uk` to extract the `model` name. 
  - For India: parse `full_name`.
  - For Europe: parse the existing `model` column.
  - For UK: parse the `model` column.
- Update `X` features to include `model`.
- Add `model` to `high_cardinality_features` for Target Encoding.
- Generate a nested dictionary structure `registry[market][brand] = [list of models]` during training.
- Save this registry to disk as `models_registry.json`.
- Re-train the models to output updated `xgb_pipeline.pkl` and `xgb_classifier_pipeline.pkl`.

### 2. Backend API Updates (`main.py`)
- Load `models_registry.json` on startup.
- Create a new `GET /config` endpoint that returns the registry.
- Update `CarFeatures` BaseModel to include `model: str` and `target_currency: str`.
- Add static exchange rates in the backend (e.g., base USD, conversion to EUR, INR, GBP).
- Update the `/predict` logic to incorporate the `model` feature into the Pandas DataFrame before prediction.
- Convert the predicted price based on `target_currency` and return the formatted value and symbol.

### 3. Frontend App Updates (`frontend/src/App.tsx`)
- Add state for `registry` (fetched from `/config`).
- Add state for selected `targetCurrency` (e.g., 'USD', 'INR', 'EUR', 'GBP').
- Update the UI to include a Currency Toggle mechanism near the configuration panel or the result display.
- Update the form to use the dynamic `registry` for cascading selections: Market dictates available Brands, Brand dictates available Models.
- Ensure the `predict` payload sends the newly selected `model` and `target_currency`.
- Render the correct currency symbol returned by the backend.

## Verification & Testing
- Run `train_pipeline.py` and verify `models_registry.json` is created successfully.
- Start the backend and verify `/config` returns the correct hierarchy.
- Test the `/predict` endpoint via cURL or Swagger UI to ensure the `model` feature improves accuracy and currency conversions apply correctly.
- Test the React frontend to ensure dropdowns cascade properly without errors and the currency toggles instantly refresh the displayed price.