#!/usr/bin/python3

"""Views module for user's navigation that will be a blueprint for
my application. Meaning it has the URLs(roots) defined here.
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')


@views.route('/user-logged_in')
@login_required
# to be added to the page route that should be dsiplayed when
# users have successfully registered or logged in.
def user_logged_in():
    return render_template('user-logged_in.html')
