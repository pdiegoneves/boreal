from core.dataproviders.equipamento_dpo import EquipamentoDpo
from app import db

class Equipamento():
    def __init__(self, descricao, marca, numero_de_serie):
        self.__id = 0
        self.__descricao = descricao
        self.__marca = marca
        self.__numero_de_serie = numero_de_serie


    def salvar(self):
        try:        
            equipamento_dpo = EquipamentoDpo()
            equipamento_dpo.descricao = self.descricao
            equipamento_dpo.marca = self.marca
            equipamento_dpo.numero_de_serie = self.numero_de_serie
            db.session.add(equipamento_dpo)
            db.session.commit()
            return True
        except:
            return False



    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        self.__marca = value

    @property
    def numero_de_serie(self):
        return self.__numero_de_serie

    @numero_de_serie.setter
    def numero_de_serie(self, value):
        self.__numero_de_serie = value

    @classmethod
    def buscarPorId(cls, id):
        return EquipamentoDpo.query.filter_by(id = id).first()

    @classmethod
    def listar(cls):
        equipamentos = EquipamentoDpo.query.all()
        return equipamentos

    @classmethod
    def buscarPorNome(cls, descricao):
        return EquipamentoDpo.query.filter_by(descricao = descricao).first()
