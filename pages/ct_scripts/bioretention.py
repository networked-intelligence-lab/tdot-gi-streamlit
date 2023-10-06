def bioretention_tab(tab_object):
    """

    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    tab_object.subheader("Capital Cost")
    drainage_area = tab_object.number_input("Drainage area (acre)", value=0)
    underdrain = tab_object.selectbox("Underdrain", options=["Yes", "No"])
    underdrain_cost = {"Yes": 89028, "No": 42254}[underdrain]
    tab_object.write(f"Total Capital Cost: ${drainage_area * underdrain_cost}")


    tab_object.subheader("Maintenance Cost")
    irim_select = tab_object.selectbox("Inspection, Reporting & Information Management", options=["Low", "Medium", "High"], key="irim_br")
    irim_value = {"Low": 60 * (1/3), "Medium": 130 * 0.5, "High": 570 * 1}[irim_select]
    vm_select = tab_object.selectbox("Vegetation Management with Trash & Minor Debris Removal", options=["Low", "Medium", "High"])
    vm_value = {"Low": 60 * 1, "Medium": 124 * 2, "High": 270 * 3}[vm_select]
    ts_select = tab_object.selectbox("Till Soil", options=["Low", "Medium", "High"])
    ts_value = {"Low": 320 * 0.2, "Medium": 448 * 0.25, "High": 560 * 0.5}[ts_select]
    ucd_select = tab_object.selectbox("Unclog Drain", options=["Low", "Medium", "High"])
    ucd_value = {"Low": 160 * 0.2, "Medium": 160 * 0.5, "High": 190 * 1}[ucd_select]
    rm_select = tab_object.selectbox("Replace Mulch", options=["Low", "Medium", "High"])
    rm_value = {"Low": 1935 * 0.25, "Medium": 1999 * 0.5, "High": 2145 * 1}[ucd_select]
    tab_object.write(f"Total Maintenance Cost: ${sum([irim_value, vm_value, ts_value, ucd_value, rm_value])}")
    return tab_object