import streamlit as st
from streamlit_js_eval import streamlit_js_eval, get_geolocation
from streamlit_extras.app_logo import add_logo
import pandas as pd
from glob import glob
from helpers.helpers import update_registry
from registry.registry import *
import os
import json
import shutil
from st_pages import show_pages_from_config, add_page_title
import time
from streamlit_folium import folium_static
import folium
from folium.plugins import Draw


st.set_page_config(layout="wide")
add_logo("media/logo.png", height=150)

st.title('TDoT GI Home')
st.subheader("Last updated: 11/09/2023")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Profiles                                                                                                           ■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
st.header("Profile")
profile_list = list(glob("profiles/*.json"))
# move last selected profile to the start of the list
last_selected_profile = registry["last_selected_profile"]
try:
    profile_list.remove(last_selected_profile)
    profile_list.insert(0, last_selected_profile)
except ValueError:
    pass

user_profile = st.selectbox("Select a profile", profile_list, key="user_profile")
update_registry(registry, "last_selected_profile", user_profile)
with st.expander("Create new profile"):
    new_profile_name = st.text_input("Enter new profile name")
    profile_template = st.selectbox("Select a profile template", glob("profiles/*.json"))
    if st.button("Create"):
        with open(f"profiles/{new_profile_name}.json", "w") as f:
            shutil.copyfile(profile_template, f"profiles/{new_profile_name}.json")
        user_profile = f"profiles/{new_profile_name}.json"
        update_registry(registry, "last_selected_profile", user_profile)
        st.experimental_rerun()

with st.expander("Delete profile"):
    selected_profile = st.selectbox("Select a profile to delete", profile_list)
    if st.button("Delete"):
        os.remove(selected_profile)
        profile_list = list(glob("profiles/*.json"))
        registry["user_profile"] = glob("profiles/*.json")[0]
        st.experimental_rerun()

st.write(f"Selected profile: {user_profile}")

st.header("Configuration")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Locations                                                                                                          ■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
if "locations" not in st.session_state:
    st.session_state["locations"] = {}

if "num_locations" not in st.session_state:
    st.session_state["num_locations"] = 1


num_cols = st.number_input("Select number of GI points of interest", min_value=1, max_value=3, value=st.session_state.num_locations, step=1)
cols = st.columns(num_cols)
loc = get_geolocation()
for idx, col in enumerate(cols):
    if num_cols > 1:
        col.header(f"Location {idx + 1}")
    else:
        col.header("Location")

    time.sleep(2)
    if loc:
        # loc_df = pd.DataFrame([[loc["coords"]["latitude"], loc["coords"]["longitude"]]], columns=["lat", "lon"])
        input_loc = [loc["coords"]["latitude"], loc["coords"]["longitude"]]
        loc_input = col.text_input("Enter latitude and longitude", value=f"{loc['coords']['latitude']}, {loc['coords']['longitude']}", key=f"loc_input{idx}")
    else:
        loc_input = col.text_input("Enter latitude and longitude", value="36.1627, -86.7816", key=f"loc_input{idx}")
        # loc_df = pd.DataFrame([[float(loc_input.split(",")[0]), float(loc_input.split(",")[1])]], columns=["lat", "lon"])
        input_loc = [float(loc_input.split(",")[0]), float(loc_input.split(",")[1])]
    col.write("Enter latitude and longitude in the format: 36.1627, -86.7816")
    st.session_state["locations"][f"Location {idx + 1}"] = input_loc

    with col:
        # Create a map object
        m = folium.Map(location=input_loc, zoom_start=14)

        # Add the draw tool to the map
        draw = Draw(export=True)
        draw.add_to(m)

        # Display the map
        folium_static(m)

        # You can also retrieve the drawn shapes as GeoJSON
        draw_data = st.session_state.get('draw_data', {})
        if draw_data:
            st.json(draw_data)
