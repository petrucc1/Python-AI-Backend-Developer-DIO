# [].count() -> Retorna o número de vezes que um valor ocorre na tupla.
cores = ('verde', 'amarelo', 'azul', 'vermelho',)

cores.count('verde') # 1
cores.count('azul') # 1
cores.count('preto') # 0

# [].index() -> Retorna o índice da primeira ocorrência de um valor na tupla.

linguagens = ("python", "java", "c", "c++", "python", "java", "c", "c++",)

linguagens.index("python") # 0
linguagens.index("java") # 1

# len() -> Retorna o número de elementos da tupla.

linguagens = ("python", "java", "c", "c++", "python", "java", "c", "c++",)

len(linguagens) # 8
