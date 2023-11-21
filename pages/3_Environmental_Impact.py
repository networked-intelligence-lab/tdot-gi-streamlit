import streamlit as st
from streamlit_extras.app_logo import add_logo
import json

climate_zones_data = json.load(open("data/climate_tree.json"))
add_logo("media/logo.png", height=150)

# Initialize air pollutant session states
if any([f"{pollutant}_acp" not in st.session_state for pollutant in climate_zones_data[list(climate_zones_data.keys())[0]]["Pollutant Uptake"].keys()]):
    st.session_state["O3_acp"] = 3.34
    st.session_state["NO2_acp"] = 3.34
    st.session_state["SO2_acp"] = 2.06
    st.session_state["PM10_acp"] = 2.84

# Initialize session state variables for number inputs
input_keys = ["num_small_trees", "num_medium_trees", "num_large_trees",
              "precipitation", "element_area", "drainage_area",
              "pp_annual_precipitation", "permeable_pavement_area",
              "wh_annual_precipitation", "gi_element_surface_area",
              "conversion_factor"]

for key in input_keys:
    if key not in st.session_state:
        st.session_state[key] = 0

st.title("Environmental Impact")
st.header("Options")

# Selection of climate zone
climate_zone = st.selectbox("Select STRATUM Climate Zone", list(climate_zones_data.keys()))

# Input fields for tree numbers with multipliers
st.session_state["num_small_trees"] = st.number_input("Number of Small Trees", value=st.session_state["num_small_trees"]) * climate_zones_data[climate_zone]["Annual Interception"]["Small Tree"]
st.session_state["num_medium_trees"] = st.number_input("Number of Medium Trees", value=st.session_state["num_medium_trees"]) * climate_zones_data[climate_zone]["Annual Interception"]["Medium Tree"]
st.session_state["num_large_trees"] = st.number_input("Number of Large Trees", value=st.session_state["num_large_trees"]) * climate_zones_data[climate_zone]["Annual Interception"]["Large Tree"]

# Reduced Stormwater Runoff Section
st.header("Reduced Stormwater Runoff")
st.subheader("Tree Plantation")
q_tp = st.session_state["num_small_trees"] + st.session_state["num_medium_trees"] + st.session_state["num_large_trees"]
st.write(f"Runoff amount reduced by tree plantation: {q_tp} gallons/year")
st.session_state["q_tp"] = q_tp

st.subheader("Bioretention and Infiltration")
st.session_state["precipitation"] = st.number_input("Precipitation (in)", value=st.session_state["precipitation"])
st.session_state["element_area"] = st.number_input("Element Area (sq.ft.)", value=st.session_state["element_area"])
st.session_state["drainage_area"] = st.number_input("Drainage Area (sq.ft.)", value=st.session_state["drainage_area"])
q_bi = st.session_state["precipitation"] * (st.session_state["element_area"] + st.session_state["drainage_area"]) * 0.80 * 144 * 0.00433
st.write(f"Runoff amount reduced by bioretention and infiltration: {q_bi} gallons/year")
st.session_state["q_bi"] = q_bi

st.subheader("Permeable Pavement")
st.session_state["pp_annual_precipitation"] = st.number_input("Annual Precipitation (in)", value=st.session_state["pp_annual_precipitation"])
st.session_state["permeable_pavement_area"] = st.number_input("Permeable Pavement Area (sq.ft.)", value=st.session_state["permeable_pavement_area"])
q_pp = st.session_state["pp_annual_precipitation"] * st.session_state["permeable_pavement_area"] * 0.80 * 144 * 0.00433
st.write(f"Runoff amount reduced by permeable pavement: {q_pp} gallons/year")
st.session_state["q_pp"] = q_pp

st.subheader("Water Harvesting")
st.session_state["wh_annual_precipitation"] = st.number_input("Annual Precipitation (in)", value=st.session_state["wh_annual_precipitation"], key="_wh_annual_precipitation")
st.session_state["gi_element_surface_area"] = st.number_input("GI Element Surface Area (sq.ft.)", value=st.session_state["gi_element_surface_area"])
q_wh = st.session_state["wh_annual_precipitation"] * st.session_state["gi_element_surface_area"] * 0.75 * 144 * 0.00433
st.write(f"Runoff amount reduced by water harvesting: {q_wh} gallons/year")
st.session_state["q_wh"] = q_wh

st.subheader("Total Amount of Reduced Stormwater Runoff")
q_t = q_tp + q_bi + q_pp + q_wh
st.write(f"Total amount of reduced stormwater runoff: {q_t} gallons/year")
st.session_state["q_t"] = q_t

# Benefit Monetization Section
st.subheader("Benefit Monetization")
st.session_state["conversion_factor"] = st.number_input("Conversion Factor from 2009 to current USD", value=st.session_state["conversion_factor"])
monetary_gain = q_t * 0.01 * st.session_state["conversion_factor"]
st.write(f"Monetary Gain from Avoided Stormwater Treatment: {monetary_gain} USD/year")
st.session_state["environmental_monetary_gain"] = monetary_gain

# Reduced Air Pollutants Section
st.header("Reduced Air Pollutants")
lb_reduc_per_pollutant = {}
for pollutant in climate_zones_data[climate_zone]["Pollutant Uptake"].keys():
    small_tree_pollutant_amt = st.session_state["num_small_trees"] * climate_zones_data[climate_zone]["Pollutant Uptake"][pollutant]["Small Tree"]
    medium_tree_pollutant_amt = st.session_state["num_medium_trees"] * climate_zones_data[climate_zone]["Pollutant Uptake"][pollutant]["Medium Tree"]
    large_tree_pollutant_amt = st.session_state["num_large_trees"] * climate_zones_data[climate_zone]["Pollutant Uptake"][pollutant]["Large Tree"]
    lb_reduc_per_pollutant[pollutant] = small_tree_pollutant_amt + medium_tree_pollutant_amt + large_tree_pollutant_amt

tot_value_pol_reduc = sum([st.session_state[f"{pollutant}_acp"] * lb_reduc_per_pollutant[pollutant] for pollutant in lb_reduc_per_pollutant.keys()])
st.write("Total annual air pollutant reduction (lbs):", sum(lb_reduc_per_pollutant.values()))
st.write("Total value of pollutant reduction ($):", tot_value_pol_reduc)
st.session_state["lb_reduc_per_pollutant"] = lb_reduc_per_pollutant
st.session_state["tot_value_pol_reduc"] = tot_value_pol_reduc

# Reduced Energy Use Section
st.header("Reduced Energy Use")
k_es = sum([st.session_state["num_small_trees"] * climate_zones_data[climate_zone]["Energy Saved"]["Small Tree"],
            st.session_state["num_medium_trees"] * climate_zones_data[climate_zone]["Energy Saved"]["Medium Tree"],
            st.session_state["num_large_trees"] * climate_zones_data[climate_zone]["Energy Saved"]["Large Tree"]])

st.write("40 Year Average of Energy Saved (kWh/tree per year):", k_es)
value_energy_saved = k_es * (11.88 / 100)
st.write("Value of Energy Saved ($):", value_energy_saved)
st.session_state["k_es"] = k_es
st.session_state["value_energy_saved"] = value_energy_saved