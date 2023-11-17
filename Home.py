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
from helpers.debug import get_last_commit_time, get_total_commits


st.set_page_config(layout="wide")
add_logo("media/logo.png", height=150)

st.title('TDoT GI Home')
owner, repo = "networked-intelligence-lab", "tdot-gi-streamlit"

# st.subheader(f"Last updated: {get_last_commit_time('networked-intelligence-lab', 'tdot-gi-streamlit')}")
st.markdown(f"""**version 0.0.{get_total_commits(owner, repo)}
<br><sup>Last updated: {get_last_commit_time('networked-intelligence-lab', 'tdot-gi-streamlit')}<sup>**""", unsafe_allow_html=True)
with st.expander("Demo"):
    case_study = st.selectbox("Select a case study", ["", "1 - Laura 11/15 ver."]).split(" - ")[0]

    if case_study == "1":
        st.subheader("Selected case study: Laura 11/15 ver.")
        st.markdown("<h4>Site Requirements</h4>", unsafe_allow_html=True)
#         st.markdown("""
# - Site slope: 0.06
# - Cross-sectional and side slope: 0.04
# - Contributing drainage area: 0.5 acres
# - % impervious: 0.1""")




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
# Initialize session state
if "locations" not in st.session_state:
    st.session_state["locations"] = {}

if "num_locations" not in st.session_state:
    st.session_state["num_locations"] = 1

# Get the number of locations from user input
num_cols = st.number_input("Select number of GI points of interest", min_value=1, max_value=3, value=st.session_state["num_locations"], step=1)
st.session_state["num_locations"] = num_cols  # Update session state with the current number of locations

cols = st.columns(num_cols)
loc = get_geolocation()

for idx, col in enumerate(cols):
    col.header(f"Location {idx + 1}" if num_cols > 1 else "Location")
    time.sleep(2)

    if loc:
        # Use the geolocation if available
        default_value = f"{loc['coords']['latitude']}, {loc['coords']['longitude']}"
    else:
        # Use a default value if no geolocation is found
        default_value = "36.1627, -86.7816"

    # Get the location input from the user
    loc_input = col.text_input("Enter latitude and longitude", value=default_value, key=f"loc_input{idx}")
    input_loc = [float(coord.strip()) for coord in loc_input.split(',')]

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

# Retrieve the drawn shapes as GeoJSON (assuming this part is handled elsewhere in the code)
draw_data = st.session_state.get('draw_data', {})
if draw_data:
    st.json(draw_data)