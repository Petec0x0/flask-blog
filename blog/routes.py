from blog import app, db
from flask import render_template, url_for, flash, redirect
from blog.forms import RegisterForm, LoginForm
from blog.models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

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

@app.route('/register', methods=('GET', 'POST'))
def register():
    register_form = RegisterForm()

    # validate form and register users
    if register_form.validate_on_submit():
        # create a user object from the User class/model
        user = User(
            username=register_form.username.data,
            email=register_form.email.data,
            password=generate_password_hash(register_form.password.data))   
        
        # add and commit changes to the database
        db.session.add(user)
        db.session.commit()
        
        flash("User created successfully! login to continue", category='success')
        return redirect(url_for('login'))

    # check if an error occured and send flash message
    if register_form.errors:
        # ilterate and flash error messages if it exist
        for errors in register_form.errors.values():
            flash(f'Error : {errors[0]}', category='danger')


    return render_template('register.html', title='Register', register_form=register_form)

@app.route('/login', methods=('GET', 'POST'))
def login():
    # get the LoginForm class from form.py
    login_form = LoginForm()
    """
        validate the form using all the written validations from the 
        LoginForm class
    """
    if login_form.validate_on_submit():
        # authenticate user if correct credentials is entered
        user = User.query.filter_by(username=login_form.username.data).first()
        
        # check if user exist and if password is correct
        if user and check_password_hash(user.password, login_form.password.data):
            # login the user
            login_user(user) 
            # flash success message for the user
            flash("User logged in successfully", category='success')
            # redirect user to market page
            return redirect(url_for('home'))
        else:
            # flash error message is authentication fails
            flash("Username or Password Incorrect", category='danger')
            
    
    # check for error messages     
    if form.errors:
        # ilterate and flash error messages if it exist
        for errors in form.errors.values():
            flash(f'Error : {errors[0]}', category='danger')
    
    return render_template('login.html', title='Login', login_form=login_form)