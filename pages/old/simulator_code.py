import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from matplotlib.ticker import StrMethodFormatter
from matplotlib import rcParams
from matplotlib.pyplot import figure
from streamlit_extras.app_logo import add_logo
from modules.sidebar import build_sidebar
from glob import glob
import json

# build_sidebar()
add_logo("media/logo.png", height=150)


st.title("Quantify Benefits")
# st.write(st.session_state)

profile_list = list(glob("profiles/*.json"))
select_profiles = st.multiselect("Select Profiles", profile_list, [])
if select_profiles:
    cols = st.columns(len(select_profiles))
    for idx, profile in enumerate(select_profiles):
        with open(profile, "r") as f:
            st.session_state.update(json.load(f))
            st.session_state[f"_profile_{idx}"] = st.session_state

        with cols[idx]:
            st.subheader("Determine Green Infrastructure")
            determine_gi_output = st.session_state["determine_gi_output"]
            for major_category, minor_categories_list in determine_gi_output.items():
                st.multiselect(major_category, minor_categories_list, minor_categories_list, key=f"{major_category}_{idx}")


            st.subheader("Determine Economic Impacts")
            st.text_input("Capital Cost", value=st.session_state["cisterns_capital_cost"], key=f"capital_cost_{idx}")
            st.text_input("Maintenance Cost", value=st.session_state["cisterns_maintenance_cost"], key=f"maintenance_cost_{idx}")

            st.subheader("Environmental Impact")
            st.write(f"Runoff amount reduced by tree plantation: {st.session_state['q_tp']} gallons/year")
            st.write(f"Runoff amount reduced by bioretention and infiltration: {st.session_state['q_bi']} gallons/year")
            st.write(f"Runoff amount reduced by permeable pavement: {st.session_state['q_pp']} gallons/year")
            st.write(f"Runoff amount reduced by water harvesting: {st.session_state['q_wh']} gallons/year")
            st.write(f"Total amount of reduced stormwater runoff: {st.session_state['q_t']} gallons/year")
            st.write(f"Monetary Gain from Avoided Stormwater Treatment: {st.session_state['environmental_monetary_gain']} USD/year")
            st.write("Total annual air pollutant reduction (lbs):", st.session_state["lb_reduc_per_pollutant"])
            st.write("Total value of pollutant reduction ($):", st.session_state["tot_value_pol_reduc"])
            st.write("40 Year Average of Energy Saved (kWh/tree per year):", st.session_state['k_es'])
            st.write("Value of Energy Saved ($):", st.session_state['k_es'] * (11.88 / 100))



df = pd.read_excel('data/social_criteria.xlsx')
df = df.dropna()

df2 = pd.read_excel('data/env_cri.xlsx', sheet_name="Form Responses 1")
df2 = df2.dropna()

df2 = df2.drop('energy', axis=1)
level_one_cri = pd.read_excel('data/lvl1_cri_pairwise.xlsx')
level_one_cri = level_one_cri.iloc[:2, 1:3]

social = df.copy()

for i in range(len(social.columns)):
    for j in range(len(social.iloc[:, i])):
        # [0])
        social.iloc[j, i] = str(social.iloc[j, i]).split()[0]

options = {'a.': 9, 'b.': 6.34, 'c.': 3.67, 'd.': 1, 'e.': 0}

for i in range(len(social.columns)):
    social.iloc[:, i] = [options[item] for item in social.iloc[:, i]]

for i in range(len(social.columns)):
    social = social[social.iloc[:, i].isin([0]) == False]

env = df2.copy()
for i in range(len(env.columns)):
    for j in range(len(env.iloc[:, i])):
        env.iloc[j, i] = str(env.iloc[j, i]).split()[0]

options = {'a.': 9, 'b.': 6.34, 'c.': 3.67, 'd.': 1, 'e.': 0}

for i in range(len(env.columns)):
    env.iloc[:, i] = [options[item] for item in env.iloc[:, i]]

for i in range(len(env.columns)):
    env = env[env.iloc[:, i].isin([0]) == False]

mat = np.zeros((4, 4))
mat_env = np.zeros((2, 2))
# # for i in range(len(social.columns)):
# for i in range(len(social.iloc[0,:])):
#     for j in range(len(mat)):
#         #
#         mat[j][i] = social.iloc[0,j]/social.iloc[0,i]
#     #

