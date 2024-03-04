#!/usr/bin/python3

"""Views module for user's navigation that will be a blueprint for
my application. Meaning it has the URLs(roots) defined here.
"""

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import HealthStatus
from . import db


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html', user=current_user)


@views.route('/user-logged_in', methods=['GET', 'POST'])
@login_required
# to be added to the page route that should be dsiplayed when
# users have successfully registered or logged in.
def user_logged_in():
    if request.method == 'POST':
        healthStatus = request.form.get('healthStatus')

        if len(healthStatus) < 1:
            flash('Details🙂, how do you actually feel?', category='error')
        else:
            new_status = HealthStatus(symptoms=healthStatus, user_id=current_user.id)
            db.session.add(new_status)
            db.session.commit()
            flash('Health tracked successfully! Remember to drink more water.😁',
                  category='success')

    return render_template('user-logged_in.html', user=current_user)
