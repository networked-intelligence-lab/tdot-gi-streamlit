import streamlit as st


def superscript(st_object, text):
    return st_object.markdown(f"<sup>{text}</sup>", unsafe_allow_html=True)
