import streamlit as st


def icpv_tab(tab_object):
    """
    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    # Initialize session state variables if they don't exist
    if 'ic_planter_drainage_area_pv' not in st.session_state:
        st.session_state['ic_planter_drainage_area_pv'] = 0.0
    if 'ic_planter_impervious_area_percent_pv' not in st.session_state:
        st.session_state['ic_planter_impervious_area_percent_pv'] = 0.0
    if 'ic_planter_construction_type_pv' not in st.session_state:
        st.session_state['ic_planter_construction_type_pv'] = "In Situ"
    if 'ic_planter_irim_select_pv' not in st.session_state:
        st.session_state['ic_planter_irim_select_pv'] = "Low"
    if 'ic_planter_vm_select_pv' not in st.session_state:
        st.session_state['ic_planter_vm_select_pv'] = "Low"
    if 'ic_planter_vs_select_pv' not in st.session_state:
        st.session_state['ic_planter_vs_select_pv'] = "Low"
    if 'ic_planter_ucd_select_pv' not in st.session_state:
        st.session_state['ic_planter_ucd_select_pv'] = "Low"
    if 'ic_planter_upg_select_pv' not in st.session_state:
        st.session_state['ic_planter_upg_select_pv'] = "Low"

    if 'use_ic' not in st.session_state:
        st.session_state['use_ic'] = False
    def toggle_usage():
        st.session_state["use_ic"] = not st.session_state["use_ic"]

    use = tab_object.checkbox("Use IC Planter Vaults", value=st.session_state["use_ic"], on_change=toggle_usage)
    if use:
        tab_object.subheader("Capital Cost")
        st.session_state['ic_planter_drainage_area_pv'] = tab_object.number_input("Drainage area (acre)", value=st.session_state['ic_planter_drainage_area_pv'], key="_drainage_area_pv")
        st.session_state['ic_planter_impervious_area_percent_pv'] = tab_object.number_input("Impervious area (%)", value=st.session_state['ic_planter_impervious_area_percent_pv'], step=1.0, key="_impervious_area_percent_pv") / 100
        impervious_area = st.session_state['ic_planter_drainage_area_pv'] * st.session_state['ic_planter_impervious_area_percent_pv']
        st.session_state['ic_planter_construction_type_pv'] = tab_object.selectbox("Construction Type", options=["In Situ", "Prefabricated"], index=["In Situ", "Prefabricated"].index(st.session_state['ic_planter_construction_type_pv']))
        num_vaults = max([1, impervious_area])
        construction_type_value = {"In Situ": 155827 * impervious_area, "Prefabricated": num_vaults * 10000}[st.session_state['ic_planter_construction_type_pv']]
        tab_object.write(f"Total Capital Cost: ${construction_type_value}")
        st.session_state["icpv__capital_cost"] = construction_type_value

        tab_object.subheader("Maintenance Cost")
        st.session_state['ic_planter_irim_select_pv'] = tab_object.selectbox("Inspection, Reporting & Information Management", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ic_planter_irim_select_pv']), key="_irim_pv")
        irim_value = {"Low": 20 * (1 / 3), "Medium": 31 * 1, "High": 45 * 3}[st.session_state['ic_planter_irim_select_pv']]
        st.session_state['ic_planter_vm_select_pv'] = tab_object.selectbox("Litter & Minor Debris Removal, and Vegetation Management", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ic_planter_vm_select_pv']))
        vm_value = {"Low": 45 * 1, "Medium": 60 * 2, "High": 75 * 6}[st.session_state['ic_planter_vm_select_pv']]
        st.session_state['ic_planter_vs_select_pv'] = tab_object.selectbox("In-Curb Planter Vault Sweeping", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ic_planter_vs_select_pv']))
        vs_value = {"Low": 65 * 1, "Medium": 80 * 2, "High": 95 * 6}[st.session_state['ic_planter_vs_select_pv']]
        st.session_state['ic_planter_ucd_select_pv'] = tab_object.selectbox("Unclog Drain", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ic_planter_ucd_select_pv']), key="_ucd_pv")
        ucd_value = {"Low": 160 * 0.2, "Medium": 160 * 0.5, "High": 190 * 1}[st.session_state['ic_planter_ucd_select_pv']]
        st.session_state['ic_planter_upg_select_pv'] = tab_object.selectbox("Up-Fill Growth Medium", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['ic_planter_upg_select_pv']))
        upg_value = {"Low": 125 * 0.2, "Medium": 130 * 0.5, "High": 200 * 1}[st.session_state['ic_planter_upg_select_pv']]
        icpv_maintenance_cost = sum([irim_value, vm_value, vs_value, ucd_value, upg_value])
        tab_object.write(f"Total Maintenance Cost: ${icpv_maintenance_cost}")
        st.session_state["icpv__maintenance_cost"] = icpv_maintenance_cost
    else:
        st.session_state["icpv__capital_cost"] = 0
        st.session_state["icpv__maintenance_cost"] = 0

    return tab_object
