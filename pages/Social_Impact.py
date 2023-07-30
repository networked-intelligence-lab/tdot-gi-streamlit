import streamlit as st
from streamlit_js_eval import streamlit_js_eval, get_geolocation
import pandas as pd
from streamlit_extras.app_logo import add_logo

add_logo("media/logo.png", height=150)

st.title("Social Impact")

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

st.header("Enhanced Property Value")
median_prop_val = st.number_input("Median of the property value for that area and anticipated enhancement in value", value=0)
num_properties = st.number_input("Approximate number of properties in the area", value=0)
st.write(f"Total monetary gain: ${median_prop_val * num_properties}")

st.header("Recreational Use")
total_ant_veg_area = st.number_input("Total anticipated vegetation area", value=0)
total_parklot_veg_area = st.number_input("Total anticipated parking lot area to be vegetated", value=0)
total_green_roof = st.number_input("Total anticipated green roof area", value=0)
st.write(f"Total anticipated vegetated area for recreational use: {total_ant_veg_area + total_parklot_veg_area + total_green_roof} sq. ft.")
