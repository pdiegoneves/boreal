from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_babel import Babel

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)
csrf.init_app(app)

babel = Babel(app)

from core.dataproviders import tratamento_dpo, equipamento_dpo, paciente_dpo, refracao_dpo, tecnica_dpo, tipo_de_refracao_dpo
from app.routes import equipamento_routes
from app.view import equipamento_view