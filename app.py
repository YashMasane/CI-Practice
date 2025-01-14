import streamlit as st

def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI)."""
    return round(weight / (height ** 2), 2)

st.title("BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (in meters):", min_value=0.0, format="%.2f")

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi}")
        
        # Interpret BMI
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than 0!")
