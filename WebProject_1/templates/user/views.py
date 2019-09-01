from datetime import datetime
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from WebProject_1 import app, db
from WebProject_1.models import User


@app.route('/itinerary')
@app.route('/user/itinerary')
@login_required
def itinerary():
    return render_template(
            'user/itinerary.html',
            title='Itinerary',
            year=datetime.now().year,
            message='This is your itinerary.',
        )

@app.route('/forum')
@app.route('/user/forum')
@login_required
def forum():
    return render_template(
            'user/forum.html',
            title='Forum',
            year=datetime.now().year,
            message='This is your forum.',
        )

@app.route('/blog')
@app.route('/user/blog')
@login_required
def blog():
    return render_template(
            'user/blog.html',
            title='Blog',
            year=datetime.now().year,
            message='This is your blog.',
        )