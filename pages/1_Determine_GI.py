import streamlit as st
import pandas as pd
from collections import defaultdict
from helpers.helpers import filter_nested_dict

col1, col2 = st.columns(2)

option_df = pd.read_excel("data/ResearchProjectSpreadsheet.xlsx", sheet_name="DesignConsiderations")
categories_df = option_df[["Unnamed: 0", "Subcategory"]][3:]
category_dict = defaultdict(dict)
curr_category = None
dict_of_vals = {}
for index, row in categories_df.iterrows():
    category = row["Unnamed: 0"]
    subcategory = row["Subcategory"]
    if category != curr_category and str(category) != "nan":
        curr_category = category

    if str(subcategory) != "nan":
        category_dict[curr_category][subcategory] = index
    else:
        category_dict[curr_category][category] = index

def determine_logic():
    global category_dict, col2
    if st.session_state["<h4>Cross-sectional & Side Slope Restrictions</h4>_input"] == "Per Device":
        category_dict = filter_nested_dict(category_dict, 25)
    with col2:
        st.subheader("Possible Green Infrastructure")
        for major_category in category_dict.keys():
            if len(category_dict[major_category]) > 0:
                sub_dict = category_dict[major_category]
                st.multiselect(major_category, [k for k in sub_dict.keys()], [k for k in sub_dict.keys()])
    st.write(category_dict)


with col1:
    st.title('Determine GI')
    spreadsheet_t = st.tabs(["Tool Options"])
    for col in option_df.columns[2:]:
        col_header = [v for v in option_df[col][:3] if str(v) != "nan"]
        headers = []
        for idx in range(3, -1, -1):
            h_val = idx + 4
            try:
                headers.append(f'<h{h_val}>{col_header[idx]}</h{h_val}>')
            except IndexError:
                pass
        headers.reverse()
        options_text = headers.pop().split(">")[1].split("<")[0]

        st.write("".join(headers), unsafe_allow_html=True)
        options = list(set([str(v) for v in option_df[col][3:] if str(v) != "nan"]))
        options.insert(0, "")
        options.sort()
        col_name = ''.join(headers)
        if col_name != '':
            dict_of_vals[f"{col_name}_input"] = st.selectbox(options_text, options, key=f"{col_name}_input")
    st.write(dict_of_vals)

determine_logic()
# categories_df = option_df[["Unnamed: 0", "Subcategory"]][3:]
#
# category_dict = defaultdict(dict)
# curr_category = None
# for index, row in categories_df.iterrows():
#     category = row["Unnamed: 0"]
#     subcategory = row["Subcategory"]
#     if category != curr_category and str(category) != "nan":
#         curr_category = category
#
#     if str(subcategory) != "nan":
#         category_dict[curr_category][subcategory] = index
#     else:
#         category_dict[curr_category][category] = index
#
# major_category = st.selectbox("Major Category", [k for k in category_dict.keys()])
# sub_dict = category_dict[major_category]
# subcategory = st.selectbox("Subcategory", [k for k in sub_dict.keys()])
#
# for col in option_df.columns[2:]:
#     col_header = [v for v in option_df[col][:3] if str(v) != "nan"]
#     headers = []
#     for idx in range(3, -1, -1):
#         h_val = idx + 2
#         try:
#             headers.append(f'<h{h_val}>{col_header[idx]}</h{h_val}>')
#         except IndexError:
#             pass
#     headers.reverse()
#
#     st.write("".join(headers), unsafe_allow_html=True)
#     st.markdown(f"<p>{option_df[col][category_dict[major_category][subcategory]]}</p>", unsafe_allow_html=True)
