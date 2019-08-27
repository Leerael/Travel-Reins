from datetime import datetime
from WebProject_1 import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    firstName = db.Column(db.String(256))
    lastName = db.Column(db.String(256))
    birthDate = db.Column(db.Date)
    createDate = db.Column(db.DateTime, default=datetime.utcnow)
    lastLoginDate = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))
    easting = db.Column(db.Numeric(18, 6))
    northing = db.Column(db.Numeric(18, 6))
    countryStates = db.relationship('CountryState', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country {}>'.format(self.body)


class CountryState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))
    easting = db.Column(db.Numeric(18, 6))
    northing = db.Column(db.Numeric(18, 6))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    places = db.relationship('Place', backref='country_state', lazy='dynamic')

    def __repr__(self):
        return '<State {}>'.format(self.body)


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))
    easting = db.Column(db.Numeric(18, 6))
    northing = db.Column(db.Numeric(18, 6))
    countrystate_id = db.Column(db.Integer, db.ForeignKey('country_state.id'))

    def __repr__(self):
        return '<Place {}>'.format(self.body)

