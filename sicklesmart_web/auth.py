#!/usr/bin/python3

"""Auth module for user's authentication.
"""

from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Log out</p>"


@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")