# mat_df = pd.DataFrame(mat)
# # display(mat_df)


r10 = []
r20 = []
r30 = []
r21 = []
r31 = []
r32 = []

for x in range(0, 93):
    for i in range(len(social.iloc[0, :])):
        for j in range(len(mat)):
            #
            mat[j][i] = social.iloc[x, j] / social.iloc[x, i]

    r10.append(mat[1][0])
    r20.append(mat[2][0])
    r30.append(mat[3][0])
    r21.append(mat[2][1])
    r31.append(mat[3][1])
    r32.append(mat[3][2])

e_r10 = []

for x in range(0, 94):
    for i in range(len(env.iloc[0, :])):
        for j in range(len(mat_env)):
            #
            mat_env[j][i] = env.iloc[x, j] / env.iloc[x, i]

    e_r10.append(mat_env[1][0])

new_df = pd.read_excel('data/pairwise_mat_lvl2.xlsx', sheet_name='social')
new_df_env = pd.read_excel('data/pairwise_mat_lvl2.xlsx', sheet_name='env')

#
# def prio_vec(A):
#     e = np.linalg.eig(A)[1][:, 0]
#     p = e / e.sum()
#
#     return p.real
#
#
# mat1 = np.ones((4, 4))
# mat2 = np.ones((4, 4))
# mat3 = np.ones((4, 4))
# mat4 = np.ones((4, 4))
#
# for i in range(4):
#     for j in range(4):
#         mat1[i][j] = new_df.iloc[i, 5] / new_df.iloc[j, 5]
#         print(mat1[i][j])
# mat1 = mat1.round(4)
#
# for i in range(4):
#     for j in range(4):
#         mat2[i][j] = new_df.iloc[i, 6] / new_df.iloc[j, 6]
# mat2 = mat2.round(4)
#
# for i in range(4):
#     for j in range(4):
#         mat3[i][j] = new_df.iloc[i, 7] / new_df.iloc[j, 7]
# mat3 = mat3.round(4)
#
# for i in range(4):
#     for j in range(4):
#         mat4[i][j] = new_df.iloc[i, 8] / new_df.iloc[j, 8]
# mat4 = mat4.round(4)


def prio_vec(A):
    e = np.linalg.eig(A)[1][:, 0]
    p = e / e.sum()

    return p.real


env_mat1 = np.ones((4, 4))
env_mat2 = np.ones((4, 4))

for i in range(4):
    for j in range(4):
        env_mat1[i][j] = new_df_env.iloc[i, 4] / new_df_env.iloc[j, 4]
env_mat1 = env_mat1.round(4)

for i in range(4):
    for j in range(4):
        env_mat2[i][j] = new_df_env.iloc[i, 5] / new_df_env.iloc[j, 5]
env_mat2 = env_mat2.round(4)

# local_var_transposed = [prio_vec(mat1), prio_vec(mat2), prio_vec(mat3), prio_vec(mat4)]
# local_var = [[local_var_transposed[j][i] for j in range(len(local_var_transposed))] for i in
#              range(len(local_var_transposed[0]))]

local_var_transposed_env = [prio_vec(env_mat1), prio_vec(env_mat2)]
local_var_env = [[local_var_transposed_env[j][i] for j in range(len(local_var_transposed_env))] for i in
                 range(len(local_var_transposed_env[0]))]

local_var_combined = np.concatenate((local_var, local_var_env), axis=1)

mat = np.ones((4, 4))

wts_25 = []
wts_50 = []
wts_75 = []
wts_100 = []


