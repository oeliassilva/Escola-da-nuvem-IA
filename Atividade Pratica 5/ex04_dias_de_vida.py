'''
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
'''
from datetime import datetime

while True:
    try:
        data_nascimento = input("Digite sua data de nascimento (formato: DD/MM/AAAA) ou 'sair' para finalizar: ").strip().lower()
        if data_nascimento == 'sair':
            print("Obrigado por usar a nossa calculadora de dias de vida!")
            break
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        dias_vivo = (hoje - nascimento).days
        data_formatada = hoje.strftime("%d/%m/%Y")
        print(f"Hoje é dia {data_formatada} e você está vivo há {dias_vivo} dias.")

        print ("\nDeseja realizar mais algum cálculo?")
        print ("1 - Sim")
        print ("2 - Não")
        opcao = input ("Digite uma opcão ( 1 ou 2): ").strip()
        if opcao == 1:
            continue
        else:
            print("Obrigado por usar a nossa calculadora de dias de vida!")
    except ValueError:
        print("Erro: Data inválida. Use o formato DD/MM/AAAA.")
