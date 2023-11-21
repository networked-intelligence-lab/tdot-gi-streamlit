import streamlit as st
from streamlit_js_eval import streamlit_js_eval, get_geolocation
import pandas as pd
from streamlit_extras.app_logo import add_logo
import googlemaps
import pprint
import json
import geopy.distance
import warnings

# Suppress all warnings
warnings.simplefilter("ignore")

# Use streamlit secrets for sensitive data like API keys
tokens = st.secrets

add_logo("media/logo.png", height=150)
st.title("Social Impact")

# Initialize session state variables for number inputs and location input
input_keys = ["loc_input", "radius_input", "median_prop_val", "num_properties",
              "total_ant_veg_area", "total_parklot_veg_area", "total_green_roof"]

for key in input_keys:
    if key not in st.session_state:
        st.session_state[key] = '' if key == 'loc_input' else 0

loc = get_geolocation()

if loc:
    st.session_state["loc_input"] = st.text_input("Enter latitude and longitude", value=f"{loc['coords']['latitude']}, {loc['coords']['longitude']}" if st.session_state["loc_input"] == '' else st.session_state["loc_input"])
else:
    st.session_state["loc_input"] = st.text_input("Enter latitude and longitude", value="36.1627, -86.7816" if st.session_state["loc_input"] == '' else st.session_state["loc_input"])

st.write("Enter latitude and longitude in the format: 36.1627, -86.7816")

if float(st.session_state["radius_input"]) == 0:
    st.session_state["radius_input"] = 1.5

# Nearby Parks Section
st.subheader("Nearby Parks")
st.session_state["radius_input"] = st.slider("Radius (miles)", min_value=0.1, max_value=30.0, value=float(st.session_state["radius_input"]))
gmaps = googlemaps.Client(key=tokens["gmaps"])
user_loc = tuple(map(float, st.session_state["loc_input"].split(", ")))
nearby_result = gmaps.places_nearby(
    location=user_loc,
    radius=st.session_state["radius_input"] * 1609.344,
    keyword="park")

pp = pprint.PrettyPrinter(indent=1)
parks_list = []
loc_df_list = []
for place_result in nearby_result["results"]:
    place_loc = (place_result["geometry"]["location"]["lat"], place_result["geometry"]["location"]["lng"])
    loc_df_list.append({"lat": place_loc[0], "lon": place_loc[1], "color": "#0000FF90"})
    parks_list.append({"Distance Away (straight-line; in miles)": geopy.distance.distance(user_loc, place_loc).miles, "Park Name": place_result["name"]})
loc_df = pd.DataFrame.from_dict(loc_df_list)
parks_df = pd.DataFrame.from_dict(parks_list).sort_values(by="Distance Away (straight-line; in miles)", ascending=True)
st.dataframe(parks_df, hide_index=True)
st.header("User Location")
st.map(loc_df, latitude="lat", longitude="lon", size=20)

# Enhanced Property Value Section
st.header("Enhanced Property Value")
st.session_state["median_prop_val"] = st.number_input("Median of the property value for that area and anticipated enhancement in value", value=st.session_state["median_prop_val"])
st.session_state["num_properties"] = st.number_input("Approximate number of properties in the area", value=st.session_state["num_properties"])
enhanced_property_value = st.session_state["median_prop_val"] * st.session_state["num_properties"]
st.write(f"Total monetary gain: ${enhanced_property_value}")

# Recreational Use Section
st.header("Recreational Use")
st.session_state["total_ant_veg_area"] = st.number_input("Total anticipated vegetation area", value=st.session_state["total_ant_veg_area"])
st.session_state["total_parklot_veg_area"] = st.number_input("Total anticipated parking lot area to be vegetated", value=st.session_state["total_parklot_veg_area"])
st.session_state["total_green_roof"] = st.number_input("Total anticipated green roof area", value=st.session_state["total_green_roof"])
st.write(f"Total anticipated vegetated area for recreational use: {st.session_state['total_ant_veg_area'] + st.session_state['total_parklot_veg_area'] + st.session_state['total_green_roof']} sq. ft.")
