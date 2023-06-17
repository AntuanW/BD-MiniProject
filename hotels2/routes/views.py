from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("start_page.html")


@views.route('/loggedin')
def logged_home():
    return render_template("logged_home.html")
