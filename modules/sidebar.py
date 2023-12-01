import streamlit as st
import json
from glob import glob
import os
import shutil
from helpers.helpers import update_registry, save_session_state_to_file, dict_equivalent
from helpers.debug import print_dict_differences
from registry.registry import *

def add_scenario():
    new_scenario = f"Scenario {len(st.session_state.scenarios) + 1}"
    st.session_state.scenarios.append(new_scenario)


def remove_scenario():
    global scenario
    # Prevent removing the last scenario if desired
    if len(st.session_state.scenarios) > 1:
        st.session_state.scenarios.remove(scenario)
    else:
        st.warning("You cannot remove the last scenario.")




def build_sidebar():
    with st.sidebar:
        st.subheader("Profiles")
        profile_list = list(glob("profiles/*.json"))
        # move last selected profile to the start of the list
        last_selected_profile = registry["last_selected_profile"]
        try:
            profile_list.remove(last_selected_profile)
            profile_list.insert(0, last_selected_profile)
        except ValueError:
            pass

        user_profile = st.selectbox("Select a profile", profile_list, key="user_profile", label_visibility="collapsed")
        update_registry(registry, "last_selected_profile", user_profile)


        create_col, load_col, save_col, rename_col, delete_col = st.columns(5)
        create_col, load_col, save_col, delete_col = st.columns(4)
        with load_col:
            if st.button("📁", use_container_width=True, help="Load the selected profile"):
                with open(user_profile, "r") as file:
                    session_state_dict = json.load(file)
                    # Delete everything from session state except user_profile
                    for key in list(st.session_state.keys()):
                        if key != "user_profile":
                            del st.session_state[key]
                    st.session_state.update(session_state_dict)
                st.experimental_rerun()

        save_dict = {key: value for key, value in json.load(open(user_profile, "r")).items() if key != "user_profile"}
        current_session_state_dict = {key: value for key, value in st.session_state.items() if key != "user_profile"}
        with save_col:
            debug = False
            if user_profile == "profiles/Default.json" and not debug:
                st.button("💾", use_container_width=True, help="You cannot save to the default profile", type="secondary", disabled=True)
            else:
                if dict_equivalent(save_dict, current_session_state_dict):
                    if st.button("💾", use_container_width=True, help="Save the current session state to the selected profile", type="secondary"):
                        save_session_state_to_file(user_profile)
                else:
                    if st.button("💾", use_container_width=True, help="You have unsaved changes. Save the current session state to the selected profile", type="secondary"):
                        save_session_state_to_file(user_profile)
                    print_dict_differences(save_dict, current_session_state_dict)


        # with rename_col:
        #     if st.button("✏️", use_container_width=True, help="Rename the selected profile"):
        #         pass

        if "create_expander" not in st.session_state:
            st.session_state.create_expander = False

        def toggle_create_expander():
            st.session_state.create_expander = not st.session_state.create_expander
        with create_col:
            if not st.session_state.create_expander:
                st.button("➕", use_container_width=True, help="Create a new profile", type="secondary", on_click=toggle_create_expander)
            else:
                st.button("➕", use_container_width=True, help="Create a new profile", type="primary", on_click=toggle_create_expander)
        if st.session_state.create_expander:
            with st.expander("Create new profile"):
                new_profile_name = st.text_input("Enter new profile name")
                profile_template = st.selectbox("Select a profile template", list(glob("profiles/*.json")))
                if st.button("Create"):
                    with open(f"profiles/{new_profile_name}.json", "w") as f:
                        shutil.copyfile(profile_template, f"profiles/{new_profile_name}.json")
                    user_profile = f"profiles/{new_profile_name}.json"
                    update_registry(registry, "last_selected_profile", user_profile)
                    st.experimental_rerun()

        with delete_col:
            if user_profile != "profiles/Default.json":
                if st.button("🗑️", use_container_width=True, help="Delete the selected profile"):
                    os.remove(user_profile)
                    registry["user_profile"] = glob("profiles/*.json")[0]
                    st.experimental_rerun()
            else:
                st.button("🗑️", use_container_width=True, help="You cannot delete the default profile", disabled=True)

        # st.subheader("Scenarios")
        # if 'scenarios' not in st.session_state:
        #     st.session_state.scenarios = ["Scenario 1"]
        #
        # scenario = st.selectbox('Select a scenario', st.session_state.scenarios)
        #
        # create_scen_col, rename_scen_col, delete_scen_col = st.columns(3)
        # with create_scen_col:
        #     st.button('➕', on_click=add_scenario, use_container_width=True, key="add_scenario", help="Add a new scenario")
        #
        # with rename_scen_col:
        #     st.button('✏️', use_container_width=True, key="rename_scenario", help="Rename the selected scenario")
        #
        # with delete_scen_col:
        #     st.button('🗑️', on_click=remove_scenario, use_container_width=True, key="remove_scenario", help="Delete the selected scenario")