import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df, '\n')
print(df > 0, '\n')  # IMPRIME DATAFRAME COM VALORES TRUE E FALSE
bol = df > 0
print(bol, '\n')  # IMPRIME DATAFRAME COM VALORES TRUE E FALSE
print(df[bol], '\n')  # IMPRIME OS VALORES EXATOS ONDE A EXPREÇÃO DE BOL É TRUE

# QUAIS VALORES DA LINHA 'W' SÃO MAIORES QUE ZERO?
print(df[df['W'] > 0])  # DATAFRAME REDIMENCIONADO, NESTE CASO DELETOU A LINHA C

print(df[df['W'] > 0]['Y'])  # FILTRA A COLUNA Y

# FILTRO CONDICIONAL COM MÚLTIPLAS CONDIÇÕES
print(df[(df['W'] > 0) & (df['Y'] > 1)])  # usar & no lugar de and, pois 'and' não compara series
print(df[(df['W'] > 0) | (df['Y'] > 1)])  # USAR | NO LUGAR DE 'or'


# RESETAR O INDEX
df = df.reset_index()  # O INDEX VOLTA AS CONFIGURAÇÕES PADRÕES
print(df, '\n')

# ESTADOS DO BRAZIL COMO INDEX
col = 'RJ SP RS AM SC'.split()
df['Estado'] = col
df = df.set_index('Estado')  # .set_index()
print(df)
