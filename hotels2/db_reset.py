from hotels2.server.dbOperations import *


def clear_db():
    mongo.rooms.delete_many({})
    mongo.logs.delete_many({})
    mongo.hotels.delete_many({})
    mongo.customers.delete_many({})


def reset_db():
    add_validators()
    hotel_ids = mongo.hotels.insert_many([
        {
            "name": "Marina Resort",
            "street": "Bulwar Nadmorski 10",
            "city": "Gdynia",
            "zip_code": "81001"
        },
        {
            "name": "Gołębiewski",
            "street": "Zielona 10",
            "city": "Rzeszów",
            "zip_code": "12345"
        }
    ]).inserted_ids

    rooms = [
        Room(hotel_ids[0], 2, 1, 150.0, True),
        Room(hotel_ids[0], 2, 2, 250.0, True),
        Room(hotel_ids[0], 3, 3, 350.0, True),
        Room(hotel_ids[0], 4, 4, 400.0, True),
        Room(hotel_ids[1], 1, 1, 110.0, True),
        Room(hotel_ids[1], 2, 2, 265.0, False),
        Room(hotel_ids[1], 2, 3, 270.0, True),
        Room(hotel_ids[1], 2, 4, 250.0, True),
        Room(hotel_ids[1], 3, 5, 300.0, True),
        Room(hotel_ids[1], 4, 6, 460.0, False),
    ]

    room_dicts = []
    for room in rooms:
        room_dicts.append(room.to_dict())

    mongo.rooms.insert_many(room_dicts)

    names = ["Jesse", "Gustavo", "Walter", "Mike", "Steven"]
    surnames = ["Pinkman", "Fring", "White", "Ehrmantrout", "Gomez"]
    mails = ["jesse@mail.com", "hermanos@mail.com", "heisenberg@mail.com", "mike@mail.com", "gomey@mail.com"]
    passwds = ["1234", "5432", "7654", "7868", "4432"]

    for i in range(len(names)):
        add_customer(names[i], surnames[i], mails[i], passwds[i])


def add_example_bookings():
    add_new_booking("648b44e51905fb3623930785", "648b44e51905fb362393077b",
                    datetime(2023, 6, 25), datetime(2023, 6, 30))
    add_new_booking("648b44e51905fb3623930785", "648b44e51905fb362393077c",
                    datetime(2023, 7, 15), datetime(2023, 7, 25))
    add_new_booking("648b44e51905fb3623930786", "648b44e51905fb362393077c",
                    datetime(2023, 7, 1), datetime(2023, 7, 10))
    add_new_booking("648b44e51905fb3623930787", "648b44e51905fb362393077d",
                    datetime(2023, 8, 1), datetime(2023, 8, 3))
    add_new_booking("648b44e51905fb3623930788", "648b44e51905fb362393077e",
                    datetime(2023, 6, 21), datetime(2023, 7, 1))
    add_new_booking("648b44e51905fb3623930789", "648b44e51905fb362393077c",
                    datetime(2023, 7, 10), datetime(2023, 7, 14))


# add_example_bookings()
# clear_db()
# reset_db()
