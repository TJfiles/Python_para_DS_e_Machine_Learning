import pandas as pd
import numpy as np
'''dias_da_semana = ['Segunda Terça Quarta Quinta Sexta'.split()]
horarios = ['7h 12h 15h 16h 18h'.split()]
vitaminas = np.array([('Gingko Ginseng Omega3 COQ10 Magnésio'.split())*5]).reshape(5, 5)

df = pd.DataFrame(vitaminas, index=horarios, columns=dias_da_semana)
print(df)'''

# print(help(np.random.seed))
np.random.seed(101)  # define o padrão dos números aleatórios
df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df, '\n')

# PRINT DE UMA COLUNA
print('#PRINT DE UMA COLUNA')
print(df['Y'], '\n')

# GERAR COLUNA NOVA
print('#GERAR COLUNA NOVA')
df['X+Z'] = df['X'] + df['Z']
print(df, '\n')

# DELETANDO UMA COLUNA
print('#DELETANDO UMA COLUNA')
# AXIS = 0 (INDEX)PADRÃO, AXIS = 1 (COLUNA),  se atentar a isso quando tiver que escolher entre deletar coluna ou índice
df = df.drop('X+Z', axis=1)  # Atribuir o resultado da expreção a uma variável para salvar,
# ou utilizar o parâmetro inplace=True, também altera o df original
print(df, '\n')

# LOCALIZAÇÃO DE ELEMENTOS POR ÍNCICE
print(df.loc["A", "Z"], '\n')  # .loc['linha', 'coluna']
print(df.loc[['A', 'B'], ['X', 'Y', 'Z']])

print(df.iloc[1:4, 2:])  # Com .iloc[] é possível localizar data como no numpy


