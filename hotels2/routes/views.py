from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("start_page.html")


@views.route('/bookings')
@login_required
def logged_home():
    return render_template("my_bookings.html")
