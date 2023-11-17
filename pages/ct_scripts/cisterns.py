import streamlit as st


def cisterns_tab(tab_object):
    """

    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    tab_object.subheader("Capital Cost")
    impervious_area = tab_object.number_input("Impervious Area (ft^2)", value=0)
    rainfall_event = tab_object.number_input("Max Design Rainfall Event (in)", value=2)
    precip_volume_gen = (impervious_area * (rainfall_event / 12)) * 7.48
    material = tab_object.selectbox("Material", options=["Steel", "Fiberglass", "Concrete", "HDPE"])
    total_storage_needed = tab_object.number_input("Total Storage Needed (gal)", value=precip_volume_gen)
    material_costs = {"Steel": 1.33, "Fiberglass": 2.51, "Concrete": 1.43, "HDPE": 1.66}
    tab_object.write(f"Total Capital Cost: ${total_storage_needed * material_costs[material]}")
    st.session_state["cisterns_capital_cost"] = total_storage_needed * material_costs[material]


    tab_object.subheader("Maintenance Cost")
    irim_select = tab_object.selectbox("Inspection, Reporting & Information Management", options=["Low", "Medium", "High"])
    irim_value = {"Low": 135, "Medium": 130 * 2, "High": 340 * 12}[irim_select]
    rwc_select = tab_object.selectbox("Roof Washing, Cleaning Inflow Filters", options=["Low", "Medium", "High"])
    rwc_value = {"Low": 150, "Medium": 240 * 2, "High": 540 * 12}[rwc_select]
    tid_select = tab_object.selectbox("Tank inspection and disinfection", options=["Low", "Medium", "High"])
    tid_value = {"Low": 120 * 0.5, "Medium": 240 * 1, "High": 360 * 2}[tid_select]
    ism_select = tab_object.selectbox("Intermittent System Maintenance (System flush, debris/sediment removal from tank)", options=["Low", "Medium", "High"])
    ism_value = {"Low": 270 * (1/3), "Medium": 390 * (1/3), "High": 510 * (1/3)}[ism_select]

    tab_object.write(f"Total Maintenance Cost: ${sum([irim_value, rwc_value, tid_value, ism_value])}")
    st.session_state["cisterns_maintenance_cost"] = sum([irim_value, rwc_value, tid_value, ism_value])
    return tab_object
