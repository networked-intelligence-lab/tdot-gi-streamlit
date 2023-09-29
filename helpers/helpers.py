import streamlit as st
import json


def update_registry(registry, key, value):
    registry[key] = value
    with open("registry/registry.json", "w") as f:
        json.dump(registry, f)


def filter_nested_dict(d, values_to_keep):
    if isinstance(d, dict):
        return {
            key: filter_nested_dict(value, values_to_keep)
            for key, value in d.items()
            if filter_nested_dict(value, values_to_keep)
        }
    else:
        return d if d in values_to_keep else None


def get_leaf_values(d):
    if isinstance(d, dict):
        values = []
        for key, value in d.items():
            values.extend(get_leaf_values(value))
        return values
    else:
        return [d]


def count_leaf_values(d):
    if isinstance(d, dict):
        count = 0
        for key, value in d.items():
            count += count_leaf_values(value)
        return count
    else:
        return 1

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False