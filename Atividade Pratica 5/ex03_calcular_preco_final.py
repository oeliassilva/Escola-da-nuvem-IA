'''
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
'''
def calcular_preco_final(preco, desconto_percentual):
    desconto = preco * (desconto_percentual / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)

while True:
    try:
        preco = float(input("Digite o preço do produto (R$): "))
        desconto = float(input("Digite o desconto (%): "))
        final = calcular_preco_final(preco, desconto)
        print(f"Preço final com desconto: R$ {final:.2f}")

        print("\nDeseja verificar mais alguam desconto? ")
        print ("1 - Sim")
        print ("2 - Não")
        opcao = input("Escolha uma opção (1 ou 2): ").strip()
        if opcao == '1':
            continue
        else:
            print("Obrigado por usar a nossa calculadora de desconto!")
    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos.")


