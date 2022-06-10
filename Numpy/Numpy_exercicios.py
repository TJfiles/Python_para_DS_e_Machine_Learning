# https://www.machinelearningplus.com/python/101-numpy-exercises-python/
import numpy as np

# Import numpy as np and print the version number.
print(np.__version__)

# Create a 1D array of numbers from 0 to 9
arr = np.arange(0, 10)

# Create a 3×3 numpy array of all True’s
# print(help(np.full))
arr_true = np.full((3, 3), True)

# Extract all odd numbers from arr
# INPUT: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# DESIRED OUTPUT: > array([1, 3, 5, 7, 9])

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = arr[arr % 2 == 1]
print(arr, '\n')

# Replace all odd numbers in arr with -1
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 == 1] = -1
print(arr, '\n')

# Replace all odd numbers in arr with -1 without changing arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = arr.copy()
out[out % 2 == 1] = -1
print(out)
print(arr)

# Convert a 1D array to a 2D array with 2 rows
arr = np.arange(10).reshape(2, 5)
print(arr)
