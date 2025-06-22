# train_model.py
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("features/aqi_features.csv")

X = df[['pm2_5', 'pm10', 'no2', 'o3']]
y = df['aqi']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBRegressor()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "models/aqi_model.pkl")
