from app import app
from flask import Flask, render_template, request
from core.entities.paciente_entity import Paciente

@app.route('/pacientes/')
def pacientes():
     pacientes = Paciente.listar()
     return render_template('pacientes/index.html', pacientes=pacientes)