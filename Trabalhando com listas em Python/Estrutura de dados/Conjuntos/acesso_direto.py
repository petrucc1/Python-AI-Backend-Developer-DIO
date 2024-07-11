"""
Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores 
é necessário converter o conjunto para lista.
"""

# Convertendo um conjunto para lista
numeros = {1, 2, 3, 2}

numeros = list(numeros)

numeros[0] # 1
