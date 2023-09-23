```python
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(UserMixin, db.Document):
    meta = {'collection': 'users'}
    username = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255, required=True)
    password_hash = db.StringField(required=True)
    roles = db.ListField(db.StringField(), default=[])

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return 'admin' in self.roles

def get_all_users():
    return User.objects.all()

def get_user(username):
    return User.objects(username=username).first()

def create_user(username, email, password, roles):
    user = User(username=username, email=email, roles=roles)
    user.set_password(password)
    user.save()

def update_user(username, email=None, password=None, roles=None):
    user = get_user(username)
    if user:
        if email:
            user.email = email
        if password:
            user.set_password(password)
        if roles:
            user.roles = roles
        user.save()

def delete_user(username):
    user = get_user(username)
    if user:
        user.delete()
```