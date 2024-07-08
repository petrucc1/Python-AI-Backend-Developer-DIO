# [].append - adiciona um elemento ao final da lista
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, 'Python', [40, 30, 20]]

# [].clear - remove todos os elementos da lista
lista = [1, 'Python', [40, 30, 20]]

print(lista) # [1, 'Python', [40, 30, 20]]

lista.clear()

print(lista) # []

# [].copy - retorna uma cópia da lista
lista = [1, 'Python', [40, 30, 20]]

copia = lista.copy()

print(copia) # [1, 'Python', [40, 30, 20]]

# [].count - conta quantas vezes um elemento aparece na lista
cores = ['vermelho', 'azul', 'verde', 'azul']

cores.count('vermelho') # 1
cores.count('azul') # 2
cores.count('verde') # 1

# [].extend - adiciona elementos de uma lista a outra
linguagens = ['Python', 'Java', 'C++']

print(linguagens) # ['Python', 'Java', 'C++']

linguagens.extend(['JavaScript', 'Ruby']) # lista com elementos que serão adicionados

print(linguagens) # ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']

# [].index - retorna o índice do primeiro elemento com o valor especificado (se houver dado repetido ele retorna apenas a primeira ocorrencia)
linguagens = ['Python', 'Java', 'C++']

linguagens.index('Python') # 0
linguagens.index('Java') # 1

# [].pop - remove o elemento de um índice específico (se não for passado o índice, ele remove o último elemento)
linguagens = ['Python', 'Java', 'C++']

linguagens.pop() # 'C++'
linguagens.pop(1) # 'Java'

print(linguagens) # ['Python']

# [].remove - remove o primeiro elemento com o valor especificado
linguagens = ['Python', 'Java', 'C++']

linguagens.remove('Java')

print(linguagens) # ['Python', 'C++']

# [].reverse - reverte a ordem dos elementos da lista
linguagens = ['Python', 'Java', 'C++']

linguagens.reverse()

print(linguagens) # ['C++', 'Java', 'Python']

# [].sort - ordena a lista
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort() # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# [].sort(reverse=True) - ordena a lista em ordem decrescente
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort(reverse=True) # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# [].sort(key=lambda x: len(x)) - ordena a lista com base no tamanho dos elementos
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort(key=lambda x: len(x)) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# [].sort(key=lambda x: len(x), reverse=True) - ordena a lista com base no tamanho dos elementos em ordem decrescente
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort(key=lambda x: len(x), reverse=True) # [1, 1, 3, 3, 5, 5, 5, 4, 9, 2, 6]

# len - retorna o tamanho da lista
linguagens = ['Python', 'Java', 'C++']

len(linguagens) # 3

# sorted - retorna uma lista ordenada
linguagens = ['Python', 'Java', 'C++']

# ordena a lista em ordem crescente
sorted(linguagens, key=lambda x: len(x)) # ['Java', 'C++', 'Python']

# ordena a lista em ordem decrescente
sorted(linguagens, key=lambda x: len(x), reverse=True) # ['Python', 'Java', 'C++']