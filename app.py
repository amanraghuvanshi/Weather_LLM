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