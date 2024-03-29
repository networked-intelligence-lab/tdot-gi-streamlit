def cisterns_tab(tab_object):
    tab_object.header('Design and Maintenance Options')
    tab_object.subheader("Storage Requirements")
    tank_size = tab_object.number_input('Tank Size (gallons)', value=6300, step=1)
    impervious_area = tab_object.number_input('Impervious Drainage Area, DA (often roof area; sq.ft)', value=5000,
                                             step=1)
    rainfall_event = tab_object.number_input('Max Design Rainfall Event (inches)', value=2)

    tab_object.write(f"Total storage needed: {(impervious_area * (rainfall_event / 12)) * 7.48}")

    tab_object.subheader("System Characteristics")
    material = tab_object.selectbox('Type of Tank Desired', ('Steel', 'Fiberglass', 'Concrete', 'HDPE'))
    tank_costs_gallon = {
        'Steel': 2.51,
        'Fiberglass': 1.33,
        'Concrete': 1.66,
        'HDPE': 1.43}

    tab_object.write(f"Estimated tank cost: {tank_costs_gallon[material] * tank_size}")
    install_cost = tab_object.number_input('Installation cost', value=6275)
    pump_size = tab_object.number_input('Pump Size Needed (horsepower)', value=0.5)
    pump_cost = tab_object.number_input('Pump Cost', value=599)
    potable_resup = tab_object.number_input('Potable Re-Supply', value=0)

    tab_object.write(
        f"System base cost: {sum([tank_costs_gallon[material] * tank_size, install_cost, pump_cost, potable_resup])}")

    system_design_cost = tab_object.number_input('System Design Cost', value=1387)

    tab_object.write(
        f"Total facility cost: {sum([tank_costs_gallon[material] * tank_size, install_cost, pump_cost, potable_resup, system_design_cost])}")

    return tab_object
