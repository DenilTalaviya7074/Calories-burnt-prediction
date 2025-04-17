import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Calories Burnt Predictor", layout="centered")
st.title("🔥 Calories Burnt Prediction App")

# Load the trained model
model = joblib.load("Calories_Burnt_prediction.pkl")  # Ensure this file is in the same directory

st.subheader("📝 Enter Your Information")

# Collect user inputs through form
with st.form("calories_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=20, max_value=100, value=25, step=1)
    height = st.number_input("Height (cm)", min_value=123, max_value=222, value=170, step=1)
    weight = st.number_input("Weight (kg)", min_value=36, max_value=132, value=70, step=1)
    workout_duration = st.number_input("Workout Duration (minutes)", min_value=1, max_value=30, value=20, step=1)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=67, max_value=128, value=110, step=1)
    body_temp = st.number_input("Body Temperature (°C)", min_value=37.0, max_value=42.0, value=37.0, step=0.1)

    submit = st.form_submit_button("Predict Calories Burnt")

# Process and predict when form is submitted
if submit:
    # Convert gender to numeric
    gender_num = 0 if gender == "Male" else 1

    # Prepare input for model with correct column names
    input_data = pd.DataFrame([{
        'Gender': gender_num,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'Workout Duration': workout_duration,
        'Heart_Rate': heart_rate,
        'Body_Temp': body_temp   # Corrected key here
    }])

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🔥 Predicted Calories Burnt: {round(prediction, 2)} kcal")
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
