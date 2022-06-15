import pandas as pd
import numpy as np

df = pd.read_csv('exemplo')
print(df)

# Salvar arquivo em csv
df = df + 1
print(df)
df.to_csv('exemplo_salvo.csv')

# Importar arquivo excel
df = pd.read_excel('Exemplo_Excel.xlsx', sheet_name='Sheet1')

print(df, '\n')

df['Nova_Coluna'] = [1, 2, 3, 4]
print(df)
df.to_excel('Exemplo_Excel_Salvo.xlsx', sheet_name='Sheet 1')  # Arquivo Salvo excel

# Importando dados de HTML
# Talvez seja necessário instalar algumas biblitecas como: xlml, html5lib, BeautifulSoup4
# df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# print(type(df))
# Link com erro "No tables found