def simulator(n):
    count = 0
    s_mat = np.ones((4, 4))
    e_mat = np.ones((2, 2))
    for i in range(1, n + 1):
        # random.seed(11)
        s_mat[1][0] = random.choice(r10)
        s_mat[0][1] = 1 / s_mat[1][0]
        s_mat[2][0] = random.choice(r20)
        s_mat[0][2] = 1 / s_mat[2][0]
        s_mat[3][0] = random.choice(r30)
        s_mat[0][3] = 1 / s_mat[3][0]
        s_mat[2][1] = random.choice(r21)
        s_mat[1][2] = 1 / s_mat[2][1]
        s_mat[3][1] = random.choice(r31)
        s_mat[1][3] = 1 / s_mat[3][1]
        s_mat[3][2] = random.choice(r32)
        s_mat[2][3] = 1 / s_mat[3][2]

        e_mat[1][0] = random.choice(e_r10)
        e_mat[0][1] = 1 / e_mat[1][0]

        w1, v1 = np.linalg.eig(s_mat)
        lambda_max1 = max(w1)

        CI1 = (lambda_max1 - len(s_mat)) / (len(s_mat) - 1)
        CR1 = CI1 / 0.90

        w2, v2 = np.linalg.eig(e_mat)
        lambda_max2 = max(w2)

        CI2 = (lambda_max2 - len(e_mat)) / (len(e_mat) - 1)
        CR2 = CI2 / 0.90
        if CR1 > 0.1 or abs(prio_vec(s_mat)[0]) > 1 or CR2 > 0.1 or abs(prio_vec(e_mat)[0]) > 1:
            continue
        else:
            mat1 = (prio_vec(level_one_cri)[1] * prio_vec(s_mat))
            mat2 = (prio_vec(level_one_cri)[0] * prio_vec(e_mat))

            multply_mat = np.concatenate((mat1, mat2))

            count = count + 1
            wts = (np.dot(local_var_combined, multply_mat))
            wts_25.append(wts[0])
            wts_50.append(wts[1])
            wts_75.append(wts[2])
            wts_100.append(wts[3])


