# https://www.templodocodigo.com.br/post/exerc%C3%ADcios-python-pandas

import pandas as pd

salaries = pd.read_csv('Salaries.csv')
df = pd.DataFrame(salaries)
# A partir da base de dados Salaries, responder às questões abaixo:

# Ex1- Quais colunas tem nesta base?
print(df.columns, '\n')

# Ex2- Qual é a coluna de salario base?
print(df['BasePay'], '\n')

# Ex3- Qual é o salário médio?
print(df['TotalPay'].mean(), '\n')

# Ex4- Qual é o salário máximo?
print(df['TotalPay'].max(), '\n')

# Ex5- Qual é o emprego do JOSEPH DRISCOLL?
print(df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPay'], '\n')

# Ex6- Qual o nome da pessoa que tem o maior salário de todos?
print(df[df['TotalPay'] == df['TotalPay'].max()]['EmployeeName'])

# Ex7- Qual é o salário médio por ano?

# Ex8- Quais são os cinco empregos mais comuns (JobTitle)?

# Ex9- Existe correlação entre ano e salário?

# Ex10- Como criar um outro dataframe selecionando apenas algumas colunas do dataframe original?