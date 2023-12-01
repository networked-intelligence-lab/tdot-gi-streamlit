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
build_sidebar()
add_logo("media/logo.png", height=150)


st.title('TDoT GI Home')

# st.markdown(f"""**version 0.0.{get_total_commits()}
# <br><sup>Last updated: {get_last_commit_time()}<sup>**""", unsafe_allow_html=True)

st.markdown("""
Welcome to the TDoT GI Tool! This tool is designed to help you explore the potential benefits of green infrastructure in your area.
As a start, you may check out the "User Guide" page in the sidebar. As a summary, you may follow the pages in the sidebar in order:
1. Determine GI to determine suitable GI types for your project/scenario
2. Enter information in Economic, Environmental, and Social impact pages to see the benefits of each GI/scenario
3. View the "Quantify Benefits" page to see the total benefits and comparison of each GI/scenario
""", unsafe_allow_html=True)

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
