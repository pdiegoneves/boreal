from app import db
from dataclasses import dataclass
from sqlalchemy.ext.declarative import declarative_base

@dataclass
class EquipamentoDpo(db.Model):
    __tablename__ = "equipamentos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(255), nullable=False)
    marca = db.Column(db.String(255), nullable=False)
    numero_de_serie = db.Column(db.String(255), nullable=False, unique=True)

