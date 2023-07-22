import streamlit as st

st.title('Green Roofs Cost Tool')
st.header('Design and Maintenance Options')
st.subheader("Roof Characteristics")

roof_area = st.number_input('Roof Area (RA) (sq. ft.)', value=10000)
building_height = st.number_input('Building Height (in stories)', value=4)

st.subheader("Design & Maintenance Options")
roof_function = st.selectbox("Primary Roof Function", ('O: Operational, only basic costs are added to achieve basic '
                                                       'Green Roof benefits',
                                                       'P: Promotional or Aesthetics and social environment '
                                                       'enhancement. Assumes a more elaborate installation'))
roof_function = roof_function.split(':')[0]
if roof_function == 'O':
    irrigation_needed = st.selectbox("Irrigation Needed", ('No', 'Yes, if P is elected above, yes is assumed.'))
elif roof_function == 'P':
    irrigation_needed = st.selectbox("Irrigation Needed", ('Yes, if P is elected above, yes is assumed.', 'No'))

maintenance = st.selectbox("Choose Level of Maintenance", ("High", "Medium", "Low"))

st.subheader("Whole Life Cost Options")
discount_rate = st.number_input('Discount Rate (in %)', value=5.5)

st.header("Capital Costs")
st.subheader("Cost Based on Roof Area")
st.write("Roof Area (in sq. ft.): ", roof_area)
est_basic_mod_roof_comp_cost = st.number_input('Estimated Basic Modular Roof Components Cost ($/sq. ft.)', value=19.5)
base_facility_cost = st.number_input('Base Facility Cost ($)', value=max([roof_area * est_basic_mod_roof_comp_cost, 100]))
cost_adj_small_proj = st.number_input('Cost Adjustment for Small Projects ($)', value=0)
cost_adj_height_above_5st = st.number_input('Cost Adjustment for Heights Above 5 Stories ($)', value=0)

if cost_adj_small_proj == 0:
    if roof_area < 4000:
        cost_adj_small_proj = 0.1 * base_facility_cost
    else:
        cost_adj_small_proj = 0
st.write("Cost Adjustment for Small Projects ($): ", cost_adj_small_proj)

if cost_adj_height_above_5st == 0:
    if building_height < 5:
        cost_adj_height_above_5st = 0
    else:
        cost_adj_height_above_5st = 0.1 * base_facility_cost
st.write("Cost Adjustment for Heights Above 5 Stories ($): ", cost_adj_height_above_5st)

delivery_costs = st.number_input('Delivery Costs ($)', value=0.85 * roof_area)
resulting_base_cost_per_sf = st.number_input('Resulting Base Cost per Square Foot ($/sq. ft.)',
                                             value=(base_facility_cost + cost_adj_small_proj + cost_adj_height_above_5st + delivery_costs)/roof_area)