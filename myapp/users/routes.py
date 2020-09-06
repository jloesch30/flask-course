from flask import Blueprint, request, redirect, url_for, render_template, session
from .models import User
from myapp import auth, firebase

import pyrebase

users = Blueprint('users', __name__, url_prefix='/user')

@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # using pyrebase syntax to create a user using email and password
        user = auth.create_user_with_email_and_password(email, password)
        print('Saving user data')
        
        # saving session data inside flask session
        session['user'] = user
        return redirect(url_for('main.home', name='Josh'))
    else:
        return render_template("index.html")


@users.route('/signout', methods=['POST', 'GET'])
def signout(user=None):
    if user:
        user = session['user']
        user.signOut()
        print('signed out')
        return 'user signed out'
    else:
        return 'user not found'