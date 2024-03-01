#!/usr/bin/python3

"""Views module for user's navigation that will be a blueprint for
my application. Meaning it has the URLs(roots) defined here.
"""

from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')
