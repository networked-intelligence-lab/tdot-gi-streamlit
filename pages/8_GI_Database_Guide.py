import streamlit as st
import base64

# Opening file from file path
with open("data/GI Repository-Database Description.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

# Embedding PDF in HTML
pdf_display =  f"""<embed
class="pdfobject"
type="application/pdf"
title="Embedded PDF"
src="data:application/pdf;base64,{base64_pdf}"
style="overflow: auto; width: 100%; height: 100%;">"""

# Displaying File
st.markdown(pdf_display, unsafe_allow_html=True)