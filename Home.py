import streamlit as st
from streamlit_js_eval import streamlit_js_eval, get_geolocation
from streamlit_extras.app_logo import add_logo
import pandas as pd
from glob import glob
from helpers.helpers import update_registry, limit_string, get_location_name
from registry.registry import *
import os
import json
import shutil
from st_pages import show_pages_from_config, add_page_title
from modules.sidebar import build_sidebar
import time
from streamlit_folium import folium_static
import folium
from folium.plugins import Draw
from helpers.debug import get_last_commit_time, get_total_commits


st.set_page_config(layout="wide",
                   page_title="TDoT GI Tool")
add_logo("media/logo.png", height=150)

st.title('TDoT GI Home')
owner, repo = "networked-intelligence-lab", "tdot-gi-streamlit"

# st.subheader(f"Last updated: {get_last_commit_time('networked-intelligence-lab', 'tdot-gi-streamlit')}")
st.markdown(f"""**version 0.0.{get_total_commits(owner, repo)}
<br><sup>Last updated: {get_last_commit_time('networked-intelligence-lab', 'tdot-gi-streamlit')}<sup>**""", unsafe_allow_html=True)

st.markdown("""
Welcome to the TDoT GI Tool! This tool is designed to help you explore the potential benefits of green infrastructure in your area.
As a start, you may check out the "User Guide" page in the sidebar. As a summary, you may follow the pages in the sidebar in order:
1. Determine GI to determine suitable GI types for your project/scenario
2. Enter information in Economic, Environmental, and Social impact pages to see the benefits of each GI/scenario
3. View the "Quantify Benefits" page to see the total benefits and comparison of each GI/scenario
""", unsafe_allow_html=True)
#         st.markdown("""
# - Site slope: 0.06
# - Cross-sectional and side slope: 0.04
# - Contributing drainage area: 0.5 acres
# - % impervious: 0.1""")


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Profiles                                                                                                           ■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

build_sidebar()
# st.header("Profile")
# profile_list = list(glob("profiles/*.json"))
# # move last selected profile to the start of the list
# last_selected_profile = registry["last_selected_profile"]
# try:
#     profile_list.remove(last_selected_profile)
#     profile_list.insert(0, last_selected_profile)
# except ValueError:
#     pass
#
# user_profile = st.selectbox("Select a profile", profile_list, key="user_profile")
# update_registry(registry, "last_selected_profile", user_profile)
#
# # Load session state from file
# if st.button("Load Session State"):
#     with open(user_profile, "r") as file:
#         session_state_dict = json.load(file)
#         # Delete everything from session state except user_profile
#         for key in list(st.session_state.keys()):
#             if key != "user_profile":
#                 del st.session_state[key]
#         st.session_state.update(session_state_dict)
#     st.experimental_rerun()
#
# with st.expander("Create new profile"):
#     new_profile_name = st.text_input("Enter new profile name")
#     profile_template = st.selectbox("Select a profile template", ["New"] + list(glob("profiles/*.json")))
#     if st.button("Create"):
#         if profile_template == "New":
#             with open(f"profiles/{new_profile_name}.json", "w") as f:
#                 json.dump({"app": "ni-gitool"}, f, indent=4)
#         else:
#             with open(f"profiles/{new_profile_name}.json", "w") as f:
#                 shutil.copyfile(profile_template, f"profiles/{new_profile_name}.json")
#             user_profile = f"profiles/{new_profile_name}.json"
#             update_registry(registry, "last_selected_profile", user_profile)
#             st.experimental_rerun()
#
# with st.expander("Delete profile"):
#     selected_profile = st.selectbox("Select a profile to delete", profile_list)
#     if st.button("Delete"):
#         os.remove(selected_profile)
#         profile_list = list(glob("profiles/*.json"))
#         registry["user_profile"] = glob("profiles/*.json")[0]
#         st.experimental_rerun()
#
# st.write(f"Selected profile: {user_profile}")
# # Function to save session state to a JSON file
#
# # Button to save session state
# if st.button("Save Session State"):
#     save_session_state_to_file(user_profile)
#     st.success("Session state saved to file")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■ Locations                                                                                                          ■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
loc = get_geolocation()
if loc:
    loc_value = f"{loc['coords']['latitude']}, {loc['coords']['longitude']}"
else:
    st.warning("Location not found. You may not have allowed location permissions in your browser; using default location instead.")
    loc_value = "36.1627, -86.7816"

lat, lon = [float(c) for c in loc_value.split(", ")]
data = pd.DataFrame({
    'lat': [lat],
    'lon': [lon]
})
st.markdown(f"**Your location**: {get_location_name(lat, lon)} @ {loc_value}")
st.map(data)
