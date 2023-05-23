from hotels2.server.mongoConnection import *
from hotels2.models.hotel import Hotel
from hotels2.models.room import Room
from hotels2.models.customer import Customer
from datetime import date
from bson.objectid import ObjectId
import re

mongo = MongoConnection()


# ### Mongo schemas ###
hotel_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "street", "city", "zip_code"],
        "properties": {
            "name": {
                "bsonType": "string"
            },
            "street": {
                "bsonType": "string"
            },
            "city": {
                "bsonType": "string"
            },
            "zip_code": {
                "bsonType": "string",
                "description": "string consisting of 5 digit without any separators"
            }
        }
    }
}


# room_validator = {
#     "$jsonSchema": {
#         "bsonType": "object",
#         "required": ["hotel_id", "room_type", "room_number", "price_per_night", "is_available"],
#         "properties": {
#             "hotel_id": {
#                 "bsonType": "objectId"
#             },
#             "room_type": {
#                 "bsonType": "int"
#             },
#             "room_number": {
#                 "bsonType": "int"
#             },
#             "price_per_night": {
#                 "bsonType": "double"
#             },
#             "is_available": {
#                 "bsonType": "bool"
#             },
#             "bookings": {
#                 "bsonType": "array",
#                 "minItems": 0,
#                 "items": {
#                     "bsonType": ["object", "null"],
#                     "required": ["booking_id", "date_from", "date_to"],
#                     "properties": {
#                         "booking_id": {
#                             "bsonType": "objectId"
#                         },
#                         "date_from": {
#                             "bsonType": "date"
#                         },
#                         "date_to": {
#                             "bsonType": "date"
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }
room_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["hotel_id", "room_type", "room_number", "price_per_night", "is_available"],
        "properties": {
            "hotel_id": {
                "bsonType": "objectId"
            },
            "room_type": {
                "bsonType": "int"
            },
            "room_number": {
                "bsonType": "int"
            },
            "price_per_night": {
                "bsonType": "double"
            },
            "is_available": {
                "bsonType": "bool"
            },
            "bookings": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": ["booking_id", "date_from", "date_to"],
                    "properties": {
                        "booking_id": {
                            "bsonType": "objectId"
                        },
                        "date_from": {
                            "bsonType": "date"
                        },
                        "date_to": {
                            "bsonType": "date"
                        }
                    }
                }
            }
        },
        "allOf": [
            {
                "anyOf": [
                    {"not": {"properties": {"bookings": {"items": {"type": "object"}}}}},
                    {"properties": {"bookings": {"items": {"not": {"required": ["booking_id", "date_from", "date_to"]}}}}}
                ]
            }
        ]
    }
}

# customer_validator = {
#     "$jsonSchema": {
#         "bsonType": "object",
#         "required": ["name", "surname", "email", "password", "bookings"],
#         "properties": {
#             "name": {
#                 "bsonType": "string"
#             },
#             "surname": {
#                 "bsonType": "string"
#             },
#             "email": {
#                 "bsonType": "string"
#             },
#             "password": {
#                 "bsonType": "string"
#             },
#             "bookings": {
#                 "bsonType": "array",
#                 "items": {
#                     "bsonType": "object",
#                     "required": ["room_id", "check_in_date", "check_out_date"],
#                     "properties": {
#                         "room_id": {
#                             "bsonType": "objectId"
#                         },
#                         "check_in_date": {
#                             "bsonType": "date"
#                         },
#                         "check_out_date": {
#                             "bsonType": "date"
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }
customer_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "surname", "email", "password", "bookings"],
        "properties": {
            "name": {
                "bsonType": "string"
            },
            "surname": {
                "bsonType": "string"
            },
            "email": {
                "bsonType": "string"
            },
            "password": {
                "bsonType": "string"
            },
            "bookings": {
                "bsonType": ["array"],
                "items": {
                    "bsonType": "object",
                    "required": ["room_id", "check_in_date", "check_out_date"],
                    "properties": {
                        "room_id": {
                            "bsonType": "objectId"
                        },
                        "check_in_date": {
                            "bsonType": "date"
                        },
                        "check_out_date": {
                            "bsonType": "date"
                        }
                    }
                }
            }
        },
        "allOf": [
            {
                "anyOf": [
                    {"not": {"properties": {"bookings": {"items": {"type": "object"}}}}},
                    {"properties": {"bookings": {"items": {"not": {"required": ["room_id", "check_in_date", "check_out_date"]}}}}}
                ]
            }
        ]
    }
}


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
        print("Invalid zip code format. The format is: xxxxx")
        return False


