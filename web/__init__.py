from flask import Flask
from flask_migrate import Migrate
from src.models import db,Admin
from src import CONFIG

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['SQLALCHEMY_DATABASE_URI']
    # set optional bootswatch theme
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = CONFIG['SQLALCHEMY_TRACK_MODIFICATIONS']
    app.config['SECRET_KEY'] = CONFIG['SECRET_KEY']
    db.init_app(app)
    Migrate(app,db)
    with app.app_context():
        db.create_all()

    from web.api.inscription_formulaire import form_view
    from web.api.connexion import connexion_view

    app.register_blueprint(form_view)
    app.register_blueprint(connexion_view)

    return app
