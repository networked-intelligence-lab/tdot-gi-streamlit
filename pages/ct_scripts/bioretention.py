import streamlit as st


def bioretention_tab(tab_object):
    """
    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    # Initialize session state variables if they don't exist
    if 'drainage_area' not in st.session_state:
        st.session_state['drainage_area'] = 0
    if 'underdrain' not in st.session_state:
        st.session_state['underdrain'] = "Yes"
    if 'irim_select_br' not in st.session_state:
        st.session_state['irim_select_br'] = "Low"
    if 'vm_select_br' not in st.session_state:
        st.session_state['vm_select_br'] = "Low"
    if 'ts_select_br' not in st.session_state:
        st.session_state['ts_select_br'] = "Low"
    if 'ucd_select_br' not in st.session_state:
        st.session_state['ucd_select_br'] = "Low"
    if 'rm_select_br' not in st.session_state:
        st.session_state['rm_select_br'] = "Low"

    tab_object.subheader("Capital Cost")
    st.session_state['drainage_area'] = tab_object.number_input("Drainage area (acre)", value=st.session_state['drainage_area'])
    st.session_state['underdrain'] = tab_object.selectbox("Underdrain", options=["Yes", "No"], index=["Yes", "No"].index(st.session_state['underdrain']))
    underdrain_cost = {"Yes": 89028, "No": 42254}[st.session_state['underdrain']]
    bioretention_capital_cost = st.session_state['drainage_area'] * underdrain_cost
    tab_object.write(f"Total Capital Cost: ${bioretention_capital_cost}")
    st.session_state["bioretention_capital_cost"] = bioretention_capital_cost

    tab_object.subheader("Maintenance Cost")
    st.session_state['irim_select_br'] = tab_object.selectbox("Inspection, Reporting & Information Management", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['irim_select_br']), key="_irim_br")
    irim_value = {"Low": 60 * (1/3), "Medium": 130 * 0.5, "High": 570 * 1}[st.session_state['irim_select_br']]
    st.session_state['vm_select_br'] = tab_object.selectbox("Vegetation Management with Trash & Minor Debris Removal", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['vm_select_br']), key="_vm_br")
    vm_value = {"Low": 60 * 1, "Medium": 124 * 2, "High": 270 * 3}[st.session_state['vm_select_br']]
    st.session_state['ts_select_br'] = tab_object.selectbox("Till Soil", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ts_select_br']))
    ts_value = {"Low": 320 * 0.2, "Medium": 448 * 0.25, "High": 560 * 0.5}[st.session_state['ts_select_br']]
    st.session_state['ucd_select_br'] = tab_object.selectbox("Unclog Drain", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ucd_select_br']))
    ucd_value = {"Low": 160 * 0.2, "Medium": 160 * 0.5, "High": 190 * 1}[st.session_state['ucd_select_br']]
    st.session_state['rm_select_br'] = tab_object.selectbox("Replace Mulch", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['rm_select_br']))
    rm_value = {"Low": 1935 * 0.25, "Medium": 1999 * 0.5, "High": 2145 * 1}[st.session_state['rm_select_br']]
    bioretention_maintenance_cost = sum([irim_value, vm_value, ts_value, ucd_value, rm_value])
    tab_object.write(f"Total Maintenance Cost: ${bioretention_maintenance_cost}")
    st.session_state["bioretention_maintenance_cost"] = bioretention_maintenance_cost
    return tab_object
