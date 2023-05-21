from hotels2.server.mongoConnection import *
from hotels2.models.hotel import Hotel
from hotels2.models.room import Room
from hotels2.models.customer import Customer
from bson.objectid import ObjectId
import re

mongo = MongoConnection()


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
    if hotels is None:
        print("Currently there is no hotels in the database.")
        return []
    return list(hotels)


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
    if rooms is None:
        print("No available rooms.")
        return []
    return list(rooms)


def get_all_rooms_of_specific_hotel(hotel_id: str):
    _id = ObjectId(hotel_id)
    rooms = mongo.rooms.find_one({"_id": _id, "is_available": True})
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


# ### Customers methods ###
