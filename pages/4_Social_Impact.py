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

# with open("tokens/tokens") as tokens_file:
#     tokens = json.load(tokens_file)

tokens = st.secrets

add_logo("media/logo.png", height=150)
st.title("Social Impact")

loc = get_geolocation()
if loc:
    loc_input = st.text_input("Enter latitude and longitude", value=f"{loc['coords']['latitude']}, {loc['coords']['longitude']}")
    loc_df = pd.DataFrame([[float(loc_input.split(", ")[0]), float(loc_input.split(", ")[1]), "#FF000090"]],
                          columns=["lat", "lon", "color"])
else:
    loc_input = st.text_input("Enter latitude and longitude", value="36.1627, -86.7816")
    loc_df = pd.DataFrame([[float(loc_input.split(",")[0]), float(loc_input.split(",")[1]), "#FF000090"]], columns=["lat", "lon", "color"])
st.write("Enter latitude and longitude in the format: 36.1627, -86.7816")

st.subheader("Nearby Parks")
radius_input = st.slider("Radius (miles)", min_value=0.1, max_value=30.0, value=0.5)
gmaps = googlemaps.Client(key=tokens["gmaps"])
user_loc = (loc_df.iloc[0]["lat"], loc_df.iloc[0]["lon"])
nearby_result = gmaps.places_nearby(
    location=user_loc,
    radius=radius_input * 1609.344,
    keyword="park")

pp = pprint.PrettyPrinter(indent=1)
parks_list = []
loc_df_list = []
for place_result in nearby_result["results"]:
    place_loc = (place_result["geometry"]["location"]["lat"], place_result["geometry"]["location"]["lng"])
    # result_df = pd.DataFrame([[place_loc[0], place_loc[1], "#0000FF90"]], columns=["lat", "lon", "color"])
    # loc_df = loc_df.append({"lat": place_loc[0], "lon": place_loc[1], "color": "#0000FF90"}, ignore_index=True)
    loc_df_list.append({"lat": place_loc[0], "lon": place_loc[1], "color": "#0000FF90"})
    parks_list.append({"Distance Away (straight-line; in miles)": geopy.distance.distance(user_loc, place_loc).miles, "Park Name": place_result["name"]})
loc_df = loc_df.from_dict(loc_df_list)
parks_df = pd.DataFrame.from_dict(parks_list).sort_values(by="Distance Away (straight-line; in miles)", ascending=True)
st.dataframe(parks_df, hide_index=True)
st.header("User Location")
st.map(loc_df, latitude="lat", longitude="lon", size=20)

st.header("Enhanced Property Value")
median_prop_val = st.number_input("Median of the property value for that area and anticipated enhancement in value", value=0)
num_properties = st.number_input("Approximate number of properties in the area", value=0)
st.write(f"Total monetary gain: ${median_prop_val * num_properties}")

st.header("Recreational Use")
total_ant_veg_area = st.number_input("Total anticipated vegetation area", value=0)
total_parklot_veg_area = st.number_input("Total anticipated parking lot area to be vegetated", value=0)
total_green_roof = st.number_input("Total anticipated green roof area", value=0)
st.write(f"Total anticipated vegetated area for recreational use: {total_ant_veg_area + total_parklot_veg_area + total_green_roof} sq. ft.")

st.header("Heat Reduction")