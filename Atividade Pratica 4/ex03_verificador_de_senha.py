'''
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
'''
def verificador_senha():
    while True:
        senha = input("Digite a senha (ou 'sair' para finalizar): ").strip().lower()
        
        if senha.lower() == 'sair':
            print("\nPrograma encerrado.")
            break
        
        if len(senha) < 8:
            print("Erro: A senha deve ter pelo menos 8 caracteres.\n")
            continue
        
        senha_com_numero = "0123456789"
        if not any(caractere in senha_com_numero for caractere in senha):
            print("Erro: A senha deve conter pelo menos um número.\n")
            continue
        
        if not senha_com_numero:
            print("(Erro: A senha deve conter pelo menos um número.\n")
            continue
        
        print(f"A senha '{senha}' é válida! Atende a todos os requistos de segurança!\n")
        
        print("Deseja verificar outra senha?")
        print("1 - Sim")
        print("2 - Não")
        opcao = input("Escolha uma opção (1 ou 2): ").strip()
        
        if opcao != '1':
            print("\nObrigado por usar o nosso verificador de senha!")
            break
        print("\n")

verificador_senha()