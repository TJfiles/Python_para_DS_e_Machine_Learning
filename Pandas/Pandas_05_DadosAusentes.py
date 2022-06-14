import pandas as pd
import numpy as np

d = {
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'c': [1, 2, 3]
}

df = pd.DataFrame(d)
print(df, '\n')

# Excluir dados ausentes
print(df.dropna(), '\n')  # Exclui as linhas que contem NaN
print(df.dropna(thresh=2), '\n')  # thresh=2, Só exclui as linhas com 2 valores NaN

# Preencher valores NaN com outro valor
print(df.fillna(value='Vazio'), '\n')
print(df['A'].fillna(value=df['A'].mean()), '\n')  # Substituiu o valor Nan da Coluna A pela média dos valores de A

# mothod=ffill, 'Forward Fill' preenche os valores NaN com o ultimo valor registrado
print(df.fillna(method='ffill'), '\n')
