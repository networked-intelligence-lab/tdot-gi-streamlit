import streamlit as st
from pages.ct_scripts import *

st.title('Cost Tool')
(cistern_st,
 bioretention_st,
 ed_basin_st,
 green_roof_st,
 swales_st) = st.tabs(["Cistern",
                       "Bioretention",
                       "Extended Detention Basin",
                       "Green Roof",
                       "Swales"])

cisterns_tab(cistern_st)
swales_tab(swales_st)
ed_basin_tab(ed_basin_st)
bioretention_tab(bioretention_st)
green_roof_tab(green_roof_st)
