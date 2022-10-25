from core.dataproviders.paciente_dpo import PacienteDpo
from app import db


class Paciente():
    def __init__(self, nome, data_de_nascimento, identificador, sexo):
        self.__nome = nome
        self.__data_de_nascimento = data_de_nascimento
        self.__identificador = identificador
        self.__sexo = sexo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, value):
        self.__data_de_nascimento = value

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, value):
        self.__identificador = value

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, value):
        self.__sexo = value

    def salvar(self):
        try:
            paciente_dpo = PacienteDpo()
            paciente_dpo.nome = self.nome
            paciente_dpo.data_de_nascimento = self.data_de_nascimento
            paciente_dpo.identificador = self.identificador
            paciente_dpo.sexo = self.sexo
            db.session.add(paciente_dpo)
            db.session.commit()
            return True
        except:
            return False

    @classmethod
    def buscarPorId(cls, id):
        return PacienteDpo.query.filter_by(id=id).first()

    @classmethod
    def listar(cls):
        equipamentos = PacienteDpo.query.all()
        return equipamentos

    @classmethod
    def buscarPorNome(cls, nome):
        return PacienteDpo.query.filter_by(nome=nome).first()
