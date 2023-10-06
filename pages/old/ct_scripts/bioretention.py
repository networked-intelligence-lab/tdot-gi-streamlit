def bioretention_tab(tab_object):
    tab_object.header('Design and Maintenance Options')
    tab_object.subheader("Watershed Characteristics")
    drainage_area = tab_object.number_input('Drainage Area (ac)', value=1.0)
    drainage_area_ic = tab_object.number_input('Drainage Area Impervious Cover (percent)', value=80)
    underdrain_to_conventional = tab_object.selectbox('Underdrain to Conventional Storm Drain?', ('Yes', 'No'))

    tab_object.subheader("Design and Maintenance Options")
    level_of_maintenance = tab_object.selectbox("Choose Level of Maintenance", ("High", "Medium", "Low"), key="bioret_lom")
    retro_vs_new = tab_object.selectbox("Retrofit vs. New Construction", ("Retrofit", "New Construction"))
    tank_costs_gallon = {
        'Steel': 2.51,
        'Fiberglass': 1.33,
        'Concrete': 1.66,
        'HDPE': 1.43}

    tab_object.subheader("Whole Life Cost Options")
    discount_rate = tab_object.number_input('Discount Rate', value=5.50, key="bioret_discount_rate")

    tab_object.header('Capital Costs')
    cc_method_selects = {'a': "Method A: Simple Cost Based on Drainage Area",
                         'b': "Method B: User-Entered Engineer's Estimate"}
    cc_method = tab_object.selectbox('Select Method of Calculation', cc_method_selects.values())

    if cc_method == cc_method_selects['a']:
        tab_object.subheader("Cost Based on Drainage Area")

        effective_drainage_area = drainage_area * drainage_area_ic
        tab_object.write(f"Effective Drainage Area (DA) (acres): {effective_drainage_area}")
        tab_object.write(f"Suggested Garden Size (SF): {max([0.07 * effective_drainage_area, 100])}")
    else:
        tab_object.subheader("Total Facility Base Costs")
    return tab_object
