from streamlit_extras.app_logo import add_logo
from modules.helpers import subsubheader
import streamlit as st

add_logo("media/logo.png", height=150)

st.header("User Guide")
st.subheader("Introduction")
st.write("Welcome to the tool user guide! This guide is intended to help you navigate the tool and understand the different features and functionalities of the tool. The tool is divided into the following sections:")
st.markdown("""
1. Home
2. Determine Green Infrastructure
3. Economic Impact
4. Environmental Impact
5. Social Impact
6. Quantify Benefits""")

st.subheader("Home")
st.write("The home page is the first page you will see when you open the tool. It contains general configuration, profile, and location for the tool. The home page is divided into the following sections:")
st.markdown("""
1. Configuration
2. Profile
3. Location""")

subsubheader(st, "Profile")
st.write("The profile section allows you to select a profile to use for the tool. A profile contains information to the inputs provided in this tool. The profile section is divided into the following sections:")
st.markdown("""
1. Select a profile - select a profile to use for the tool
2. Create a profile - create a new profile based on another profile or the Default profile
3. Delete a profile - delete a profile and its associated data""")


subsubheader(st, "Configuration")
st.write("The configuration section allows you to configure the tool to your liking. Currently, configuration is limited to the following:")
st.markdown("""
1. Number of locations - the number of locations you would like to analyze per profile. This is limited to 53 locations per profile.
""")

subsubheader(st, "Location")
st.write("The location section allows you to select a location to analyze. Here, you can input a location, and it defaults to your current location if provided. If not, a default location is provided as an example.")

