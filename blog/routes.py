from . import app
from flask import render_template, url_for, flash
from .forms import RegisterForm, LoginForm

posts = [
        {
            'author': 'Petec 0x0',
            'title': 'First blog',
            'content': 'This is the content of the first blog post on the flask blog',
            'date_posted': 'March 29 2021'
         },
        {
            'author': 'Onyedikachi',
            'title': 'Techinical blog',
            'content': 'THere you can get help of any object by pressing Ctrl+I in front of it, either on the Editor or the Console.',
            'date_posted': 'March 30 2021'
         }
    ]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    register_form = RegisterForm()

    return render_template('register.html', title='Register', register_form=register_form)

@app.route('/login')
def login():
    login_form = LoginForm()
    
    return render_template('login.html', title='Login', login_form=login_form)