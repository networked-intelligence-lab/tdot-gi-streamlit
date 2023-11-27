import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.ticker import StrMethodFormatter

# Reading the provided DataFrames
social_criteria_df = pd.read_excel('../../data/social_criteria.xlsx').dropna()
lvl1_cri_pairwise_df = pd.read_excel('../../data/lvl1_cri_pairwise.xlsx').dropna()
pairwise_lvl2_df = pd.read_excel('../../data/pairwise_mat_lvl2.xlsx').dropna()  # Your new level 2 data

# Simplified conversion of criteria to numeric values
conversion_dict = {'a.': 9, 'b.': 6.34, 'c.': 3.67, 'd.': 1, 'e.': 0}
social_criteria_df.replace(conversion_dict, inplace=True)
social_criteria_df = social_criteria_df[social_criteria_df != 0]


# Function to compute priority vector with added checks
def priority_vector(A):
    if A.size == 0 or np.isnan(A).any():
        print("Error: Input matrix is empty or contains NaNs.")
        return np.array([])

    eigvals, eigvecs = np.linalg.eig(A)
    if len(eigvals) == 0:
        print("Error: Eigenvalues could not be computed.")
        return np.array([])

    eigvec_max = eigvecs[:, np.argmax(eigvals)]
    priority_vec = eigvec_max / eigvec_max.sum()
    return priority_vec.real


# Dynamically handling different shapes for Level 2 Pairwise Matrices
def compute_matrices_from_df(df):
    matrices = []
    for col in df.columns:
        n = len(df[col].dropna())
        if n == 0:
            print(f"Error: Column '{col}' is empty or all NaNs.")
            continue
        mat = np.ones((n, n))
        for i in range(n):
            for j in range(n):
                mat[i, j] = df.iloc[i][col] / df.iloc[j][col]
        vec = priority_vector(mat)
        if vec.size > 0:
            matrices.append(vec)
        else:
            print(f"Error in computing priority vector for column '{col}'.")
    return matrices


# Before computing matrices, check if the DataFrame is empty
if pairwise_lvl2_df.empty:
    print("Error: Pairwise Level 2 DataFrame is empty.")
else:
    lvl2_matrices = compute_matrices_from_df(pairwise_lvl2_df)
    print("Level 2 Matrices Computed Successfully.")


# Dynamically handling different shapes for Level 2 Pairwise Matrices
def compute_matrices_from_df(df):
    matrices = []
    for col in df.columns:
        n = len(df[col].dropna())
        mat = np.ones((n, n))
        for i in range(n):
            for j in range(n):
                mat[i, j] = df.iloc[i][col] / df.iloc[j][col]
        matrices.append(priority_vector(mat))
    return matrices


# Compute the matrices for level 2
lvl2_matrices = compute_matrices_from_df(pairwise_lvl2_df)


# Simulation function (simplified)
def simulator(num_simulations, lvl1_df, lvl2_matrices):
    results = []
    for _ in range(num_simulations):
        # Random selections for simulation
        random_selections = [random.choice(col) for col in social_criteria_df.T.values]

        # Compute priority vectors
        s_mat = np.array(random_selections).reshape(len(random_selections), len(random_selections))
        s_vec = priority_vector(s_mat)

        lvl1_vec = priority_vector(lvl1_df.values)

        # Combine and normalize
        combined_mat = np.dot(np.array(lvl2_matrices).T, lvl1_vec * s_vec)
        results.append(combined_mat / combined_mat.sum())
    return np.array(results)


# Example usage
num_simulations = 100  # Or any other number
simulation_results = simulator(num_simulations, lvl1_cri_pairwise_df, lvl2_matrices)


# Plotting the results
def plot_simulation_results(results):
    # Example plotting code (can be expanded based on specific requirements)
    plt.hist(results, bins=20)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()


plot_simulation_results(simulation_results)
