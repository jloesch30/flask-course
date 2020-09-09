from flask import Blueprint, request, redirect, url_for, render_template, session
from myapp.users.models import User
from myapp.users.utils import create_user
from myapp import auth, firebase

# Url prefix
users = Blueprint('users', __name__, url_prefix='/user')

@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        new_user = None
        email = request.form.get('email')
        password = request.form.get('password')
        fname = request.form.get('fname')
        session['fname'] = fname
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['signed-in'] = True
        except Exception:
            user = auth.create_user_with_email_and_password(email, password)
            session['signed-in'] = True
            # Check if user exists
            try: 
                user = User.objects(email=email).get()
                print('User found')
            except Exception as e:
                new_user = create_user(fname, email)
                new_user.save()
                print('New user created')

        return redirect(url_for('main.home', fname=fname))
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