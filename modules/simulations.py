import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from matplotlib import rcParams
from matplotlib.pyplot import figure
import random
import json


def handle_simulations(profiles, tab_object):
    social_df = pd.read_excel('data/social_criteria.xlsx').dropna()
    env_criteria = pd.read_excel('data/env_cri.xlsx', sheet_name="Form Responses 1").dropna()
    level_one_df = pd.read_excel('data/lvl1_cri_pairwise.xlsx')

    econ_data = []
    env_data = []

    for idx, profile in enumerate(profiles):
        with open(profile, "r") as f:
            st.session_state.update(json.load(f))
            st.session_state[f"_profile_{idx}"] = st.session_state

            capital_costs = sum([st.session_state[key] for key in st.session_state.keys() if "_capital_cost" in key])
            maintenance_costs = sum([st.session_state[key] for key in st.session_state.keys() if "_maintenance_cost" in key])

            econ_data.append([capital_costs,
                                maintenance_costs])

            env_data.append([st.session_state['environmental_monetary_gain'],
                             st.session_state["tot_value_pol_reduc"],
                             st.session_state['k_es'] * (11.88 / 100)])


    econ_data = np.array(econ_data)
    env_data = np.array(env_data)

    data_matrices = [econ_data, env_data]

    def map_letter_vals(cell_value):
        map_values = {'a': 9, 'b': 6.34, 'c': 3.67, 'd': 1, 'e': 0}
        if isinstance(cell_value, str):
            letter = cell_value.split('.')[0]
            return map_values[letter]
        return cell_value

    def create_pairwise(column, arr):
        col_values = arr[:, column]
        col_reshaped = col_values.reshape(-1, 1)
        mat = col_reshaped / col_values
        return np.round(mat, 4)

    def prio_vec(A):
        e = np.linalg.eig(A)[1][:, 0]
        p = e / e.sum()

        return p.real

    social = social_df.copy()
    env = env_criteria.copy()

    social = social.applymap(map_letter_vals)
    env = env.applymap(map_letter_vals)

    # Convert DataFrame to NumPy array
    social_np = social.to_numpy()

    # Dictionary to hold the r values
    r_values = {f'r{i}{j}': [] for i in range(2) for j in range(2) if i != j}

    # Generate the r values
    for x in range(len(social_np)):
        row = social_np[x, :]
        mat = np.divide.outer(row, row)

        for i in range(2):
            for j in range(2):
                if i != j:
                    key = f'r{i}{j}'
                    r_values[key].append(mat[i, j])

    # Convert DataFrame to NumPy array
    env_np = env.to_numpy()

    # List to hold the e_r10 values
    e_r10 = []

    # Generate the e_r10 values
    for x in range(len(env_np)):
        row = env_np[x, :]
        mat_env = np.divide.outer(row, row)

        # Append the necessary value to e_r10
        e_r10.append(mat_env[1, 0])

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

    local_var_combined = np.concatenate(local_vars, axis=1)

    wts_25 = []
    wts_50 = []

    level_one_cri = pd.read_excel('data/lvl1_cri_pairwise.xlsx')
    level_one_cri = level_one_cri.iloc[:2, 1:3]

    def simulator(n, r_values, level_one_cri, local_var_combined, wts_25, wts_50):
        count = 0
        s_mat = np.ones((2, 2))
        e_mat = np.ones((3, 3))

        for _ in range(n):
            try:
                # Fill s_mat with random choices from r_values
                for k, v in r_values.items():
                    i, j = map(int, k[1:])
                    s_mat[i, j] = random.choice(v)
                    s_mat[j, i] = 1 / s_mat[i, j]  # Inverse for the symmetric element

                # Similar logic for e_mat if you have e_r values
                try:
                    e_mat[1][0] = random.choice(e_r10)
                    e_mat[0][1] = 1 / e_mat[1][0]
                except:
                    pass

                # Eigenvalue calculations for s_mat
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

                    count += 1
                    wts = (np.dot(local_var_combined, multply_mat))
                    wts_25.append(wts[0])
                    wts_50.append(wts[1])
            except:
                pass

        return count

    simulator(5000, r_values, level_one_cri, local_var_combined, wts_25, wts_50)

    wts = pd.DataFrame(columns=profiles + profiles)

    wts['wts_25'] = wts_25
    wts['wts_50'] = wts_50
    wts = wts.round(5)

    tab_object.header('Range of weights for all selected profiles')
    figure(figsize=(6.9, 3))

    rcParams['font.family'] = 'Arial'

    plt.hist(x=wts['wts_25'], bins=len(pd.unique(wts['wts_25'])), color='black',
             alpha=1)
    plt.hist(x=wts['wts_50'], bins=len(pd.unique(wts['wts_50'])), color='brown',
             alpha=1)
    plt.gcf().set_size_inches(7.5, 3)

    # plt.xticks(np.linspace(0.0, 0.45, 10), rotation = 0)

    plt.legend(profiles, fontsize=7)
    plt.xticks(fontsize=6)
    plt.yticks(fontsize=6)
    plt.ylabel('Density', fontsize=7)
    plt.xlabel('Weight', fontsize=7)

    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.3f}'))

    txt = "(A) Range of weights for all selected profiles"
    plt.figtext(0.5, -0.028, txt, wrap=True, horizontalalignment='center', fontsize=7)

    tab_object.pyplot(plt)