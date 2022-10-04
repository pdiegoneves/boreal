from app import db
from sqlalchemy.ext.declarative import declarative_base

class Tecnica(db.Model):
    __tablename__ = "tecnicas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(255), nullable=False)
    