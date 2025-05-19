import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("/content/drive/MyDrive/data/outputs/best_rf_model.pkl")
le_vision = joblib.load("/content/drive/MyDrive/data/outputs/le_vision.pkl")
le_region = joblib.load("/content/drive/MyDrive/data/outputs/le_region.pkl")

st.set_page_config(page_title="Cost of Living Predictor", layout="centered")
st.title("Predict Cost of Living")

income = st.slider("Income Index", 1000.0, 10000.0, 4500.0)
vision_cat = st.selectbox("Vision Category", le_vision.classes_)
urban_score = st.selectbox("Region", le_region.classes_)
cost_lag = st.slider("Last Month's Cost (Lag)", 500.0, 9000.0, 2800.0)
income_roll = st.slider("Rolling Avg Income", 1000.0, 10000.0, 4400.0)

if st.button("Predict"):
    vision_code = le_vision.transform([vision_cat])[0]
    urban_code = le_region.transform([urban_score])[0]

    X = pd.DataFrame([{
        "income_index": income,
        "vision_code": vision_code,
        "urbanization_code": urban_code,
        "cost_lag1": cost_lag,
        "income_rolling": income_roll
    }])

    pred = model.predict(X)[0]
    st.success(f"Estimated Cost of Living: ₹{round(pred, 2)}")
