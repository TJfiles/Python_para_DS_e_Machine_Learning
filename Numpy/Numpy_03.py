import numpy as np


arr = np.arange(0, 16)
arr2 = np.arange(0, 16)

# Somando Arrays de tamanhos iguais
soma = arr + arr2
print(soma, '\n')  # cada valor com mesmo índice é somado

arr = arr + 100  # isso irá adcionar 100 para cada valor em cada índice do array
print(arr, '\n')

# SOMAR COLUNAS OU LINHAS

mat = np.arange(0, 50).reshape(5, 10)
print(mat, '\n')
soma_colunas = mat.sum(axis=0)  # AXIS = 0 SOMA COLUNAS
soma_linhas = mat.sum(axis=1)  # AXIS = 1 SOMA LINHAS

print(soma_colunas)
print(soma_linhas)
