#menu
print("""-------- MENU --------
     [1] DEPÓSITO
     [2] SAQUE
     [3] EXTRATO
     [4] SAIR
----------------------""")

extrato = ""
saldo = 0
LIMITE_SAQUE = 500.00
nro_saque = 3

while True:
    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        print("Opção selecionada: DEPÓSITO")
        valor_deposito = float(input("Informe o valor a ser depositado: "))
        if valor_deposito < 0:
            print("Erro!!! Depósito somente de valores positivos maiores que zero!")
        else:
            saldo = saldo + valor_deposito
            extrato = extrato + (f"Depósto: {valor_deposito:.2f}\n")
    elif opcao == 2:
        print("Opção selecionada: SAQUE")
        valor_saque = float(input("Informe o valor do saque: "))
        if valor_saque > LIMITE_SAQUE:
            print("Opção inválida! Valor maior do que o permitido por saque.")
        elif valor_saque > saldo:
            print("Opção inválida! Saldo insuficiente.")
        elif nro_saque <= 0:                
                print("Opção inválida! Numero de saques excedido.")
        else:
            saldo = saldo - valor_saque
            extrato = extrato + (f"Saque: {valor_saque:.2f}\n")
            nro_saque = nro_saque - 1

    elif opcao == 3:
        print("Opção selecionada: EXTRATO")
        print("-------- EXTRATO --------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: {saldo:.2f}")
        print("----------------------")
    
    elif opcao == 4:
        print("Saindo...")
        break

    else:
        print("Opção inválida! Selecione uma opção válida.")
