#!/usr/bin/python3

"""Module for database?
"""

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class HealthStatus(db.Model):
    healthStatusID = db.Column(db.Integer, primary_key=True)
    updated_date = db.Column(db.DateTime(timezone=True), default=func.now())
    symptoms = db.Column(db.String(5000))
    medication = db.Column(db.String(2500))
    hydration_level = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class EducationalResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    link = db.Column(db.String(255))
    description = db.Column(db.Text)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    healthStatus = db.relationship('HealthStatus')
