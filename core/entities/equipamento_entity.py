from core.dataproviders.equipamento_dpo import EquipamentoDpo

class Equipamento():
    def __init__(self, id, descricao, marca, numero_de_serie):
        self.id = id
        self.descricao = descricao
        self.marca = marca
        self.numero_de_serie = numero_de_serie


    def salvar(self):
        try:        
            equipamento_dpo = EquipamentoDpo()
            equipamento_dpo.descricao = self.descricao
            equipamento_dpo.marca = self.marca
            equipamento_dpo.numero_de_serie = self.numero_de_serie
            return True
        except:
            return False

    @classmethod
    def buscarPorId(cls, id):
        return EquipamentoDpo.query.filter_by(id=id).first()

    @classmethod
    def listar(cls):
        return EquipamentoDpo.query.all()

    @classmethod
    def buscarPorNome(cls, descricao):
        return EquipamentoDpo.query.filter_by(descricao = descricao)
