from flask import Blueprint, request, render_template
from .utils import make_theme

themes = Blueprint('themes', __name__, url_prefix='/theme')

# TODO: in class
@themes.route('/make-theme', methods=['GET', 'POST'])
def makeTheme():
    if request.method == 'POST':
        # capture report data
        title = request.form.get('title')
        # TODO
        new_theme = make_theme()

        if new_theme:
            new_theme.save()
        return render_template('new_theme.html')
    else:
        return render_template('new_theme.html')