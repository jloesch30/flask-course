from flask import Blueprint, request, redirect, url_for, render_template, session
from myapp import auth,firebase


users = Blueprint('users', __name__)

@users.route('/signout', methods=['POST', 'GET'])
def signout():
    user = session['user']
    if user:
        user = session['user']
        user.signOut()
        print('signed out')
        return 'user signed out'
    else:
        return 'user not found'