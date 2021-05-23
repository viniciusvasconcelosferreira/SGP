from controller import Controller

print('|======================================================|')
print('|BEM VINDO AO SISTEMA DE GERENCIAMENTO DE PESSOAS - SGP|')
print('|======================================================|')
print()
listPessoaMedico = []
listPessoaAdvogado = []
while True:
    print('|=============================|')
    print('|          SISTEMAS           |')
    print('|=============================|')
    print('|1 - Advogado                 |')
    print('|2 - Médico                   |')
    print('|3 - Sair                     |')
    print('|=============================|')
    sistema = int(input('Escolha uma das opções acima: '))
    print()
    if sistema == 1:
        while True:
            print('|=============================|')
            print('|            MENU             |')
            print('|=============================|')
            print('|1 - Adicionar                |')
            print('|2 - Listar                   |')
            print('|3 - Pesquisar                |')
            print('|4 - Qtd. de Cadastros        |')
            print('|5 - Atualizar                |')
            print('|6 - Excluir Pessoa           |')
            print('|7 - Excluir Pessoas          |')
            print('|8 - Sair                     |')
            print('|=============================|')
            opcao = int(input('Escolha uma das opções acima: '))
            print()
            if opcao == 1:
                print('|====================================|')
                print('|        CADASTRO DE ADVOGADO        |')
                print('|====================================|')
                oab = int(input('Digite o registro do advogado: '))
                nome = input('Digite o nome do advogado: ')
                idade = int(input('Digite a idade do advogado: '))
                data_nascimento = input('Digite a data de nascimento do advogado: ')
                cpf = int(input('Digite o CPF do advogado: '))
                telefone = int(input('Digite o telefone do advogado: '))
                listPessoaAdvogado.append(Controller.inserirAdvogado(oab, nome, idade, data_nascimento, cpf, telefone))
                print(f'Advogado {nome} cadastrado com sucesso!')
                print()
            elif opcao == 2:
                print('|=====================================|')
                print('|        LISTAGEM DE ADVOGADOS        |')
                print('|=====================================|')
                Controller.listarAdvogado(listPessoaAdvogado)
                print()
            elif opcao == 3:
                print('|====================================|')
                print('|        PESQUISA DE ADVOGADO        |')
                print('|====================================|')
                nome = input('Digite o nome do advogado para a pesquisa: ')
                Controller.pesquisaNomeAdvogado(listPessoaAdvogado, nome)
                print()
            elif opcao == 4:
                print('|==================================|')
                print('|            QUANTIDADE            |')
                print('|     DE ADVOGADOS CADASTRADOS     |')
                print('|            NO SISTEMA            |')
                print('|==================================|')
                print(
                    f"Existem {'0' if len(listPessoaAdvogado) == 0 else len(listPessoaAdvogado)} advogados "
                    f"cadastrados no sistema")
                print()
            elif opcao == 5:
                pass
            elif opcao == 6:
                print('|====================================|')
                print('|        EXCLUSÃO DE ADVOGADO        |')
                print('|====================================|')
                nome = input('Digite o nome do advogado para exclusão: ')
                print(Controller.deleteNomeAdvogado(listPessoaAdvogado, nome))
                print()
            elif opcao == 7:
                print('|====================================|')
                print('|    ZERAR REGISTRO DOS ADVOGADOS    |')
                print('|====================================|')
                print(Controller.deleteAllAdvogados(listPessoaAdvogado))
                print()
            else:
                break
    elif sistema == 2:
        while True:
            print('|=============================|')
            print('|            MENU             |')
            print('|=============================|')
            print('|1 - Adicionar                |')
            print('|2 - Listar                   |')
            print('|3 - Pesquisar                |')
            print('|4 - Qtd. de Cadastros        |')
            print('|5 - Atualizar                |')
            print('|6 - Excluir Pessoa           |')
            print('|7 - Excluir Pessoas          |')
            print('|8 - Sair                     |')
            print('|=============================|')
            opcao = int(input('Escolha uma das opções acima: '))
            print()
            if opcao == 1:
                print('|====================================|')
                print('|        CADASTRO DE MÉDICO          |')
                print('|====================================|')
                crm = int(input('Digite o registro do médico: '))
                nome = input('Digite o nome do médico: ')
                idade = int(input('Digite a idade do médico: '))
                data_nascimento = input('Digite a data de nascimento do médico: ')
                cpf = int(input('Digite o CPF do médico: '))
                telefone = int(input('Digite o telefone do médico: '))
                listPessoaMedico.append(Controller.inserirMedico(crm, nome, idade, data_nascimento, cpf, telefone))
                print(f'Médico {nome} cadastrado com sucesso!')
                print()
            elif opcao == 2:
                print('|===================================|')
                print('|        LISTAGEM DE MÉDICOS        |')
                print('|===================================|')
                Controller.listarMedico(listPessoaMedico)
                print()
            elif opcao == 3:
                print('|===================================|')
                print('|        PESQUISA DE MÉDICOS        |')
                print('|===================================|')
                nome = input('Digite o nome do advogado para a pesquisa: ')
                Controller.pesquisaNomeMedico(listPessoaMedico, nome)
                print()
            elif opcao == 4:
                print('|==================================|')
                print('|            QUANTIDADE            |')
                print('|      DE MÉDICOS CADASTRADOS      |')
                print('|            NO SISTEMA            |')
                print('|==================================|')
                print(
                    f"Existem {'0' if len(listPessoaMedico) == 0 else len(listPessoaMedico)} médicos cadastrados no "
                    f"sistema")
                print()
            elif opcao == 5:
                pass
            elif opcao == 6:
                print('|===================================|')
                print('|        EXCLUSÃO DE MÉDICOS        |')
                print('|===================================|')
                nome = input('Digite o nome do médico para exclusão: ')
                print(Controller.deleteNomeMedico(listPessoaMedico, nome))
                print()
            elif opcao == 7:
                print('|==================================|')
                print('|    ZERAR REGISTRO DOS MÉDICOS    |')
                print('|==================================|')
                print(Controller.deleteAllMedicos(listPessoaMedico))
                print()
            else:
                break
    else:
        print('Obrigado e volte sempre!')
        break
