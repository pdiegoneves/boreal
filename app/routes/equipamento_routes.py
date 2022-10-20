from app import app
from flask import Flask, render_template, request
from core.entities.equipamento_entity import Equipamento

@app.route('/configuracoes/equipamento/novo')
def cadastro_de_equipamento():
     return render_template('configuracoes/form-novo-equipamento.html')


@app.route('/configuracoes/equipamento/gravar-equipamento', methods=['POST'])
def gravar_equipamento():
     equipamento = Equipamento(
          descricao = request.form.get('descricao'),
          marca = request.form.get('marca'),
          numero_de_serie = request.form.get('numero-de-serie')
     )
     equipamento.salvar()
     equipamentos = Equipamento.listar() 
     return render_template('configuracoes/index.html', equipamentos=equipamentos)
