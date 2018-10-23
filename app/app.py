from services.services import *
from services.attributes import *

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
            staging = StagingArea()
            while True:
                opc = input('>>')

                if len(opc) >= 8 and opc[:8] == 'copy con':
                    name = opc.split()[2]
                    content = input('con: ')
                    repo.create_file(name, content)

                elif len(opc) >= 7 and opc[:7] == 'git add':
                    name = opc.split()[2]
                    repo.add(name)
                    for file in repo.files:
                        if file.name == name:
                            packed = {file.name, file.status.type}
                            if file.status.staged is False:
                                staging.rm_unstage_area(packed)
                                staging.add_stage_area(packed)
                            else:
                                staging.add_stage_area(packed)

                elif len(opc) >= 4 and opc[:4] == 'edit':
                    name = opc.split()[1]
                    content = input()
                    repo.edit(name, content)
                    for file in repo.files:
                        if file.name == name:
                            packed = {file.name, file.status.type}
                            staging.add_unstage_area(packed)

                elif opc == 'remove':
                    name = opc.split()[1]
                    repo.remove_file(name)

                elif opc == 'dir':
                    for file in repo.files:
                        if file.status is None:
                            print(file.name)
                        else:
                            for sta in staging.stageds:
                                print('Stagging Area')
                                print(sta)
                            for sta in staging.unstageds:
                                print('Unstagging Area')
                                print(sta)

                else:
                    print('error')

        else:
            print('Comece com o "git init"')


if __name__ == '__main__':
    main()
