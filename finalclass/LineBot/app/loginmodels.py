from flask_login import UserMixin
from app import lm

class User(UserMixin):
    pass

@lm.user_loader
def user_loader(users):
    if users not in users_dict:
        return

    user = User()
    user.id = users
    return user

@lm.request_loader
def request_loader(request):
    user = request.form.get('user_id')
    if user not in users_dict:
        return
    
    user = User()
    user.id = user

    user.is_authenticated = request.form['password'] == users_dict[user]['password']

    return user

users_dict = {'Owner': {'password': 'HelloWorld'}}