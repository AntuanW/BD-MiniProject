import pprint

from hotels2.server.mongoConnection import *
from hotels2.models.hotel import Hotel
from hotels2.models.room import Room
from hotels2.models.customer import Customer
from datetime import datetime
from bson.objectid import ObjectId
from hotels2.models.validators import *
import re

mongo = MongoConnection()


def add_validators():
    mongo.db.command("collMod", "Rooms", validator=room_validator)
    mongo.db.command("collMod", "Hotels", validator=hotel_validator)
    mongo.db.command("collMod", "Customers", validator=customer_validator)


# ### Hotels methods ###
def add_hotel(name: str, street: str, city: str, zip_code: str):
    zip_regex = r"^\d{5}$"
    result = re.match(zip_regex, zip_code)

    if result:
        new_hotel = Hotel(name, street, city, zip_code)
        mongo.hotels.insert_one(new_hotel.to_dict())
        return True
    else:
        print("[SERVER] Invalid zip code format. The format is: xxxxx")
        return False


def remove_hotel(hotel_id: str):
    try:
        _id = ObjectId(hotel_id)
    except Exception as e:
        print("[SERVER]", e)
        return False
    res1 = mongo.hotels.delete_one({"_id": _id})
    res2 = mongo.rooms.delete_many({"hotel_id": _id})
    print("[SERVER] Removed:", res1.deleted_count, "hotels")
    print("[SERVER] Removed:", res2.deleted_count, "rooms")
    return True


def get_all_hotels():
    hotels = mongo.hotels.find()
    hotels = list(hotels)
    if not len(hotels):
        print("[SERVER] No hotels in the database.")
    return hotels


# ### Rooms methods ###
def add_room(hotel_id: str, room_type: int, room_number: int, ppn, availability: bool = True):
    try:
        _id = ObjectId(hotel_id)
    except Exception as e:
        print("[SERVER]", e)
        return False

    count = mongo.rooms.count_documents({"room_number": room_number})
    if count > 0:
        print("[SERVER] Room number", room_number, "already exists.")
        return False
    else:
        new_room = Room(_id, room_type, room_number, float(ppn), availability)
        mongo.rooms.insert_one(new_room.to_dict())
        return True


def remove_room(room_id: str):
    try:
        _id = ObjectId(room_id)
    except Exception as e:
        print("[SERVER]", e)
        return False

    res = mongo.rooms.delete_one({"_id": _id})
    print("[SERVER] Removed:", res.deleted_count, "elements")
    return True


# def get_all_rooms():
#     # TODO: maybe remove it and make it into filters
#     rooms = mongo.rooms.find({"is_available": True})
#     rooms = list(rooms)
#     if len(rooms) == 0:
#         print("No available rooms.")
#     return rooms


# def get_all_rooms_of_specific_hotel(hotel_id: str):
#     # TODO: maybe remove it and make it into filters
#     try:
#         _id = ObjectId(hotel_id)
#     except Exception as e:
#         print("[SERVER]", e)
#         return False
#
#     rooms = mongo.rooms.find({"hotel_id": _id, "is_available": True})
#     if rooms is None:
#         print("There is no hotel with such id in the database.")
#         return []
#     return list(rooms)


def set_price_per_night(room_id: str, new_price):
    try:
        _id = ObjectId(room_id)
    except Exception as e:
        print("[SERVER]", e)
        return False

    price_update = {
        "$set": {"price_per_night": float(new_price)}
    }
    try:
        update = mongo.rooms.update_one({"_id": _id}, price_update)
        if update.matched_count <= 0:
            print("[SERVER] No room with such id")
            return False
        return True
    except Exception as e:
        print("[SERVER] Validation failed")
        pprint.pprint(e)
        return False


def set_availability(room_id: str, availability: bool):
    try:
        _id = ObjectId(room_id)
    except Exception as e:
        print("[SERVER]", e)
        return False

    availability_update = {
        "$set": {"is_available": availability}
    }
    update = mongo.rooms.update_one({"_id": _id}, availability_update)
    if update.matched_count <= 0:
        print("[SERVER] No room with such id")
        return False
    return True


