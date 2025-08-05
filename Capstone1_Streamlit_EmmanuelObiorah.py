import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("./best_rf_model.pkl")

# Page setup
st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")
st.title("🔐 SecureLife Insurance Premium Estimator")
st.markdown("Use this app to estimate customer insurance premiums based on lifestyle and policy information.")

# 👤 Input layout
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 30)
    income = st.number_input("Annual Income", min_value=0, value=0)
    health = st.slider("Health Score", 0, 100, 75)
    credit = st.slider("Credit Score", 300, 900, 700)
    dependents = st.slider("Number of Dependents", 0, 10, 2)

with col2:
    policy_age = st.slider("Policy Age (years)", 0, 30, 5)
    vehicle_age = st.slider("Vehicle Age (years)", 0, 20, 3)
    insurance_duration = st.slider("Insurance Duration (months)", 1, 120, 12)
    previous_claims = st.number_input("Number of Previous Claims", min_value=0, max_value=10, value=0)

# 🎯 Predict
# ✅ Place this OUTSIDE the button so it's always available
expected_cols = [
    'Age', 'Annual Income', 'Health Score', 'Credit Score', 'Number of Dependents',
    'Policy Age', 'Vehicle Age', 'Insurance Duration', 'Previous Claims'
]

# 🎯 Predict
if st.button("Predict Premium"):
    input_data = pd.DataFrame([[
        age,
        income,
        health,
        credit,
        dependents,
        policy_age,
        vehicle_age,
        insurance_duration,
        previous_claims
    ]], columns=expected_cols)

    # Optional debug
    st.write("🧾 Input Data:", input_data)

    # Safety check
    if input_data.isnull().values.any():
        st.error("⚠️ One or more input values are missing or invalid. Please review your inputs.")
    else:
        prediction = model.predict(input_data)
        st.success(f"💰 Estimated Premium: ₦{prediction[0]:,.2f}")
