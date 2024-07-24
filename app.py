import os
import openai
import requests
import streamlit as st

# Function handling the data from the openweather 
def weather_data(city, WEATHER_TOKEN):
    base_URI = "http://api.openweather.org/data/2.5/weather?"
    complete_uri = base_URI + "appid=" + WEATHER_TOKEN + "&q=" + city
    resp = requests.get(complete_uri)
    return resp.json()

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
