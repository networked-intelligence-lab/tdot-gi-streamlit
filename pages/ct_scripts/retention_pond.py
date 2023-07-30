def retention_pond_tab(tab_object):
    tab_object.header('Design and Maintenance Options')
    tab_object.subheader("Watershed Characteristics")
    drainage_area = tab_object.number_input('Drainage Area (acres)', value=50)
    drainage_area_ic = tab_object.number_input('Drainage Area Impervious Cover (percent)*', value=40, key="ret_pond_drainage_area_ic")
    watershed_land_use_type = tab_object.selectbox('Watershed Land Use Type', ('Residential',
                                                                               'Commercial',
                                                                               'Industrial',
                                                                               'Roads'), key="ret_pond_wlut")
    tab_object.write("* Included since frequently used to calculate storage volume.")

    tab_object.subheader("Facility Storage Volume")
    water_quality_volume = tab_object.number_input('Water Quality Volume (WQV; ft. cubed)*', value=drainage_area*0.5/12*43560)
    perm_pool_vol_ratio = tab_object.number_input('Permanent Pool Volume as Ratio of Water Quality Volume**', value=1.0)
    perm_pool_vol = tab_object.number_input('Permanent Pool Volume', value=(drainage_area*0.5/12*43560) * perm_pool_vol_ratio)
    flood_det_att_vol = tab_object.number_input('Flood Detention/Attenuation Volume (ft. cubed)', value=0)
    channel_prot_eros_ctrl_vol = tab_object.number_input('Channel Protection/Erosion Control Volume (ft. cubed)***', value=0)
    other_volume = tab_object.number_input('Other Volume (e.g., Recharge Volume)', value=0, key="ret_pond_other_volume")
    tab_object.write("* Model default is 1/2-inch of capture over drainage area; actual volume will depend on regional regulatory requirements and site-specific characteristics, etc.")
    tab_object.write("** Model default ratio = 1.0 (i.e., permanent pool volume EQUALS the water quality volume).")
    tab_object.write("*** For example, 24-hour extended detention storage.")
    tab_object.write(f"Total Facility Storage Volume: {water_quality_volume + perm_pool_vol + flood_det_att_vol + channel_prot_eros_ctrl_vol + other_volume}")


    tab_object.subheader("Design and Maintenance Options")
    level_of_maintenance = tab_object.selectbox("Choose Level of Maintenance", ("Medium", "High", "Low"), key="ret_pond_lom")
    forebay_size = tab_object.number_input('Forebay Size (percent of total pool)', value=0) / 100
    tab_object.write("[Enter 0% if no forebay or if not maintained separately from main pool]*")

    forbay_vol = tab_object.number_input('Forebay Volume (yd. cubed)', value=0)
    main_pool_vol = tab_object.number_input('Main Pool Volume (yd. cubed)', value=(1-forebay_size)*perm_pool_vol/27)
    pct_full_sed_rem = tab_object.number_input('Pct. Full when sediment removed from Forebay/Main Pool (percent)**', value=25) / 100
    quantity_sed_removed_forebay = tab_object.number_input('Quantity of Sediment Removed from Forebay (yd. cubed)', value=forbay_vol * pct_full_sed_rem)
    quantity_sed_removed_mainpool = tab_object.number_input('Quantity of Sediment Removed from Main Pool (yd. cubed)', value=main_pool_vol * pct_full_sed_rem)
    tab_object.write("* Model default is no separate maintenance of the forebay.")
    tab_object.write("** Can adjust to be higher if expect heavy soils/sediment deposition to basin.")

    tab_object.subheader("Whole Life Cost Options")
    discount_rate = tab_object.number_input('Discount Rate', value=5.50, key="rp_discount_rate")
    return tab_object
