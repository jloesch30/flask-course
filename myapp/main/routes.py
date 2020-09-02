from flask import Blueprint, redirect, url_for

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect(url_for('main.home'))

@main.route('/home')
def home():
    return "welcome to the homepage"
