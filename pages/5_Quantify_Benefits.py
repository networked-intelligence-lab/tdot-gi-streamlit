import streamlit as st
from streamlit_extras.app_logo import add_logo
from glob import glob
import json
from modules.simulations import handle_simulations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from matplotlib import rcParams
from matplotlib.pyplot import figure
import random

# build_sidebar()
add_logo("media/logo.png", height=150)


st.title("Quantify Benefits")
# st.write(st.session_state)

profile_list = list(glob("profiles/*.json"))
select_profiles = st.multiselect("Select Profiles", profile_list, [])


simulation_data_tab, raw_output_tab = st.tabs(["Simulation Data", "Raw Output"])
with raw_output_tab:
    if select_profiles:
        cols = st.columns(len(select_profiles))
        for idx, profile in enumerate(select_profiles):
            with open(profile, "r") as f:
                st.session_state.update(json.load(f))
                st.session_state[f"_profile_{idx}"] = st.session_state

            with cols[idx]:
                st.header(f"{profile}")
                st.subheader("Determine Green Infrastructure")
                determine_gi_output = st.session_state["determine_gi_output"]
                for major_category, minor_categories_list in determine_gi_output.items():
                    st.multiselect(major_category, minor_categories_list, minor_categories_list,
                                   key=f"{major_category}_{idx}")

                st.subheader("Determine Economic Impacts")
                capital_costs = sum(
                    [st.session_state[key] for key in st.session_state.keys() if "__capital_cost" in key])
                maintenance_costs = sum(
                    [st.session_state[key] for key in st.session_state.keys() if "__maintenance_cost" in key])
                st.text_input("Capital Cost", value=capital_costs, key=f"capital_cost_{idx}")
                st.text_input("Maintenance Cost", value=maintenance_costs,
                              key=f"maintenance_cost_{idx}")

                st.subheader("Environmental Impact")
                st.write(f"Runoff amount reduced by tree plantation: {st.session_state['q_tp']} gallons/year")
                st.write(f"Runoff amount reduced by bioretention and infiltration: {st.session_state['q_bi']} gallons/year")
                st.write(f"Runoff amount reduced by permeable pavement: {st.session_state['q_pp']} gallons/year")
                st.write(f"Runoff amount reduced by water harvesting: {st.session_state['q_wh']} gallons/year")
                st.write(f"Total amount of reduced stormwater runoff: {st.session_state['q_t']} gallons/year")
                st.write(
                    f"Monetary Gain from Avoided Stormwater Treatment: {st.session_state['environmental_monetary_gain']} USD/year")
                st.write("Total annual air pollutant reduction (lbs):", st.session_state["lb_reduc_per_pollutant"])
                st.write("Total value of pollutant reduction ($):", st.session_state["tot_value_pol_reduc"])
                st.write("40 Year Average of Energy Saved (kWh/tree per year):", st.session_state['k_es'])
                st.write("Value of Energy Saved ($):", st.session_state['k_es'] * (11.88 / 100))

with simulation_data_tab:
    if len(select_profiles) >= 2:
        num_sims = st.number_input('Enter the number of simulations', min_value=1, max_value=10000, value=5000, step=1,
                                   key=None)
        if st.button("Simulate"):
            handle_simulations(select_profiles, simulation_data_tab)
    else:
        st.warning("Please select at least two profiles above to simulate their weights/outcomes.")
