import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

print(x, '\n')
print(y)

# PLOT COM UM GRÁFICO

'''
plt.plot(x, y, 'r--')  # DEFINE OS DADOS DO PLOT E APARÊNCIA

plt.xlabel('Eixo X')  # NOME DO EIXO X
plt.ylabel('Eixo y')  # NOME DO EIXO Y
plt.title('Título')  # TÍTULO DO GRÁFICO
plt.show()  # EXIBE O GRÁFICO NA IDE EM UMA NOVA JANELA
'''

# PLOT COM DOIS GRÁFICOS

'''
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r--')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'g*-')
plt.show()
'''

# Criando instâncias da classe matplotlib

figura = plt.figure()  # Instância de matplotlib
# Método para adcionar eixos, lista de quatro argumentos [esquerda, baixo, largura, altura]
axes = figura.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y, 'g*-')
axes.set_xlabel('Eixo X')
axes.set_ylabel('Eixo Y')
axes.set_title('Título')

axes2 = figura.add_axes([0.2, 0.5, 0.3, 0.3])
axes2.plot(y, x, 'r--')
axes2.set_xlabel('Little x')
axes2.set_ylabel('Little y')
axes2.set_title('Little plot')

plt.show()




