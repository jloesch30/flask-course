from .models import Theme

# TODO: in class

def make_theme():
    try:
        new_theme = Theme(
        # TODO
        )
    except Exception as e:
        print(str(e))
        new_theme = None
        
    return new_theme