from flask import Blueprint, redirect, url_for, render_template, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('users.login'))

# how to pass variables
# @main.route('/home') # we can add extra decorators on the web page
@main.route('/home/<string:fname>', methods=['GET'])
def home(fname=None):
    return render_template('home.html', fname=fname)