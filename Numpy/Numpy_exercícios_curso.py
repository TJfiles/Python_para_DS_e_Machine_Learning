import numpy as np

# 1. Crie uma matriz de 10 zeros
arr = np.zeros(10)
print(arr, '\n')

# 2. Crie uma matriz de 10 ones
arr = np.ones(10)
print(arr, '\n')

# 3. Crie uma matriz de 10 cincos
arr = np.full(10, 5)  # também é possível criar uma matriz de zeros ou ones e multiplicar por 5
print(arr, '\n')

# 4. Crie uma matriz de inteiros de 10 até 50
arr = np.arange(10, 51)
print(arr, '\n')

# 5. Crie um array dos números pares de 10 até 50
arr = np.arange(10, 51, 2)
print(arr, '\n')

# 6. Crie uma matriz 3x3 com valores de 0 a 8
arr = np.arange(0, 9).reshape(3, 3)
print(arr, '\n')

# 7. Crie uma matriz identidade 3x3
arr = np.eye(3, 3)
print(arr, '\n')

# 8. Use numpy para gerar números aleatórios entre 0 e 1
arr = np.random.rand(4)
print(arr, '\n')

# 9. Use numpy para gerar 25 números aleatórios tirados de uma distribuição normal
arr = np.random.randn(25)
print(arr, '\n')

# 10. Crie a seguinte matriz: (exemplo no vídeo)
arr = np.arange(0, 101) / 100
print(arr, '\n')
print(len(arr))

# 11. Crie um array de tamanho 20 igualmente espaçado entre 0 e 1
arr = np.linspace(0, 1, 20)
print(arr, '\n')

# 12. INDEXAÇÃO E SELEÇÃO

mat = np.arange(1, 26).reshape(5, 5)

mat1 = mat[2:, 1:]
print(mat1, '\n')

mat2 = mat[-2, -1]
print(mat2, '\n')

mat3 = mat[0:3, 1:2]
print(mat3, '\n')

mat4 = mat[-1:, :]
print(mat4, '\n')

mat5 = mat[3:, :]
print(mat5, '\n')

# Obter a soma de todos os valores no mat
soma = np.sum(mat)
print(soma, '\n')

# Desvio padrão dos valores em mat
desv_padr = np.std(mat)
print(desv_padr, '\n')

# Obter a soma de todas as colunas em mat
soma_col = mat.sum(axis=0)  # AXIS = 0 (COLUNAS), AXIS = 1 (LINHAS)
print(soma_col, '\n')

