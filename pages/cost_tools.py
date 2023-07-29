import streamlit as st
import pandas as pd
import numpy as np

from pages.ct_scripts import *


st.title('Cost Tool')
cistern_st, bioretention_st, swales_st = st.tabs(["Cistern", "Bioretention", "Swales"])

cisterns_tab(cistern_st)
swales_tab(swales_st)




