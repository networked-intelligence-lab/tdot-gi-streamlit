import streamlit as st
from streamlit_extras.app_logo import add_logo
import json

climate_zones_data = json.load(open("data/climate_tree.json"))
add_logo("media/logo.png", height=150)

st.title("Environmental Impact")
st.header("Climate Zone")
climate_zone = st.selectbox("Select STRATUM Climate Zone", climate_zones_data.keys())

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
num_small_trees = st.number_input("Number of Small Trees", value=0) * climate_zones_data[climate_zone]["Annual Interception"]["Small Tree"]
num_medium_trees = st.number_input("Number of Medium Trees", value=0) * climate_zones_data[climate_zone]["Annual Interception"]["Medium Tree"]
num_large_trees = st.number_input("Number of Large Trees", value=0) * climate_zones_data[climate_zone]["Annual Interception"]["Large Tree"]
q_tp = num_small_trees + num_medium_trees + num_large_trees
st.write(f"Runoff amount reduced by tree plantation: {q_tp} gallons/year")

st.subheader("Bioretention and Infiltration")
"""
Q_BI(gal)=[Precipitation (in)×{Element Area (sq.ft.)+Drainage Area (sq.ft.)}]× 0.80 ×144  (sq.in.)/(sq.ft.)×0.00433  gal/(in^3 )
"""
precipitation = st.number_input("Precipitation (in)", value=0)
element_area = st.number_input("Element Area (sq.ft.)", value=0)
drainage_area = st.number_input("Drainage Area (sq.ft.)", value=0)
q_bi = precipitation * (element_area + drainage_area) * 0.80 * 144 * 0.00433
st.write(f"Runoff amount reduced by bioretention and infiltration: {q_bi} gallons/year")

st.subheader("Permeable Pavement")
"""
Q_PP  (gal)=Annual Precipitation (in)×Permeable Pavement Area (sq.ft.)×0.80×144 (sq.in.)/(sq.ft.)×0.00433 gal/(in^3 )
"""
pp_annual_precipitation = st.number_input("Annual Precipitation (in)", value=0)
permeable_pavement_area = st.number_input("Permeable Pavement Area (sq.ft.)", value=0)
q_pp = pp_annual_precipitation * permeable_pavement_area * 0.80 * 144 * 0.00433
st.write(f"Runoff amount reduced by permeable pavement: {q_pp} gallons/year")

st.subheader("Water Harvesting")
"""
Q_WH (gal)=Annual Precipitation (in)×GI Element Surface Area (sq.ft.)×0.75×144 (sq.in.)/(sq.ft.)×0.00433 gal/(in^3 )
"""
wh_annual_precipitation = st.number_input("Annual Precipitation (in)", value=0, key="wh_annual_precipitation")
gi_element_surface_area = st.number_input("GI Element Surface Area (sq.ft.)", value=0)
q_wh = wh_annual_precipitation * gi_element_surface_area * 0.75 * 144 * 0.00433
st.write(f"Runoff amount reduced by water harvesting: {q_wh} gallons/year")

st.subheader("Total Amount of Reduced Stormwater Runoff")
q_t = q_tp + q_bi + q_pp + q_wh
st.write(f"Total amount of reduced stormwater runoff: {q_t} gallons/year")

st.subheader("Benefit Monetization")
conversion_factor = st.number_input("Conversion Factor from 2009 to current USD", value=1.42)
st.write(f"Monetary Gain from Avoided Stormwater Treatment: {q_t * 0.01 * conversion_factor} USD/year")

