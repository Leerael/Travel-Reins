# app/home/views.py

from datetime import datetime
from flask import render_template
from flask_login import login_required
from WebProject_1 import app, db
from WebProject_1.models import User

from . import home


@app.route('/')
@app.route('/home')
def home():
    """
    Render the homepage template on the / route
    """
    return render_template(
        'home/index.html',
        title='Home Page',
        year=datetime.now().year
    )


@app.route('/dashboard')
@app.route('/home/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template(
        'home/dashboard.html',
        title='Dashboard',
        year=datetime.now().year,
        message='Your dashboard page.'
    )


@app.route('/contact')
@app.route('/home/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'home/contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
@app.route('/home/about')
def about():
    """Renders the about page."""
    return render_template(
        'home/about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/support')
@app.route('/home/support')
def support():
    """Renders the support page."""
    return render_template(
        'home/support.html',
        title='Support',
        year=datetime.now().year,
        message='Your application support page.'
    )