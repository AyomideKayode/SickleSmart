#!/usr/bin/python3

"""
Views module containing routes for user navigation,
serving as a blueprint for the application with defined URLs (roots).
"""

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import HealthStatus
from . import db
import json


views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Render the index page.
    Returns:
        str: HTML content of the index page.
    """
    return render_template('index.html', user=current_user)


@views.route('/user-logged_in', methods=['GET', 'POST'])
@login_required
def user_logged_in():
    """Handle user logins and health status submissions.
    Returns:
        str: HTML content of the user-logged_in page.
    """
    if request.method == 'POST':
        healthStatus = request.form.get('healthStatus')

        if len(healthStatus) < 1:
            flash('Details🙂, how do you actually feel?', category='error')
        else:
            new_status = HealthStatus(
                symptoms=healthStatus, user_id=current_user.id)
            db.session.add(new_status)
            db.session.commit()
            flash('Health tracked successfully! Remember to drink more water.😁',
                  category='success')

    return render_template('user-logged_in.html', user=current_user)


@views.route('/delete-entry', methods=['POST'])
def delete_entry():
    """Handle deletion of a health status entry.
    Returns:
        dict: Empty JSON response.
    """
    print('Delete entry route hit!')
    healthstatusId = request.json.get('healthStatusId')
    if healthstatusId is not None:
        healthstatus = HealthStatus.query.get(healthstatusId)
        print(f'Deleting entry with ID: {healthstatusId}')
        if healthstatus and healthstatus.user_id == current_user.id:
            db.session.delete(healthstatus)
            db.session.commit()

    return jsonify({})
