import streamlit as st
from pages.ct_scripts import *

st.title('Cost Tool')
(
    retention_pond_st,
    cistern_st,
 bioretention_st,
 ed_basin_st,
 green_roof_st,
 icpv_st,
 perm_pavements_st,
 rain_garden_st,
 swales_st) = st.tabs(["Retention Pond",
                       "Cistern",
                       "Bioretention",
                       "Extended Detention Basin",
                       "Green Roof",
                       "In-Curb Planter Vault",
                       "Permeable Pavement",
                       "Residential Rain Garden",
                       "Swales"])

cisterns_tab(cistern_st)
swales_tab(swales_st)
ed_basin_tab(ed_basin_st)
bioretention_tab(bioretention_st)
green_roof_tab(green_roof_st)
icpv_tab(icpv_st)
perm_pavements_tab(perm_pavements_st)
rain_garden_tab(rain_garden_st)
retention_pond_tab(retention_pond_st)
