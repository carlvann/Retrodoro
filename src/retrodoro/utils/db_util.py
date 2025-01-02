from retrodoro.models import Users
from uuid import uuid4
from datetime import datetime

def add_user(username, password):
    new_user = Users(uuid=str(uuid4()), 
                     name=username, 
                     password=password, 
                     creation_date=datetime.now())
    new_user.save()

def user_exists(username):
    user = Users.objects.filter(name=username)
    if user:
        return True
    return False

def get_all_users():
    return Users.objects.all()
