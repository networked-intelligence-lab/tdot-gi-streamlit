import streamlit as st
import pandas as pd
import numpy as np

st.title('Cost Tool')

# Define Tabs
cistern_t, bioretention_t, swales_st = st.tabs(["Cistern", "Bioretention", "Swales"])

# Cistern Tab
cistern_t.header('Design and Maintenance Options')
cistern_t.subheader("Storage Requirements")
tank_size = cistern_t.number_input('Tank Size (gallons)', value=6300, step=1)
impervious_area = cistern_t.number_input('Impervious Drainage Area, DA (often roof area; sq.ft)', value=5000, step=1)
rainfall_event = cistern_t.number_input('Max Design Rainfall Event (inches)', value=2)

cistern_t.write(f"Total storage needed: {(impervious_area * (rainfall_event/12)) * 7.48}")

cistern_t.subheader("System Characteristics")
material = cistern_t.selectbox('Type of Tank Desired', ('Steel', 'Fiberglass', 'Concrete', 'HDPE'))
tank_costs_gallon = {
    'Steel': 2.51,
    'Fiberglass': 1.33,
    'Concrete': 1.66,
    'HDPE': 1.43}

cistern_t.write(f"Estimated tank cost: {tank_costs_gallon[material] * tank_size}")
install_cost = cistern_t.number_input('Installation cost', value=6275)
pump_size = cistern_t.number_input('Pump Size Needed (horsepower)', value=0.5)
pump_cost = cistern_t.number_input('Pump Cost', value=599)
potable_resup = cistern_t.number_input('Potable Re-Supply', value=0)

cistern_t.write(f"System base cost: {sum([tank_costs_gallon[material] * tank_size, install_cost, pump_cost, potable_resup])}")

system_design_cost = cistern_t.number_input('System Design Cost', value=1387)

cistern_t.write(f"Total facility cost: {sum([tank_costs_gallon[material] * tank_size, install_cost, pump_cost, potable_resup, system_design_cost])}")

swales_st.title('Swale')

swales_st.header('Design and Maintenance Options')
swales_st.subheader('Watershed Characteristics')
drainage_area = swales_st.number_input('Drainage Area (ac)', value=2, step=1)
impervious_cover = swales_st.number_input('Drainage Area Impervious Cover (pct)', value=40)
land_use_type = swales_st.selectbox("Land Use Type", ('R: Residential', 'C: Commercial', 'Ro: Roads', 'I: Industrial'))

swales_st.subheader('Design & Maintenance Options')
level_of_maintenance = swales_st.selectbox("Level of Maintenance", ('H: High', 'M: Medium', 'L: Low'))

swales_st.subheader('Whole Life Cost Options')
discount_rate = swales_st.number_input('Discount Rate (%)', value=5.5)

swales_st.header('Method A: Simple Cost based on Drainage Area')
swales_st.subheader('Cost based on Drainage Area')
drainage_area = swales_st.number_input('Drainage Area (DA) (acres)', value=2)
base_facility_cost = swales_st.number_input('Base Facility Cost per acre DA ($)', value=3000)
default_cost_adjustment = swales_st.number_input('Default Cost Adjustment fro Smaller Projects', value=2.2)
resulting_base_cost = swales_st.number_input('Resulting Base Cost per acre DA ($)', value=6600)
base_facility_cost = swales_st.number_input('Base Facility Cost (rounded p to nearest $100) ($)', value=13200)
engineering_and_planning = swales_st.number_input('Engineering & Planning (default = 25% of Base Cost) ($)', value=3300)
land_cost = swales_st.number_input('Land Cost ($)', value=0)
other_cost = swales_st.number_input('Other Costs ($)', value=0)

swales_st.header('Method B: User-Entered Engineers Estimate')
swales_st.subheader('Total Facility Base Costs')
mobilization = swales_st.number_input('Mobilization (LS)')
clearing_and_grubbing = swales_st.number_input('Clearing & Grubbing (AC)')
excavation = swales_st.number_input('Excavation/Grading (CY)')
dewatering = swales_st.number_input('Dewatering (LS)')
haul_of_excavated_material = ('Haul/Dispose of Excavated Material (CY)')
sediment_pretreatment_struct = swales_st.number_input('Sediment Pretreatment Struct (e.g.,inlet sump) (LF)')
inflow_structure = swales_st.number_input('Inflow Structure(s) (LS)')
energy_dissipation_apron = swales_st.number_input('Energy Dissipation Apron (LS)')
overflow_structure = swales_st.number_input('Overflow Structure (concrete or rock riprap) (CY)')
revegetation_controls = swales_st.number_input('Revegetation/Erosion Controls (SY)')
traffic_control = swales_st.number_input('Traffic Control')
signage_public_education_materials = swales_st.number_input('Signage, Public Education Materials,etc (LS)')

swales_st.subheader('Associated Capital Cots')
project_management = ('Project Management')
engineering_preliminary = swales_st.number_input('Engineering: Preliminary')
engineering_final_design = swales_st.number_input('Engineering; Final Design')
topographic_survey = swales_st.number_input('Topographic Survey')
geotechnical = swales_st.number_input('Geotechnical')
landscape_design = swales_st.number_input('Landscape Design')
land_acquisition = swales_st.number_input('Land Acquisition (site, easements, etc)')
utility_relocation = swales_st.number_input('Utility Relocation')
legal_services = swales_st.number_input('Legal Services')
permitting_and_construction_inspection = swales_st.number_input('Permitting & Construction Inspection')
sales_tax = swales_st.number_input('Sales Tax')
contingency = swales_st.number_input('Contingency (e.g. 30%)')

swales_st.header('Maintenance Costs')
swales_st.subheader('Routine Maintenance Activities( Frequent, scheduled events')

swales_st.header('Cost Summary')
swales_st.subheader('Capital Costs')
total_base_facility_cost = swales_st.number_input('Total Base Facility Cost')
total_associated_capital_cost = swales_st.number_input('Total Associated Capital Cost')




