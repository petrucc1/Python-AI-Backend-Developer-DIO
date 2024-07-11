dados = {nome: 'João', idade: 25, cidade: 'São Paulo'}

# Podemos acessar os valores diretamente pelas chaves
dados["nome"] # João
dados["idade"] # 25
dados["cidade"] # São Paulo

# Podemos adicionar novos pares chave-valor
dados["nome"] = "Maria"
dados["idade"] = 30
dados["cidade"] = "Rio de Janeiro"

dados # {'nome': 'Maria', 'idade': 30, 'cidade': 'Rio de Janeiro'}
