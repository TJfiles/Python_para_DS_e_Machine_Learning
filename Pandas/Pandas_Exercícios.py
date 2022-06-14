# https://www.templodocodigo.com.br/post/exerc%C3%ADcios-python-pandas

import pandas as pd
import numpy as np

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
print(df[df['TotalPay'] == df['TotalPay'].max()]['EmployeeName'], '\n')

# Ex7- Qual é o salário médio por ano?

# Ex8- Quais são os cinco empregos mais comuns (JobTitle)?

# Ex9- Existe correlação entre ano e salário?

# Ex10- Como criar um outro dataframe selecionando apenas algumas colunas do dataframe original?


# https://www.machinelearningplus.com/python/101-pandas-exercises-python/

# 1. How to import pandas and check the version?
print(pd.__version__, '\n')

# 2. How to create a series from a list, numpy array and dict?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

s1 = pd.Series(mylist)
s2 = pd.Series(myarr)
s3 = pd.Series(mydict)

# 3. How to convert the index of a series into a column of a dataframe?
# Convert the series ser into a dataframe with its index as another column on the dataframe.

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df = ser.to_frame().reset_index()
print(df.head(), '\n')

# 4. How to combine many series to form a dataframe?
# Combine ser1 and ser2 to form a dataframe.

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.DataFrame(ser1, ser2)
print(df.head(), '\n')

# Solution 1
df = pd.concat([ser1, ser2], axis=1)
print(df.head(), '\n')
# Solution 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2})
print(df.head(), '\n')

# 5. How to assign name to the series’ index?

ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

ser.name = 'Alphabets'
print(ser.head(), '\n')
