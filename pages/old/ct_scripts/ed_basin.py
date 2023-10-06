def ed_basin_tab(tab_object):
    tab_object.header('Design and Maintenance Options')
    tab_object.subheader("Watershed Characteristics")
    drainage_area = tab_object.number_input('Drainage Area (ac)', value=10.0)
    drainage_area_ic = tab_object.number_input('Drainage Area Impervious Cover (percent)', value=40)
    ws_land_use_type = tab_object.selectbox("Watershed Land Use Type", ("Residential",
                                                                        "Commercial",
                                                                        "Industrial",
                                                                        "Roads"))

    tab_object.subheader("Facility Storage Volume")
    water_quality_volume = tab_object.number_input('Water Quality Volume (WQV; ft. cubed)*', value=18150)
    flood_detatt_volume = tab_object.number_input('Flood Detention/Attenuation Volume', value=0)
    channel_protero_volume = tab_object.number_input('Channel Protection/Erosion Control Volume**', value=0)
    other_volume = tab_object.number_input('Other Volume (e.g., Recharge Volume)', value=0)
    tab_object.write("* Model default is 1/2-inch of capture over drainage area; actual volume will depend on regional regulatory requirements and site-specific characteristics, etc.")
    tab_object.write("** For example, 24-hour extended detention storage.")
    tab_object.write(f"Total Facility Storage Volume: {water_quality_volume + flood_detatt_volume + channel_protero_volume + other_volume}")

    tab_object.subheader("Design and Maintenance Options")
    level_of_maintenance = tab_object.selectbox("Choose Level of Maintenance", ("High", "Medium", "Low"))
    main_pool_volume = tab_object.number_input('Main Pool Volume (yd. cubed)', value=672)
    pct_full_sed_rem = tab_object.number_input('Pct. Full when sediment removed from Basin (percent)*', value=25)
    quantity_sed_removed = tab_object.number_input('Quantity of Sediment Removed (yd. cubed)', value=168)
    tab_object.write("* Can adjust to be higher if expect heavy soils/sediment deposition to basin.")

    tab_object.subheader("Whole Life Cost Options")
    discount_rate = tab_object.number_input('Discount Rate', value=5.50)
    return tab_object
