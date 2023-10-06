def ed_basin_tab(tab_object):
    """

    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    tab_object.subheader("Capital Cost")
    drainage_area = tab_object.number_input("Drainage area (acre)", value=0, key="drainage_area_ed")
    base_facility_cost = tab_object.selectbox("Base Facility Cost", options=["Low", "Medium", "High", "Very High"])
    base_facility_cost_value = {"Low": 1000, "Medium": 3000, "High": 5000, "Very High": 15000}[base_facility_cost]
    tab_object.write(f"Total Capital Cost: ${drainage_area * base_facility_cost_value}")

    tab_object.subheader("Maintenance Cost")
    irim_select = tab_object.selectbox("Inspection, Reporting & Information Management",
                                       options=["Low", "Medium", "High"], key="irim_ed")
    irim_value = {"Low": 90 * (1 / 3), "Medium": 140 * (1/3), "High": 260 * 1}[irim_select]
    vm_select = tab_object.selectbox("Vegetation Management with Trash & Minor Debris Removal",
                                     options=["Low", "Medium", "High"], key="vm_ed")
    vm_value = {"Low": 360 * (1/3), "Medium": 480 * 1, "High": 825 * 12}[vm_select]
    vc_select = tab_object.selectbox("Vector Control", options=["Low", "Medium", "High"])
    vc_value = {"Low": 200 * (1/6), "Medium": 200 * (1/3), "High": 2675 * 12}[vc_select]
    ifm_select = tab_object.selectbox("Intermittent Facility Maintenance (Excluding Sediment Removal)", options=["Low", "Medium", "High"])
    ifm_value = {"Low": 250 * 1, "Medium": 1000 * 1, "High": 2800 * 1}[ifm_select]
    tab_object.write(f"Total Maintenance Cost: ${sum([irim_value, vm_value, vc_value, ifm_value])}")

    return tab_object
