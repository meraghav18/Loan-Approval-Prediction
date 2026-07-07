import streamlit as st
import pandas as pd
import joblib

# Load model, scaler and feature names
model = joblib.load("loan_model.pkl")
scaler = joblib.load("scaler1.pkl")
feature_names = joblib.load("feature_names.pkl")

st.set_page_config(page_title="Loan Approval Prediction", page_icon="🏦")

st.title("🏦 Loan Approval Prediction")
st.write("Fill the details below to predict whether the loan will be Approved or Rejected.")

# ---------------------- Input Fields ----------------------

no_of_dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=10,
    value=0
)

income_annum = st.number_input(
    "Annual Income",
    min_value=0,
    value=500000
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=1000000
)

loan_term = st.number_input(
    "Loan Term (Years)",
    min_value=1,
    value=10
)

cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900,
    value=750
)

residential_assets_value = st.number_input(
    "Residential Assets Value",
    min_value=0,
    value=0
)

commercial_assets_value = st.number_input(
    "Commercial Assets Value",
    min_value=0,
    value=0
)

luxury_assets_value = st.number_input(
    "Luxury Assets Value",
    min_value=0,
    value=0
)

bank_asset_value = st.number_input(
    "Bank Asset Value",
    min_value=0,
    value=0
)

# ---------------------- Prediction ----------------------

if st.button("Predict Loan Status"):

    data = pd.DataFrame([[

        no_of_dependents,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value

    ]], columns=feature_names)

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")