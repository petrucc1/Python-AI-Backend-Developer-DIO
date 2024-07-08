#Old style %
nome = 'João'
idade = 22
profissao = 'programador'
linguagem = 'Python'

print('Olá, %s. Você tem %d anos e é %s. Você gosta de programar em %s?' % (nome, idade, profissao, linguagem))

# .format() style
# 1. Sem especificar a ordem
print('Olá, {}. Você tem {} anos e é {}. Você gosta de programar em {}?'.format(nome, idade, profissao, linguagem))
# 2. Especificando a ordem
print('Olá, {0}. Você tem {1} anos e é {2}. Você gosta de programar em {3}?'.format(nome, idade, profissao, linguagem))
# 3. Especificando o nome
print('Olá, {nome}. Você tem {idade} anos e é {profissao}. Você gosta de programar em {linguagem}?'.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
# 4. Usando um dicionário
print('Olá, {nome}. Você tem {idade} anos e é {profissao}. Você gosta de programar em {linguagem}?'.format(**pessoa))
# Dicionário usado acima
pessoa = {'nome': 'João', 'idade': 22, 'profissao': 'programador', 'linguagem': 'Python'}

# f-string style
print(f'Olá, {nome}. Você tem {idade} anos e é {profissao}. Você gosta de programar em {linguagem}?')

PI = 3.14159265359
print(f'O valor de PI é {PI:.2f}')
# O valor de PI é 3.14

print(f'O valor de PI é {PI:10.2f}')
# O valor de PI é       3.14
