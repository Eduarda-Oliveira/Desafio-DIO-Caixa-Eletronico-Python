menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

saques = []
depositos = []

while True:

    opcao = input(menu)

    if opcao == "d":
        print ('Depósito')
        entrada = int(input("Valor do deposito: "))
        saldo += entrada
        depositos.append(entrada)

    elif opcao == "s":
        print ('Saque')
        saida = int(input("Valor do saque: "))
        if saida <=limite and LIMITE_SAQUE != 0 and saldo >= saida:
            saldo -= saida
            LIMITE_SAQUE -=1
            numero_saques +=1
            saques.append(saida)
        else:
            print ('Não foi possivel realizar a opração')

    elif opcao == "e":
        print ('Extrato')
        print ('Entradas: ')
        for x in depositos:
            print ('R$ {:.2f}'.format(x))
        print ('Saidas: ')
        for x in saques:
            print ('R$ {:.2f}'.format(x))
        print ('Saldo: R$ {:.2f}'.format(saldo))

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")