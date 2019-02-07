from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '163636029a1361627800422b1aa32e30'

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

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account is created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form, title='Register')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title='Login')


if __name__ == "__main__":
    app.run(debug=True)


































