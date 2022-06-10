import numpy as np

minha_lista = [1, 2, 3]

minha_lista = np.array(minha_lista)  # Cria um array da lista

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Cria uma Matriz
print(matriz)
matriz = np.array(matriz)  # Array da Matriz
print(matriz, '\n')

# numpy.arange(#1, #2, #3) gera uma lista de números, #1 - diz o início, #2 - diz o range, #3 - diz o passo
l1 = np.arange(1, 10, 2)
print(l1, '\n')

# GERA UMA LISTA DE ZEROS
arr = np.zeros(5)
print(arr)
arr = np.zeros((5, 5))
print(arr, '\n')

# GERA UMA LISTA DE UNS
arr = np.ones((3, 3))
print(arr, '\n')

# GERA UMA LISTA DE NÚMEROS,
# #1 - INÍCIO DA LISTA, #2 - FINAL DA LISTA, #3 A QUANTIDADE DE NÚMEROS EQUIDISTANTES DENTRO DESTA LISTA
l2 = np.linspace(0, 10, 5)
print(l2, '\n')

# print(help(np.linspace))

# GERA LISTA ALEATORIA DE 5 NÚMEROS ENTRE 0 E 1
rd = np.random.rand(5)
print(rd)

# GERA UM BLOCO DE NÚMEROS ALEATÓRIOS ENTRE 0 E 1, COM DIMENÇÃO 4 X 3
rd = np.random.randn(4, 3)
print(rd)

# GERA UMA LISTA DE 10 NÚMEROS ALEATÓRIOS ENTRE 0 E 100, #1 INICIO #2 FIM #3 QUANTIDADE DE NÚMEROS
rd = np.random.randint(0, 100, 10)
print(rd)

# GERA UM VETOR COM 25 ELEMENTOS
arr = np.random.rand(25)
print(arr, 'n')

# REDEFINE O TAMANHO DO ARRAY, ele deixou de ser um vetor de tamanho 25 e passou a ser uma matriz de tamanho 5 x 5
arr = arr.reshape(5, 5)
print(arr)

# se quiser saber o tamanho, use o atributo .shape
print(arr.shape)

# Encontra o maíor
print(arr.max())

# ENCONTRA O MENOR
print(arr.min())

# ENCONTRA O ÍNDICE DO MAIOR NÚMERO
print(arr.argmax())

# ENCONTRA O ÍNDICE DO MENOR NÚMERO
print(arr.argmin())
