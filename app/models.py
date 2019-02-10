from datetime import datetime
from app import db

"""

<<<<< creating models >>>>>>>
passing in the db.Model as to mention that we are passing the database instance of the sqlalchemy app

simply save the types of data you want into variables and using arguments required.

the db.Column / db.<type of data> / primary_key / nullable / unique / etc. . . 

relationship for database, backref is to get the user who created the post, when sqlalchemy loads data necessary in one go

"""

# for the User database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # the user id is for the author
    # in the user model, the post class is used, user.id is for the table name
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
