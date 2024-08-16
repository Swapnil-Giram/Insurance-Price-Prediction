import streamlit as st
import pickle
import numpy as np


# Load the trained model using pickle
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)
    # print(model)


# App title
st.title("Insurance Premium Price Predictor")

# Collect user input
age = st.number_input("Age", min_value=18, max_value=100, value=30)
diabetes = st.selectbox("Diabetes", options=[0, 1])
blood_pressure_problems = st.selectbox("Blood Pressure Problems", options=[0, 1])
any_transplants = st.selectbox("Any Transplants", options=[0, 1])
any_chronic_diseases = st.selectbox("Any Chronic Diseases", options=[0, 1])
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
known_allergies = st.selectbox("Known Allergies", options=[0, 1])
history_of_cancer_in_family = st.selectbox("History of Cancer in Family", options=[0, 1])
number_of_major_surgeries = st.number_input("Number of Major Surgeries", min_value=0, max_value=10, value=0)
BMI_Score = st.number_input("BMI", min_value=10, max_value=50, value=15)

# Prepare input for prediction
user_input = np.array([[age, diabetes, blood_pressure_problems, any_transplants, any_chronic_diseases,
                        height, weight, known_allergies, history_of_cancer_in_family, number_of_major_surgeries,BMI_Score]])

# Predict the premium price
if st.button("Predict Premium Price"):
    prediction = model.predict(user_input)
    st.success(f"Predicted Premium Price: RS {prediction[0]:,.2f}")



