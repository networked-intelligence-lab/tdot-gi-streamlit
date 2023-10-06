def swales_tab(tab_object):
    """

    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    tab_object.subheader("Capital Cost")
    drainage_area = tab_object.number_input("Drainage Area (acre)", value=2.0)
    impervious_area_percent = tab_object.number_input("Impervious area (%)", value=40, step=1, key="imp_s") / 100
    impervious_area = drainage_area * impervious_area_percent
    base_cost_level = tab_object.selectbox("Base Cost Level", options=["Low", "Medium", "High", "Very High"])
    base_cost_value = {"Low": 1000, "Medium": 3000, "High": 5000, "Very High": 15000}[base_cost_level]
    tab_object.write(f"Total Capital Cost: ${impervious_area * base_cost_value}")

    tab_object.subheader("Maintenance Cost")
    irim_select = tab_object.selectbox("Inspection, Reporting & Information Management",
                                       options=["Low", "Medium", "High"], key="irim_s")
    irim_value = {"Low": 90 * (1 / 3), "Medium": 140 * (1/3), "High": 260 * 1}[irim_select]
    vm_select = tab_object.selectbox("Vegetation Management with Trash & Minor Debris Removal",
                                     options=["Low", "Medium", "High"], key="vm_s")
    vm_value = {"Low": 360 * (1/3), "Medium": 480 * 1, "High": 480 * 12}[vm_select]
    cm_select = tab_object.selectbox("Corrective Maintenance", options=["Low", "Medium", "High"])
    cm_value = {"Low": 960 * 0.1, "Medium": 1440 * 0.25, "High": 1440 * 0.5}[cm_select]
    tab_object.write(f"Total Maintenance Cost: ${sum([irim_value, vm_value, cm_value])}")

    return tab_object
