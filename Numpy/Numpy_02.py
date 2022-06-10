import numpy as np

arr = np.arange(0, 100, 5)

# FATIAMENTO
print(arr)
print(arr[3])
print(arr[5:8])
print(arr[10:])
print(arr[:15])
print(len(arr))

# SUBSTITUI ITENS DENTRO DO ARRAY
arr[17:] = 100
print(arr)
