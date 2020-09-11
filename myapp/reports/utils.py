from .models import Report
from myapp.themes.models import Theme

from myapp.users.utils import get_user

def make_report(title, theme_name, summary, report_tags):
    current_user = get_user()
    try:
        theme = Theme.objects(theme_name=theme_name).get()
    except Exception:
        theme = None
    try:
        new_report = Report(
            title=title,
            author=current_user,
            theme=theme,
            summary=summary,
            report_tags=report_tags
        )
    except Exception as e:
        print(str(e))
        new_report = None
        
    return new_report