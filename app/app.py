import streamlit as st
import numpy as np
import pandas as pd
import joblib
import shap
import plotly.graph_objects as go

# Load model, scaler, background data
model = joblib.load("models/xgb_model.joblib")
scaler = joblib.load("models/scaler.joblib")
background_data = pd.read_csv("data/x_train_background.csv")

# Load SHAP explainer once
@st.cache_resource
def get_explainer():
    return shap.Explainer(model, background_data)

explainer = get_explainer()

# Threshold for classification
THRESHOLD = 0.95

# UI layout
st.set_page_config(page_title="Machine Failure Predictor", layout="centered")
st.title("🛠️ AI-Based Machine Failure Prediction")
st.markdown("Enter the sensor values below to predict potential machine failure.")

with st.form(key="prediction_form"):
    air_temp = st.number_input("Air Temperature [K]", 250.0, 400.0, value=298.0)
    process_temp = st.number_input("Process Temperature [K]", 250.0, 500.0, value=308.0)
    speed = st.number_input("Rotational Speed [rpm]", 500.0, 3000.0, value=1500.0)
    torque = st.number_input("Torque [Nm]", 0.0, 100.0, value=40.0)
    tool_wear = st.number_input("Tool Wear [min]", 0.0, 300.0, value=0.0)

    product_quality = st.selectbox("Product Quality Variant", ("L", "M", "H"))
    _L, _M, _H = 0, 0, 0
    if product_quality == "L":
        _L = 1
    elif product_quality == "M":
        _M = 1
    else:
        _H = 1

    submit = st.form_submit_button(label="Predict Failure")

if submit:
    # Derived features
    temp_diff = process_temp - air_temp
    power = torque * speed
    torque_per_wear = torque / (tool_wear + 1)

    input_data = pd.DataFrame([[
        air_temp, process_temp, speed, torque, tool_wear,
        _H, _L, _M, temp_diff, power, torque_per_wear
    ]], columns=background_data.columns)

    scaled = scaler.transform(input_data)
    proba = model.predict_proba(scaled)[0][1]

    # Risk zone text
    if proba < 0.40:
        st.success(f"✅ Low Risk of Failure\nProbability: {round(proba, 4)}")
    elif proba < 0.75:
        st.warning(f"⚠️ Moderate Risk of Failure\nProbability: {round(proba, 4)}")
    elif proba < 0.91:
        st.error(f"🔥 High Risk of Failure\nProbability: {round(proba, 4)}")
    else:
        st.error(f"🚨 CRITICAL: Likely Machine Failure!\nProbability: {round(proba, 4)}")

    # Speedometer gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=proba * 100,
        number={'suffix': "%"},
        title={'text': "Failure Risk Level"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "black"},
            'steps': [
                {'range': [0, 40], 'color': "green"},
                {'range': [40, 75], 'color': "yellow"},
                {'range': [75, 90], 'color': "orange"},
                {'range': [90, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': proba * 100
            }
        }
    ))
    st.plotly_chart(fig)

    # SHAP Explanation
    st.subheader("🔍 Feature Contributions to Risk Prediction")
    shap_values = explainer(input_data)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    shap.plots.waterfall(shap_values[0], max_display=10)
    st.pyplot(bbox_inches='tight')
