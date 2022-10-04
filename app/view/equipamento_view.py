from flask import json, jsonify
from core.entities.equipamento_entity import Equipamento
class EquipamentoView():
    def __init__(self, id, descricao, marca, numero_de_serie):
        self.id = id
        self.descricao = descricao
        self.marca = marca
        self.numero_de_serie = numero_de_serie

    @classmethod
    def buscarPorId(cls, id):
        equipamento = Equipamento.buscarPorId(id)
        return jsonify(equipamento)


    @classmethod
    def listar(cls):
        equipamentos = Equipamento.listar()
        return jsonify(equipamentos)

    @classmethod
    def buscarPorNome(cls, descricao):
        equipamento = Equipamento.buscarPorNome(descricao)
        