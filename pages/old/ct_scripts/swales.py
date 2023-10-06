def swales_tab(tab_object):
    col1, col2 = tab_object.columns(2)
    with col1:
        tab_object.header('Design and Maintenance Options')
        tab_object.subheader('Watershed Characteristics')
        drainage_area = tab_object.number_input('Drainage Area (ac)', value=2, step=1)
        impervious_cover = tab_object.number_input('Drainage Area Impervious Cover (pct)', value=40)
        land_use_type = tab_object.selectbox("Land Use Type",
                                            ('R: Residential', 'C: Commercial', 'Ro: Roads', 'I: Industrial'))

        tab_object.subheader('Design & Maintenance Options')
        level_of_maintenance = tab_object.selectbox("Level of Maintenance", ('H: High', 'M: Medium', 'L: Low'))

        tab_object.subheader('Whole Life Cost Options')
        discount_rate = tab_object.number_input('Discount Rate (%)', value=5.5)

        tab_object.header('Capital Costs')
        method = tab_object.selectbox('Select Method of Calculation', ('Please enter before continuing:', 'Method A: Simple Cost Based on Drainage Area', 'Method B: User-Entered Engineer\'s Estimate'))
        if method == 'Method A: Simple Cost Based on Drainage Area':
            tab_object.header('Method A: Simple Cost based on Drainage Area')
            tab_object.subheader('Cost based on Drainage Area')
            drainage_area = tab_object.number_input('Drainage Area (DA) (acres)', value=2)
            base_facility_cost_per_acre = tab_object.number_input('Base Facility Cost per acre DA ($)', value=3000)
            default_cost_adjustment = tab_object.number_input('Default Cost Adjustment for Smaller Projects', value=2.2)
            resulting_base_cost = tab_object.number_input('Resulting Base Cost per acre DA ($)', value=6600)
            base_facility_cost = tab_object.number_input('Base Facility Cost (rounded p to nearest $100) ($)', value=drainage_area * resulting_base_cost)
            engineering_and_planning = tab_object.number_input('Engineering & Planning (default = 25% of Base Cost) ($)',
                                                              value=3300)
            land_cost = tab_object.number_input('Land Cost ($)', value=0)
            other_cost = tab_object.number_input('Other Costs ($)', value=0)
            total_associated_other_cost = tab_object.number_input('Total Associated Other Costs ($)', value=sum([engineering_and_planning, land_cost, other_cost]))
            total_facility_base_cost = tab_object.number_input('Total Facility Base Cost ($)', value=sum([base_facility_cost, total_associated_other_cost]))

            capital_cost = tab_object.number_input('Capital Cost ($)', value=total_facility_base_cost)
        elif method == 'Method B: User-Entered Engineer\'s Estimate':
            tab_object.header('Method B: User-Entered Engineers Estimate')
            tab_object.subheader('Total Facility Base Costs')
            mobilization = tab_object.number_input('Mobilization (LS)')
            clearing_and_grubbing = tab_object.number_input('Clearing & Grubbing (AC)')
            excavation = tab_object.number_input('Excavation/Grading (CY)')
            dewatering = tab_object.number_input('Dewatering (LS)')
            haul_of_excavated_material = ('Haul/Dispose of Excavated Material (CY)')
            sediment_pretreatment_struct = tab_object.number_input('Sediment Pretreatment Struct (e.g.,inlet sump) (LF)')
            inflow_structure = tab_object.number_input('Inflow Structure(s) (LS)')
            energy_dissipation_apron = tab_object.number_input('Energy Dissipation Apron (LS)')
            overflow_structure = tab_object.number_input('Overflow Structure (concrete or rock riprap) (CY)')
            revegetation_controls = tab_object.number_input('Revegetation/Erosion Controls (SY)')
            traffic_control = tab_object.number_input('Traffic Control')
            signage_public_education_materials = tab_object.number_input('Signage, Public Education Materials,etc (LS)')


            tab_object.subheader('Associated Capital Costs')
            project_management = ('Project Management')
            engineering_preliminary = tab_object.number_input('Engineering: Preliminary')
            engineering_final_design = tab_object.number_input('Engineering; Final Design')
            topographic_survey = tab_object.number_input('Topographic Survey')
            geotechnical = tab_object.number_input('Geotechnical')
            landscape_design = tab_object.number_input('Landscape Design')
            land_acquisition = tab_object.number_input('Land Acquisition (site, easements, etc)')
            utility_relocation = tab_object.number_input('Utility Relocation')
            legal_services = tab_object.number_input('Legal Services')
            permitting_and_construction_inspection = tab_object.number_input('Permitting & Construction Inspection')
            sales_tax = tab_object.number_input('Sales Tax')
            contingency = tab_object.number_input('Contingency (e.g. 30%)')

            tab_object.header('Maintenance Costs')
            tab_object.subheader('Routine Maintenance Activities( Frequent, scheduled events')

    with col2:
        try:
            if method != '':
                tab_object.header('Cost Summary')
                tab_object.subheader('Capital Costs')
                total_facility_base_cost = tab_object.number_input('Total Base Facility Cost', value=total_facility_base_cost)
                total_associated_capital_cost = tab_object.number_input('Total Associated Capital Cost', value=3300)
        except UnboundLocalError:
            pass
    
    return tab_object