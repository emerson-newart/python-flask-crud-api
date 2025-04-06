from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import bp
from app.models import db

def create_app():
    app = Flask(__name__)

    # Configuração do MYSQl
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:new0147@mysql/dbpython'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) 

    with app.app_context():
        from . import models  # importa as models
        db.create_all()       # cria todas as tabelas automaticamente
        from . import routes  # importa as rotas

    app.register_blueprint(bp)
    return app

