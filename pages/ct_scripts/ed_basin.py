import streamlit as st


def ed_basin_tab(tab_object):
    """
    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    # Initialize session state variables if they don't exist
    if 'ed_basin_drainage_area_ed' not in st.session_state:
        st.session_state['ed_basin_drainage_area_ed'] = 0
    if 'ed_basin_base_facility_cost' not in st.session_state:
        st.session_state['ed_basin_base_facility_cost'] = "Low"
    if 'ed_basin_irim_select_ed' not in st.session_state:
        st.session_state['ed_basin_irim_select_ed'] = "Low"
    if 'ed_basin_vm_select_ed' not in st.session_state:
        st.session_state['ed_basin_vm_select_ed'] = "Low"
    if 'ed_basin_vc_select_ed' not in st.session_state:
        st.session_state['ed_basin_vc_select_ed'] = "Low"
    if 'ed_basin_ifm_select_ed' not in st.session_state:
        st.session_state['ed_basin_ifm_select_ed'] = "Low"

    if 'use_ed_basin' not in st.session_state:
        st.session_state['use_ed_basin'] = False
    def toggle_usage():
        st.session_state["use_ed_basin"] = not st.session_state["use_ed_basin"]

    use = tab_object.checkbox("Use ED Basin", value=st.session_state["use_ed_basin"], on_change=toggle_usage)
    if use:
        tab_object.subheader("Capital Cost")
        st.session_state['ed_basin_drainage_area_ed'] = tab_object.number_input("Drainage area (acre)", value=st.session_state['ed_basin_drainage_area_ed'], key="_drainage_area_ed")
        st.session_state['ed_basin_base_facility_cost'] = tab_object.selectbox("Base Facility Cost", options=["Low", "Medium", "High", "Very High"], index=["Low", "Medium", "High", "Very High"].index(st.session_state['ed_basin_base_facility_cost']))
        base_facility_cost_value = {"Low": 1000, "Medium": 3000, "High": 5000, "Very High": 15000}[st.session_state['ed_basin_base_facility_cost']]
        ed_basin_capital_cost = st.session_state['ed_basin_drainage_area_ed'] * base_facility_cost_value
        tab_object.write(f"Total Capital Cost: ${ed_basin_capital_cost}")
        st.session_state["ed_basin__capital_cost"] = ed_basin_capital_cost

        tab_object.subheader("Maintenance Cost")
        st.session_state['ed_basin_irim_select_ed'] = tab_object.selectbox("Inspection, Reporting & Information Management", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ed_basin_irim_select_ed']), key="irim_ed")
        irim_value = {"Low": 90 * (1 / 3), "Medium": 140 * (1/3), "High": 260 * 1}[st.session_state['ed_basin_irim_select_ed']]
        st.session_state['ed_basin_vm_select_ed'] = tab_object.selectbox("Vegetation Management with Trash & Minor Debris Removal", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ed_basin_vm_select_ed']), key="vm_ed")
        vm_value = {"Low": 360 * (1/3), "Medium": 480 * 1, "High": 825 * 12}[st.session_state['ed_basin_vm_select_ed']]
        st.session_state['ed_basin_vc_select_ed'] = tab_object.selectbox("Vector Control", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ed_basin_vc_select_ed']))
        vc_value = {"Low": 200 * (1/6), "Medium": 200 * (1/3), "High": 2675 * 12}[st.session_state['ed_basin_vc_select_ed']]
        st.session_state['ed_basin_ifm_select_ed'] = tab_object.selectbox("Intermittent Facility Maintenance (Excluding Sediment Removal)", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ed_basin_ifm_select_ed']))
        ifm_value = {"Low": 250 * 1, "Medium": 1000 * 1, "High": 2800 * 1}[st.session_state['ed_basin_ifm_select_ed']]
        ed_basin_maintenance_cost = sum([irim_value, vm_value, vc_value, ifm_value])
        tab_object.write(f"Total Maintenance Cost: ${ed_basin_maintenance_cost}")
        st.session_state["ed_basin__maintenance_cost"] = ed_basin_maintenance_cost
    else:
        st.session_state["ed_basin__capital_cost"] = 0
        st.session_state["ed_basin__maintenance_cost"] = 0

    return tab_object
