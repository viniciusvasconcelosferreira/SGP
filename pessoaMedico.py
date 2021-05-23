from pessoa import Pessoa


class Medico(Pessoa):
    def __init__(self, crm, nome, idade, data_nascimento, cpf, telefone):
        self.__crm = crm
        super(Medico, self).__init__(nome, idade, data_nascimento, cpf, telefone)

    def getCrm(self):
        return self.__crm

    def setCrm(self, crm):
        self.__crm = crm
