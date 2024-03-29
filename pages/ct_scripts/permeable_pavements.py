import streamlit as st


def perm_pavements_tab(tab_object):
    """
    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    # Initialize session state variables if they don't exist
    if 'pp_surface_area_pp' not in st.session_state:
        st.session_state['pp_surface_area_pp'] = 0.0
    if 'pp_paver_type_pp' not in st.session_state:
        st.session_state['pp_paver_type_pp'] = "Asphalt"
    if 'pp_paver_low_high_pp' not in st.session_state:
        st.session_state['pp_paver_low_high_pp'] = "Low"
    if 'pp_irim_select_pp' not in st.session_state:
        st.session_state['pp_irim_select_pp'] = "Low"
    if 'pp_lm_select_pp' not in st.session_state:
        st.session_state['pp_lm_select_pp'] = "Low"
    if 'pp_pps_select_pp' not in st.session_state:
        st.session_state['pp_pps_select_pp'] = "Low"

    if 'use_pp' not in st.session_state:
        st.session_state['use_pp'] = False
    def toggle_usage():
        if 'use_pp' not in st.session_state:
            st.session_state['use_pp'] = False
        st.session_state["use_pp"] = not st.session_state["use_pp"]

    use = tab_object.checkbox("Use Permeable Pavements", value=st.session_state["use_pp"], on_change=toggle_usage)
    if use:
        tab_object.subheader("Capital Cost")
        st.session_state['pp_surface_area_pp'] = tab_object.number_input("Surface Area of Permeable Pavement System (ft2)", value=st.session_state['pp_surface_area_pp'])
        paver_type_dict = {
            "Asphalt": {"Low": 0.5, "High": 1},
            "Concrete": {"Low": 2, "High": 6.5},
            "Grass": {"Low": 1.5, "High": 5.75},
            "Interlocking Concrete Paving Blocks": {"Low": 5, "High": 10},
        }
        st.session_state['pp_paver_type_pp'] = tab_object.selectbox("Paver Type", options=list(paver_type_dict.keys()), index=list(paver_type_dict.keys()).index(st.session_state['pp_paver_type_pp']))
        st.session_state['pp_paver_low_high_pp'] = tab_object.selectbox("Cost Estimate", options=["Low", "High"], index=["Low", "High"].index(st.session_state['pp_paver_low_high_pp']))
        perm_pavements_capital_cost = st.session_state['pp_surface_area_pp'] * paver_type_dict[st.session_state['pp_paver_type_pp']][st.session_state['pp_paver_low_high_pp']]
        tab_object.write(f"Total Capital Cost: ${perm_pavements_capital_cost}")
        st.session_state['perm_pavements__capital_cost'] = perm_pavements_capital_cost

        tab_object.subheader("Maintenance Cost")
        st.session_state['pp_irim_select_pp'] = tab_object.selectbox("Inspection, Reporting & Information Management", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['pp_irim_select_pp']), key="irim_pp")
        irim_value = {"Low": 90 * (1 / 3), "Medium": 140 * (1/3), "High": 260 * 1}[st.session_state['pp_irim_select_pp']]
        st.session_state['pp_lm_select_pp'] = tab_object.selectbox("Litter & Minor Debris Removal", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['pp_lm_select_pp']))
        lm_value = {"Low": 45 * (1/3), "Medium": 120 * 1, "High": 120 * 12}[st.session_state['pp_lm_select_pp']]
        st.session_state['pp_pps_select_pp'] = tab_object.selectbox("Permeable pavement sweeping", options=["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(st.session_state['pp_pps_select_pp']))
        pps_value = {"Low": 160 * (1/3), "Medium": 80 * 1, "High": 80 * 12}[st.session_state['pp_pps_select_pp']]
        perm_pavements_maintenance_cost = sum([irim_value, lm_value, pps_value])
        tab_object.write(f"Total Maintenance Cost: ${sum([irim_value, lm_value, pps_value])}")
        st.session_state['perm_pavements__maintenance_cost'] = perm_pavements_maintenance_cost
    else:
        st.session_state['perm_pavements__capital_cost'] = 0
        st.session_state['perm_pavements__maintenance_cost'] = 0

    return tab_object
