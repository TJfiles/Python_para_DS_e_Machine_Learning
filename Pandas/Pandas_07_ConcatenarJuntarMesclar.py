import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])
print(df1, '\n')
print(df2, '\n')
print(df3, '\n')

# Concatenação:
# É importante que os dataframes tenham o mesmo tamanho no eixo em que você está os unindo
print(pd.concat([df1, df2, df3]), '\n')  # axis=0(padrão), concatenando no sentido das linhas
print(pd.concat([df1, df2, df3], axis=1), '\n')  # axis=1, concatenando no sentido das colunas

#OUTRO EXEMPLO:
esquerda = pd.DataFrame({'Key': ['K0', 'K1', 'K2', 'K3'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})

direita = pd.DataFrame({'Key': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
print(esquerda, '\n')
print(direita, '\n')
print(pd.concat([esquerda, direita], axis=1), '\n')

# MESCLAR
# O método mesclar permite que você mescle os quadros de dados juntos usando uma lógica semelhante a mesclagem de
# tabelas SQL juntas, dado que elas compartilhem algum elemento em comun, neste caso a coluna Key, exemplo:
print(pd.merge(esquerda, direita, how='inner', on='Key'), '\n')

# Outro exemplo
esquerda = pd.DataFrame({'Key1': ['K0', 'K1', 'K2', 'K3'],
                         'Key2': ['K0', 'K1', 'K2', 'K3'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})

direita = pd.DataFrame({'Key1': ['K0', 'K1', 'K2', 'K3'],
                        'Key2': ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(esquerda, direita, on=['Key1', 'Key2']), '\n')
print(pd.merge(esquerda, direita, how='outer', on=['Key1', 'Key2']), '\n')

# JUNTAR
# Juntar é um método conveniente para combinar as colunas de dois DataFrames indexados potencialmente diferentes em um
# único resultado DataFrame

esquerda = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                         'B': ['B0', 'B1', 'B2']},
                        index=['K0', 'K1', 'K2'])
direita = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                        'D': ['D0', 'D1', 'D2']},
                       index=['K0', 'K2', 'K3'])
print(esquerda.join(direita), '\n')
print(esquerda.join(direita, how='outer'), '\n')