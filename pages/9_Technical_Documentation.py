import streamlit as st
from modules.helpers import subsubheader
from streamlit_extras.app_logo import add_logo
import json

add_logo("media/logo.png", height=150)

st.title('Documentation')
st.subheader('Technical Documentation')
st.write('This documentation is intended for the technical user. It provides a detailed description of the methods used to develop the tool and the data sources used to populate the tool. The documentation is divided into the following sections:')
st.markdown('''
1. Introduction
2. Data Sources
3. Data Processing
4. Code Structure''')

subsubheader(st, 'Introduction')
st.write('The tool is developed using Python and the Streamlit library. The tool is developed primarily through the following libraries:')
st.markdown('''
1. Streamlit
2. Pandas
3. streamlit-extras
4. googlemaps (Python library)
5. geopy
''')

subsubheader(st, 'Data Sources')
st.write('The tool uses the following data sources:')
st.markdown('''
1. In-house Research Spreadsheet
    - Containing information such as site requirements, subgrade requirements, etc. for each green infrastructure.
2. Google Places API for maps/parks location searching
    - Allows us to calculate other nearby green infrastructure such as local parks and other landmarks of interest
3. STRATUM Climate Zone GIS Shape files for STRATUM climate determination
    - Allows us to accommodate user climate zone based on GPS locations automatically
4. Collated equations data from research
    - For calculations such as total stormwater runoff, etc.
''')

subsubheader(st, 'Data Processing')
st.markdown("""
##### Overview
External data processing is handled mostly by both Pandas and JSON libraries for local files, and the Google Maps API 
for places data found in the social impact module to determine nearby parks. Internal data processing, such as user
input (e.g., numeric input for "number of trees" in the environmental impact module) is handled by storing the data in 
Streamlit session state, and either making calculations using locally defined variables or variables found in session 
state. 

##### External Data Processing
###### Local
Referring to the two example snippets below:
""")
st.code('option_df = pd.read_excel("data/ResearchProjectSpreadsheet_ReadForm.xlsx", sheet_name="DesignConsiderations")')
st.code("""
climate_zones_data = json.load(open("data/climate_tree.json"))

# Initialize air pollutant session states
if any([f"{pollutant}_acp" not in st.session_state for pollutant in climate_zones_data[list(climate_zones_data.keys())[0]]["Pollutant Uptake"].keys()]):
    st.session_state["O3_acp"] = 3.34
    st.session_state["NO2_acp"] = 3.34
    st.session_state["SO2_acp"] = 2.06
    st.session_state["PM10_acp"] = 2.84
""")
st.markdown("""...we can see that external data is handled as standard Pandas dataframes and JSON objects. These local 
files are then usually further processed into various lists and dictionary objects for more straightfoward logic.

###### Google Maps API
Referring to the example snippet below:
""")
st.code("""

nearby_result = gmaps.places_nearby(
    location=user_loc,
    radius=st.session_state["radius_input"] * 1609.344,
    keyword="park")

pp = pprint.PrettyPrinter(indent=1)
parks_list = []
loc_df_list = []
for place_result in nearby_result["results"]:
    place_loc = (place_result["geometry"]["location"]["lat"], place_result["geometry"]["location"]["lng"])
    loc_df_list.append({"lat": place_loc[0], "lon": place_loc[1], "color": "#0000FF90"})
    parks_list.append({"Distance Away (straight-line; in miles)": geopy.distance.distance(user_loc, place_loc).miles, "Park Name": place_result["name"]})
""")
st.markdown("""...we can see that the Google Maps API is used to determine nearby parks. Like most other APIs, 
the Google Maps API returns a JSON object, which is then further processed into a list of dictionaries to be 
further processed as a Pandas dataframe (using `pd.DataFrame.from_dict()`).

##### Internal Data Processing
In almost all cases, internal data processing is handled by storing the data in Streamlit session state, and either
making calculations using locally defined variables or variables found in session state. For more detailed 
information on how session state works, please refer to the 
[Streamlit documentation](https://docs.streamlit.io/en/stable/api.html#streamlit.session_state).

###### Common session state syntax
Due to how commonly the session state syntax is used for almost all variables of the tool, a simple example of the 
syntax is provided here. Note that the session state may simply be thought of as a dictionary of variables (with 
a few caveats in terms of problems such as mutual exclusivity during update of variables). 

Refer to the example snippets below for instantiation and update of session state variables, which shares most 
of the same syntax as a standard Python dictionary:""")
st.code("""
# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'

# Update
st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API
""")

