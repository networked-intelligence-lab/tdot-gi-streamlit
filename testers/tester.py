import streamlit as st

st.text_input("test", key="test", value="test")
print(st.session_state["test"])