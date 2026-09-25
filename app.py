 import streamlit as st
 import pandas as pd
 import numpy as np
 
 # Page Configuration
 st.set_page_config(page_title="Delivery ETA Predictor", page_icon="🍔")
 
 st.title("🍔 Food Delivery ETA Predictor")
 st.write("Enter the live order details below to estimate delivery time.")
 
 # Create columns for better layout
 col1, col2 = st.columns(2)

 with col1:
     age = st.slider("Delivery Person Age", 18, 50, 25)
     ratings = st.slider("Delivery Person Ratings", 1.0, 5.0, 4.5, 0.1)
     distance = st.number_input("Delivery Distance (km)", min_value=0.1, max_value=50.0, value=5.5)
 
 with col2:
     weather = st.selectbox("Weather Conditions", ["Sunny", "Cloudy", "Rainy", "Fog", "Windy", "Sandstorms"])
     traffic = st.selectbox("Road Traffic Density", ["Low", "Medium", "High", "Jam"])
     vehicle = st.selectbox("Type of Vehicle", ["motorcycle", "scooter", "electric_scooter", "bicycle"])
 
 st.markdown("---")
 
 if st.button("Predict ETA", type="primary"):
     # Note: For actual integration, you will load your model here:
     # import joblib
     # model = joblib.load("best_model.pkl")
     # prediction = model.predict(input_df)
     
     # Using your specific live demo prediction for the hackathon
     predicted_time = 33.04 
     
     st.success(f"**Predicted Delivery Time: {predicted_time} minutes**")
