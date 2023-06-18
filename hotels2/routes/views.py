from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from hotels2.server.dbOperations import *

views = Blueprint('views', __name__)


@views.route('/')
def home():
    hotels = get_all_hotels()
    for hotel in hotels:
        hotel['_id'] = str(hotel['_id'])
    return render_template("start_page.html", user=current_user, hotels=hotels)


@views.route('/bookings', methods=['GET', 'POST'])
@login_required
def logged_home():
    return render_template("my_bookings.html", user=current_user)


@views.route('/rooms')
def rooms_list():
    rooms = list(mongo.rooms.find())
    print(rooms)
    return render_template("rooms_list.html", user=current_user, rooms=rooms)


@views.route('/reserve_rooms', methods=['GET', 'POST'])
@login_required
def reserve_list():
    if request.method == 'POST':
        date_format = "%Y-%m-%d"
        check_in = request.form.get('checkin')
        check_in = datetime.strptime(check_in, date_format)

        check_out = request.form.get('checkout')
        check_out = datetime.strptime(check_out, date_format)
        if check_out < check_in:
            flash('Check in date must be less or equal than check out date.', category='error')

            room_id = request.form.get('room_id')
            customer_id = request.form.get('customer_id')

            # if add_new_booking(customer_id, room_id, check_in, check_out):
            #     flash('Room booked successfully!', category='success')
            # else:
            #     flash('Room is already booked in this period of time.', category='error')

    rooms = list(mongo.rooms.find())
    return render_template("reserve_rooms.html", user=current_user, rooms=rooms)
