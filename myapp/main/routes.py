from flask import Blueprint, redirect, url_for, render_template, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('main.login'))

@main.route('/login',methods=['GET', 'POST'])
def login():
    return render_template('index.html')
