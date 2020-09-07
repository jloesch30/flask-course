from flask import Blueprint, redirect, url_for, render_template, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('users.login'))

@main.route('/home/<string:name>',methods=['GET', 'POST'])
def home(name):
    return f'User was made {name}'
