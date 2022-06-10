import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']
minha_lista = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {
    'a': 10,
    'b': 20,
    'c': 30,
}

# Gerar uma series
series = pd.Series(data=minha_lista, index=labels)
print(series)
print(series['b'], '\n')  # acessando um valor pelo index

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'URS', 'JAPAN', 'GERMANY'])
ser2 = pd.Series([1, 2, 3, 4], ['ITALY', 'JAPAN', 'URS', 'GERMANY'])
print(ser1)
print(ser2, '\n')

# OPERAÇÕES ARITMÉTICAS COM SERIES

ser3 = ser1 + ser2
print(ser3)
