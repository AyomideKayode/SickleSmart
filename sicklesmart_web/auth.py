#!/usr/bin/python3

"""Auth module for user's authentication.
"""

from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Log out</p>"


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        age = request.form.get('age')
        bloodGroup = request.form.get('bloodGroup')
        genotype = request.form.get('genotype')

        if len(email) < 4:
            flash('Email must be greater than 3 characters and be valid',
                  category='error')
        elif len(name) < 2:
            flash('Valid name longer that two characters is required',
                  category='error')
        elif password1 != password2:
            flash("Passwords don't match", category='error')
        elif len(password1) < 8:
            flash("Password length is too short", category='error')
        else:
            # add user to database
            flash('Sign Up for SickleSmart successful!', category='success')

    return render_template("register.html")
