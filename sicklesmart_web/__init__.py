#!/usr/bin/python3

"""Module for the SickleSmart Web App
To be imported as a package to the other python files for running.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

    return app