st.markdown("""
###### The case for session state
Session state is heavily employed throughout the entire tool, as it is the only way to maintain user input across
multiple pages. Additionally, it provides an easy way to save all user input into a locally defined JSON file, which
we use extensively in order to load and save "profiles" of user input that we use to compare during the 
Quantify Benefits portion of the tool. As such, profile files are just "flat" JSON files that contain a dictionary of
all variables stored in session state.

Below, you can see what a profile file internals looks like, which are a straight JSON dump from the session state:""")
st.code("""
{
    "<h4>Cost Considerations</h4><h5>Installation Cost Range</h5>LowUnit_input": true,
    "<h4>Maintenance Cost Range</h4>LowHigh_input": true,
    "<h4>Environmental Benefits</h4>Total Suspended Solids (TSS) (%; Minimum required)Organism removal (%; Minimum required)_input": true,
    "use_bioretention": false,
    "lb_reduc_per_pollutant": {
        "O3": 0.0,
        "NO2": 0.0,
        "SO2": 0.0,
        "PM10": 0.0
    },
    "<h4>Distance to High Water Table</h4>Minimum (ft.)_type": "Do not filter",
    "<h4>Cross-sectional & Side Slope Restrictions</h4>Maximum_input@Ratio": null,
    "<h4>Subgrade Requirements</h4><h5>Soil Infiltration Rate</h5>Minimum (in. per hour)_input@Do not filter": null,
    "<h4>Cost Considerations</h4><h5>Installation Cost Range</h5>Low_input": true,
    "<h4>Site Requirements</h4><h5>Site Slope Restrictions</h5>Maximum_type": "Do not filter",
    "<h4>Distance from Drinking Wells</h4>Minimum (ft.)_input@Range": null,
    "<h4>Cost Considerations</h4><h5>Installation Cost Range</h5>Low_type": "Do not filter",
    "use_cisterns": false,
    ...
}""")


subsubheader(st, 'Code Structure')
st.markdown("""
##### Overview
The code is structured into the following files:
1. `./Home.py`: The main Home file that runs the Streamlit app.
2. `./pages/*.py`: The rest of the pages that are imported into the Streamlit page. This follows regular Streamlit convention 
of putting all subpages into a `pages` folder.
    - Notably, there are a few further dependencies for these subpages:
        1. `./pages/1_Determine_GI.py` dynamically creates selection and numeric input boxes from the data in 
        `./data/ResearchProjectSpreadsheet_ReadForm.xlsx`. As such, unlike other pages, none of the inputs seem 
        to be hard-coded into the script.
        2. `./pages/2_Economic_Impact.py` heavily relies on function definitions found under `./pages/ct_scripts/*.py`, 
        and contains its own `__init__.py` file to allow for relative imports into the main `2_Economic_Impact.py` file.
        3. `./pages/3_Environmental_Impact.py` gathers important climate data from `./data/Environmental_Impact_Data.csv`
3. `./helpers/*.py`: Contains helper functions that are used across multiple pages. This includes functions such as
`subsubheader` and `add_logo`.
4. `./modules/*.py`: Contains modules that are used across multiple pages. These distinguish themselves from helper
functions in that they generally contribute to whole functionalities rather than helpers towards a specific function.

##### Page Structure
Page structure follows normal Streamlit convention, with a Home page in the "root" folder while all other subpages 
defined in a `pages` folder. Notably, much of the functionality that is shared across multiple pages (such as 
the sidebar-definition for selection, loading, and saving of profiles) are handled by functions found within places 
like `./modules/sidebar.py`. These functions are then called within every single page/subpage as required. For example, 
since generally there would be no more need to define profiles in the Quantify Benefits page, due to the assumption
that the user would have already defined and filled out profiles in the previous pages, the Quantify Benefits page does 
not call the `build_sidebar` function and therefore does not contain the profile-building portion of the sidebar.

Commonly called per-page functions may be found at the top of each script, which may handle things such as
1. Adding a logo to the page
2. Adding a profile section to the sidebar
3. Defining the "wide" page layout (as Streamlit defaults to a narrow page layout)

###### Page File Name Convention
The page file names are numbered based on the order in of which we would like them to appear in the Streamlit app.

##### Helper and Module Structure
Helper and module structure is fairly straightforward, with helper functions being defined in `./helpers/*.py` and
modules being defined in `./modules/*.py`. For simplicity, no functions are defined within classes as in typical 
object-oriented programming, and all functions are defined as standalone functions. This is due to the fact that
Streamlit is not designed to be object-oriented, and as such, it is easier to simply define all functions as standalone
functions. Additionally, to circumvent potential issues in complicating objects as they are passed around through 
Streamlit (especially quirks within session state, which as aforementioned this app heavily relies on), we had simply 
decided to avoid defining complicated objects altogether.

###### Differences between Helpers and Modules
The main difference between helpers and modules is that helpers are generally functions that may contribute to a 
specific function, while modules are generally functions that contribute to a whole functionality. For example, helpers 
contain these functions to help narrow down tree values based on user input within the Determine GI page:
""")

