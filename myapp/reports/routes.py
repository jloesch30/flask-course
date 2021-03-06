from flask import Blueprint, request, redirect, url_for, render_template
from .utils import make_report, get_user_reports

reports = Blueprint('reports', __name__, url_prefix='/report')

@reports.route('/make-report', methods=['GET', 'POST'])
def makeReport():
    if request.method == 'POST':
        # capture report data
        title = request.form.get('title')
        theme_name = request.form.get('theme')
        summary = request.form.get('summary')
        report_tags = request.form.getlist('report_tags')
        new_report = make_report(title, theme_name, summary, report_tags)

        if new_report:
            new_report.save()

        # user report as a list
        user_reports = get_user_reports()

        return render_template('new_report.html', reports=user_reports)
    else:
        user_reports = get_user_reports()
        return render_template('new_report.html', reports=user_reports)
        