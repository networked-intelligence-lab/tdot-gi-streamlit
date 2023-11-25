import streamlit as st
from pages.ct_scripts import *
from streamlit_extras.app_logo import add_logo
from modules.sidebar import build_sidebar

build_sidebar()
add_logo("media/logo.png", height=150)

st.title('Economic Impact')
(cistern_st,
 bioretention_st,
 ed_basin_st,
 icpv_st,
 perm_pavements_st,
 swales_st) = st.tabs(["Cistern",
                       "Bioretention",
                       "Extended Detention Basin",
                       "In-Curb Planter Vault",
                       "Permeable Pavement",
                       "Swales",
                       ])

cisterns_tab(cistern_st)
swales_tab(swales_st)
ed_basin_tab(ed_basin_st)
bioretention_tab(bioretention_st)
icpv_tab(icpv_st)
perm_pavements_tab(perm_pavements_st)
