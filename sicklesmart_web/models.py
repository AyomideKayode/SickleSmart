#!/usr/bin/python3

"""
Module for defining database models.
"""

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class HealthStatus(db.Model):
    """Model representing the health status of users.
    """
    healthStatusID = db.Column(db.Integer, primary_key=True)
    updated_date = db.Column(db.DateTime(timezone=True), default=func.now())
    symptoms = db.Column(db.String(5000))
    medication = db.Column(db.String(2500))
    hydration_level = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    """Model representing user information.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    healthStatus = db.relationship('HealthStatus')
