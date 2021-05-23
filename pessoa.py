class Pessoa:
    def __init__(self, nome, idade, data_nascimento, cpf, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__telefone = telefone

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getDataNascimento(self):
        return self.__data_nascimento

    def getCpf(self):
        return self.__cpf

    def getTelefone(self):
        return self.__telefone

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setDataNascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def setCpf(self, cpf):
        self.__cpf = cpf

    def setTelefone(self, telefone):
        self.__telefone = telefone
