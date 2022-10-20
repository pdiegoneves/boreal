from app import app
from flask import Flask, render_template, request

@app.route('/tratamentos/')
def tratamentos():
     return render_template('tratamentos/index.html')