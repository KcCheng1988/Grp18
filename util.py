from matplotlib import pyplot as plt
import numpy as np

'''
Generate an array of binary entries
:param integer n_row: The row dimension of the array, representing the sample size
:param integer n_col: The column dimension of the array, representing the feature size
:param bool single: If set to True, only one entry of each row will be 1 (default False)
:param bool seed: Whether to use a specific random seed value
:param int seed_val: Random seed value

:return: the binary array
:raises ValueError: if seed is set to True but no seed_val is passed.
'''

def _generate_binary_samples(n_row, n_col, single=False, seed=False,
                             seed_val=None):
    if seed==True:
        if seed_val is None:
            raise ValueError("Specify seed_val when setting seed as True.")
        else:
            np.random.seed(seed_val)

    if single==False:
        return np.random.randint(2, size=(n_row, n_col))
    else:
        output = np.zeros(shape=(n_row, n_col))
        for row in range(n_row):
            non_zero_col = np.random.randint(n_col, size=(1))
            output[row, non_zero_col] = 1
        return output



