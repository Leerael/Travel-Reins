"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from WebProject_1 import app, db
from WebProject_1.models import User
from WebProject_1.forms import LoginForm, SignupForm

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    error = None
    connError = None
    loginForm = LoginForm(request.form)
    signupForm = SignupForm()
    if request.method == 'POST' and loginForm.validate_on_submit():
        user = User.query.filter_by(username=loginForm.username.data).first()
        if user is None or not user.check_password(loginForm.password.data):
            loginForm.username.errors.append('Invalid Username or Password')
            loginForm.password.errors.append('Invalid Username or Password')
            return render_template(
                'login.html',
                title='Login/Signup',
                year=datetime.now().year,
                message='Login or Signup.',
                loginForm=loginForm,
                signupForm=SignupForm(),
                error=error,
                connError=connError
            )
        login_user(user, remember=loginForm.remember_me.data)
        next_page = request.args.get('next')
        flash('Welcome ' + loginForm.username.data)
        if not next_page or url_parse(next_page).netloc != '':
            return redirect(url_for('home'))
        return redirect(next_page)
    return render_template(
        'login.html',
        title='Login/Signup',
        year=datetime.now().year,
        message='Login or Signup.',
        loginForm=loginForm,
        signupForm=SignupForm(),
        error=error,
        connError=connError
    )

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    isError = False
    error = None
    connError = None
    loginForm = LoginForm(request.form)
    signupForm = SignupForm(request.form)
    if request.method == 'POST' and signupForm.validate_on_submit():
        user = User(username=signupForm.username.data, email=signupForm.email.data,
                    password_hash=signupForm.password.data, firstName=signupForm.firstName.data, 
                    lastName=signupForm.lastName.data, birthDate=signupForm.birthDate.data)
        user.set_password(signupForm.password.data)
        if User.query.filter_by(username=signupForm.username.data).first() != None:
            isError = True
            signupForm.username.errors.append('Username Already In Use.')
        if User.query.filter_by(email=signupForm.email.data).first() != None:
            isError = True
            signupForm.email.errors.append('Email Already In Use.')
        if isError == False:
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
    return render_template(
            'login.html',
            title='Login/Signup',
            year=datetime.now().year,
            message='Login or Signup.',
            loginForm=LoginForm(),
            signupForm=signupForm,
            error=error,
            connError=connError
        )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/itinerary')
@login_required
def itinerary():
    return render_template(
            'itinerary.html',
            title='Itinerary',
            year=datetime.now().year,
            message='This is your itinerary.',
        )
