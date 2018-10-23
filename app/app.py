from services import *


def main():
    files = []

    menu = '*** GIT ***' \
           '1 - Criar Repositório\n' \
           '2 - Adicionar novo arquivo em seu repositório\n' \
           '3 - Listar arquivos do repositório\n' \
           '4 - Alterar ou excluir arquivo\n' \
           '5 - Add: adicionar a Stage Zone as alterações de um arquivo\n' \
           '6 - Add: adicionar a Stage Zone as todas as alterações\n' \
           '7 - Reset: desfazer última alteração da Stage Zone\n' \
           '8 - Commit: confirmar alterações\n' \
           '9 - Status: listar alterações pendentes\n' \
           '10 - Log: listar commits\n' \
           '11 - Remote add: associar repositórios\n' \
           '12 - Push: enviar commits para o repositório remoto\n' \
           '13 - Pull: receber commits para o repositório local\n' \
           '14 - Remote remove: desvincular repositório remoto\n'

    while True:
        opcao = input(menu)

        if opcao == 'git init':
            repo = Repo()

        if opcao == 2:
            name = input()
            content = input()
            file = File(name, content)
            files.append({file: 'new_file'})


if __name__ == '__main__':
    main()
