import streamlit as st
import pandas as pd
from collections import defaultdict
from helpers.helpers import filter_nested_dict, get_leaf_values, count_leaf_values, is_float, get_location_name, limit_string


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


def add_scenario():
    new_scenario = f"Scenario {len(st.session_state.scenarios) + 1}"
    st.session_state.scenarios.append(new_scenario)


def remove_scenario():
    # Prevent removing the last scenario if desired
    if len(st.session_state.scenarios) > 1:
        st.session_state.scenarios.remove(scenario)
    else:
        st.warning("You cannot remove the last scenario.")


def determine_logic():
    """
    This function determines what GI options are available based on the user's input and maniuplates the category_dict/
    col2 options directly.

    :return: Returns nothing. Manipulates the category_dict and col2 options directly.
    :rtype: None
    """
    global category_dict, col2
    valid_options = get_leaf_values(category_dict)
    # print(_type)
    for option_header in options_dict.keys():
        _type = st.session_state[f"{option_header.replace('_input', '')}_type"]
        print(_type)
        if _type != '':
            option_session_key = f"{option_header}@{_type}"
        else:
            option_session_key = option_header
        default_filters = [st.session_state[option_session_key] != ""]
        st.write(option_header)
        if "Max" in option_header:
            if _type == "Numeric":
                try:
                    user_value = float(st.session_state[option_session_key])
                except (ValueError, TypeError) as e:
                    pass
                else:
                    for gi_index, option_max in options_dict[option_header]["options"].items():
                        try:
                            option_max = float(option_max)
                        except (ValueError, TypeError):
                            try:
                                valid_options.remove(gi_index)
                            except ValueError:
                                pass
                        else:
                            st.write(f"{user_value}, {option_max}")
                            if all([user_value > option_max] + default_filters):
                                try:
                                    valid_options.remove(gi_index)
                                except ValueError:
                                    pass
            else:
                for gi_index, option_max in options_dict[option_header]["options"].items():
                    if all([st.session_state[option_session_key] > option_max] + default_filters):
                        try:
                            valid_options.remove(gi_index)
                        except ValueError:
                            pass

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
    if 'scenarios' not in st.session_state:
        st.session_state.scenarios = ["Scenario 1"]

    # Select box for displaying scenarios
    scenario = st.selectbox('Select a scenario', st.session_state.scenarios)

    add_col, remove_col = st.columns(2)
    with add_col:
        st.button('Add Scenario', on_click=add_scenario, use_container_width=True)

    with remove_col:
        st.button('Remove Scenario', on_click=remove_scenario, use_container_width=True)


    # You can display the selected scenario or do further processing
    st.write(f"You have selected: {scenario}")

    if "locations" not in st.session_state:
        st.error("""Locations not found! Please go back to the home page, under *Configuration* and 
        ensure that location is set.""")
    else:
        st.selectbox("Location", [f"1: {limit_string(get_location_name(v[0], v[1]), 40)} @ {v}" for v in st.session_state.locations.values()])


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

        types_of_options = []
        for option in options:
            option = option.strip()
            if is_float(option):
                types_of_options.append("Numeric")
            elif ":" in option:
                types_of_options.append("Ratio")
            elif any(["Range" in option, '-' in option]):
                types_of_options.append("Range")
            elif all([str(option) != 'nan', option != ""]):
                print(option)
                types_of_options.append("Other")
        types_of_options = list(set(types_of_options))
        options.insert(0, "")
        options.sort()
        # print(col_name, types_of_options)
        if len(types_of_options) > 1:
            type_col, opt_col = st.columns(2)
            # st.session_state[f"{col_name}_type"] = types_of_options[0]
            with type_col:
                types_of_options.sort()
                dict_of_vals[f"{col_name}_type"] = st.selectbox("Type", types_of_options, key=f"{col_name}_type")

            with opt_col:
                _type = st.session_state[f"{col_name}_type"]
                if st.session_state[f"{col_name}_type"] == "Range":
                    st.selectbox("Range", [o for o in options if any(["Range" in o, "-" in o, o == ''])], key=f"{col_name}_input@{_type}")
                elif st.session_state[f"{col_name}_type"] == "Ratio":
                    st.selectbox(options_text, [o for o in options if any([":" in o, o == ''])], key=f"{col_name}_input@{_type}")
                elif st.session_state[f"{col_name}_type"] == "Numeric":
                    st.selectbox(options_text, [o for o in options if any([is_float(o), o == ''])], key=f"{col_name}_input@{_type}")
                elif st.session_state[f"{col_name}_type"] == "Other":
                    st.selectbox(options_text,
                                 [o for o in options if not any(["Range" in o, "-" in o,
                                                                 ":" in o,
                                                                 o.isnumeric()])],
                                 key=f"{col_name}_input@{_type}")
        else:
            st.session_state[f"{col_name}_type"] = ''
            if col_name != '':
                dict_of_vals[f"{col_name}_input"] = st.selectbox(options_text, options, key=f"{col_name}_input")
    st.write(st.session_state)

determine_logic()