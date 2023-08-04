import streamlit as st
import pandas as pd
from collections import defaultdict

st.title('Research Spreadsheet')
spreadsheet_t = st.tabs(["Spreadsheet Tool"])

option_df = pd.read_excel("data/ResearchProjectSpreadsheet.xlsx", sheet_name="DesignConsiderations")
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
    st.selectbox(options_text, options)

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
