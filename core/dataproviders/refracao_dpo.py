from app import db
from sqlalchemy.ext.declarative import declarative_base

class RefracaoDpo(db.Model):
    __tablename__ = "refracoes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    olho = db.Column(db.String(2))
    tipo_de_refracao_id = db.Column(db.Integer, db.ForeignKey('tipos_de_refracao.id'))
    sphere = db.Column(db.Float)
    cylinder = db.Column(db.Float)
    axis = db.Column(db.Integer)
    data_da_refracao = db.Column(db.DateTime)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))

