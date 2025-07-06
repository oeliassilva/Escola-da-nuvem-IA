'''
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
'''
def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
        except ValueError:
            print("Favor, digitar um número correto")
            continue

        print("Escolha a operação:")
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("0 - Sair")
        operacao = input("Digite a opção (0 a 4): ").strip()

        if operacao == '0':
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Opção inválida! Por favor, digite uma opção entre 0 e 4.")
            continue

        try:
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Favor, digitar um número correto")
            continue

        if operacao == '1':
            resultado = num1 + num2
        elif operacao == '2':
            resultado = num1 - num2
        elif operacao == '3':
            resultado = num1 * num2
        elif operacao == '4':
            if num2 == 0:
                print("Erro: divisão por zero.")
                continue
            resultado = num1 / num2

        print("\nResultado:", resultado, "\n")

        print("Deseja realizar uma nova operação?")
        print("1 - Sim")
        print("2 - Não")
        nova_operacao = input("Escolha uma opção (1 ou 2): ").strip()

        if nova_operacao != '1':
            print("\nObrigado por usar a nossa calculadora!")
            break

calculadora()