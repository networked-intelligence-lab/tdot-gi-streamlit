import streamlit as st
from modules.helpers import subsubheader
from streamlit_extras.app_logo import add_logo
from modules.sidebar import build_sidebar

build_sidebar()
add_logo("media/logo.png", height=150)

st.title('Advanced Options')
with st.expander("Environmental Impact"):
    st.subheader("Reduced Air Pollutants")
    subsubheader(st, "Avoided Cost of Criteria Pollutants")
    st.number_input("O3 Price (USD/lb)", value=3.34, key="O3_acp")
    st.number_input("NO2 Price (USD/lb)", value=3.34, key="NO2_acp")
    st.number_input("SO2 Price (USD/lb)", value=2.06, key="SO2_acp")
    st.number_input("PM10 Price (USD/lb)", value=2.84, key="PM10_acp")
