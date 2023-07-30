def icpv_tab(tab_object):
    tab_object.header('Design and Maintenance Options')
    tab_object.subheader("Watershed Characteristics")
    drainage_area = tab_object.number_input('Drainage Area (acres)', value=0.25)
    drainage_area_ic = tab_object.number_input('Drainage Area Impervious Cover (percent)', value=100)
    total_ic_drained = tab_object.number_input('Total Impervious Cover to be Drained', value=drainage_area * drainage_area_ic)

    tab_object.subheader("Design and Maintenance Options")
    construction_type = tab_object.selectbox("Construction Type", ("Prefabricated Vault", "In-situ Vault Fabrication"))
    level_of_maintenance = tab_object.selectbox("Choose Level of Maintenance", ("High", "Medium", "Low"), key="icpv_lom")

    tab_object.subheader("Whole Life Cost Options")
    discount_rate = tab_object.number_input('Discount Rate', value=5.50, key="icpv_discount_rate")

    return tab_object
