import streamlit as st
import pandas as pd
import numpy as np

st.title('Cost Tool')

# Define Tabs
cistern_t, bioretention_t = st.tabs(["Cistern", "Bioretention"])

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






