from flask import Blueprint, request, redirect, url_for, render_template, session
from myapp.users.models import User
from myapp import auth, firebase

# Url prefix
users = Blueprint('users', __name__, url_prefix='/user')

@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['signed-in'] = True
        except Exception:
            user = auth.create_user_with_email_and_password(email, password)
            session['signed-in'] = True

        return redirect(url_for('main.home', fname="Josh"))
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