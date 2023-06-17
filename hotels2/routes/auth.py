from flask import Blueprint, render_template, request, flash
from hotels2.server.dbOperations import *
import re
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('firstName')
        surname = request.form.get('surname')
        mail = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        result = re.match(email_pattern, mail)
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
            flash('Account created successfully!', category='success')

    return render_template("signup.html")
