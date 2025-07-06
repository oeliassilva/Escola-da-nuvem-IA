'''
2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
'''
import unicodedata

def formata_texto(texto):
    texto = texto.lower().replace(" ", "")
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn' and c.isalnum()
    )
    return texto

def verifica_palindromo(texto):
    texto = formata_texto(texto)
    return texto == texto[::-1]

while True:

    try:
        entrada = input("Digite uma palavra ou frase ou 'sair' para finalizar: ").strip().lower()
        if entrada == 'sair':
            print("Obrigado por usar o nosso verificador de Políndromo!")
            break
        
        if not entrada.strip():
            raise ValueError("Entrada vazia.")
        print("Sim" if verifica_palindromo(entrada) else "Não")
    except ValueError as erro:
        print(f"Erro: {erro}")
