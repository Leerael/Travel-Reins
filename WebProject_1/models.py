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
    code = db.Column(db.String(10))
    code2 = db.Column(db.String(10))
    name = db.Column(db.String(150))
    phonecode = db.Column(db.Integer)
    description = db.Column(db.String(255))
    easting = db.Column(db.Numeric(18, 6))
    northing = db.Column(db.Numeric(18, 6))
    countrySubdivisions = db.relationship('CountrySubdivision', backref='country', lazy='dynamic')
    cities = db.relationship('City', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country {}>'.format(self.body)


class CountrySubdivision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))
    easting = db.Column(db.Numeric(18, 6))
    northing = db.Column(db.Numeric(18, 6))
    countrySubdivisionType_id = db.Column(db.Integer, db.ForeignKey('country_subdivision_type.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    cities = db.relationship('City', backref='country_subdivision', lazy='dynamic')

    def __repr__(self):
        return '<Country Subdivision {}>'.format(self.body)

class CountrySubdivisionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))
    countrySubdivisons = db.relationship('CountrySubdivision', backref='country_subdivision_type', lazy='dynamic')

    def __repr__(self):
        return '<Country Subdivision Type {}>'.format(self.body)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))
    easting = db.Column(db.Numeric(18, 6))
    northing = db.Column(db.Numeric(18, 6))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    countrySubdivision_id = db.Column(db.Integer, db.ForeignKey('country_subdivision.id'))

    def __repr__(self):
        return '<City {}>'.format(self.body)


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(100))
    symbol = db.Column(db.String(100))

    def __repr__(self):
        return '<Currency {}>'.format(self.body)


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))
    activityType_id = db.Column(db.Integer, db.ForeignKey('activity_type.id'))

    def __repr__(self):
        return '<Activity {}>'.format(self.body)

class ActivityType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))
    countrySubdivisons = db.relationship('Activity', backref='activity_type', lazy='dynamic')

    def __repr__(self):
        return '<Activity Type {}>'.format(self.body)


class EquipmentType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Equipment Type {}>'.format(self.body)


class AccommodationType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Accommodation Type {}>'.format(self.body)


class TransportType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Transport Type {}>'.format(self.body)
