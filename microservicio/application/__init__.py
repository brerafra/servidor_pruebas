import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#flask db init
#flask db migrate
#flask db upgrade

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    environment_configuration = os.environ['CONFIGURATION_SETUP']

    app.config.from_object(environment_configuration)

    db.init_app(app)

    with app.app_context():
        #Registrar la blueprint
        from .dog_api import dog_api_blueprint
        app.register_blueprint(dog_api_blueprint)
        return app