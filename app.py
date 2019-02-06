from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
