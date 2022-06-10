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
# AXIS = 0 (INDEX)PADRÃO, AXIS = 1 (COLUNA)
df = df.drop('X+Z', axis=1, inplace=True)
print(df)
