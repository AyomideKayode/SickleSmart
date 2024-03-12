#!/usr/bin/python3

"""
Auth module for handling user authentication.
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login.
    Returns:
        redirect: Redirects to user_logged_in view upon successful login.
        render_template: Renders login page for GET requests.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in succesfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.user_logged_in'))
            else:
                flash('You dey wyn me? E no correct jhur', category='error')
        else:
            flash('Email does not exist - I no sabi you before',
                  category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    """Handle user logout.
    Returns:
        redirect: Redirects to login view after logging out.
    """
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration.
    Returns:
        redirect: Redirects to user_logged_in view upon successful registration.
        render_template: Renders registration page for GET requests.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # Additional form fields
        age = request.form.get('age')
        bloodGroup = request.form.get('bloodGroup')
        genotype = request.form.get('genotype')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Person don use this email before, change am',
                  category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters and be valid',
                  category='error')
        elif len(name) < 2:
            flash('Name must be at least 2 characters', category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        elif len(password1) < 8:
            flash("Password must be at least 8 characters", category='error')
        else:
            # Add user to database
            new_user = User(email=email, user_name=name,
                            password=generate_password_hash(password1,
                                                            method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Sign Up for SickleSmart successful!', category='success')
            return redirect(url_for('views.user_logged_in'))

    return render_template("register.html", user=current_user)
