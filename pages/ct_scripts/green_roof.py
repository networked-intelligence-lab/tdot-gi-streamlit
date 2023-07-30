import pandas as pd
def green_roof_tab(tab_object):
    tab_object.header('Design and Maintenance Options')
    tab_object.subheader("Roof Characteristics")
    roof_area = tab_object.number_input('Roof Area (sq. ft)', value=10000, step=1)
    building_height = tab_object.number_input('Building Height (stories)', value=4,
                                             step=1)

    """
    Primary Roof Function ("P"; Promotional or Aesthetics and social environment enhancement.)
    """
    tab_object.subheader("Design and Maintenance Options")
    primary_roof_function = tab_object.selectbox('Primary Roof Function',
                                    ('O: Operational, only basic costs are added to achieve basic Green Roof benefits',
                                     'P: Promotional or Aesthetics and social environment enhancement*'))
    prf_rows = [{'Assumptions for "Operational" Roof Function': 'Option A (modular green roof assembly), "operational" design type, assumes standard modular installation (some manufactures may offer a light or extra-light product, and may cost less); option B (non-modular custom green roof), "operational" design type, assumes basic Sedum species mat with growth media incorporated. Both "operational" design types assume no botanical upgrades, irrigation, or access patios. All assumptions and their associated costs can be modified on the "Capitol Costs" section.',
                 'Assumptions for "Promotional or Aesthetic" Roof Function': 'Option A (modular green roof assembly), "Promotional or Aesthetic" design type, assumes basic modular installation; option B (non-modular custom green roof), "Promotional or Aesthetic" design type assumes 6" engineered growth media with Sedum mat. Both "Promotional or Aesthetic" installation types assume a modest botanical upgrade, irrigation, and 10% roof coverage of access patios. All assumptions and their associated costs can be modified on the "Capitol Costs" section.'}]
    prf_df = pd.DataFrame.from_dict(prf_rows)
    tab_object.table(prf_df)

    prf_choice = primary_roof_function.split(":")[0]
    if prf_choice == "O":
        irrigation_needed = tab_object.selectbox('Irrigation Needed', ('No', 'Yes'))
    else:
        irrigation_needed = tab_object.selectbox('Irrigation Needed', ('Yes', 'No'))

    level_of_maintenance = tab_object.selectbox('Level of Maintenance', ('Low', 'Medium', 'High'))

    tab_object.subheader("Whole Life Cost Options")
    discount_rate = tab_object.number_input('Discount Rate', value=5.50, key="green_roof_discount_rate")

    return tab_object
