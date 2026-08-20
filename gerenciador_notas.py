"""
Gerenciador de Notas de Alunos
Autor: Richard Barsotti Silva

Sistema via terminal para cadastrar alunos, lançar notas de disciplinas,
calcular médias e verificar situação (aprovado/reprovado/recuperação).
"""

alunos = {}
proximo_id = 1

MEDIA_APROVACAO = 7.0
MEDIA_RECUPERACAO = 5.0


def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n===== GERENCIADOR DE NOTAS =====")
    print("1 - Cadastrar aluno")
    print("2 - Lançar nota")
    print("3 - Listar alunos")
    print("4 - Ver boletim de um aluno")
    print("5 - Remover aluno")
    print("6 - Sair")


def obter_numero(mensagem, tipo=float):
    """Solicita um número ao usuário, validando a entrada."""
    while True:
        try:
            return tipo(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def cadastrar_aluno():
    """Cadastra um novo aluno no sistema."""
    global proximo_id
    nome = input("Nome do aluno: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return

    alunos[proximo_id] = {"nome": nome, "notas": {}}
    print(f"Aluno '{nome}' cadastrado com ID {proximo_id}.")
    proximo_id += 1


def lancar_nota():
    """Lança a nota de uma disciplina para um aluno."""
    aluno_id = int(obter_numero("ID do aluno: ", int))
    if aluno_id not in alunos:
        print("Aluno não encontrado.")
        return

    disciplina = input("Nome da disciplina: ").strip()
    if not disciplina:
        print("Disciplina não pode ser vazia.")
        return

    nota = obter_numero("Nota (0 a 10): ", float)
    if nota < 0 or nota > 10:
        print("Nota inválida. Deve estar entre 0 e 10.")
        return

    alunos[aluno_id]["notas"][disciplina] = nota
    print(f"Nota de {disciplina} lançada para {alunos[aluno_id]['nome']}.")


def calcular_situacao(media):
    """Retorna a situação do aluno com base na média."""
    if media >= MEDIA_APROVACAO:
        return "Aprovado"
    elif media >= MEDIA_RECUPERACAO:
        return "Recuperação"
    else:
        return "Reprovado"


def listar_alunos():
    """Lista todos os alunos cadastrados com sua média geral."""
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print(f"\n{'ID':<5}{'Nome':<20}{'Média':<10}{'Situação':<15}")
    print("-" * 50)
    for aluno_id, dados in alunos.items():
        notas = dados["notas"].values()
        media = sum(notas) / len(notas) if notas else 0
        situacao = calcular_situacao(media) if notas else "Sem notas"
        print(f"{aluno_id:<5}{dados['nome']:<20}{media:<10.2f}{situacao:<15}")


def ver_boletim():
    """Exibe o boletim completo de um aluno, com notas por disciplina."""
    aluno_id = int(obter_numero("ID do aluno: ", int))
    aluno = alunos.get(aluno_id)
    if not aluno:
        print("Aluno não encontrado.")
        return

    print(f"\n===== BOLETIM: {aluno['nome']} =====")
    if not aluno["notas"]:
        print("Nenhuma nota lançada ainda.")
        return

    for disciplina, nota in aluno["notas"].items():
        print(f"{disciplina}: {nota:.1f}")

    media = sum(aluno["notas"].values()) / len(aluno["notas"])
    situacao = calcular_situacao(media)
    print(f"\nMédia geral: {media:.2f}")
    print(f"Situação: {situacao}")


def remover_aluno():
    """Remove um aluno do sistema."""
    aluno_id = int(obter_numero("ID do aluno: ", int))
    if aluno_id in alunos:
        nome = alunos[aluno_id]["nome"]
        del alunos[aluno_id]
        print(f"Aluno '{nome}' removido com sucesso.")
    else:
        print("Aluno não encontrado.")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            lancar_nota()
        elif opcao == "3":
            listar_alunos()
        elif opcao == "4":
            ver_boletim()
        elif opcao == "5":
            remover_aluno()
        elif opcao == "6":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