num_sims = st.number_input('Enter the number of simulations', min_value=1, max_value=10000, value=100, step=1, key=None)
if st.button('Simulate', on_click=simulator(num_sims)):

    column_names = ["wts_25", "wts_50", "wts_75", "wts_100"]

    wts = pd.DataFrame(columns=column_names)

    wts['wts_25'] = wts_25
    wts['wts_50'] = wts_50
    wts['wts_75'] = wts_75
    wts['wts_100'] = wts_100

    wts = wts.round(5)

    # ))
    # ))
    # ))
    # ))

    ## social overall plot
    st.header('Range of weights for all four alternatives')
    figure(figsize=(6.9, 3))

    rcParams['font.family'] = 'Arial'

    plt.hist(x=wts['wts_25'], bins=len(pd.unique(wts['wts_25'])), color='black',
             alpha=1)
    plt.hist(x=wts['wts_50'], bins=len(pd.unique(wts['wts_50'])), color='brown',
             alpha=1)
    plt.hist(x=wts['wts_75'], bins=len(pd.unique(wts['wts_75'])), color='blue',
             alpha=1)
    plt.hist(x=wts['wts_100'], bins=len(pd.unique(wts['wts_100'])), color='green',
             alpha=1)
    plt.gcf().set_size_inches(7.5, 3)

    # plt.xticks(np.linspace(0.0, 0.45, 10), rotation = 0)


    plt.legend(['25% GI', '50% GI', '75% GI', '100% GI'], fontsize=7)
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    plt.ylabel('Density', fontsize=7)
    plt.xlabel('Weight', fontsize=7)

    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.3f}'))

    txt = "(A). Range of weights for all four alternatives"
    plt.figtext(0.5, -0.028, txt, wrap=True, horizontalalignment='center', fontsize=7)

    plt.savefig('wts.png', dpi=300, bbox_inches="tight")

    st.pyplot(plt)

    plt.hist(x=wts['wts_25'], bins=len(pd.unique(wts['wts_25'])), color='black',
             alpha=1)

    # plt.legend(['25% GI'])
    plt.ylabel('Density', fontsize=7)
    plt.xlabel('Weight', fontsize=7)

    from matplotlib.ticker import StrMethodFormatter
    st.header('Range of weights for 25% GI')
    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.3f}'))

    fig = plt.gcf()
    fig.set_size_inches(3.25, 2.3)

    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    txt = "(B) 25% GI, 75% TI"
    plt.figtext(0.54, -0.02, txt, wrap=True, horizontalalignment='center', fontsize=7)

    plt.tight_layout()

    plt.savefig('wts_25.png', dpi=300, bbox_inches="tight")

    st.pyplot(plt)

    st.header('Range of weights for 50% GI')
    plt.hist(x=wts['wts_50'], bins=len(pd.unique(wts['wts_50'])), color='brown',
             alpha=1)

    # plt.legend(['50% GI'])
    plt.ylabel('Density', fontsize=7)
    plt.xlabel('Weight', fontsize=7)

    from matplotlib.ticker import StrMethodFormatter

    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.3f}'))

    fig = plt.gcf()
    fig.set_size_inches(3.25, 2.3)

    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    txt = "(C) 50% GI, 50% TI"
    plt.figtext(0.54, -0.02, txt, wrap=True, horizontalalignment='center', fontsize=7)

    plt.tight_layout()
    plt.savefig('wts_50.png', dpi=300, bbox_inches="tight")

    st.pyplot(plt)

    st.header('Range of weights for 75% GI')
    plt.hist(x=wts['wts_75'], bins=len(pd.unique(wts['wts_75'])), color='blue',
             alpha=1)

    # plt.legend(['75% GI'])
    plt.ylabel('Density', fontsize=7)
    plt.xlabel('Weight', fontsize=7)

    from matplotlib.ticker import StrMethodFormatter

    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.3f}'))

    fig = plt.gcf()
    fig.set_size_inches(3.25, 2.3)

    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    txt = "(D) 75% GI, 25% TI"
    plt.figtext(0.54, -0.02, txt, wrap=True, horizontalalignment='center', fontsize=7)

    plt.tight_layout()
    plt.savefig('wts_75.png', dpi=300, bbox_inches="tight")

    st.pyplot(plt)

    st.header('Range of weights for 100% GI')
    plt.hist(x=wts['wts_100'], bins=len(pd.unique(wts['wts_100'])), color='green',
             alpha=1)

    # plt.legend(['100% GI'])
    plt.ylabel('Density', fontsize=7)
    plt.xlabel('Weight', fontsize=7)

    from matplotlib.ticker import StrMethodFormatter

    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.3f}'))

    fig = plt.gcf()
    fig.set_size_inches(3.25, 2.3)

    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)

    txt = "(E) 100% GI"
    plt.figtext(0.54, -0.02, txt, wrap=True, horizontalalignment='center', fontsize=7)
    plt.tight_layout()
    plt.savefig('wts_100.png', dpi=300, bbox_inches="tight")

    st.pyplot(plt)

    from matplotlib import font_manager

    font_manager_inst = font_manager.fontManager

    import matplotlib.pyplot as plt
    import numpy

    from matplotlib import rcParams

    rcParams['font.family'] = 'Arial'

    data = r10
    #
    sorted_random_data = numpy.sort(data)
    p = 1. * numpy.arange(len(sorted_random_data)) / float(len(sorted_random_data) - 1)
    #

    fig = plt.figure()
    # fig.suptitle('CDF of R[1,0]')
    ax2 = fig.add_subplot(111)

    ax2.plot(sorted_random_data, p)
    ax2.set_xlabel("(A) " + '$c_2$/$c_1$', fontsize=22)
    ax2.set_ylabel('Cumulative probabilty', fontsize=22)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.savefig("1.png", dpi=300, bbox_inches="tight")
    st.header("CDF of $c_2$/$c_1$")
    st.pyplot(plt)


    rcParams['font.family'] = 'Arial'

    data = r20
    #
    sorted_random_data = numpy.sort(data)
    p = 1. * numpy.arange(len(sorted_random_data)) / float(len(sorted_random_data) - 1)
    #

    fig = plt.figure()
    # fig.suptitle('CDF of data points')
    ax2 = fig.add_subplot(111)
    ax2.plot(sorted_random_data, p)
    ax2.set_xlabel("(B) " + '$c_3$/$c_1$', fontsize=22)
    ax2.set_ylabel('Cumulative probabilty', fontsize=22)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.savefig("2.png", dpi=300, bbox_inches="tight")
    st.header("CDF of $c_3$/$c_1$")
    st.pyplot(plt)

    rcParams['font.family'] = 'Arial'

    data = r31
    #
    sorted_random_data = numpy.sort(data)
    p = 1. * numpy.arange(len(sorted_random_data)) / float(len(sorted_random_data) - 1)
    #

    fig = plt.figure()
    # fig.suptitle('CDF of data points')
    ax2 = fig.add_subplot(111)
    ax2.plot(sorted_random_data, p)
    ax2.set_xlabel("(E) " + '$c_4$/$c_2$', fontsize=22)
    ax2.set_ylabel('Cumulative probabilty', fontsize=22)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    plt.savefig("5.png", dpi=300, bbox_inches="tight")
    st.header("CDF of $c_4$/$c_2$")
    st.pyplot(plt)
