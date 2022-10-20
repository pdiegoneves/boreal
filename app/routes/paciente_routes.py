from app import app
from flask import Flask, render_template, request

@app.route('/pacientes/')
def pacientes():
     return render_template('pacientes/index.html')