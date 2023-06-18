from flask import Blueprint, render_template
from flask_login import login_required, current_user
from hotels2.server.dbOperations import *

views = Blueprint('views', __name__)


@views.route('/')
def home():
    hotels = get_all_hotels()
    return render_template("start_page.html", user=current_user, hotels=hotels)


@views.route('/bookings')
@login_required
def logged_home():
    return render_template("my_bookings.html", user=current_user)


@views.route('/rooms')
def rooms_list():
    return render_template("rooms_list.html", user=current_user)


@views.route('/reserve_rooms')
@login_required
def reserve_list():
    return render_template("reserve_rooms.html", user=current_user)
