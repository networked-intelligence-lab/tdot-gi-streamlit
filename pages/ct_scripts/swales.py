import streamlit as st


def swales_tab(tab_object):
    """
    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    # Initialize session state variables if they don't exist
    if 'drainage_area_s' not in st.session_state:
        st.session_state['drainage_area_s'] = 2.0
    if 'impervious_area_percent_s' not in st.session_state:
        st.session_state['impervious_area_percent_s'] = 40.0
    if 'base_cost_level_s' not in st.session_state:
        st.session_state['base_cost_level_s'] = "Low"
    if 'irim_select_s' not in st.session_state:
        st.session_state['irim_select_s'] = "Low"
    if 'vm_select_s' not in st.session_state:
        st.session_state['vm_select_s'] = "Low"
    if 'cm_select_s' not in st.session_state:
        st.session_state['cm_select_s'] = "Low"

    if 'use_swales' not in st.session_state:
        st.session_state['use_swales'] = False
    def toggle_usage():
        st.session_state["use_swales"] = not st.session_state["use_swales"]

    use = tab_object.checkbox("Use Swales", value=st.session_state["use_swales"], on_change=toggle_usage)
    if use:
        tab_object.subheader("Capital Cost")
        st.session_state['drainage_area_s'] = tab_object.number_input("Drainage Area (acre)", value=st.session_state['drainage_area_s'])
        st.session_state['impervious_area_percent_s'] = tab_object.number_input("Impervious area (whole number %)", value=st.session_state['impervious_area_percent_s'], step=1.0, key="imp_s")
        impervious_area = st.session_state['drainage_area_s'] * (st.session_state['impervious_area_percent_s'] / 100)
        st.session_state['base_cost_level_s'] = tab_object.selectbox("Base Cost Level", options=["Low", "Medium", "High", "Very High"], index=["Low", "Medium", "High", "Very High"].index(st.session_state['base_cost_level_s']))
        base_cost_value = {"Low": 1000, "Medium": 3000, "High": 5000, "Very High": 15000}[st.session_state['base_cost_level_s']]
        swales_capital_cost = impervious_area * base_cost_value
        tab_object.write(f"Total Capital Cost: ${impervious_area * base_cost_value}")
        st.session_state['swales__capital_cost'] = swales_capital_cost

        tab_object.subheader("Maintenance Cost")
        st.session_state['irim_select_s'] = tab_object.selectbox("Inspection, Reporting & Information Management", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['irim_select_s']), key="irim_s")
        irim_value = {"Low": 90 * (1 / 3), "Medium": 140 * (1/3), "High": 260 * 1}[st.session_state['irim_select_s']]
        st.session_state['vm_select_s'] = tab_object.selectbox("Vegetation Management with Trash & Minor Debris Removal", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['vm_select_s']))
        vm_value = {"Low": 360 * (1/3), "Medium": 480 * 1, "High": 480 * 12}[st.session_state['vm_select_s']]
        st.session_state['cm_select_s'] = tab_object.selectbox("Corrective Maintenance", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['cm_select_s']))
        cm_value = {"Low": 960 * 0.1, "Medium": 1440 * 0.25, "High": 1440 * 0.5}[st.session_state['cm_select_s']]
        swales_maintenance_cost = irim_value + vm_value + cm_value
        tab_object.write(f"Total Maintenance Cost: ${sum([irim_value, vm_value, cm_value])}")
        st.session_state['swales__maintenance_cost'] = swales_maintenance_cost
    else:
        st.session_state['swales__capital_cost'] = 0
        st.session_state['swales__maintenance_cost'] = 0

    return tab_object
