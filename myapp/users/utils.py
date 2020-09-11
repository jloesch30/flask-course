from flask import session

from myapp.users.models import User

def create_user(fname, email):
    new_user = None
    
    try:
        new_user = User(
            email=email,
            fname=fname
        )
    except Exception as e:
        print(str(e))
    
    return new_user

def get_user():
    email = session['email']
    try:
        user = User.objects(email=email).get()
    except Exception as e:
        print(str(e))
        user = None
    return user