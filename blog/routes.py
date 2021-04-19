from blog import app, db
from flask import render_template, url_for, flash, redirect, request, abort
from blog.forms import RegisterForm, LoginForm
from blog.models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


# route to the home page
@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()

    return render_template('index.html', posts=posts)

# about page route
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# register page route
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

# login page route
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
    if login_form.errors:
        # ilterate and flash error messages if it exist
        for errors in login_form.errors.values():
            flash(f'Error : {errors[0]}', category='danger')
    
    return render_template('login.html', title='Login', login_form=login_form)

# logout functionality route
@app.route('/logout')
@login_required
def logout():
    # render the market.html template
    logout_user()
    # flash info message about the logout
    flash('Signed out successfully!', category='info')
    # redirect to home page after logout
    return redirect(url_for('home'))

# create post page route
@app.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    # check if a post have been created
    if request.method == "POST":
        # get the post request values
        post_title = request.form.get('title')
        post_slug = post_title.replace(' ', '-')
        post_body = request.form.get('body')
        post_author = current_user.username
        # validate to make sure the fields are not empty
        if post_title and post_body:
            # create an object of the Post class
            post = Post(title=post_title, slug=post_slug, body=post_body, author=post_author)
            # commit post to the database
            db.session.add(post)
            db.session.commit()

            # flash success message
            flash('Post created successfully', category='success')
            # redirect to the home page
            return redirect(url_for('home'))
        else:
            # flash an error message if the fields are empty
            flash('Fields cannot be empty', category='danger')

    return render_template('create.html', title='Create Post')

# detail post page route
@app.route('/posts/details/<post_slug>')
def detail_page(post_slug):
    # find the post check if a post with the requested slug exists
    post = Post.query.filter_by(slug=post_slug).first()
    if not post:
        # abort and return 404 if post does not exist
        abort(404)
    
    return render_template('details.html', title=post.title, post=post)

# route for the "Update post" page
@app.route('/posts/update/<post_id>')
def update_post(post_id):
    
    return render_template('update.html', title="Update -")