import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})
print(df.head(), '\n')

# Quais os valores únicos na coluna 2?
print(df['col2'].unique(), '\n')
#OU COM NUMPY:
print(np.unique(df['col2']), '\n')

# Qual a quantidade de valores únios na coluna dois?
print(df['col2'].nunique(), '\n')  # retorna o tamanho do vetor
# A mesma coisa que:
print(len(df['col2'].unique()), '\n')

# UMA FORMA MAIS COMPLETA, QUE UNE OS MÉTODOS .unique() e .nunique():
print(df['col2'].value_counts(), '\n')

# CONDICIONAIS:
print(df[df['col1'] > 2], '\n')  # imprime as linhas onde os valores da coluna 1 são maiores que 2
print(df[(df['col1'] > 2) & (df['col2'] == 444)], '\n')  # linhas onde valores de (col1 > 2) e (col2 == 444)

# .apply(), você pode definir uma função própria sua e aplicá-la a cada elemento do seu DataFrame
def vezes2(x):
    return x*2

print(df['col1'].apply(vezes2), '\n')

# OU UTILIZAR lambda
# EXEMPLO:

print(df['col1'].apply(lambda x: x*x), '\n')

# DELETAR COLUNAS COM O MÉTODO DEL(MÉTODO PADRÃO DO PYTHON)
del df['col2']
print(df, '\n')

# Parâmetros de DataFrame
print(df.columns, '\n')
print(df.index, '\n')

# ORDENAR VALORES
print(df.sort_values('col1'), '\n')


# Outros métodos:
print(df.isnull(), '\n')

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}
df = pd.DataFrame(data)
print(df, '\n')

df = df.pivot_table(values='D', index=['A', 'B'], columns='C')
print(df, '\n')