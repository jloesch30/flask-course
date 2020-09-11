from flask import Blueprint, request, render_template
from .utils import make_theme
themes = Blueprint('themes', __name__, url_prefix='/theme')

# TODO: in class
@themes.route('/make-theme', methods=['GET', 'POST'])
def makeTheme():
    if request.method == 'POST':
        # capture report data
        title = request.form.get('title')
        theme_name = request.form.get('theme')
        summary = request.form.get('summary')
        report_tags = request.form.getlist('report_tags')
        new_report = make_theme(title, theme_name, summary, report_tags)

        if new_report:
            new_report.save()
        return render_template('new_theme.html')
    else:
        return render_template('new_theme.html')