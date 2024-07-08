import sys

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

# Condição simples com if e else
if saldo >= saque:
    print("Realizando saque.")
else:
    print("Saldo insuficiente.")

# Adição de uma ou mais condições utilizando o elif
opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato"))

if opcao == 1:
    valor = float(input("Informe uma quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida!")

# If aninhado
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")
    else:
        print("Não foi possível executar o saque. Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Conta não encontrada! Entre em contato com o seu gerente.")

# If ternário
status = "Sucesso!" if saldo >= saque else "Falha."
print(f"{status} ao realizar o saque!")
