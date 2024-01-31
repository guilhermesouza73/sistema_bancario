menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":      
      valor_deposito = float(input("Digite o valor que deseja depositar: ")) 
      if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
      else:
        print("Operação não realizada. Valor informado incorretamente.")
      
    elif opcao == "2":
      valor_saque = float(input("Digite o valor que deseja sacar (máximo R$ 500,00): "))
      if saldo > valor_saque:
        if valor_saque <= 500 and numero_saques <= 3:
          saldo -= valor_saque
          extrato += f"Saque: R$ {valor_saque:.2f}\n"
          numero_saques += 1
        else:
          print("Limite de saques diários excedidos ou saque superior ao limite de R$500,00.")
      else:
        print("Não foi possível realizar a operação. Saldo indisponível.")
        
    elif opcao == "3":
      if extrato != "":
        print(extrato)
        print(f"Seu saldo final é de: R$: {saldo:.2f}")
      else:
        print("Não foram realizadas movimentações em sua conta.")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")