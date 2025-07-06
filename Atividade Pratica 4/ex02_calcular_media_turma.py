'''
2 - Criar um código que registre as notas de alunos e calcular a média da turma.

'''
def calcular_media_turma():
    notas = []
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ").strip().lower()
        if nome.lower() == 'sair':
            break
        
        try:
            nota = float(input(f"Digite a nota de {nome}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"Nota de {nome} registrada: {nota}\n")
            else:
                print("Nota inválida! Deve estar entre 0 e 10.\n")
        except ValueError:
            print("Favor, digitar um número válido.\n")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
        print(f"Total de alunos registrados: {len(notas)}")
    else:
        print("\nNenhuma nota foi registrada.")

calcular_media_turma()