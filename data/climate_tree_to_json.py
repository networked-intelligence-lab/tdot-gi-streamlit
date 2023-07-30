import pandas as pd
from collections import defaultdict
import json

nested_dict = lambda: defaultdict(nested_dict)
climate_dict = nested_dict()
ai_df = pd.read_excel("climate_tree_annual_interception.xlsx")
pu_df = pd.read_excel("climate_tree_pollutant_uptake.xlsx")
es_df = pd.read_excel("climate_tree_energy_saved.xlsx")

climate_list = ai_df["Climate Zones"].unique().tolist()

for idx, row in ai_df.iterrows():
    climate_dict[row["Climate Zones"]]["Annual Interception"]["Small Tree"] = row["Small Tree"]
    climate_dict[row["Climate Zones"]]["Annual Interception"]["Medium Tree"] = row["Medium Tree"]
    climate_dict[row["Climate Zones"]]["Annual Interception"]["Large Tree"] = row["Large Tree"]

for idx, row in pu_df.iterrows():
    climate_dict[row["Climate Zones"]]["Pollutant Uptake"][row["Pollutant"]]["Small Tree"] = row["Small Tree"]
    climate_dict[row["Climate Zones"]]["Pollutant Uptake"][row["Pollutant"]]["Medium Tree"] = row["Medium Tree"]
    climate_dict[row["Climate Zones"]]["Pollutant Uptake"][row["Pollutant"]]["Large Tree"] = row["Large Tree"]

for idx, row in es_df.iterrows():
    climate_dict[row["Climate Zones"]]["Energy Saved"]["Small Tree"] = row["Small Tree"]
    climate_dict[row["Climate Zones"]]["Energy Saved"]["Medium Tree"] = row["Medium Tree"]
    climate_dict[row["Climate Zones"]]["Energy Saved"]["Large Tree"] = row["Large Tree"]

with open("climate_tree.json", "w") as f:
    json.dump(climate_dict, f, indent=4)
