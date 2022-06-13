import pandas as pd
import numpy as np

# Níveis de índice
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

# Dataframe com indice multinivel
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
print(df, '\n')
print(df.loc['G1'], '\n')
print(df.loc['G1'].loc[1], '\n')

# Os index possuem nomes
print(df.index.names)  # Mostra os nomes
df.index.names = ['Grupo', 'Número']  # Atribui os nomes
print(df, '\n')

# Buscar elementos por índice interno sem precisar usar index externo
print(df.xs(1, level='Número'))
