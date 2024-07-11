# clear
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"},
    "muriel@gmail.com": {"nome": "Muriel", "telefone": "11977777777"},
    "jolie@gmail.com": {"nome": "Jolie", "telefone": "11966666666"},
    "jade@gmail.com": {"nome": "Jade", "telefone": "11955555555"},
    "cristalzinha@gmail.com": {"nome": "Cristalzinha", "telefone": "11944444444", "ano": {"idade": 11}}
}

contatos.clear()
contatos # {}


# copy
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"}
}

copia = contatos.copy()
copia["sarah@gmail.com"] = {"nome": "Petrucci"}

contatos["sarah@gmail.com"] # {'nome': 'Sarah', 'telefone': '11988888888'}

copia["sarah@gmail.com"] # {'nome': 'Petrucci'}


# fromkeys
dict.fromkeys(["nome", "telefone"]) # {'nome': None, 'telefone': None}

dict.fromkeys(["nome", "telefone"], "vazio") # {'nome': 'vazio', 'telefone': 'vazio'}


# get
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"}
}

# Isso acontece porque a chave "chave" não existe no dicionário
contatos["chave"] # KeyError: 'chave'

# Então, para evitar esse erro, podemos usar o método get, se a chave não existir, ele retorna None
# Também tem uma funcionalidade a mais, que é passar um valor padrão, caso a chave não exista, como um dicionário vazio {}
contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("sarah@gmail.com", {}) # {'nome': 'Sarah', 'telefone': '11988888888'}


# items
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"}
}

contatos.items() # dict_items([('sarah@gmail.com', {'nome': 'Sarah', 'telefone': '11988888888'})])


# keys
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"}
}

contatos.keys() # dict_keys(['sarah@gmail.com'])

# Retorna apenas as chaves do dicionário
novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
novo_dicionario.keys() # dict_keys(['a', 1, 'b'])


# pop
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"}
}

contatos.pop("sarah@gmail.com") # {'nome': 'Sarah', 'telefone': '11988888888'}

contatos.pop("sarah@gmail.com", {}) # {}


# popitem
# A diferença entre o popitem e o pop é que o popitem remove o último item do dicionário e o pop remove um item específico
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"}
}

contatos.popitem() # ("sarah@gmail.com", {'nome': 'Sarah', 'telefone': '11988888888'})

contatos.popitem() # KeyError: 'popitem(): dictionary is empty'


# setdefault
contato = {"nome": "Sarah", "telefone": "11988888888"}

# Se o atributo existir, ele retorna o valor original
contato.setdefault("nome", "Cristal") # 'Sarah'
contato # {'nome': 'Sarah', 'telefone': '11988888888'}

# Se o atributo não existir, ele cria um novo
contato.setdefault("idade", 28) # 28
contato # {'nome': 'Sarah', 'telefone': '11988888888', 'idade': 28}


# update
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"}
}

contatos.update({"sarah@gmail.com": {"nome": "Petrucci"}})
contatos # {'sarah@gmail.com': {'nome': 'Petrucci'}}

contatos.update({"sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"}})
contatos # {'sarah@gmail.com': {'nome': 'Sarah', 'telefone': '11988888888'}}


# values
# Retorna apenas os valores do dicionário
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"},
    "muriel@gmail.com": {"nome": "Muriel", "telefone": "11977777777"},
    "jolie@gmail.com": {"nome": "Jolie", "telefone": "11966666666"},
    "jade@gmail.com": {"nome": "Jade", "telefone": "11955555555"},
    "cristalzinha@gmail.com": {"nome": "Cristalzinha", "telefone": "11944444444", "ano": {"idade": 11}}
}

contatos.values() # dict_values([{'nome': 'Sarah', 'telefone': '11988888888'}, {'nome': 'Muriel', 'telefone': '11977777777'}, {'nome': 'Jolie', 'telefone': '11966666666'}, {'nome': 'Jade', 'telefone': '11955555555'}, {'nome': 'Cristalzinha', 'telefone': '11944444444', 'ano': {'idade': 11}}])


# in
contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"},
    "muriel@gmail.com": {"nome": "Muriel", "telefone": "11977777777"},
    "jolie@gmail.com": {"nome": "Jolie", "telefone": "11966666666"},
    "jade@gmail.com": {"nome": "Jade", "telefone": "11955555555"},
    "cristalzinha@gmail.com": {"nome": "Cristalzinha", "telefone": "11944444444", "ano": {"idade": 11}}
}

"sarah@gmail.com" in contatos # True
"sarahpetrucci@gmail.com" in contatos # False
"idade" in contatos["sarah@gmail.com"] # False 
"telefone" in contatos["sarah@gmail.com"] # True

