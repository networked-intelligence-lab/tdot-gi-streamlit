import streamlit as st
from streamlit_js_eval import streamlit_js_eval, get_geolocation
from streamlit_extras.app_logo import add_logo
import pandas as pd

add_logo("media/logo.png", height=150)

st.title('TDoT GI Home')
loc = get_geolocation()
if loc:
    loc_df = pd.DataFrame([[loc["coords"]["latitude"], loc["coords"]["longitude"]]], columns=["lat", "lon"])
    loc_input = st.text_input("Enter latitude and longitude", value=f"{loc['coords']['latitude']}, {loc['coords']['longitude']}")
else:
    loc_input = st.text_input("Enter latitude and longitude", value="36.1627, -86.7816")
    loc_df = pd.DataFrame([[float(loc_input.split(",")[0]), float(loc_input.split(",")[1])]], columns=["lat", "lon"])
st.write("Enter latitude and longitude in the format: 36.1627, -86.7816")

st.header("User Location")
st.map(data=loc_df)