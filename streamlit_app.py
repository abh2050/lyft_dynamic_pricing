
import streamlit as st
import joblib
import numpy as np

# Load the trained Linear Regression model
model = joblib.load('linear_regression_model.joblib')

# Define the Streamlit app
st.title('Lyft Trip Cost Predictor')

# Input fields
trip_distance = st.number_input('Enter the trip distance (in miles):', min_value=0.0, format='%f')
pickup_day_of_week = st.selectbox('Select the pickup day of the week:', options=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], index=0)
pickup_hour = st.slider('Select the pickup hour:', 0, 23, 0)
is_peak_hour = st.checkbox('Is it peak hour?')

# Convert inputs to model format
pickup_day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(pickup_day_of_week)
is_peak_hour = int(is_peak_hour)

# Predict button
if st.button('Predict Cost'):
    # Make prediction
    features = np.array([[trip_distance, pickup_day_of_week, pickup_hour, is_peak_hour]])
    prediction = model.predict(features)
    
    # Display the prediction
    st.success(f'The estimated trip cost is: ${prediction[0]:.2f}')
