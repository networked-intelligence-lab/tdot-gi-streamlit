import streamlit as st
from streamlit_extras.app_logo import add_logo
import json

climate_zones_data = json.load(open("data/climate_tree.json"))
add_logo("media/logo.png", height=150)

if any([f"{pollutant}_acp" not in st.session_state for pollutant in climate_zones_data[list(climate_zones_data.keys())[0]]["Pollutant Uptake"].keys()]):
    st.session_state["O3_acp"] = 3.34
    st.session_state["NO2_acp"] = 3.34
    st.session_state["SO2_acp"] = 2.06
    st.session_state["PM10_acp"] = 2.84

st.title("Environmental Impact")
st.header("Options")
climate_zone = st.selectbox("Select STRATUM Climate Zone", climate_zones_data.keys())
num_small_trees = st.number_input("Number of Small Trees", value=0) * \
                  climate_zones_data[climate_zone]["Annual Interception"]["Small Tree"]
num_medium_trees = st.number_input("Number of Medium Trees", value=0) * \
                   climate_zones_data[climate_zone]["Annual Interception"]["Medium Tree"]
num_large_trees = st.number_input("Number of Large Trees", value=0) * \
                  climate_zones_data[climate_zone]["Annual Interception"]["Large Tree"]

st.header("Reduced Stormwater Runoff")
"""
Q_T=Q_TP+Q_BI+Q_PP+Q_WH

Where,
	QT = Total amount of reduced stormwater runoff
	QTP  = Runoff amount reduced by tree plantation
	QBI  = Runoff amount reduced by bioretention and infiltration
	QPP  = Runoff amount reduced by permeable pavement
	QWH  = Runoff amount reduced by water harvesting
	
Q_(TP) (gallons)=Number of Trees×i_t
"""
st.subheader("Tree Plantation")

q_tp = num_small_trees + num_medium_trees + num_large_trees
st.write(f"Runoff amount reduced by tree plantation: {q_tp} gallons/year")
st.session_state["q_tp"] = q_tp

st.subheader("Bioretention and Infiltration")
"""
Q_BI(gal)=[Precipitation (in)×{Element Area (sq.ft.)+Drainage Area (sq.ft.)}]× 0.80 ×144  (sq.in.)/(sq.ft.)×0.00433  gal/(in^3 )
"""
precipitation = st.number_input("Precipitation (in)", value=0)
element_area = st.number_input("Element Area (sq.ft.)", value=0)
drainage_area = st.number_input("Drainage Area (sq.ft.)", value=0)
q_bi = precipitation * (element_area + drainage_area) * 0.80 * 144 * 0.00433
st.write(f"Runoff amount reduced by bioretention and infiltration: {q_bi} gallons/year")
st.session_state["q_bi"] = q_bi

st.subheader("Permeable Pavement")
"""
Q_PP  (gal)=Annual Precipitation (in)×Permeable Pavement Area (sq.ft.)×0.80×144 (sq.in.)/(sq.ft.)×0.00433 gal/(in^3 )
"""
pp_annual_precipitation = st.number_input("Annual Precipitation (in)", value=0)
permeable_pavement_area = st.number_input("Permeable Pavement Area (sq.ft.)", value=0)
q_pp = pp_annual_precipitation * permeable_pavement_area * 0.80 * 144 * 0.00433
st.write(f"Runoff amount reduced by permeable pavement: {q_pp} gallons/year")
st.session_state["q_pp"] = q_pp

st.subheader("Water Harvesting")
"""
Q_WH (gal)=Annual Precipitation (in)×GI Element Surface Area (sq.ft.)×0.75×144 (sq.in.)/(sq.ft.)×0.00433 gal/(in^3 )
"""
wh_annual_precipitation = st.number_input("Annual Precipitation (in)", value=0, key="wh_annual_precipitation")
gi_element_surface_area = st.number_input("GI Element Surface Area (sq.ft.)", value=0)
q_wh = wh_annual_precipitation * gi_element_surface_area * 0.75 * 144 * 0.00433
st.write(f"Runoff amount reduced by water harvesting: {q_wh} gallons/year")
st.session_state["q_wh"] = q_wh

st.subheader("Total Amount of Reduced Stormwater Runoff")
q_t = q_tp + q_bi + q_pp + q_wh
st.write(f"Total amount of reduced stormwater runoff: {q_t} gallons/year")
st.session_state["q_t"] = q_t

st.subheader("Benefit Monetization")
conversion_factor = st.number_input("Conversion Factor from 2009 to current USD", value=1.42)
st.write(f"Monetary Gain from Avoided Stormwater Treatment: {q_t * 0.01 * conversion_factor} USD/year")
st.session_state["environmental_monetary_gain"] = q_t * 0.01 * conversion_factor

st.header("Reduced Air Pollutants")
lb_reduc_per_pollutant = {}
for pollutant in climate_zones_data[climate_zone]["Pollutant Uptake"].keys():
    small_tree_pollutant_amt = num_small_trees * climate_zones_data[climate_zone]["Pollutant Uptake"][pollutant]["Small Tree"]
    medium_tree_pollutant_amt = num_medium_trees * climate_zones_data[climate_zone]["Pollutant Uptake"][pollutant]["Medium Tree"]
    large_tree_pollutant_amt = num_large_trees * climate_zones_data[climate_zone]["Pollutant Uptake"][pollutant]["Large Tree"]
    lb_reduc_per_pollutant[pollutant] = small_tree_pollutant_amt + medium_tree_pollutant_amt + large_tree_pollutant_amt
tot_value_pol_reduc = sum([st.session_state[f"{pollutant}_acp"] * lb_reduc_per_pollutant[pollutant] for pollutant in lb_reduc_per_pollutant.keys()])
st.write("Total annual air pollutant reduction (lbs):", sum(lb_reduc_per_pollutant.values()))
st.write("Total value of pollutant reduction ($):", tot_value_pol_reduc)
st.session_state["lb_reduc_per_pollutant"] = lb_reduc_per_pollutant
st.session_state["tot_value_pol_reduc"] = tot_value_pol_reduc

st.header("Reduced Energy Use")
k_es = sum([num_small_trees * climate_zones_data[climate_zone]["Energy Saved"]["Small Tree"],
            num_medium_trees * climate_zones_data[climate_zone]["Energy Saved"]["Medium Tree"],
            num_large_trees * climate_zones_data[climate_zone]["Energy Saved"]["Large Tree"]])

st.write("40 Year Average of Energy Saved (kWh/tree per year):", k_es)
st.write("Value of Energy Saved ($):", k_es * (11.88 / 100))
st.session_state["k_es"] = k_es
st.session_state["value_energy_saved"] = k_es * (11.88 / 100)
