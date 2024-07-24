import os
import openai
import requests
import streamlit as st

# main function that is handling the streamlit
def main():
    # Sidebar configuration
    st.sidebar.title("Weather Forecasting Application using LLM")
    location = st.sidebar.text_input("Enter the location:", "Kolkata")
    
    # OpenWeather Tokens
    OPEN_WEATHER_TOKEN = os.getenv("OPENWEATHERTOKEN")
    OPENAI_TOKEN = os.getenv("SECRET_KEY")
    
    # Button to fetch and display weather data
    response = st.sidebar.button("Accumulate Information")
    
    
# Entry Point
if __name__ == "__main__":
    main()
