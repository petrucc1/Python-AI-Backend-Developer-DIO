# É um conjunto de pares chave-valor, onde a chave é um identificador único e o valor é o dado associado a essa chave.
# Dicionários são mutáveis, ou seja, podem ser alterados durante a execução do programa.
# Dicionários são representados por chaves {} e os pares chave-valor são separados por vírgula.
# As chaves podem ser de qualquer tipo imutável, como inteiros, strings, tuplas, etc.
# Os valores podem ser de qualquer tipo, inclusive listas, dicionários e funções.
# Dicionários são úteis para armazenar dados de forma organizada e acessá-los de maneira eficiente.

pessoa = {nome: 'João', idade: 25, cidade: 'São Paulo'}

pessoa = dict(nome='João', idade=25, cidade='São Paulo')

pessoa["telefone"] = "11999999999" # {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo', 'telefone': '11999999999'}
