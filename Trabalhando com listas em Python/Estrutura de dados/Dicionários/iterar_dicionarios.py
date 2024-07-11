# Para acessar os valores do dicionário será necessário informar o nome dele junto com a chave novamente, isso não é muito prático e não possui uma leitura muito clara
for chave in contatos:
    print(chave, contatos[chave])

# Podemos usar o método items() para iterar sobre um dicionário, ele retorna uma lista de tuplas, onde cada tupla contém a chave e o valor correspondente.
# Mais recomendado para iterar sobre dicionários, pois é mais eficiente.
for chave, valor in contatos.item():
    print(chave, valor)

# O resultado para ambos os casos será:
# "sarah@gmail.com" {'nome': 'Sarah', 'telefone': '11988888888'}
# "muriel@gmail.com" {'nome': 'Muriel', 'telefone': '11977777777'}
# "jolie@gmail.com" {'nome': 'Jolie', 'telefone': '11966666666'}
# "jade@gmail.com" {'nome': 'Jade', 'telefone': '11955555555'}
# "cristalzinha@gmail.com" {'nome': 'Cristalzinha', 'telefone': '11944444444', 'ano': {'idade': 11}}
