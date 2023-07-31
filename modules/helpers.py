import streamlit as st


def superscript(st_object, text):
    return st_object.markdown(f"<sup>{text}</sup>", unsafe_allow_html=True)

def subsubheader(st_object, text):
    return st_object.markdown(f"<h4>{text}</h4>", unsafe_allow_html=True)
