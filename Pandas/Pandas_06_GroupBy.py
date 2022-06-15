import pandas as pd
import numpy as np

data = {'Empresa': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Nome': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Venda': [200, 120, 340, 124, 223, 350]
        }
df = pd.DataFrame(data)
print(df, '\n')
print(df.groupby('Empresa'), '\n')  # Apenas aponta onde o grupo foi salvo na memória

group = df.groupby('Empresa')  # Salvo os dados em uma variável

print('Soma das vendas: \n', group.sum(), '\n')  # A soma das vendas por empresa
print('Média das vendas: \n', group.mean(), '\n')  # A média das vendas por empresa

# .describe() == contagem, média, desvio padrão, mínimo, porcentagem, máximo
print('Descrição estatística: \n', group.describe(), '\n')

# Total de vendas da Amy:

# Agrupar por nome
group = df.groupby('Nome')
print(group.sum().loc['Amy'], '\n')
amy_vendas = group.sum().loc['Amy']
print('Vendas da Amy: ', int(amy_vendas), '\n')
