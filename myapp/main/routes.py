from flask import Blueprint, redirect, url_for, render_template, request, session
from myapp import auth, firebase

main = Blueprint('main', __name__)

@main.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = auth.create_user_with_email_and_password(email, password)
        session['user'] = user
        print(session)
        return redirect(url_for('users.signout', user=user))
    else:
        return render_template("index.html")

@main.route('/home')
def home():
    return "welcome to the homepage"
