def icpv_tab(tab_object):
    """

    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    tab_object.subheader("Capital Cost")
    drainage_area = tab_object.number_input("Drainage area (acre)", value=0.0, key="drainage_area_pv")
    impervious_area_percent = tab_object.number_input("Impervious area (%)", value=0, step=1) / 100
    impervious_area = drainage_area * impervious_area_percent
    construction_type = tab_object.selectbox("Construction Type", options=["In Situ", "Prefabricated"])
    num_vaults = max([1, impervious_area])
    construction_type_value = {"In Situ": 155827 * impervious_area, "Prefabricated": num_vaults * 10000}[construction_type]
    tab_object.write(f"Total Capital Cost: ${construction_type_value}")

    tab_object.subheader("Maintenance Cost")
    irim_select = tab_object.selectbox("Inspection, Reporting & Information Management",
                                       options=["Low", "Medium", "High"], key="irim_pv")
    irim_value = {"Low": 20 * (1 / 3), "Medium": 31 * 1, "High": 45 * 3}[irim_select]
    vm_select = tab_object.selectbox("Litter & Minor Debris Removal, and Vegetation Management",
                                     options=["Low", "Medium", "High"])
    vm_value = {"Low": 45 * 1, "Medium": 60 * 2, "High": 75 * 6}[vm_select]
    vs_select = tab_object.selectbox("In-Curb Planter Vault Sweeping", options=["Low", "Medium", "High"])
    vs_value = {"Low": 65 * 1, "Medium": 80 * 2, "High": 95 * 6}[vs_select]
    ucd_select = tab_object.selectbox("Unclog Drain", options=["Low", "Medium", "High"], key="ucd_pv")
    ucd_value = {"Low": 160 * 0.2, "Medium": 160 * 0.5, "High": 190 * 1}[ucd_select]
    upg_select = tab_object.selectbox("Up-Fill Growth Medium", options=["Low", "Medium", "High"])
    upg_value = {"Low": 125 * 0.2, "Medium": 130 * 0.5, "High": 200 * 1}[upg_select]
    tab_object.write(f"Total Maintenance Cost: ${sum([irim_value, vm_value, vs_value, ucd_value, upg_value])}")

    return tab_object
