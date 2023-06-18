from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from hotels2.server.dbOperations import *
import json

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
    if request.method == 'POST' and request.form.get('checkin') is not None:
        booking_id = request.form.get('booking_id')
        customer_id = current_user._id

        date_format = "%Y-%m-%d"
        new_checkin = request.form.get('new_checkin')
        new_checkin = datetime.strptime(new_checkin, date_format)

        new_checkout = request.form.get('new_checkout')
        new_checkout = datetime.strptime(new_checkout, date_format)

        if new_checkout < new_checkin:
            flash('Check in date must be less or equal than check out date.', category='error')
        else:
            # if change_booking():
            #     flash('Room booked successfully!', category='success')
            # else:
            #     flash('Room is already booked in this period of time.', category='error')
            pass

    my_bookings = get_all_user_bookings(current_user._id)   # str
    return render_template("my_bookings.html", user=current_user, bookings=my_bookings)


@views.route('/rooms')
def rooms_list():
    rooms = list(mongo.rooms.find())
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
        else:
            room_id = request.form.get('room_id')
            customer_id = request.form.get('customer_id')

            # if add_new_booking(customer_id, room_id, check_in, check_out):
            #     flash('Room booked successfully!', category='success')
            # else:
            #     flash('Room is already booked in this period of time.', category='error')

    rooms = list(mongo.rooms.find())
    return render_template("reserve_rooms.html", user=current_user, rooms=rooms)


@views.route('/remove-booking', methods=['POST'])
def remove_booking():
    print('================')
    print(request.get_json(force=True))
    booking = request.get_json()
    booking_id = booking['booking_id']
    # if remove_specific_booking(booking_id):
    #     flash('Successfully removed the reservation.', category='success')
    # else:
    #     flash('Something went wrong.', category='error')
    return jsonify({})
