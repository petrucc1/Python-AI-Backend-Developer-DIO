contatos = {
    "sarah@gmail.com": {"nome": "Sarah", "telefone": "11988888888"},
    "muriel@gmail.com": {"nome": "Muriel", "telefone": "11977777777"},
    "jolie@gmail.com": {"nome": "Jolie", "telefone": "11966666666"},
    "jade@gmail.com": {"nome": "Jade", "telefone": "11955555555"},
    "cristalzinha@gmail.com": {"nome": "Cristalzinha", "telefone": "11944444444", "ano": {"idade": 11}}
}

# Acessando um contato específico
contatos["cristalzinha@gmail.com"]["telefone"] # 11944444444

# Acessando um dado dentro de um dicionário dentro de outro dicionário

contatos["cristalzinha@gmail.com"]["ano"]["idade"] # 11
