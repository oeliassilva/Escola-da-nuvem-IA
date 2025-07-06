'''
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
'''
def analisador__de_numeros():
    pares = 0
    impares = 0
    
    while True:
        entrada = input("Digite um número inteiro (ou 'sair' para finalizar): ").strip().lower()
        
        if entrada.lower() == 'sair':
            break
        
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                pares += 1
                print(f"{numero} é par.\n")
            else:
                impares += 1
                print(f"{numero} é ímpar.\n")
        except ValueError:
            print("Favor, digitar um número inteiro válido.\n")
            continue
    
    print(f"\nTotal de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")
    print(f"Total de números inseridos: {pares + impares}")
    print("\nObrigado por usar o nosso analisador de números!")

analisador__de_numeros()