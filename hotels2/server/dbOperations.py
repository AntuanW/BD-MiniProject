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
    mongo.db.command("collMod", "Booking_Logs", validator=booking_logs_validator)


# ### Hotels methods ###
def add_hotel(name: str, street: str, city: str, zip_code: str, img: str):
    zip_regex = r"^\d{5}$"
    result = re.match(zip_regex, zip_code)

    if result:
        new_hotel = Hotel(name, street, city, zip_code, img)
        mongo.hotels.insert_one(vars(new_hotel))
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
def add_room(hotel_id: str, room_type: int, room_number: int, ppn, img: str, availability: bool = True):
    try:
        _id = ObjectId(hotel_id)
    except Exception as e:
        print("[SERVER]", e)
        return False

    count = mongo.rooms.count_documents({"hotel_id": _id, "room_number": room_number})
    if count > 0:
        print("[SERVER] Room number", room_number, "already exists.")
        return False
    else:
        new_room = Room(_id, room_type, room_number, float(ppn), availability, img)
        mongo.rooms.insert_one(vars(new_room))
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
    # email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # result = re.match(email_pattern, mail)

    # if result:
    #     count = mongo.customers.count_documents({"email": mail})
    #     if count > 0:
    #         print("[SERVER] This email address is already taken.")
    #         return False
    #     new_customer = Customer(name, surname, mail, passwd)
    #     mongo.customers.insert_one(vars(new_customer))
    #     return True
    # else:
    #     print("[SERVER] Invalid email format, try - (string1)@(string2).(2+characters)")
    #     return False
    count = mongo.customers.count_documents({"email": mail})
    if count > 0:
        print("[SERVER] This email address is already taken.")
        return False
    new_customer = Customer(name, surname, mail, passwd)
    mongo.customers.insert_one(vars(new_customer))
    return True


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


def can_be_booked(room_id: ObjectId, check_in: datetime, check_out: datetime, booking_id: ObjectId = None):
    if check_in >= check_out:
        print("[SERVER] Check in date must be less than check out date.")
        return False

    query = [
        {
            '$match': {
                '_id': ObjectId(room_id)
            }
        },
        {
            '$project': {
                '_id': 0,
                'bookings': 1
            }
        },
        {
            '$unwind': '$bookings'
        }
    ]
    if booking_id is not None:
        query.append({
            "$match": {
                "bookings.booking_id": {'$nin': [ObjectId(booking_id)]}
            }
        })
    query.append({
        '$match': {
            '$nor': [
                {
                    'bookings.date_from': {
                        '$gte': check_out
                    }
                },
                {
                    'bookings.date_to': {
                        '$lte': check_in
                    }
                }
            ]
        }
    })

    bookings = list(mongo.rooms.aggregate(query))
    return len(bookings) == 0


def push_bookings(booking_id: ObjectId, customer_id: ObjectId, room_id: ObjectId, check_in: datetime,
                  check_out: datetime):
    # TODO: testing required
    booking_in_customers = {
        "booking_id": booking_id,
        "customer_id": room_id,
        "date_from": check_in,
        "date_to": check_out
    }
    booking_in_rooms = {
        "booking_id": booking_id,
        "room_id": room_id,
        "date_from": check_in,
        "date_to": check_out
    }

    room_update = mongo.rooms.update_one({"_id": room_id}, {"$push": {"bookings": booking_in_rooms}})
    if room_update.matched_count <= 0:
        print("[SERVER] Failed to add booking to a room.")
        return False

    customer_update = mongo.customers.update_one({"_id": customer_id},
                                                 {"$push": {"bookings": booking_in_customers}})
    if customer_update.matched_count <= 0:
        print("[SERVER] Failed to add booking to a customer.")
        return False
    print("[SERVER] Successfully booked a room.")
    return True


def add_new_booking(customer_id: str, room_id: str, check_in: datetime, check_out: datetime):
    # TODO: testing required
    if can_be_booked(ObjectId(room_id), check_in, check_out):
        booking_id = ObjectId()
        return push_bookings(booking_id, ObjectId(customer_id), ObjectId(room_id), check_in, check_out)
    else:
        print("[SERVER] Term is colliding.")
        return False


def change_booking(customer_id: str, new_room: str, booking_id: str, check_in: datetime, check_out: datetime):
    # TODO: testing required
    if can_be_booked(ObjectId(new_room), check_in, check_out, ObjectId(booking_id)):
        old_room = mongo.customers.aggregate(
            [
                {
                    '$match': {
                        '_id': ObjectId(customer_id)
                    }
                }, {
                    '$project': {
                        '_id': 0,
                        'bookings': 1
                    }
                },
                {
                    '$unwind': '$bookings'
                }, {
                    '$match': {
                        'bookings.booking_id': ObjectId(booking_id)
                    }
                }, {
                    '$project': {
                        'old_room': '$bookings.room_id'
                    }
                }
            ]
        )

        old_room = list(old_room)[0].get('old_room')
        # update w customers
        mongo.customers.update_one(
            {
                "_id": ObjectId(customer_id),
                "bookings.booking_id": ObjectId(booking_id)
            },
            {
                "$set": {
                    "bookings.$.room_id": ObjectId(new_room),
                    "bookings.$.date_from": check_in,
                    "bookings.$.date_to": check_out
                }
            }
        )

        # wywalenie i dodanie w Rooms
        mongo.rooms.update_one({"_id": old_room}, {
            "$pull": {
                "bookings": {"booking_id": ObjectId(booking_id)}
            }
        })

        booking_in_rooms = {
            "booking_id": ObjectId(booking_id),
            "customer_id": ObjectId(customer_id),
            "date_from": check_in,
            "date_to": check_out
        }
        room_update = mongo.rooms.update_one({"_id": ObjectId(new_room)}, {
            "$push": {
                "bookings": booking_in_rooms
            }
        })
        if room_update.matched_count <= 0:
            print("[SERVER] Failed to add booking to a room.")
            return False
        return True
    else:
        print("[SERVER] You cannot rebook this room.")
        return False


def list_all_bookings(customer_id: str):
    try:
        _id = ObjectId(customer_id)
    except Exception as e:
        print("[SERVER]", e)
        return False

    bookings = mongo.customers.find_one({"_id": _id})
    return bookings['bookings']


def filter_rooms(min_price: float = None, max_price: float = None,
                 check_in: datetime = None, check_out: datetime = None,
                 hotel_id: str = None, room_type: int = None):
    # TODO: testing required
    filters = {}
    if min_price is not None:
        filters.update(
            {
                "price_per_night": {"$gte": min_price}
            }
        )
    if max_price is not None:
        filters.update(
            {
                "price_per_night": {"$lte": max_price}
            }
        )
    if check_in is not None:
        filters.update(
            {
                "date_from": {"$gte": check_in}
            }
        )
    if check_out is not None:
        filters.update(
            {
                "date_to": {"$lte": check_out}
            }
        )
    if hotel_id is not None:
        filters.update(
            {
                "hotel_id": ObjectId(hotel_id)
            }
        )
    if room_type is not None:
        filters.update(
            {
                "room_type": room_type
            }
        )
    return list(mongo.rooms.find(filters))
