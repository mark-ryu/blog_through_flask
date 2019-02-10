from app.models import User, Post
from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm


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