import streamlit as st
from prediction_file import predict

st.title("Health Insurance Price Predictor")

categorical_options = {
    'Gender' : ["Male", "Female"],
    'Marital Status' : ["Unmarried", "Married"],
    'BMI Category' : ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status' : ['No Smoking', 'Regular', 'Occasionally'],
    'Employment Status' : ['Salaried', 'Self Employed', 'Freelancer', ' '],
    'Region' : ['Northwest', 'Southwest', 'Northeast', 'Southeast'],
    'Medical History' : [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart Disease', 'Heart Disease & High blood pressure', 'Diabetes & Thyroid',
        'Diabetes & Heart Disease'
    ],
    'Insurance Plan' : ["Bronze", "Silver", "Gold"]
}

## Creating rows:

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input("Age", min_value = 18, max_value=100, step=1)
with row1[1]:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=20, step=1)
with row1[2]:
    income_lakhs = st.number_input("Income in Lakhs", min_value=0, max_value=200, step=1)


with row2[0]:
    genetical_risk = st.number_input("Genetical Risk", min_value=0, max_value=5, step=1)
with row2[1]:
    insurance_plan = st.selectbox("Insurance Plan", categorical_options["Insurance Plan"])
with row2[2]:
    employment_status = st.selectbox("Employment Status", categorical_options["Employment Status"])


with row3[0]:
    gender = st.selectbox("Gender", categorical_options["Gender"])
with row3[1]:
    marital_status = st.selectbox("Marital Status", categorical_options["Marital Status"])
with row3[2]:
    bmi_category = st.selectbox("BMI Category", categorical_options["BMI Category"])



with row4[0]:
    smoking_status = st.selectbox("Smoking Status", categorical_options["Smoking Status"])
with row4[1]:
    region = st.selectbox("Region", categorical_options["Region"])
with row4[2]:
    medical_history = st.selectbox("Medical History", categorical_options["Medical History"])


## Input Dictionary:

input_dict = {
    'Age' : age,
    'Number of Dependants' : number_of_dependants,
    'Income in Lakhs' : income_lakhs,
    'Genetical Risk' : genetical_risk,
    'Insurance Plan' : insurance_plan,
    'Employment Status' : employment_status,
    'Gender' : gender,
    'Marital Status' : marital_status,
    'BMI Category' : bmi_category,
    'Smoking Status' : smoking_status,
    'Region' : region,
    'Medical History' : medical_history
}


## Prediction Button:
if st.button("Predict"):
    prediction = predict(input_dict)
    st.success(f'Predicted Premium: {prediction}')