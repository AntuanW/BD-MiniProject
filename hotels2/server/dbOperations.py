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
            }
        }
    }
}


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
                "bsonType": "array",
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
        }
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
    else:
        print("Invalid zip code format. The format is: xxxxx")


def remove_hotel(hotel_id: str):
    _id = ObjectId(hotel_id)
    mongo.hotels.delete_one({"_id": _id})


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
    rooms = mongo.rooms.find({"is_available": True})
    rooms = list(rooms)
    if len(rooms) == 0:
        print("No available rooms.")
    return rooms


def get_all_rooms_of_specific_hotel(hotel_id: str):
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


def set_availability(room_id: str, availability: bool):
    _id = ObjectId(room_id)
    availability_update = {
        "$set": {"is_available": availability}
    }
    update = mongo.rooms.update_one({"_id": _id}, availability_update)

    if update.matched_count <= 0:
        print("Failed to set availability. There is no room with such id in the database.")


def get_specific_rooms(in_date: date, out_date: date, room_type: int):
    # specific_rooms = mongo.rooms.find({
    #     "room_type": room_type,
    #     "is_available": True,
    #     "$and": [
    #         {
    #             "check_in_date": {"$gte": in_date}
    #         },
    #         {
    #             "check_out_date": {"$lte": out_date}
    #         }
    #     ]
    # })
    # return list(specific_rooms)
    pass


# ### Customers methods ###
def add_customer():
    pass


def remove_customer():
    pass


def set_password():
    pass


def add_new_booking():
    pass


def list_all_bookings():
    pass


def change_room():
    pass


def change_booking_date():
    pass
