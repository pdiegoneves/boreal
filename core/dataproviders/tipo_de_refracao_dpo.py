from app import db
from sqlalchemy.ext.declarative import declarative_base

class TipoDeRefracaoDpo(db.Model):
    __tablename__ = "tipos_de_refracao"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(255), unique=True)
