import json

with open("registry/registry.json") as f:
    registry = json.load(f)

user_profile = registry["last_selected_profile"]
try:
    data = json.load(open(user_profile))
except FileNotFoundError:
    data = json.load(open("profiles/Default.json"))
    user_profile = "profiles/Default.json"