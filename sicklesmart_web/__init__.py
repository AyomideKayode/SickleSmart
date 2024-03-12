#!/usr/bin/python3

"""Module for the SickleSmart Web App
To be imported as a package to the other python files for running.
"""

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "sicklesmart.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sickleSmart webApp'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .web_scraper import fetch_educational_resources

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Define route for educational resources
    @app.route('/educational-resources')
    def educational_resources():
        resources = fetch_educational_resources()
        if resources is None:
            return jsonify({'error':
                            'Failed to fetch educational resources'}), 500
        return jsonify(resources)

    from .models import User, HealthStatus

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    from .models import db

    with app.app_context():
        db.create_all()
    # if not path.exists('sicklemsart_web/' + DB_NAME):
    #     db.create_all()
    #     print('Database Created!')
