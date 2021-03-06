# variables used for initializing database, the app and hashing
from app import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
# flask login extension
from flask_login import login_user, current_user, logout_user, login_required

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

# include methods alllowed
@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user_register = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user_register)
        db.session.commit()
        # success used for tags
        flash(f'Account is created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user_login = User.query.filter_by(username=form.username.data).first() 
        if user_login and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user_login, remember=form.remember.data)
            # get next page if the page requires login
            next_page_after_log = request.args.get('next')
            return redirect(next_page_after_log) if next_page_after_log else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful, try again.', 'danger')
    return render_template('login.html', form=form, title='Login')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename=f'profile_pics/{current_user.image_file}')
    return render_template('account.html', title='Account', image_file=image_file, form=form)
