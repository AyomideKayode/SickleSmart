#!/usr/bin/python3

"""Module for the SickleSmart Web App
To be imported as a package to the other python files for running.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "sicklesmart.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sickleSmart webApp'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, HealthStatus

    create_database(app)

    return app


def create_database(app):
    from .models import db

    with app.app_context():
        db.create_all()
    # if not path.exists('sicklemsart_web/' + DB_NAME):
    #     db.create_all()
    #     print('Database Created!')
