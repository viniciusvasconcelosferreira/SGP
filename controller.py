from pessoaMedico import Medico
from pessoaAdvogado import Advogado


class Controller:
    def inserirAdvogado(oab, nome, idade, data_nascimento, cpf, telefone):
        return Advogado(oab, nome, idade, data_nascimento, cpf, telefone)

    def inserirMedico(crm, nome, idade, data_nascimento, cpf, telefone):
        return Medico(crm, nome, idade, data_nascimento, cpf, telefone)

    def listarMedico(listarMedicos):
        print('NOME | IDADE | DATA DE NASCIMENTO | CPF | CRM | TELEFONE')
        print('--------------------------------------------------------')
        for medico in listarMedicos:
            print(
                f'{medico.getNome()} | {medico.getIdade()} | {medico.getDataNascimento()} | {medico.getCpf()} | {medico.getCrm()} | {medico.getTelefone()}')
            print('--------------------------------------------------------')

    def listarAdvogado(listarAdvogados):
        print('NOME | IDADE | DATA DE NASCIMENTO | CPF | OAB | TELEFONE')
        print('--------------------------------------------------------')
        for advogado in listarAdvogados:
            print(
                f'{advogado.getNome()} | {advogado.getIdade()} | {advogado.getDataNascimento()} | {advogado.getCpf()} | {advogado.getOab()} | {advogado.getTelefone()}')
            print('--------------------------------------------------------')

    def pesquisaNomeAdvogado(listarAdvogados, nome):
        contador = 0
        for advogado in listarAdvogados:
            if advogado.getNome() == nome:
                print(f'OAB: {advogado.getOab()}')
                print(f'Nome: {advogado.getNome()}')
                print(f'Idade: {advogado.getIdade()}')
                print(f'Data de Nascimento: {advogado.getDataNascimento()}')
                print(f'CPF: {advogado.getCpf()}')
                print(f'Telefone: {advogado.getTelefone()}')
                break
            else:
                print(f'Advogado {nome} não cadastrado no sistema!')
            contador += 1

    def pesquisaNomeMedico(listarMedicos, nome):
        contador = 0
        for medico in listarMedicos:
            if medico.getNome() == nome:
                print(f'CRM: {medico.getCrm()}')
                print(f'Nome: {medico.getNome()}')
                print(f'Idade: {medico.getIdade()}')
                print(f'Data de Nascimento: {medico.getDataNascimento()}')
                print(f'CPF: {medico.getCpf()}')
                print(f'Telefone: {medico.getTelefone()}')
                break
            else:
                print(f'Médico {nome} não cadastrado no sistema!')
            contador += 1

    def deleteAllAdvogados(listarAdvogados):
        if len(listarAdvogados) != 0:
            listarAdvogados.clear()
            return 'Todos os advogados foram removidos!'
        else:
            return 'A lista de advogados está vazia!'

    def deleteAllMedicos(listarMedicos):
        if len(listarMedicos) != 0:
            listarMedicos.clear()
            return 'Todos os médicos foram removidos!'
        else:
            return 'A lista de médicos está vazia!'

    def deleteNomeAdvogado(listarAdvogados, nome):
        if len(listarAdvogados) != 0:
            cont = 0
            for advogado in listarAdvogados:
                if advogado.getNome() == nome:
                    listarAdvogados.pop(cont)
                    return f'Advogado {nome} removido com sucesso!'
                else:
                    return 'Advogado não encontrado!'
        else:
            return 'Lista de times está vazia!'

    def deleteNomeMedico(listarMedicos, nome):
        if len(listarMedicos) != 0:
            cont = 0
            for medico in listarMedicos:
                if medico.getNome() == nome:
                    listarMedicos.pop(cont)
                    return f'Médico {nome} removido com sucesso!'
                else:
                    return 'Médico não encontrado!'
        else:
            return 'Lista de médicos está vazia!'
