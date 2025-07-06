'''
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada

'''

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

while True:
 
    entrada = input("Digite o valor da conta (ou 'sair' para finalizar): ").strip().lower()
        
    if entrada == 'sair':
        print("Obrigado por usar o nosso Calculador de Gorjetas!")
        break
    try:
        valor_conta = float(entrada)

        if valor_conta < 0:
            print("Erro: Valor não pode ser negativo.")
            continue
        if valor_conta == 0:
            print("A sua conta ainda está zerada!")
        else:
            porcentagem_gorjeta = float(input("Porcentagem de gorjeta (%): "))
            if porcentagem_gorjeta < 0:
                print("Erro: Porcentagem não pode ser negativa.")
                continue
                
            else:
                gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
                print(f"Gorjeta: R${gorjeta:.2f}")
                print(f"Total com gorjeta: R${valor_conta + gorjeta:.2f}")
    except ValueError:
        print("Erro: Digite números válidos ou 'sair' para encerrar.")
