import streamlit as st

st.title('TDoT GI Home')

# st.header('Design and Maintenance Options')
# st.subheader("Storage Requirements")
# tank_size = st.number_input('Tank Size (gallons)', value=6300, step=1)
# impervious_area = st.number_input('Impervious Drainage Area, DA (often roof area; sq.ft)', value=5000, step=1)
# rainfall_event = st.number_input('Max Design Rainfall Event (inches)', value=2)
#
# st.write(f"Total storage needed: {(impervious_area * (rainfall_event/12)) * 7.48}")
#
# st.subheader("System Characteristics")
# material = st.selectbox('Type of Tank Desired', ('Steel', 'Fiberglass', 'Concrete', 'HDPE'))
# tank_costs_gallon = {
#     'Steel': 2.51,
#     'Fiberglass': 1.33,
#     'Concrete': 1.66,
#     'HDPE': 1.43}
#
# st.write(f"Estimated tank cost: {tank_costs_gallon[material] * tank_size}")
# install_cost = st.number_input('Installation cost', value=6275)
# pump_size = st.number_input('Pump Size Needed (horsepower)', value=0.5)
# pump_cost = st.number_input('Pump Cost', value=599)
# potable_resup = st.number_input('Potable Re-Supply', value=0)
#
# st.write(f"System base cost: {sum([tank_costs_gallon[material] * tank_size, install_cost, pump_cost, potable_resup])}")
#
# system_design_cost = st.number_input('System Design Cost', value=1387)
# st.write(f"Total facility cost: {sum([tank_costs_gallon[material] * tank_size, install_cost, pump_cost, potable_resup, system_design_cost])}")
#
