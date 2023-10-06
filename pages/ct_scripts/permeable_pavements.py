def perm_pavements_tab(tab_object):
    """

    :param tab_object:
    :type tab_object: streamlit.tab.Tab
    :return:
    """

    tab_object.subheader("Capital Cost")
    surface_area = tab_object.number_input("Surface Area of Permeable Pavement System (ft2)", value=0.0)
    paver_type_dict = {
        "Asphalt": {"Low": 0.5, "High": 1},
        "Concrete": {"Low": 2, "High": 6.5},
        "Grass": {"Low": 1.5, "High": 5.75},
        "Interlocking Concrete Paving Blocks": {"Low": 5, "High": 10},
    }
    paver_type = tab_object.selectbox("Paver Type", options=list(paver_type_dict.keys()))
    paver_low_high = tab_object.selectbox("Paver Type", options=["Low", "High"])
    tab_object.write(f"Total Capital Cost: ${surface_area * paver_type_dict[paver_type][paver_low_high]}")

    tab_object.subheader("Maintenance Cost")
    irim_select = tab_object.selectbox("Inspection, Reporting & Information Management",
                                       options=["Low", "Medium", "High"], key="irim_pp")
    irim_value = {"Low": 90 * (1 / 3), "Medium": 140 * (1/3), "High": 260 * 1}[irim_select]
    lm_select = tab_object.selectbox("Litter & Minor Debris Removal", options=["Low", "Medium", "High"])
    lm_value = {"Low": 45 * (1/3), "Medium": 120 * 1, "High": 120 * 12}[lm_select]
    pps_select = tab_object.selectbox("Permeable pavement sweeping", options=["Low", "Medium", "High"])
    pps_value = {"Low": 160 * (1/3), "Medium": 80 * 1, "High": 80 * 12}[pps_select]
    tab_object.write(f"Total Maintenance Cost: ${sum([irim_value, lm_value, pps_value])}")

    return tab_object
