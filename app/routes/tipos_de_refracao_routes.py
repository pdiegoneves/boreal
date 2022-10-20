from app import app
from flask import Flask, render_template, request
from core.entities.equipamento_entity import Equipamento
from core.entities.tipo_de_refracao_entity import TipoDeRefracao

@app.route('/configuracoes/tipos-de-refracao/novo')
def cadastro_de_tipo_de_refracao():
    return render_template('configuracoes/form-novo-tipo-de-refracao.html')

@app.route('/configuracoes/tipos-de-refracao/gravar-tipo-de-refracao', methods=['POST'])
def gravar_tipo_de_refracao():
    tipo_de_refracao = TipoDeRefracao(
        request.form.get('descricao')
    )
    tipo_de_refracao.salvar()

    tipos_de_refracao = TipoDeRefracao.listar()
    equipamentos = Equipamento.listar() 
    return render_template('configuracoes/index.html', equipamentos=equipamentos, tipos_de_refracao=tipos_de_refracao)
