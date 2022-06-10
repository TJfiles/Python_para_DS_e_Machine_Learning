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
print(arr, '\n')

# Stack arrays a and b vertically
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# Answers
# Method 1:
c = np.concatenate([a, b], axis=0)
print(c)

# Method 2:
np.vstack([a, b])

# Method 3:
c = np.r_[a, b]
print(c)

# Stack the arrays a and b horizontally.
c = np.concatenate([a, b], axis=1)
print(c)

# Method 2:
np.hstack([a, b])

# Method 3:
c = np.c_[a, b]

# 10. How to generate custom sequences in numpy without hardcoding?
# Create the following pattern without hardcoding. Use only numpy
# functions and the below input array a.
# INPUT:
a = np.array([1, 2, 3])
# Desired Output:
# > array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