def remove_hotel(hotel_id: str):
    _id = ObjectId(hotel_id)
    mongo.hotels.delete_one({"_id": _id})
    # TODO: remove all rooms of given hotel


def get_all_hotels():
    hotels = mongo.hotels.find()
    hotels = list(hotels)
    if len(hotels):
        print("Currently there is no hotels in the database.")
    return hotels


# ### Rooms methods ###
def add_room(hotel_id: str, room_type: int, room_number: int, ppn: float, availability: bool):
    _id = ObjectId(hotel_id)
    new_room = Room(_id, room_type, room_number, ppn, availability)
    mongo.rooms.insert_one(new_room.to_dict())


def remove_room(room_id: str):
    _id = ObjectId(room_id)
    mongo.rooms.delete_one({"_id": _id})


def get_all_rooms():
    # TODO: maybe remove it and make it into filters
    rooms = mongo.rooms.find({"is_available": True})
    rooms = list(rooms)
    if len(rooms) == 0:
        print("No available rooms.")
    return rooms


def get_all_rooms_of_specific_hotel(hotel_id: str):
    # TODO: maybe remove it and make it into filters
    _id = ObjectId(hotel_id)
    rooms = mongo.rooms.find({"hotel_id": _id, "is_available": True})
    if rooms is None:
        print("There is no hotel with such id in the database.")
        return []
    return list(rooms)


def set_price_per_night(room_id: str, new_price: float):
    _id = ObjectId(room_id)
    price_update = {
        "$set": {"price_per_night": new_price}
    }
    update = mongo.rooms.update_one({"_id": _id}, price_update)

    if update.matched_count <= 0:
        print("Failed to set nie price per night. There is no room with such id in the database.")
        return False
    return True


def set_availability(room_id: str, availability: bool):
    _id = ObjectId(room_id)
    availability_update = {
        "$set": {"is_available": availability}
    }
    update = mongo.rooms.update_one({"_id": _id}, availability_update)

    if update.matched_count <= 0:
        print("Failed to set availability. There is no room with such id in the database.")
        return False
    return True


def get_specific_rooms(in_date: date, out_date: date, room_type: int):
    pass


def check_room_availability():
    pass


# ### Customers methods ###
def add_customer(name: str, surname: str, mail: str, passwd: str):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    result = re.match(email_pattern, mail)

    if result:
        new_customer = Customer(name, surname, mail, passwd)
        mongo.customers.insert_one(new_customer.to_dict())
        return True
    else:
        print("Invalid email format, try - (string1)@(string2).(2+characters)")
        return False


def remove_customer(customer_id):
    _id = ObjectId(customer_id)
    mongo.customers.delete_one({"_id": _id})


def set_password(customer_id, new_password):
    # TODO: check if new and old password are the same
    _id = ObjectId(customer_id)
    password_update = {
        "$set": {"password": new_password}
    }
    update = mongo.rooms.update_one({"_id": _id}, password_update)

    if update.matched_count <= 0:
        print("Failed to set new password. There is no customer with such id in the database.")
        return False

    return True


def add_new_booking(customer_id: str, room_id: str, check_in: date, check_out: date):
    customer_id = ObjectId(customer_id)
    room_id = ObjectId(room_id)

    if check_in >= check_out:
        print("Check in date must be less than check out date.")
        return False

    # TODO: check if room is available on 100%

    customer_booking = {
        "room_id": room_id,
        "check_in_date": check_in,
        "check_out_date": check_out
    }

    room_booking = {
        "booking_id": customer_id,
        "date_from": check_in,
        "date_to": check_out
    }

    room_update = mongo.rooms.update_one({"_id": room_id}, {"$push": {"bookings": room_booking}})
    if room_update.matched_count <= 0:
        print("Failed to add booking to a room.")
        return False

    customer_update = mongo.customers.update_one({"_id": customer_id}, {"$push": {"bookings": customer_booking}})
    if customer_update.matched_count <= 0:
        print("Failed to add booking to a customer.")
        return False

    return True


def list_all_bookings(customer_id: str):
    pass


def change_room():
    # 1. check if new room is free during that period of time
    # 2. if true -> change (remove from room bookings and update room_id in customer bookings)
    # 3. else -> return a proper information
    pass


def change_booking_date():
    # 1. check if current room is available during new period of time
    # 2. if true -> change dates in both bookings
    # 3. else -> return a proper information
    pass
