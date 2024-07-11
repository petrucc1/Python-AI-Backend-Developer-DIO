"""
Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.
"""

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

# Não confiar que ele trará os elementos na ordem que você passou
set('abacate') # {'a', 'b', 'c', 'e', 't'}

set(("palio", "gol", "uno", "palio")) # {'palio', 'gol', 'uno'}

# É possível criar um set utilizando chaves
linguagens = {"Python", "Java", "C", "C++", "Python"}
print(linguagens) # {'Java', 'Python', 'C', 'C++'}

