import streamlit as st
import pandas as pd
from collections import defaultdict
from helpers.helpers import filter_nested_dict, get_leaf_values, count_leaf_values

col1, col2 = st.columns(2)

option_df = pd.read_excel("data/ResearchProjectSpreadsheet_ReadForm.xlsx", sheet_name="DesignConsiderations")
categories_df = option_df[["Unnamed: 0", "Subcategory"]][3:]
category_dict = defaultdict(dict)
options_dict = defaultdict(dict)
valid_headers = []
col_to_option = {}
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
    """
    This function determines what GI options are available based on the user's input and maniuplates the category_dict/
    col2 options directly.

    :return: Returns nothing. Manipulates the category_dict and col2 options directly.
    :rtype: None
    """
    global category_dict, col2
    valid_options = get_leaf_values(category_dict)
    print(valid_options)
    for option_header in options_dict.keys():
        default_filters = [st.session_state[option_header] != ""]
        st.write(option_header)
        if "Maximum" in option_header:
            try:
                user_value = float(st.session_state[option_header])
            except (ValueError, TypeError) as e:
                print(e)
            else:
                for gi_index, option_max in options_dict[option_header]["options"].items():
                    print(user_value, option_max)
                    option_max = float(option_max)
                    st.write(f"{user_value}, {option_max}")
                    if all([user_value > option_max] + default_filters):
                        valid_options.remove(gi_index)

    # if st.session_state["<h4>Cross-sectional & Side Slope Restrictions</h4>_input"] == "Per Device":
    #     category_dict = filter_nested_dict(category_dict, 25)

    category_dict = filter_nested_dict(category_dict, valid_options)
    with col2:
        st.subheader(f"Possible Green Infrastructure ({count_leaf_values(category_dict)})")
        for major_category in category_dict.keys():
            if len(category_dict[major_category]) > 0:
                sub_dict = category_dict[major_category]
                st.multiselect(major_category, [k for k in sub_dict.keys()], [k for k in sub_dict.keys()])
    # st.write(category_dict)


with col1:
    st.title('Determine GI')
    spreadsheet_t = st.tabs(["Tool Options"])

    for idx, col in enumerate(option_df.columns[2:]):
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
        if len(headers) == 0:
            col_name = valid_headers[-1] + options_text
        else:
            col_name = ''.join(headers + [options_text])
            valid_headers.append(col_name)
        # st.session_state[col_name] = None
        options_dict[f"{col_name}_input"] = {"pd_col_name": col,
                                  "pd_col_idx": idx,
                                  "options": {k + 3: str(v) for k, v in enumerate(option_df[col][3:])}}

        st.write("".join(headers), unsafe_allow_html=True)
        options = list(set([str(v) for v in option_df[col][3:] if str(v) != "nan"]))
        options.insert(0, "")
        options.sort()
        if col_name != '':
            dict_of_vals[f"{col_name}_input"] = st.selectbox(options_text, options, key=f"{col_name}_input")
    st.write(st.session_state)

determine_logic()
