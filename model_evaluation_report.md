# Machine Learning Model Evaluation Report
**Project**: Global Car Resale Value Prediction
**Target**: Multi-Market ML Pipeline (India, Europe, Asia)

## 1. Problem Identification
The project addresses two distinct machine learning tasks:
1. **Regression**: Predicting the exact resale price of a vehicle (Continuous target).
2. **Classification**: Categorizing vehicles into price tiers (Budget, Mid-Range, Premium, Luxury) based on market quartiles.

## 2. Dataset Description
- **Total Records**: 355640
- **Features**: Brand, Model, Car Age, Mileage, Km per Year, Fuel Type, Transmission, Market Region.
- **Preprocessing**: 
    - Standard Scaling for numerical features.
    - One-Hot Encoding for low-cardinality categories.
    - **Target Encoding** for the high-cardinality `brand` and `model` features.

## 3. Regression Model Performance (XGBoost)
This model predicts the continuous numerical value of the car.

| Metric | Value |
|--------|-------|
| **R² Score** | 0.8796 |
| **MAE (Mean Absolute Error)** | $3316.73 |
| **RMSE (Root Mean Squared Error)** | $6145.14 |

**Interpretation**: An R² of 0.8796 indicates that the model explains 88.0% of the variance in car prices.

## 4. Classification Model Performance (Price Segments)
This model categories cars into price segments to demonstrate classification robustness.

| Metric | Value |
|--------|-------|
| **Accuracy** | 0.8139 |
| **Precision (Macro)** | 0.8151 |
| **Recall (Macro)** | 0.8140 |
| **F1-Score (Macro)** | 0.8144 |

### Detailed Classification Report
```
              precision    recall  f1-score   support

      Budget       0.88      0.88      0.88     17725
   Mid-Range       0.74      0.77      0.75     17785
     Premium       0.75      0.74      0.75     17800
      Luxury       0.89      0.86      0.88     17818

    accuracy                           0.81     71128
   macro avg       0.82      0.81      0.81     71128
weighted avg       0.82      0.81      0.81     71128

```

## 5. Visualizations
- **Confusion Matrix**: [plots/confusion_matrix.png](plots/confusion_matrix.png)
- **Predicted vs Actual**: [plots/predicted_vs_actual.png](plots/predicted_vs_actual.png)
- **Residual Plot**: [plots/residual_plot.png](plots/residual_plot.png)
- **Feature Importance**: [plots/feature_importance.png](plots/feature_importance.png)

## 6. Key Insights
- **Model Quality**: The XGBoost implementation demonstrates high predictive power in both regression and classification tasks.
- **Top Predictors**: Car age and mileage remain the strongest predictors of depreciation.
- **Market Differences**: Regional market features significantly influence the pricing baseline.
