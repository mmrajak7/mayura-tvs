from flask import render_template, Blueprint, redirect, url_for, flash

from app import db
from login.loginForm import RegisterForm, LoginForm
from models.user import User
from flask_login import login_user, logout_user

login = Blueprint("login", __name__, static_folder="static", template_folder="templates")


@login.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are logged in as: {user_to_create.username} ', category='success')
        return redirect(url_for("booking.vehicle_booking"))
    return render_template('register.html', form=form)


@login.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'success! You are logged in as: {attempted_user.username} ', category='success')
            return redirect(url_for('booking.view_booking'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
    return render_template('login.html', form=form)


@login.route('/logout', methods=['GET', 'POST'])
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("login.login_page"))
