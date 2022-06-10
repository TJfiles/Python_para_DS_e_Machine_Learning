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

arr = np.full((10, 10), 100)  # Gera uma matriz de 10x10 preenchida com 100
# Intercala quadrados de 0 e 100 dentro da matriz
arr[1:9, 1:9] = 0
arr[2:8, 2:8] = 100
arr[3:7, 3:7] = 0
arr[4:6, 4:6] = 100

# Gera blocos de 55 nos cantos da matriz
arr[0:3, 0:3] = 55  # Canto superior esquerdo
arr[1:2, 1:2] = 1  # centro do canto superior esquerto

arr[0:3, 7:] = 55  # Canto superior direito
arr[1:2, 8:9] = 1  # Centro do canto superior direito

arr[7:, 0:3] = 55  # Canto inferior esquerdo
arr[8:9, 1:2] = 1  # Centro do canto inferior esquerdo

arr[7:, 7:] = 55  # Canto inferior direito
arr[8:9, 8:9] = 1  # Centro do canto inferior direito
print(arr)

'''
OUTPUT:
[[ 55  55  55 100 100 100 100  55  55  55]
 [ 55   1  55   0   0   0   0  55   1  55]
 [ 55  55  55 100 100 100 100  55  55  55]
 [100   0 100   0   0   0   0 100   0 100]
 [100   0 100   0 100 100   0 100   0 100]
 [100   0 100   0 100 100   0 100   0 100]
 [100   0 100   0   0   0   0 100   0 100]
 [ 55  55  55 100 100 100 100  55  55  55]
 [ 55   1  55   0   0   0   0  55   1  55]
 [ 55  55  55 100 100 100 100  55  55  55]]
'''