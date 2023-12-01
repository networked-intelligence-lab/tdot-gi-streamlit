from streamlit_extras.app_logo import add_logo
from modules.helpers import subsubheader
import streamlit as st

add_logo("media/logo.png", height=150)

st.header("User Guide")
st.subheader("Introduction")
st.write("Welcome to the tool user guide! This guide is intended to help you navigate the tool and understand the different features and functionalities of the tool. The tool is divided into the following sections:")
st.markdown("""The following are the main components that you would like to use, generally in order:
1. Determine Green Infrastructure
2. Economic Impact
3. Environmental Impact
4. Social Impact
5. Quantify Benefits

Additionally, please take note of the sidebar profiles, which you will be using in order to save your scenarios.""")

st.subheader("Step 0: Sidebar & Profiles")
st.markdown("""
Before we get started, it is important to note profiles. Profiles are important as they help you make comparative
analysis between different scenarios. Profiles are also used to save your scenarios.

Below, you can see that we are able to compare between two different scenarios side-by-side, in terms of their
economic impact and environmental impact. This is useful for comparing different scenarios and determining which
GI/scenario is the most beneficial.
""")
st.image("media/user_guide/comparison_profiles.png", width=800)
st.markdown("""
Additionally, it is how we are able to run simulation data in order to quantify weights for the benefits of each
scenario, such as below.
""")
st.image("media/user_guide/sample_weights.png", width=800)
st.markdown("""
Because of this, please be sure to create your scenarios and save them accordingly. You are **not** able to save
to the Default profile, so please create a new profile and save your scenarios there.

When you create a new profile, you will be prompted to enter a name for your profile. Please enter a name that
is descriptive of the scenarios you will be saving in that profile. You can also choose a template profile to
copy from, which will copy all values from that profile to your new profile. If you want all default values, please
choose the Default profile to copy from.
""")

st.subheader("Step 1: Determine Green Infrastructure")
st.markdown("""
This section is where you will be able to determine the green infrastructure that you will be using in your
scenario. You will be able to choose from a variety of conditions, such as soil infiltration rate, GI years, distance
from water table, and more. As you choose these conditions, you will be able to see on the right most column what GI 
are potentially suitable for usage. Please note, sifting GI options in this way will ***not*** lock you out of 
future GI options in other sections (such as Economic Impact). These are simply suggestions based on the conditions
you have chosen.
""")
st.image("media/user_guide/determine_gi.png", width=800)

st.subheader("Step 2: Economic Impact")
st.markdown("""
This section is where you will be able to determine the economic impact of your scenario. You will be able to choose
a variety of parameters, such as the impervious area, anticipated tank inspection and disinfection costs, and more. 
These parameters change depending on the GIs that you choose using the checkboxes within each GI tab.

Your chosen parameter values will determine both the capital and maintenance costs of your scenario, which will be 
used in the quantification of benefits.""")
st.image("media/user_guide/economic_impact.png", width=800)

st.subheader("Step 3: Environmental Impact")
st.markdown("""
This section is where you will be able to determine the environmental impact of your scenario. You will be able to
choose a variety of environment-related parameters, such as your STRATUM Climate zone, the amount of rainfall, and
number of trees. All these parameters will be used to determine the environmental impact of your scenario in terms of 
runoff reduced by tree plantation, bioretention, reduced air usage, reduced energy usage, and more.
""")
st.image("media/user_guide/environmental_impact.png", width=800)

st.subheader("Step 4: Social Impact")
st.markdown("""
This section is where you will be able to determine the social impact of your scenario. Here, you will be able to 
choose a polygon of interest, which will be used to determine the number of parks in an area (for which your GI may
replace a percentage of), as well as other parameters. These parameters will be used to determine the social impact in 
terms of enhanced property value and recreational usage.
""")
st.image("media/user_guide/social_impact.png", width=800)

st.subheader("Step 5: Quantify Benefits")
st.markdown("""
Lastly, this section is where you will be able to quantify the benefits of your scenario. You will be able to choose
the profiles that you would like to compare. In the selectbox at the top of the page, you can choose your previously 
defined/saved profiles to compare. In the "Raw Outputs" tab, you will be able to check side-by-side the raw outputs
of each of your chosen profiles. In the Simulation tab, you will be able to run a simulation of your chosen profiles
under an AHP and Markov process in order to determine the weights of each benefit. These weights are then graphed 
for your visualization so that you can see the relative weight of each scenario.
""")
st.image("media/user_guide/comparison_profiles.png", width=800)
st.image("media/user_guide/sample_weights.png", width=800)




