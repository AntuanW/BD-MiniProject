from flask import Blueprint, render_template, request, flash, redirect, url_for
from hotels2.server.dbOperations import *
from hotels2.models.logged_user import LoggedUser
from werkzeug.security import generate_password_hash, check_password_hash
import re
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = get_user_email(email)
        if user is None:
            flash('There is no user with this email address.', category='error')
        elif check_password_hash(user['password'], password):
            user = LoggedUser(str(user['_id']), user['name'], user['surname'], user['email'], user['password'], user['bookings'])
            login_user(user, remember=True)
            flash("Logged in!", category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Incorrect password.', category='error')
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('firstName')
        surname = request.form.get('surname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        result = re.match(email_pattern, email)
        if not result:
            flash('Wrong email format!', category='error')
        elif len(name) == 0:
            flash('You must enter your name!', category='error')
        elif len(surname) == 0:
            flash('You must enter your surname!', category='error')
        elif len(password1) < 5:
            flash('Your password is too short!', category='error')
        elif password1 != password2:
            flash('Passwords do not match!', category='error')
        else:
            if add_customer(name, surname, email, generate_password_hash(password1, method='sha256')):
                flash('Account created successfully!', category='success')
                user = get_user_email(email)
                user = LoggedUser(str(user['_id']), name, surname, email, password1)
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Creating account failed, this email is already taken!', category='error')

    return render_template("signup.html", user=current_user)
