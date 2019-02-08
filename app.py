from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '163636029a1361627800422b1aa32e30'

# engine can be used for the database url/uri but this could work too
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

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

# dummy data
posts = [
    {
        'author': 'Arvin',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Feb 06, 2019'
    },
    {
        'author': 'Mark',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Feb 06, 2019'
    }
]

@app.route("/")
def index():
    return render_template('index.html', posts=posts, title='HOME')

@app.route("/about")
def about():
    return render_template('about.html', title='ABOUT PAGE')

"""
<<<<<<<Register and Login Ifs>>>>>>>

form is passed as and argument for the html to render
if the form is valid, then use the flash to send a feedback message
redirect is when the process is a success the redirected url will be shown to the user

"""
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account is created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form, title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "sample@gmail.com" and form.password.data == "password":
            flash(f'Logged in as {form.username.data}', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful, try again.', 'danger')
    return render_template('login.html', form=form, title='Login')



if __name__ == "__main__":
    app.run(debug=True)


"""

<<<<<< TERMINAL COMMANDS >>>>>>
import db as an instance since <db> is the variable used to communicate to the database using sqlalchemy
- create all the structure of the database
db.create_all()

variable = <Model Class> ( insert the parameters )
to save the data into the database 
db.session.add(the_variable)
db.session.commit()
db.drop.all()

user.id is for the user_id because it is used as the foreign key
>>>>>>>>>>>>>>>
<QUERY>

User.query.all()
User.query.filter_by(username='the username').all()
User.query.get(1)

>>>>>>>>>>>>


"""