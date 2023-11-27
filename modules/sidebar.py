import streamlit as st
import json
from glob import glob
import os
import shutil
from helpers.helpers import update_registry, save_session_state_to_file, get_location_name, limit_string
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

        with save_col:
            if st.button("💾", use_container_width=True, help="Save the current session state to the selected profile"):
                save_session_state_to_file(user_profile)

        with rename_col:
            if st.button("✏️", use_container_width=True, help="Rename the selected profile"):
                pass

        with create_col:
            if st.button("➕", use_container_width=True, help="Create a new profile"):
                pass

        with delete_col:
            if st.button("🗑️", use_container_width=True, help="Delete the selected profile"):
                pass

        # with st.expander("Create new profile"):
        #     new_profile_name = st.text_input("Enter new profile name")
        #     profile_template = st.selectbox("Select a profile template", ["New"] + list(glob("profiles/*.json")))
        #     if st.button("Create"):
        #         if profile_template == "New":
        #             with open(f"profiles/{new_profile_name}.json", "w") as f:
        #                 json.dump({"app": "ni-gitool"}, f, indent=4)
        #         else:
        #             with open(f"profiles/{new_profile_name}.json", "w") as f:
        #                 shutil.copyfile(profile_template, f"profiles/{new_profile_name}.json")
        #             user_profile = f"profiles/{new_profile_name}.json"
        #             update_registry(registry, "last_selected_profile", user_profile)
        #             st.experimental_rerun()
        #
        # with st.expander("Delete profile"):
        #     selected_profile = st.selectbox("Select a profile to delete", profile_list)
        #     if st.button("Delete"):
        #         os.remove(selected_profile)
        #         profile_list = list(glob("profiles/*.json"))
        #         registry["user_profile"] = glob("profiles/*.json")[0]
        #         st.experimental_rerun()

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
