def rain_garden_tab(tab_object):
    tab_object.header('Design and Maintenance Options')
    tab_object.subheader("Watershed Characteristics")
    drainage_area = tab_object.number_input('Drainage Area (often roof area + paved area; sq. ft.)', value=1000)
    garden_area = tab_object.number_input('Garden Area (default is 20% of drainage area; sq. ft.)', value=0.2 * drainage_area)

    tab_object.subheader("Design and Maintenance Options")
    installation_type = tab_object.selectbox("Installation Type", ("Professional",
                                                                   "Self or Volunteer"))
    single_or_neighborhood = tab_object.selectbox("Single or Neighborhood (>100 homes)", ("Single",
                                                                                          "Neighborhood"))
    level_of_maintenance = tab_object.selectbox("Choose Level of Maintenance", ("Medium", "High (omate garden)", "Low"), key="rg_lom")

    tab_object.subheader("Whole Life Cost Options")
    discount_rate = tab_object.number_input('Discount Rate', value=5.50, key="rg_discount_rate")
    return tab_object
