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

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += 'Depósito: R$ {:.2f} \n'.format(valor) 
        else:
            print ('Operação falhou! Informe um valor valido')



    elif opcao == "s":

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = saldo < valor

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE 
        
        if excedeu_saldo:
            print ('Operação falhou! Você não tem saldo suficiente')

        elif excedeu_limite:
            print ('Operação falhou! O valor do saque excede o limite')

        elif excedeu_saques:
            print ('Operação falhou! Número máximo de saques excedido')

        elif valor > 0:
            saldo -= valor
            numero_saques +=1
            extrato += 'Saque: R$ {:.2f} \n'.format(valor) 

        else:
            print ('Operação falhou! Informe um valor valido')

    elif opcao == "e":

        print ("-------------------------------------extrato-------------------------------------")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print ('Saldo: R$ {:.2f}'.format(saldo))
        print ("---------------------------------------------------------------------------------")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")