st.code("""
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
""")
st.markdown("""
Meanwhile, modules contain code to build out a whole functionality, such as the following code to build out the
sidebar for profiles functionality:
""")
st.code("""
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
                    ...
                ...
        ...
    ...
""")

st.markdown("""
##### Notable Pages
###### 1. Determine GI

It is important to note that the Determine GI page is the only page that dynamically creates selection and numeric
input boxes from the data in `./data/ResearchProjectSpreadsheet_ReadForm.xlsx`. As such, unlike other pages, none of
the inputs seem to be hard-coded into the script. For example, the following code reads each column & row pair
from the spreadsheet:
""")
st.code("""
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
        ...
    ...
...
""")
st.markdown("""
Then, logic for each of the inputs are defined within a dedicated function, which may then call on helper functions
found in `./helpers/*.py` to help narrow down the options for the input.""")
st.code("""
def determine_logic():
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
                    ...
                ...
            ...
        ...
    ...
""")
st.markdown("""
###### 2. Economic Impact
The Economic Impact page is the only page that uses subpage imports from `./pages/ct_scripts/*.py`. This was due to the
sheer amount of code required to build out the page every single GI option. As such, each tab is defined on a separate
script, each containing a function that builds out the tab. For example, here is the code for the *Cisterns* tab:""")
st.code("""
def cisterns_tab(tab_object):
    ...
    def toggle_cisterns():
        st.session_state["use_cisterns"] = not st.session_state["use_cisterns"]

    use_cisterns = tab_object.checkbox("Use Cisterns", value=st.session_state["use_cisterns"], on_change=toggle_cisterns)
    if use_cisterns:
        tab_object.subheader("Capital Cost")
        impervious_area = tab_object.number_input("Impervious Area (ft^2)", value=st.session_state['cisterns_impervious_area'])
        st.session_state['cisterns_impervious_area'] = impervious_area
    ...
    return tab_object""")
st.markdown("""Keep in mind that the `tab_object` is a passed in `st` object, which in this case is an `st.tab` object. 
However, the `tab_object` can really be any Streamlit container-like object, such as `st.sidebar` or `st.form`.""")

st.markdown("""
###### 3. Quantify Benefits
While the Quantify Benefits script may seem the shortest, it is actually the most complex. Most of the script logic
is found within the separate `./modules/simulation.py` script, which contains the lenghty `handle_simulations()` function which 
handles the lengthy pairwise Monte Carlo simulation. Then, any output that is generated from the simulation is
written into the passed in `st` object (named `tab_object`) similar to Economic Impact. 

As such, most of the code within Quantify Benefits only defines the compare side-by-side functionality within the page.

Below is part of the code for handle_simulations():""")
st.code("""
def handle_simulations(profiles, tab_object):
    social_df = pd.read_excel('data/social_criteria.xlsx').dropna()
    env_criteria = pd.read_excel('data/env_cri.xlsx', sheet_name="Form Responses 1").dropna()
    level_one_df = pd.read_excel('data/lvl1_cri_pairwise.xlsx')

    econ_data = []
    env_data = []
    current_session_state = st.session_state
    for idx, profile in enumerate(profiles):
        with open(profile, "r") as f:
            loaded_profile = json.load(f)
            # st.session_state.update(json.load(f))

            for key in list(st.session_state.keys()):
    ...
    local_vars = []
    for matrix in data_matrices:
        pairwise_mat = np.zeros(matrix.shape)
        for col_idx in range(matrix.shape[1]):
            col = matrix[:, col_idx]
            min_val = col.min()
            range_val = (matrix[:, col_idx].max() - min_val) / matrix.shape[0]

            # Check if range_val is zero to avoid division by zero
            if range_val != 0:
                pairwise_mat[:, col_idx] = 1 + (matrix[:, col_idx] - min_val) / range_val
            else:
                # Handle the case when range_val is zero
                # For example, you can assign a default value or skip
                pairwise_mat[:, col_idx] = 1  # This is a placeholder, adjust as needed

        pairwise_matrices = [create_pairwise(i, pairwise_mat) for i in range(matrix.shape[1])]
        local_vars.append(np.array([prio_vec(mat) for mat in pairwise_matrices]).T)
    ...
""")