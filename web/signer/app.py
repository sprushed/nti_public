from flask import Flask
from flask import render_template, abort, flash, request, redirect
from flask_bootstrap import Bootstrap

from flask_wtf import Form
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_required
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, AnonymousUser

import os
import wtf_helpers
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "4DM1N_L0v3S_Y0U_V3RY_MUCH,4LL_TH3_B3St"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/default_db'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_CHANGE_EMAIL'] = False
app.config['SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL'] = False
app.config['SECURITY_FLASH_MESSAGES'] = True
app.config['SECURITY_PASSWORD_SALT'] = "salt1svery1mp0rt4nt"

db = SQLAlchemy(app)

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))



user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


#db.create_all()

Bootstrap(app)
wtf_helpers.add_helpers(app)


@app.route("/")
def index():
    if current_user.is_authenticated:
        if current_user.email == 'admin@nti-contest.ru':
            return redirect("/admin", code=302)
    return render_template("index.html", current_user=current_user)

@app.route("/admin")
def admin():
    if not current_user.is_authenticated:
        return abort(403)

    if current_user.email != 'admin@nti-contest.ru':
        return abort(403)

    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
