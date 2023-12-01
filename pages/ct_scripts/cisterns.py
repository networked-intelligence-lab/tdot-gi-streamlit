import streamlit as st


def cisterns_tab(tab_object):
    """
    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    # Initialize session state variables if they don't exist
    if 'impervious_area' not in st.session_state:
        st.session_state['impervious_area'] = 0
    if 'rainfall_event' not in st.session_state:
        st.session_state['rainfall_event'] = 2
    if 'material' not in st.session_state:
        st.session_state['material'] = "Steel"
    if 'total_storage_needed' not in st.session_state:
        st.session_state['total_storage_needed'] = 0
    if 'irim_select' not in st.session_state:
        st.session_state['irim_select'] = "Low"
    if 'rwc_select' not in st.session_state:
        st.session_state['rwc_select'] = "Low"
    if 'tid_select' not in st.session_state:
        st.session_state['tid_select'] = "Low"
    if 'ism_select' not in st.session_state:
        st.session_state['ism_select'] = "Low"

    tab_object.subheader("Capital Cost")
    st.session_state['impervious_area'] = tab_object.number_input("Impervious Area (ft^2)", value=st.session_state['impervious_area'])
    st.session_state['rainfall_event'] = tab_object.number_input("Max Design Rainfall Event (in)", value=st.session_state['rainfall_event'])
    precip_volume_gen = (st.session_state['impervious_area'] * (st.session_state['rainfall_event'] / 12)) * 7.48
    st.session_state['material'] = tab_object.selectbox("Material", options=["Steel", "Fiberglass", "Concrete", "HDPE"], index=["Steel", "Fiberglass", "Concrete", "HDPE"].index(st.session_state['material']))
    st.session_state['total_storage_needed'] = tab_object.number_input("Total Storage Needed (gal)", value=max(precip_volume_gen, st.session_state['total_storage_needed']))
    material_costs = {"Steel": 1.33, "Fiberglass": 2.51, "Concrete": 1.43, "HDPE": 1.66}
    cisterns_capital_cost = st.session_state['total_storage_needed'] * material_costs[st.session_state['material']]
    tab_object.write(f"Total Capital Cost: ${cisterns_capital_cost}")
    st.session_state["cisterns__capital_cost"] = cisterns_capital_cost

    tab_object.subheader("Maintenance Cost")
    st.session_state['irim_select'] = tab_object.selectbox("Inspection, Reporting & Information Management", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['irim_select']))
    irim_value = {"Low": 135, "Medium": 130 * 2, "High": 340 * 12}[st.session_state['irim_select']]
    st.session_state['rwc_select'] = tab_object.selectbox("Roof Washing, Cleaning Inflow Filters", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['rwc_select']))
    rwc_value = {"Low": 150, "Medium": 240 * 2, "High": 540 * 12}[st.session_state['rwc_select']]
    st.session_state['tid_select'] = tab_object.selectbox("Tank inspection and disinfection", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['tid_select']))
    tid_value = {"Low": 120 * 0.5, "Medium": 240 * 1, "High": 360 * 2}[st.session_state['tid_select']]
    st.session_state['ism_select'] = tab_object.selectbox("Intermittent System Maintenance (System flush, debris/sediment removal from tank)", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ism_select']))
    ism_value = {"Low": 270 * (1/3), "Medium": 390 * (1/3), "High": 510 * (1/3)}[st.session_state['ism_select']]

    cisterns_maintenance_cost = sum([irim_value, rwc_value, tid_value, ism_value])
    tab_object.write(f"Total Maintenance Cost: ${cisterns_maintenance_cost}")
    st.session_state["cisterns__maintenance_cost"] = cisterns_maintenance_cost
    return tab_object