# ### Customers methods ###
def add_customer(name: str, surname: str, mail: str, passwd: str):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    result = re.match(email_pattern, mail)

    if result:
        count = mongo.customers.count_documents({"email": mail})
        if count > 0:
            print("[SERVER] This email address is already taken.")
            return False
        new_customer = Customer(name, surname, mail, passwd)
        mongo.customers.insert_one(new_customer.to_dict())
        return True
    else:
        print("[SERVER] Invalid email format, try - (string1)@(string2).(2+characters)")
        return False


def remove_customer(customer_id):
    try:
        _id = ObjectId(customer_id)
    except Exception as e:
        print("[SERVER]", e)
        return False

    res = mongo.customers.delete_one({"_id": _id})
    print("[SERVER] Removed:", res.deleted_count, "elements")
    return True


def set_password(customer_id, new_password):
    try:
        _id = ObjectId(customer_id)
    except Exception as e:
        print("[SERVER]", e)
        return False

    old_password = mongo.customers.find_one({"_id": _id})
    if old_password.get("password") == new_password:
        print("[SERVER] New password cannot be the same as the old one.")
        return False

    password_update = {
        "$set": {"password": new_password}
    }
    update = mongo.customers.update_one({"_id": _id}, password_update)
    if update.matched_count <= 0:
        print("[SERVER] Failed to set new password. There is no customer with such id in the database.")
        return False
    return True


def can_be_booked(room_id: ObjectId, check_in: datetime, check_out: datetime):
    # TODO change it into pipeline
    if check_in >= check_out:
        print("Check in date must be less than check out date.")
        return False

    room = mongo.rooms.find_one({"_id": room_id, "is_available": True})
    for booking in room['bookings']:
        if booking['date_from'] >= check_out or booking['date_to'] <= check_in:
            pass
        else:
            return False
    return True


def add_new_booking(customer_id: str, room_id: str, check_in: datetime, check_out: datetime):
    customer_id = ObjectId(customer_id)
    room_id = ObjectId(room_id)

    if can_be_booked(room_id, check_in, check_out):
        customer_booking = {
            "room_id": room_id,
            "check_in_date": check_in,
            "check_out_date": check_out
        }

        room_booking = {
            "customer_id": customer_id,
            "date_from": check_in,
            "date_to": check_out
        }

        room_update = mongo.rooms.update_one({"_id": room_id}, {"$push": {"bookings": room_booking}})
        if room_update.matched_count <= 0:
            print("[SERVER] Failed to add booking to a room.")
            return False

        customer_update = mongo.customers.update_one({"_id": customer_id}, {"$push": {"bookings": customer_booking}})
        if customer_update.matched_count <= 0:
            print("[SERVER] Failed to add booking to a customer.")
            return False
        print("[SERVER] Term is OK.")
        return True
    else:
        print("[SERVER] Term is colliding.")
        return False


def list_all_bookings(customer_id: str):
    try:
        _id = ObjectId(customer_id)
    except Exception as e:
        print("[SERVER]", e)
        return False

    bookings = mongo.customers.find_one({"_id": _id})
    return bookings['bookings']


def change_room(customer_id: str, old_room: str, new_room: str, check_in: datetime, check_out: datetime):
    # 1. check if new room is free during that period of time
    if add_new_booking(customer_id, new_room, check_in, check_out):
        # remove from customers bookings
        mongo.customers.update_one({"_id": ObjectId(customer_id)}, {

        })
        # remove from rooms booking
        mongo.rooms.update_one({"_id": ObjectId(old_room)}, {

        })
    else:
        print("[SERVER] You cannot change the booking to this specific room")
        return False


def change_booking_date():
    # 1. check if current room is available during new period of time
    # 2. if true -> change dates in both bookings
    # 3. else -> return a proper information
    pass

'''
check_in, check_out - argumenty funkcji sprawdzającej możliwość rezerwacji
from, to - pola w bazie danych

find musi znaleźć:
check_in < from and check_out > from
or
check_in >= from and check_out <= to
or
check_in < to and check_out >= to
or
check_in <= from and check_out >= to
'''
