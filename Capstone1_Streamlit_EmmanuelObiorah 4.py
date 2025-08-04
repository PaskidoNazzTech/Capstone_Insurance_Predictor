
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("best_rf_model.pkl")

st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")

st.title("🔐 SecureLife Insurance Premium Estimator")
st.markdown("Welcome to the SecureLife Insurance Premium Predictor App!")

# Sample inputs
age = st.slider("Age", 18, 100, 30)
income = st.number_input("Annual Income", min_value=0)
health = st.slider("Health Score", 0, 100, 75)
credit = st.slider("Credit Score", 300, 900, 700)
dependents = st.slider("Number of Dependents", 0, 10, 2)

# Add more input fields here based on your features...

# Predict
if st.button("Predict Premium"):
    input_data = pd.DataFrame({
        'Age': [age],
        'Annual Income': [income],
        'Health Score': [health],
        'Credit Score': [credit],
        'Number of Dependents': [dependents],
        # add other required features here...
    })

    prediction = model.predict(input_data)
    st.success(f"Estimated Premium: ₦{prediction[0]:,.2f}")
