import streamlit as st
import pydeck as pdk

# Define the coordinates for the bounding box around Central Park
# Top-left corner (near the Frederick Douglass Circle)
top_left = [-73.958, 40.805]
# Top-right corner (near the Engineer's Gate)
top_right = [-73.949, 40.796]
# Bottom-right corner (near the Grand Army Plaza)
bottom_right = [-73.973, 40.764]
# Bottom-left corner (near Columbus Circle)
bottom_left = [-73.983, 40.768]

# Create a polygon to represent the bounding box
bounding_box = {
    "type": "Polygon",
    "coordinates": [
        [top_left, top_right, bottom_right, bottom_left, top_left]
    ],
}

# Create a PyDeck layer for the bounding box
layer = pdk.Layer(
    "PolygonLayer",
    [bounding_box],
    get_polygon="coordinates",
    get_fill_color=[255, 0, 0, 100],
    get_line_color=[255, 0, 0],
    get_line_width=5,
    pickable=True,
    auto_highlight=True,
)

# Set the view to a location that will include the bounding box (Central Park)
view_state = pdk.ViewState(
    longitude=-73.965,  # Center longitude of Central Park
    latitude=40.782,    # Center latitude of Central Park
    zoom=13,
)

# Render the map with the bounding box
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))
