import streamlit as st

def get_user_input():
  blood_pressure = st.number_input("What is your blood pressure?")
  heart_rate = st.number_input("What is your maximum heart rate during exercise in beats per minute?")
  input_features = [[blood_pressure, heart_rate]]
  return input_features
