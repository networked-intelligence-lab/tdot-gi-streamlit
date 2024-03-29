import streamlit as st
import pandas as pd
from collections import defaultdict
from helpers.helpers import filter_nested_dict, get_leaf_values, count_leaf_values, is_float, find_max_value, find_min_value
import re
from streamlit_extras.app_logo import add_logo
from modules.sidebar import build_sidebar

build_sidebar()
add_logo("media/logo.png", height=150)

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


def numeric_parser(value):
    if pd.isnull(value):
        return None
    if isinstance(value, (int, float)):
        return value  # Return numeric values as-is

    try:
        value = float(value)
        return value  # Return numeric values as-is
    except ValueError:
        pass

    value = str(value).strip()

    # Check for "<number" pattern (e.g., "<1")
    if value.startswith('<'):
        try:
            return [0, float(value[1:])]
        except ValueError:
            return None  # In case of invalid format

    # Check for "Range xx-yy%" pattern (e.g., "Range 10-20%")
    if value.lower().startswith('range'):
        numbers = re.findall(r'\d+', value)
        try:
            return [float(numbers[0])/100, float(numbers[1])/100]
        except (ValueError, IndexError):
            return None  # In case of invalid format

    # Check for ratio pattern (e.g., "3:1")
    if ':' in value:
        numbers = value.split(':')
        try:
            return float(numbers[0]) / float(numbers[1])
        except (ValueError, ZeroDivisionError):
            return None  # In case of invalid ratio

    # Check for percentage pattern (e.g., "20%")
    if '%' in value:
        try:
            return float(value[:-1]) / 100
        except ValueError:
            return None  # In case of invalid percentage

    # Check for range pattern (e.g., "xx - yy")
    if '-' in value:
        numbers = re.findall(r'\d+', value)
        try:
            return [float(num) for num in numbers]
        except ValueError:
            return None  # In case of invalid range

    # Default case if no pattern matched
    return None

# Example usage with a DataFrame column
# Replace 'column_name' with the actual name of the column
# data['column_name'] = data['column_name'].apply(numeric_parser)


