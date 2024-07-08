# Mais performático
# List Comprehension

# Filtro Exemplo 1
numeros = [1, 30, 11, 29, 2, 10, 3, 5, 7, 9, 8, 6, 4]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Filtro Exemplo 2
numeros = [1, 30, 11, 29, 2, 10, 3, 5, 7, 9, 8, 6, 4]
pares = [numero for numero in numeros if numero % 2 == 0]

# Modificando valores
numeros = [1, 30, 11, 29, 2, 10, 3, 5, 7, 9, 8, 6, 4]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
