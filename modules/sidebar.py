import streamlit as st
import json
from glob import glob
import os
import shutil
from helpers.helpers import update_registry, save_session_state_to_file
from registry.registry import *

def build_sidebar():
    with st.sidebar:
        st.title("Profile")
        profile_list = list(glob("profiles/*.json"))
        # move last selected profile to the start of the list
        last_selected_profile = registry["last_selected_profile"]
        try:
            profile_list.remove(last_selected_profile)
            profile_list.insert(0, last_selected_profile)
        except ValueError:
            pass

        user_profile = st.selectbox("Select a profile", profile_list, key="user_profile")
        update_registry(registry, "last_selected_profile", user_profile)

        # Load session state from file
        if st.button("Load Session State"):
            with open(user_profile, "r") as file:
                session_state_dict = json.load(file)
                # Delete everything from session state except user_profile
                for key in list(st.session_state.keys()):
                    if key != "user_profile":
                        del st.session_state[key]
                st.session_state.update(session_state_dict)
            st.experimental_rerun()

        with st.expander("Create new profile"):
            new_profile_name = st.text_input("Enter new profile name")
            profile_template = st.selectbox("Select a profile template", ["New"] + list(glob("profiles/*.json")))
            if st.button("Create"):
                if profile_template == "New":
                    with open(f"profiles/{new_profile_name}.json", "w") as f:
                        json.dump({"app": "ni-gitool"}, f, indent=4)
                else:
                    with open(f"profiles/{new_profile_name}.json", "w") as f:
                        shutil.copyfile(profile_template, f"profiles/{new_profile_name}.json")
                    user_profile = f"profiles/{new_profile_name}.json"
                    update_registry(registry, "last_selected_profile", user_profile)
                    st.experimental_rerun()

        with st.expander("Delete profile"):
            selected_profile = st.selectbox("Select a profile to delete", profile_list)
            if st.button("Delete"):
                os.remove(selected_profile)
                profile_list = list(glob("profiles/*.json"))
                registry["user_profile"] = glob("profiles/*.json")[0]
                st.experimental_rerun()

        st.write(f"Selected profile: {user_profile}")
        # Function to save session state to a JSON file

        # Button to save session state
        if st.button("Save Session State"):
            save_session_state_to_file(user_profile)
            st.success("Session state saved to file")