import streamlit as st
from modules.helpers import subsubheader
from streamlit_extras.app_logo import add_logo
import json

add_logo("media/logo.png", height=150)

st.title('Documentation')
st.subheader('Technical Documentation')
st.write('This documentation is intended for the technical user. It provides a detailed description of the methods used to develop the tool and the data sources used to populate the tool. The documentation is divided into the following sections:')
st.markdown('''
1. Introduction
2. Data Sources
3. Data Processing
4. Code Structure''')

subsubheader(st, 'Introduction')
st.write('The tool is developed using Python and the Streamlit library. The tool is developed primarily through the following libraries:')
st.markdown('''
1. Streamlit
2. Pandas
3. streamlit-extras
4. googlemaps (Python library)
5. geopy
''')

subsubheader(st, 'Data Sources')
st.write('The tool uses the following data sources:')
st.markdown('''
1. In-house Research Spreadsheet
    - Containing information such as site requirements, subgrade requirements, etc. for each green infrastructure.
2. Google Places API for maps/parks location searching
    - Allows us to calculate other nearby green infrastructure such as local parks and other landmarks of interest
3. CDC Wonder for Mortality Data
    - Allows us to calculate heat-related mortality
4. STRATUM Climate Zone GIS Shape files for STRATUM climate determination
    - Allows us to accommodate user climate zone based on GPS locations automatically
5. Collated equations data from research
    - For calculations such as total stormwater runoff, etc.
''')