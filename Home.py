import streamlit as st
from streamlit_js_eval import streamlit_js_eval, get_geolocation
from streamlit_extras.app_logo import add_logo
import pandas as pd

st.set_page_config(layout="wide")

add_logo("media/logo.png", height=150)

st.title('TDoT GI Home')
st.header("Profile")
st.selectbox("Select a profile", ["TDoT", "Nashville", "Knoxville", "Memphis", "Chattanooga", "Other"])

st.header("Configuration")
num_cols = st.number_input("Select number of GI points of interest", min_value=1, max_value=3, value=1, step=1)
cols = st.columns(num_cols)

for idx, col in enumerate(cols):
    loc = get_geolocation(component_key=f"loc{idx}")
    if num_cols > 1:
        col.header(f"Location {idx + 1}")
    else:
        col.header("Location")
    if loc:
        loc_df = pd.DataFrame([[loc["coords"]["latitude"], loc["coords"]["longitude"]]], columns=["lat", "lon"])
        loc_input = col.text_input("Enter latitude and longitude", value=f"{loc['coords']['latitude']}, {loc['coords']['longitude']}", key=f"loc_input{idx}")
    else:
        loc_input = col.text_input("Enter latitude and longitude", value="36.1627, -86.7816", key=f"loc_input{idx}")
        loc_df = pd.DataFrame([[float(loc_input.split(",")[0]), float(loc_input.split(",")[1])]], columns=["lat", "lon"])
    col.write("Enter latitude and longitude in the format: 36.1627, -86.7816")
    col.map(data=loc_df)
