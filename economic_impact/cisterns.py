import streamlit as st
import pandas as pd
import numpy as np

st.title('Cisterns Cost Tool')

st.header('Design and Maintenance Options')
st.subheader("Storage Requirements")
d9 = st.number_input('Impervious Drainage Area, DA (often roof area; sq.ft)', value=5000, step=1)
d10 = st.number_input('Max Design Rainfall Event (inches)', value=1)

st.write((d9 * (d10/12)) * 7.48)