import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import Draw

# Create a map object
m = folium.Map(location=[40.7831, -73.9712], zoom_start=14)

# Add the draw tool to the map
draw = Draw(export=True)
draw.add_to(m)

# Display the map
folium_static(m)

# You can also retrieve the drawn shapes as GeoJSON
draw_data = st.session_state.get('draw_data', {})
if draw_data:
    st.json(draw_data)
