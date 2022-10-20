import re
from app import app
from flask import Flask, render_template, request
from core.entities.equipamento_entity import Equipamento
from core.entities.tipo_de_refracao_entity import TipoDeRefracao

@app.route('/configuracoes/')
def configuracoes():
     equipamentos = Equipamento.listar() 
     tipos_de_refracao = TipoDeRefracao.listar()
     return render_template('configuracoes/index.html', equipamentos=equipamentos, tipos_de_refracao=tipos_de_refracao)
