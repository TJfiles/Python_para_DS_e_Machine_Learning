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
print(arr, '\n')

# arange gera uma lista de 50 números a partir de zero, reshape gera matriz de 5 linhas e 10 colunas
arr = np.arange(50).reshape(5, 10)
print(arr, '\n')

# O PRIMEIRO COLCHETE FAZ MENÇÃO AS LINHAS E O SEGUNDO ÁS COLUNAS
# print das linhas até 3, todas as colunas
print(arr[2:4][:])

# Não copia um array, se alterar algum valor do array secundário o primário também é alterado, como nas listas
arr2 = arr
arr2[0, 0] = -10
print(arr, '\n')

# Método .copy()
l1 = np.arange(50).reshape(5, 10)
l2 = l1.copy()
l2[0, 0] = 50
print(l1)
print(l2)
print()

# OUTRA MANEIRA DE FATIAR UM ARRAY É USANDO VIRGULA, PRIMEIRO ARGUMENTO É REFERENTE AS LINHAS, E O SEGUNDO AS COLUNAS
print(l2[1:4, 5:])
print(l2[1:3, 5:7])
print()

# OPERAÇÕES LÓGICAS COM ARRAY
print(arr > 25, '\n')  # mostra quando o valor de um item é maior que 25
print(arr % 3 == 0)  # mostra quando o valor de um item é múltiplo de 3

bol = arr % 3 == 0  # aqui salva os valores boolean
print(bol)

print(arr[bol])  # imprime os valores onde bolean foi true
