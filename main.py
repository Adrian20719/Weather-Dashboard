import streamlit as st
import requests
import json
import pandas as pd
import numpy as np

st.title("Welcome to Adrian's Weather Dashboard")
st.subheader("Asia/Colombo")
# Make API request
resp=requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,wind_speed_10m_max")
# Object notation
st.sidebar.write("Weather details")
value = json.loads(resp.text)
st.sidebar.write("Latitude",value["latitude"])
st.sidebar.write("Longitude",value["longitude"])
st.sidebar.write("current temperature",value["current"]["temperature_2m"])
st.sidebar.write("current wind speed",value["current"]["wind_speed_10m"])
if value ["current"]["is_day"]==1:
    Day_Night="Night"
else:
    Day_Night="Day"
option = st.sidebar.selectbox(
    "Choose your option",
    ("temperature_2_max", "temperature_2_min", "sunrise","sunset"),
)

st.write("You selected:", option)
col1, col2, col3 = st.columns(3)
col1.metric("Current Temperature",value["current"]["temperature_2m"])
col2.metric("Current Wind Speed", value["current"]["wind_speed_10m"])
col3.metric("day or night",Day_Night)
            
st.video("https://www.youtube.com/watch?v=HBV7hrxvc2w&pp=ygUHQ29sb21ibw%3D%3D")

from datetime import datetime

# Get the current date and time
present = datetime.now()

# Display the current date and time
st.write("Current date and time:", present)

daily_max_temp_df = pd.DataFrame(value["daily"]["temperature_2m_max"], value["daily"]["time"])
daily_min_temp_df = pd.DataFrame(value["daily"]["temperature_2m_min"], value["daily"]["time"])
daily_sunrise_df = pd.DataFrame(value["daily"]["sunrise"], value["daily"]["time"])
daily_sunset_df = pd.DataFrame(value["daily"]["sunset"], value["daily"]["time"])

if option == "temperature_2_max":
    st.line_chart(daily_max_temp_df)

elif option == "temperature_2_min":
    st.line_chart(daily_min_temp_df)

elif option == "sunset":
    st.line_chart(daily_sunset_df)

else:
    st.line_chart(daily_sunrise_df)






