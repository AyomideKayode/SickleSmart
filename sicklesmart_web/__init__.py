#!/usr/bin/python3

"""
Module for the SickleSmart Web App.
To be imported as a package to other Python files for running.
"""

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize SQLAlchemy database object
db = SQLAlchemy()
DB_NAME = "sicklesmart.db"


def create_app():
    """Create and configure the Flask app.
    Returns:
        Flask: The configured Flask app.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sickleSmart webApp'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initialize the database with the app
    db.init_app(app)

    # Import blueprints for views, authentication, and web scraping
    from .views import views
    from .auth import auth
    from .web_scraper import fetch_educational_resources

    # Register blueprints with the app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Define route for educational resources
    @app.route('/educational-resources')
    def educational_resources():
        """Fetch and return educational resources.
        Returns:
            jsonify: JSON response containing educational resources.
        """
        resources = fetch_educational_resources()
        if resources is None:
            return jsonify({'error':
                            'Failed to fetch educational resources'}), 500
        return jsonify(resources)

    # Import database models
    from .models import User, HealthStatus

    # Create the database tables
    create_database(app)

    # Configure Flask-Login for user authentication
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """Load a user given their ID.
        Args:
            id: The user's ID.
        Returns:
            User: The user object.
        """
        return User.query.get(int(id))

    return app


def create_database(app):
    """Create the database tables if they do not exist.
    Args:
        app: The Flask app.
    """
    from .models import db

    with app.app_context():
        db.create_all()
