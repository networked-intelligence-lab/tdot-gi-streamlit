import streamlit as st


def scenario_change():
    print(st.session_state.scenario_picker)
    print(st.session_state.scenario_num)
    st.session_state.scenario_num = st.session_state["scenarios"].index(st.session_state.scenario_picker)