
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("income_xgb_model.pkl")

st.set_page_config(page_title="Income Prediction App")
st.title("👤 Income Classification App")
st.write("Predict whether a person earns more than 50K/year based on demographic inputs.")

# Function to take user input and format as DataFrame
def user_input():
    age = st.slider("Age", 18, 70, 30)
    workclass = st.selectbox("Workclass", [
        "Private", "Self-emp-not-inc", "Local-gov", "State-gov", "Federal-gov", "Self-emp-inc", "Without-pay", "Never-worked", "Other"
    ])
    educational_num = st.slider("Education Level (numeric)", 1, 16, 9)
    marital_status = st.selectbox("Marital Status", [
        "Never-married", "Married-civ-spouse", "Divorced", "Separated", "Widowed", "Married-spouse-absent", "Other"
    ])
    occupation = st.selectbox("Occupation", [
        "Prof-specialty", "Exec-managerial", "Adm-clerical", "Sales", "Craft-repair",
        "Transport-moving", "Handlers-cleaners", "Machine-op-inspct", "Other"
    ])
    relationship = st.selectbox("Relationship", [
        "Husband", "Not-in-family", "Own-child", "Unmarried", "Wife", "Other-relative"
    ])
    race = st.selectbox("Race", ["White", "Black", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other"])
    sex = st.selectbox("Gender", ["Male", "Female"])
    hours_per_week = st.slider("Hours per Week", 1, 80, 40)
    native_country = st.selectbox("Native Country", [
        "United-States", "Mexico", "Philippines", "Germany", "Canada", "India", "England", "Cuba", "Jamaica", "Other"
    ])
    capital_diff = st.number_input("Capital Gain - Capital Loss (capital_diff)", value=0)

    data = {
        "age": age,
        "workclass": workclass,
        "educational-num": educational_num,
        "marital-status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "sex": sex,
        "hours-per-week": hours_per_week,
        "native-country": native_country,
        "capital_diff": capital_diff
    }

    return pd.DataFrame([data])

# Get user input
input_df = user_input()

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][int(prediction)]
    
    result = ">50K" if prediction == 1 else "<=50K"
    st.markdown(f"### 🧾 Prediction: **{result}**")
    st.markdown(f"**Confidence**: {proba:.2%}")
