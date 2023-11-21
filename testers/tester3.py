import streamlit as st

# Initialize a default value in session state if not present
if 'value' not in st.session_state:
    st.session_state['value'] = 0

# Function to update the value in session state
def update_value(key, value):
    st.session_state[key] = value

# Create a number input and slider
number_input = st.number_input("Number Input", value=st.session_state['value'], on_change=update_value, args=('value', number_input))
slider_input = st.slider("Slider Input", min_value=0, max_value=100, value=st.session_state['value'], on_change=update_value, args=('value', slider_input))

# Display the current value
st.write(f"Current Value: {st.session_state['value']}")
