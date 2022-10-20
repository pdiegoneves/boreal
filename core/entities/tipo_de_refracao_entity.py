from core.dataproviders.tipo_de_refracao_dpo import TipoDeRefracaoDpo
from app import db


class TipoDeRefracao():
    def __init__(self, descricao):
        self.__id = 0
        self.__descricao = descricao

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
    

    def salvar(self):
        try:
            tipo_de_refracao_dpo = TipoDeRefracaoDpo()
            tipo_de_refracao_dpo.descricao = self.descricao
            db.session.add(tipo_de_refracao_dpo)
            db.session.commit()
        except:
            return False

    @classmethod
    def buscarPorId(cls, id):
        return TipoDeRefracaoDpo.query.filter_by(id = id).first()

    @classmethod
    def listar(cls):
        tipos_de_refracao = TipoDeRefracaoDpo.query.all()
        return tipos_de_refracao

    @classmethod
    def buscarPorNome(cls, descricao):
        return TipoDeRefracaoDpo.query.filter_by(descricao = descricao).first()