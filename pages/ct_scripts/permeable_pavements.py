def perm_pavements_tab(tab_object):
    tab_object.header('Design and Maintenance Options')
    tab_object.subheader("Watershed Characteristics")
    perm_pavement_surface_area = tab_object.number_input('Surface Area of Permeable Pavement System (ft. squared)', value=21780)
    drainage_area = tab_object.number_input('Drainage Area (ac)', value=perm_pavement_surface_area)
    drainage_area_ic = tab_object.number_input('Drainage Area Impervious Cover (percent)', value=100, key="perm_pavements_drainage_area_ic")
    watershed_land_use_type = tab_object.selectbox('Watershed Land Use Type', ('Residential',
                                                                               'Commercial',
                                                                               'Industrial',
                                                                               'Roads'))

    tab_object.subheader("Design and Maintenance Options")
    pavement_type = tab_object.selectbox("Choose a Pavement Type", ("Asphalt",
                                                                    "Porous Concrete",
                                                                    "Grass/Gravel Pavers",
                                                                    "Interlocking Concrete Paving Blocks",
                                                                    "Other"))
    capital_cost_level = tab_object.selectbox("Capital Cost Level", ("High", "Low"))
    level_of_maintenance = tab_object.selectbox("Choose Level of Maintenance", ("Medium", "High", "Low"), key="perm_pavements_lom")

    tab_object.subheader("Whole Life Cost Options")
    discount_rate = tab_object.number_input('Discount Rate', value=5.50, key="perm_pavements_discount_rate")
    return tab_object
