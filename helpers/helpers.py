import geopy.exc
import streamlit as st
import json
from geopy.geocoders import Photon

geolocator = Photon(user_agent="nilab_gitool")

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


def limit_string(s, max_length):
    if len(s) > max_length:
        return s[:max_length - 3] + '...'
    else:
        return s

def get_location_name(lat, lon):
    # Reverse geocoding to get address
    try:
        location = geolocator.reverse(f"{lat}, {lon}", exactly_one=True)
        address = location.address if location else None
    except:
        address = "Geocoder unavailable"
    return address


def find_min_value(lst):
    if not lst:
        return None  # Return None for an empty list

    min_val = float('inf')  # Initialize min_val with positive infinity

    for item in lst:
        if isinstance(item, list):
            # If the item is a list, recursively find the minimum within it
            sublist_min = find_min_value(item)
            if sublist_min is not None:
                min_val = min(min_val, sublist_min)
        elif isinstance(item, (int, float)):
            # If the item is a numeric value, update min_val if it's smaller
            min_val = min(min_val, item)

    if min_val == float('inf'):
        return None  # If no numeric values were found, return None
    else:
        return min_val


def find_max_value(lst):
    if not lst:
        return None  # Return None for an empty list

    max_val = float('-inf')  # Initialize min_val with positive infinity

    for item in lst:
        if isinstance(item, list):
            # If the item is a list, recursively find the minimum within it
            sublist_max = find_max_value(item)
            if sublist_max is not None:
                max_val = max(max_val, sublist_max)
        elif isinstance(item, (int, float)):
            # If the item is a numeric value, update min_val if it's smaller
            max_val = max(max_val, item)

    if max_val == float('-inf'):
        return None  # If no numeric values were found, return None
    else:
        return max_val


def dict_equivalent(dict1, dict2, tolerance=1e-6, ignore_keys=[]):
    for key in set(dict1.keys()).union(dict2.keys()):
        if key in ignore_keys:
            continue  # Skip the keys specified in the ignore_keys list

        if key in dict1 and key in dict2:
            if isinstance(dict1[key], float) and isinstance(dict2[key], float):
                if not (abs(dict1[key] - dict2[key]) < tolerance):
                    return False  # Floating-point values differ more than the tolerance
            elif dict1[key] != dict2[key]:
                return False  # Non-floating-point values differ
        elif key in dict1 or key in dict2:
            return False  # Key is missing in one of the dictionaries and it's not in ignore list

    return True


def save_session_state_to_file(filename):
    session_state_dict = {k: v for k, v in st.session_state.items() if "_profile" not in k}
    for k, v in session_state_dict.items():
        print(k, type(v))
    with open(filename, "w") as file:
        json.dump(session_state_dict, file, indent=4)




