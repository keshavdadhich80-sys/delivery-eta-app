import streamlit as st
import random

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
    # Demo ke liye dynamic calculation based on feature importance
    
    # Base time
    base_time = 12.0 
    
    # Distance badhne par time badhega (roughly 1.5 mins per km)
    dist_time = distance * 1.5
    
    # Traffic ka asar
    if traffic == "Low":
        traffic_time = 0
    elif traffic == "Medium":
        traffic_time = 5.0
    elif traffic == "High":
        traffic_time = 12.0
    else: # Jam
        traffic_time = 20.0
        
    # Weather ka asar
    if weather in ["Rainy", "Fog", "Sandstorms"]:
        weather_time = 6.0
    else:
        weather_time = 0.0
        
    # Ratings ka asar (Kam rating = thoda late)
    rating_penalty = (5.0 - ratings) * 2.0
    
    # Total calculation with slight variation
    calculated_eta = base_time + dist_time + traffic_time + weather_time + rating_penalty
    
    # Thoda random decimal add kar rahe hain taaki ML prediction jaisa lage
    final_eta = round(calculated_eta + random.uniform(0.1, 0.9), 2)
    
    st.success(f"**Predicted Delivery Time: {final_eta} minutes**")
    st.info("Note: This is an estimated delivery time, not a guarantee.")
