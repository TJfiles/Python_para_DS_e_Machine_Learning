import pandas as pd
import numpy as np

# Importe o arquivo CSV em um dataframe chamado ecom
ecom = pd.read_csv('Ecommerce Purchases')

# Verifique o head do DataFrame
print(ecom.head(), '\n')

# Quantas linhas e colunas existem?
print(ecom.info(), '\n')

# Qual é o preço de compra médio?
print(ecom['Purchase Price'].mean(), '\n')

# Quais foram os preços de compra mais altos e baixos?
print(ecom['Purchase Price'].max(), '\n')
print(ecom['Purchase Price'].min(), '\n')

# Quantas pessoas tem Inglês 'en' como sua lingua de escolha no site?
print(len(ecom[ecom['Language'] == 'en']), '\n')

# Quantas pessoas tem o cargo de Advogado?
print(sum(ecom['Job'] == 'Lawyer'), '\n')

# Quantas pessoas fizeram a compra durante a AM e quantas pessoas fizeram a compra durante o PM?
print(ecom['AM or PM'].value_counts(), '\n')

# Quais são os 5 títulos de trabalhos mais comuns?
print(ecom['Job'].value_counts().head(), '\n')

# Alguém fez uma compra que veio do LOT: '90 WT', Qual foi o valor de compra para esta transação?
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'], '\n')

# Qual é o email da pessoa com o seguinte cartão de crédito: 4926535242672853
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'], '\n')

# Quantas pessoas tem o American Express como seu fornecedor de cartão de Crédito e fizeram uma compra acima de US$95?
print(len(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)]), '\n')

# Quantas pessoas tem um cartão de crédito que expira em 2025?
def exp_date(x):
    if x[3:] == '25':
        return True
    else:
        return False


print(sum(ecom['CC Exp Date'].apply(exp_date)), '\n')

# Quais são os 5 principais provedores de email / host mais populares (por exemplo: gmail.com, yahoo.com, etc.


def host(x):
    at = x.find('@')
    host = x[at:]
    return host


host = ecom['Email'].apply(host)
print(host.value_counts().head())
