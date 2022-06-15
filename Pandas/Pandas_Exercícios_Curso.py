import pandas as pd
import numpy as np

# Leia o arquivo Salaries.csv como um DataFrame chamado sal
# Verifique o Head do DataFrame
sal = pd.read_csv('Salaries.csv')
print(sal.head(), '\n')

# Use o método .info() para descobrir quantas entradas existem
print(sal.info(), '\n')

# Qual é o "BasePay" médio?
print(sal['BasePay'].mean(), '\n')

# Qual é a maior quantidade de "OvertimePay" no conjunto de dados?
print(sal['OvertimePay'].max(), '\n')

# Qual é o cargo de JOSEPH DRISCOLL Nota: use todas as maíusculas, também há um Joseph Driscoll com mínusculas
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'], '\n')

# Quanto JOSEPH DRISCOLL ganha? Incluindo Benefícios
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL'], '\n')
total = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
print(total, '\n')

# Qual o nome da pessoa mais bem paga (incluindo benefícios)?
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'], '\n')

# Qual o nome da pessoa paga mais baixa (incluindo benefícios)?
# Você percebe algo estranho sobre o quanto ele ou ela é paga? Resposta: o pagamento está negativo...
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName'], '\n')

# Qual foi a média 'BasePay' de todos os funcionários por ano?

ano = sal.groupby('Year')
print(ano['BasePay'].mean(), '\n')

# Quantos títulos de trabalho únicos existem?
print(sal['JobTitle'].nunique(), '\n')

# Quais são os 5 principais empregos mais comuns?
print(sal['JobTitle'].value_counts().head(), '\n')

# Quantos títulos de trabalho foram representados por apenas uma pessoa em 2013?

print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1), '\n')

# Quantas pessoas tem a palavra chefe no seu cargo?

def chief(x):
    if 'chief' in x.lower():
        return True
    else:
        return False

chief = sal['JobTitle'].apply(chief)
print(sum(chief))

# Bônus: Existe uma correlação entre o comprimendo da sequência do título do trabalho e o salário?
sal['Tamanho da String'] = sal['JobTitle'].apply(len)
print(sal[['Tamanho da String', 'TotalPayBenefits']].corr())