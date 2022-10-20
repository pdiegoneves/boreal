from app import db
from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

@dataclass
class PacienteDpo(db.Model):
    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    data_de_nascimento = db.Column(db.Date)
    identificador = db.Column(db.String(255), nullable=True)
    sexo = db.Column(db.String(10))
