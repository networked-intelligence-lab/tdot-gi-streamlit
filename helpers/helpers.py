import streamlit as st
import json



def update_registry(registry, key, value):
    registry[key] = value
    with open("registry/registry.json", "w") as f:
        json.dump(registry, f)