def determine_logic():
    """
    This function determines what GI options are available based on the user's input and maniuplates the category_dict/
    col2 options directly.

    :return: Returns nothing. Manipulates the category_dict and col2 options directly.
    :rtype: None
    """
    global category_dict, col2
    valid_options = get_leaf_values(category_dict)
    # 
    for option_header in options_dict.keys():
        _type = st.session_state[f"{option_header.replace('_input', '')}_type"]
        
        if _type != '':
            option_session_key = f"{option_header}@{_type}"
        else:
            option_session_key = option_header

        try:
            default_filters = [st.session_state[option_session_key] != ""]
        except KeyError:
            continue

        if any(["min" in option_header.lower(), "max" in option_header.lower()]):
            if _type == "Do not filter":
                pass
            elif _type == "Numeric":
                try:
                    user_value = float(st.session_state[option_session_key])
                except (ValueError, TypeError) as e:
                    pass
                else:
                    for gi_index, option_val in options_dict[option_header]["options"].items():
                        if type(option_val) == list:
                            if "min" in option_header.lower():
                                option_val = option_val[0]
                            elif "max" in option_header.lower():
                                option_val = option_val[1]
                        try:
                            option_val = float(option_val)
                        except (ValueError, TypeError):
                            try:
                                valid_options.remove(gi_index)
                            except ValueError:
                                pass
                        else:
                            if "max" in option_header.lower():
                                if all([user_value > option_val] + default_filters):
                                    try:
                                        valid_options.remove(gi_index)
                                    except ValueError:
                                        pass
                            elif "min" in option_header.lower():
                                if all([user_value < option_val] + default_filters):
                                    try:
                                        valid_options.remove(gi_index)
                                    except ValueError:
                                        pass
            else:
                for gi_index, option_val in options_dict[option_header]["options"].items():
                    if all([st.session_state[option_session_key] > option_val] + default_filters):
                        try:
                            valid_options.remove(gi_index)
                        except ValueError:
                            pass


    category_dict = filter_nested_dict(category_dict, valid_options)
    with col2:
        st.subheader(f"Possible Green Infrastructure ({count_leaf_values(category_dict)})")
        filtered_gi_dict = {}
        for major_category in category_dict.keys():
            if len(category_dict[major_category]) > 0:
                sub_dict = category_dict[major_category]
                st.multiselect(major_category, [k for k in sub_dict.keys()], [k for k in sub_dict.keys()])
                filtered_gi_dict[major_category] = [k for k in sub_dict.keys()]

        st.session_state["determine_gi_output"] = filtered_gi_dict
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

        # Start to write the session states for all inputs
        if f"{col_name}_type" not in st.session_state:
            st.session_state[f"{col_name}_type"] = 'Do not filter'

        types_of_options = ["Do not filter"]
        for option in options:
            option = option.strip()
            if is_float(option):
                types_of_options.append("Numeric")
            elif ":" in option:
                types_of_options.append("Ratio")
            elif any(["Range" in option, '-' in option]):
                types_of_options.append("Range")
            elif all([str(option) != 'nan', option != ""]):
                
                types_of_options.append("Other")
        types_of_options = list(set(types_of_options))
        options.insert(0, "")
        options.sort()
        # 
        if len(types_of_options) > 1:
            type_col, opt_col = st.columns(2)
            # st.session_state[f"{col_name}_type"] = types_of_options[0]
            with type_col:
                types_of_options.sort()
                # if not st.session_state[f"{col_name}_type"]:
                #     dict_of_vals[f"{col_name}_type"] = st.selectbox(options_text, types_of_options, key=f"{col_name}_type")
                # else:
                #     st.selectbox(options_text, types_of_options, key=f"{col_name}_type")

                # Set the session state for the type of input
                sel_type = st.selectbox(options_text, types_of_options,
                                 index=types_of_options.index(st.session_state[f"{col_name}_type"]),
                                        key=f"_{col_name}_type")
                st.session_state[f"{col_name}_type"] = sel_type



                # Initialize the session state for each input type
                if f"{col_name}_input" not in st.session_state:
                    for _type in types_of_options:
                        st.session_state[f"{col_name}_input"] = True
                        st.session_state[f"{col_name}_input@{_type}"] = None

            with opt_col:
                _type = st.session_state[f"{col_name}_type"]
                if st.session_state[f"{col_name}_type"] == "Do not filter":
                    sel_val = None
                elif st.session_state[f"{col_name}_type"] == "Range":
                    sel_val = st.selectbox("Range", [o for o in options if any(["Range" in o, "-" in o, o == ''])], key=f"_{col_name}_input@Range")
                elif st.session_state[f"{col_name}_type"] == "Ratio":
                    sel_val = st.selectbox(options_text, [o for o in options if any([":" in o, o == ''])], label_visibility='hidden', key=f"_{col_name}_input@Ratio")
                elif st.session_state[f"{col_name}_type"] == "Numeric":
                    numeric_options = [numeric_parser(o) for o in options if numeric_parser(o) is not None]
                    min_val, max_val = find_min_value(numeric_options), find_max_value(numeric_options)
                    if min_val == max_val:
                        st.warning(f"Only one value: {min_val}")
                        sel_val = min_val
                    else:
                        if st.session_state[f"{col_name}_input@{_type}"] is None:
                            st.session_state[f"{col_name}_input@{_type}"] = min_val
                        # sel_val = st.slider(options_text, min_value=float(find_min_value(numeric_options)), max_value=float(find_max_value(numeric_options)), key=f"_{col_name}_input@Numeric",
                        #                     value=float(st.session_state[f"{col_name}_input@{_type}"]), label_visibility='hidden')
                        sel_val = st.number_input(options_text, min_value=float(find_min_value(numeric_options)), max_value=float(find_max_value(numeric_options)), value=float(st.session_state[f"{col_name}_input@{_type}"]), key=f"_{col_name}_input@Numeric")
                    # st.selectbox(options_text, , key=f"{col_name}_input@{_type}")

                elif st.session_state[f"{col_name}_type"] == "Other":
                    st.selectbox(options_text,
                                 [o for o in options if not any(["Range" in o, "-" in o,
                                                                 ":" in o,
                                                                 o.isnumeric()])],
                                 key=f"_{col_name}_input@{_type}")
                st.session_state[f"{col_name}_input@{_type}"] = sel_val
        else:
            st.session_state[f"{col_name}_type"] = ''
            if col_name != '':
                dict_of_vals[f"{col_name}_input"] = st.selectbox(options_text, options, key=f"_{col_name}_input")
determine_logic()
