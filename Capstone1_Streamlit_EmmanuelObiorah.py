import streamlit as st
import pandas as pd
import joblib
import os
import requests
import tarfile

import warnings
from sklearn.exceptions import InconsistentVersionWarning
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# ─── Download and extract model if not already present ───
if not os.path.exists("best_rf_model.pkl"):
    file_id = '1Rt-nDNkOP04L7td5kg2JJke-HnIMop1g'
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    with st.spinner("⬇️ Downloading model from Google Drive..."):
        response = requests.get(download_url, stream=True)
        with open("best_rf_model.tar.gz", "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    with st.spinner("📦 Extracting model file..."):
        with tarfile.open("best_rf_model.tar.gz", "r:gz") as tar:
            tar.extractall()

    st.success("✅ Model downloaded and extracted!")

# ─── Load model ───
model = joblib.load("best_rf_model.pkl")

# ─── Streamlit Page Config ───
st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")
st.title("🔐 SecureLife Insurance Premium Estimator")
st.markdown("Use this app to estimate customer insurance premiums based on lifestyle and policy information.")

# ─── User Inputs ───
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 30)
    income = st.number_input("Annual Income", min_value=0, value=500000)
    health = st.slider("Health Score", 0, 100, 75)
    credit = st.slider("Credit Score", 300, 900, 700)
    dependents = st.slider("Number of Dependents", 0, 10, 2)

with col2:
    policy_age = st.slider("Policy Age (years)", 0, 30, 5)
    vehicle_age = st.slider("Vehicle Age (years)", 0, 20, 3)
    insurance_duration = st.slider("Insurance Duration (months)", 1, 120, 12)
    previous_claims = st.number_input("Number of Previous Claims", min_value=0, max_value=10, value=0)

# ─── Prediction ───
if st.button("Predict Premium"):
    input_data = pd.DataFrame({
        'Age': [age],
        'Annual Income': [income],
        'Health Score': [health],
        'Credit Score': [credit],
        'Number of Dependents': [dependents],
        'Policy Age': [policy_age],
        'Vehicle Age': [vehicle_age],
        'Insurance Duration': [insurance_duration],
        'Previous Claims': [previous_claims]
    })

    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Premium: ₦{prediction[0]:,.2f}")
