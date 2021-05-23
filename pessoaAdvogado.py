from pessoa import Pessoa


class Advogado(Pessoa):
    def __init__(self, oab, nome, idade, data_nascimento, cpf, telefone):
        self.__crm = oab
        super(Advogado, self).__init__(nome, idade, data_nascimento, cpf, telefone)

    def getOab(self):
        return self.__crm

    def setOab(self, oab):
        self.__crm = oab
