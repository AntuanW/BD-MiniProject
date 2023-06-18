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
            "zip_code": "81001",
            "imgUrl": "https://triverna.pl/uploads/album_514/th_fp1_12895_b6773d_bf8e29.jpg"
        },
        {
            "name": "Gołębiewski",
            "street": "Zielona 10",
            "city": "Rzeszów",
            "zip_code": "12345",
            "imgUrl": "https://www.ahstatic.com/photos/c096_ho_00_p_1024x768.jpg"
        }
    ]).inserted_ids

    rooms = [
        vars(Room(hotel_ids[0], 2, 1, 150.0, True, "https://www.hospitality-school.com/wp-content/uploads/2022/06/classification-hotel-room-types.jpg")),
        vars(Room(hotel_ids[0], 2, 2, 250.0, True, "https://www.oetkercollection.com/media/51807/deluxe-room-the-lanesborough-hotel-london-2022.jpg?anchor=center&mode=crop&quality=85&width=680&height=460&rnd=133044220690000000")),
        vars(Room(hotel_ids[0], 3, 3, 350.0, True, "https://acehotel.com/new-york/wp-content/uploads/sites/9/2021/06/NYC-1096x722.jpg")),
        vars(Room(hotel_ids[0], 4, 4, 400.0, True, "https://hips.hearstapps.com/hmg-prod/images/sitting-rooms-hilliard-locust-18-11-20-1578948041.jpg")),
        vars(Room(hotel_ids[1], 1, 1, 110.0, True, "https://www.thespruce.com/thmb/iMt63n8NGCojUETr6-T8oj-5-ns=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/PAinteriors-7-cafe9c2bd6be4823b9345e591e4f367f.jpg")),
        vars(Room(hotel_ids[1], 2, 2, 265.0, False, "https://assets-global.website-files.com/5c6d6c45eaa55f57c6367749/624b471bdf247131f10ea14f_61d31b8dbff9b500cbd7ed32_types_of_rooms_in_a_5-star_hotel_2_optimized_optimized.jpeg")),
        vars(Room(hotel_ids[1], 2, 3, 270.0, True, "https://www.amenitiz.com/wp-content/uploads/2022/10/dervr7mcawpygipdzqvv.jpg")),
        vars(Room(hotel_ids[1], 2, 4, 250.0, True, "https://q-xx.bstatic.com/xdata/images/hotel/840x460/205684046.jpg?k=edd4b442376ac9cf1784cb06c8de0dc8a6037a871e50f060ba8bbcdc297cb74a&o=")),
        vars(Room(hotel_ids[1], 3, 5, 300.0, True, "https://gladstonehouse.agencydominion.net/uploads/2021/09/Gladstone_House_Guestroom-NoArt-King-1440x700.jpg")),
        vars(Room(hotel_ids[1], 4, 6, 460.0, False, "https://imageio.forbes.com/specials-images/imageserve/5cdb058a5218470008b0b00f/Nobu-Ryokan-Malibu/0x0.jpg?format=jpg&height=1009&width=2000")),
    ]

    mongo.rooms.insert_many(rooms)

    names = ["Jesse", "Gustavo", "Walter", "Mike", "Steven"]
    surnames = ["Pinkman", "Fring", "White", "Ehrmantrout", "Gomez"]
    mails = ["jesse@mail.com", "hermanos@mail.com", "heisenberg@mail.com", "mike@mail.com", "gomey@mail.com"]
    passwords = ["12345", "12345", "12345", "12345", "12345"]

    for i in range(len(names)):
        add_customer(names[i], surnames[i], mails[i], passwords[i])


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
