from services.services import *


def main():

    menu = '*** GIT ***' \
           'Criar Repositório\n' \
           'Adicionar novo arquivo em seu repositório\n' \
           'Listar arquivos do repositório\n' \
           'Alterar ou excluir arquivo\n' \
           'Add: adicionar a Stage Zone as alterações de um arquivo\n' \
           'Add: adicionar a Stage Zone as todas as alterações\n' \
           'Reset: desfazer última alteração da Stage Zone\n' \
           'Commit: confirmar alterações\n' \
           'Status: listar alterações pendentes\n' \
           'Log: listar commits\n' \
           'Remote add: associar repositórios\n' \
           'Push: enviar commits para o repositório remoto\n' \
           'Pull: receber commits para o repositório local\n' \
           'Remote remove: desvincular repositório remoto\n'

    while True:
        opc = input(menu)

        if opc == 'git init':
            repo = Repo()
            while True:
                opc = input('>>')

                if len(opc) >= 8 and opc[:8] == 'copy con':
                    name = opc.split()[2]
                    content = input('con: ')
                    repo.create_file(name, content)

                elif len(opc) >= 7 and opc[:7] == 'git add':
                    name = opc.split()[2]
                    repo.add(name)

                elif len(opc) >= 4 and opc[:4] == 'edit':
                    name = opc.split()[1]
                    content = input()
                    repo.edit(name, content)

                elif opc == 'remove':
                    name = opc.split()[1]
                    repo.remove_file(name)

                elif opc == 'dir':
                    for file in repo.files:
                        if file.status is None:
                            print(file.name)
                        else:
                            if file.status.staged:
                                print('Stagging Area')
                                print(file.name, ':', file.status.type)
                            if file.status.staged is False:
                                print('Unstagging Area')
                                print(file.name, ':', file.status.type)

                else:
                    print('kmdkkfmkfm')

        else:
            print('Comece com o "git init"')


if __name__ == '__main__':
    main()
