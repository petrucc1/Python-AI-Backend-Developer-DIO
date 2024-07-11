numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1) # {2, 3, 4, 5, 6, 7, 8, 9, 0}

# Se o elemento a ser removido não existe, ele apenas ignora, diferente do método remove
numeros.discard(45) # {2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}
