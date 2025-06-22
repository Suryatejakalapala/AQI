# app.py
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/aqi_model.pkl")
data = pd.read_csv("features/aqi_features.csv").tail(3)

preds = model.predict(data[['pm2_5', 'pm10', 'no2', 'o3']])

st.title("🌍 Air Quality Index Predictor")
st.write("Predictions for the next 3 time steps:")
st.write("Input data:")
st.dataframe(data[['pm2_5', 'pm10', 'no2', 'o3']])

for i, pred in enumerate(preds):
    st.metric(f"Time {i+1}", f"AQI: {round(pred, 2)}")
