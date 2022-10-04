from app import app
from flask import Flask
from app.view.equipamento_view import EquipamentoView


@app.route('/listar-equipamentos/')
def litar_equipamentos():
    return EquipamentoView.listar()

@app.route('/buscar-equipamento/<int:id>')
def buscarPorId(id):
    return EquipamentoView.buscarPorId(id)