from hotels2.server.dbOperations import *
import pprint

mongo.rooms.delete_many({})
mongo.logs.delete_many({})
mongo.hotels.delete_many({})
mongo.customers.delete_many({})
add_validators()

hotel_data = [
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
    },
    {
        "name": "Samaria",
        "street": "Wesoła 11",
        "city": "Gdynia",
        "zip_code": "24323",
        "imgUrl": "https://www.hotel-cyprus.pl/thumb?w=1200&h=630&file=hotel-cyprus%2Fuser%2Fhotel%2Fnowe.jpg"
    }
]

hotel_ids = mongo.hotels.insert_many(hotel_data).inserted_ids

room_data = [
        vars(Room(hotel_ids[0], 2, 1, 150.0, True, "https://www.hospitality-school.com/wp-content/uploads/2022/06/classification-hotel-room-types.jpg")),
        vars(Room(hotel_ids[0], 2, 2, 250.0, True, "https://www.oetkercollection.com/media/51807/deluxe-room-the-lanesborough-hotel-london-2022.jpg?anchor=center&mode=crop&quality=85&width=680&height=460&rnd=133044220690000000")),
        vars(Room(hotel_ids[0], 3, 3, 350.0, True, "https://acehotel.com/new-york/wp-content/uploads/sites/9/2021/06/NYC-1096x722.jpg")),
        vars(Room(hotel_ids[0], 4, 4, 400.0, True, "https://hips.hearstapps.com/hmg-prod/images/sitting-rooms-hilliard-locust-18-11-20-1578948041.jpg")),
        vars(Room(hotel_ids[0], 1, 5, 110.0, True, "https://www.thespruce.com/thmb/iMt63n8NGCojUETr6-T8oj-5-ns=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/PAinteriors-7-cafe9c2bd6be4823b9345e591e4f367f.jpg")),
        vars(Room(hotel_ids[0], 2, 6, 265.0, True, "https://assets-global.website-files.com/5c6d6c45eaa55f57c6367749/624b471bdf247131f10ea14f_61d31b8dbff9b500cbd7ed32_types_of_rooms_in_a_5-star_hotel_2_optimized_optimized.jpeg")),
        vars(Room(hotel_ids[0], 2, 7, 270.0, True, "https://www.amenitiz.com/wp-content/uploads/2022/10/dervr7mcawpygipdzqvv.jpg")),
        vars(Room(hotel_ids[0], 2, 8, 250.0, True, "https://q-xx.bstatic.com/xdata/images/hotel/840x460/205684046.jpg?k=edd4b442376ac9cf1784cb06c8de0dc8a6037a871e50f060ba8bbcdc297cb74a&o=")),
        vars(Room(hotel_ids[0], 3, 9, 300.0, True, "https://gladstonehouse.agencydominion.net/uploads/2021/09/Gladstone_House_Guestroom-NoArt-King-1440x700.jpg")),
        vars(Room(hotel_ids[0], 4, 10, 460.0, False, "https://imageio.forbes.com/specials-images/imageserve/5cdb058a5218470008b0b00f/Nobu-Ryokan-Malibu/0x0.jpg?format=jpg&height=1009&width=2000")),
        vars(Room(hotel_ids[1], 2, 1, 150.0, True, "https://www.hospitality-school.com/wp-content/uploads/2022/06/classification-hotel-room-types.jpg")),
        vars(Room(hotel_ids[1], 2, 2, 250.0, True, "https://www.oetkercollection.com/media/51807/deluxe-room-the-lanesborough-hotel-london-2022.jpg?anchor=center&mode=crop&quality=85&width=680&height=460&rnd=133044220690000000")),
        vars(Room(hotel_ids[1], 3, 3, 350.0, True, "https://acehotel.com/new-york/wp-content/uploads/sites/9/2021/06/NYC-1096x722.jpg")),
        vars(Room(hotel_ids[1], 4, 4, 400.0, True, "https://hips.hearstapps.com/hmg-prod/images/sitting-rooms-hilliard-locust-18-11-20-1578948041.jpg")),
        vars(Room(hotel_ids[1], 1, 5, 110.0, True, "https://www.thespruce.com/thmb/iMt63n8NGCojUETr6-T8oj-5-ns=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/PAinteriors-7-cafe9c2bd6be4823b9345e591e4f367f.jpg")),
        vars(Room(hotel_ids[1], 2, 6, 265.0, True, "https://assets-global.website-files.com/5c6d6c45eaa55f57c6367749/624b471bdf247131f10ea14f_61d31b8dbff9b500cbd7ed32_types_of_rooms_in_a_5-star_hotel_2_optimized_optimized.jpeg")),
        vars(Room(hotel_ids[1], 2, 7, 270.0, True, "https://www.amenitiz.com/wp-content/uploads/2022/10/dervr7mcawpygipdzqvv.jpg")),
        vars(Room(hotel_ids[1], 2, 8, 250.0, True, "https://q-xx.bstatic.com/xdata/images/hotel/840x460/205684046.jpg?k=edd4b442376ac9cf1784cb06c8de0dc8a6037a871e50f060ba8bbcdc297cb74a&o=")),
        vars(Room(hotel_ids[1], 3, 9, 300.0, False, "https://gladstonehouse.agencydominion.net/uploads/2021/09/Gladstone_House_Guestroom-NoArt-King-1440x700.jpg")),
        vars(Room(hotel_ids[1], 4, 10, 460.0, True, "https://imageio.forbes.com/specials-images/imageserve/5cdb058a5218470008b0b00f/Nobu-Ryokan-Malibu/0x0.jpg?format=jpg&height=1009&width=2000")),
        vars(Room(hotel_ids[2], 2, 1, 150.0, True, "https://www.hospitality-school.com/wp-content/uploads/2022/06/classification-hotel-room-types.jpg")),
        vars(Room(hotel_ids[2], 2, 2, 250.0, True, "https://www.oetkercollection.com/media/51807/deluxe-room-the-lanesborough-hotel-london-2022.jpg?anchor=center&mode=crop&quality=85&width=680&height=460&rnd=133044220690000000")),
        vars(Room(hotel_ids[2], 3, 3, 350.0, True, "https://acehotel.com/new-york/wp-content/uploads/sites/9/2021/06/NYC-1096x722.jpg")),
        vars(Room(hotel_ids[2], 4, 4, 400.0, True, "https://hips.hearstapps.com/hmg-prod/images/sitting-rooms-hilliard-locust-18-11-20-1578948041.jpg")),
        vars(Room(hotel_ids[2], 1, 5, 110.0, True, "https://www.thespruce.com/thmb/iMt63n8NGCojUETr6-T8oj-5-ns=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/PAinteriors-7-cafe9c2bd6be4823b9345e591e4f367f.jpg")),
        vars(Room(hotel_ids[2], 2, 6, 265.0, True, "https://assets-global.website-files.com/5c6d6c45eaa55f57c6367749/624b471bdf247131f10ea14f_61d31b8dbff9b500cbd7ed32_types_of_rooms_in_a_5-star_hotel_2_optimized_optimized.jpeg")),
        vars(Room(hotel_ids[2], 2, 7, 270.0, False, "https://www.amenitiz.com/wp-content/uploads/2022/10/dervr7mcawpygipdzqvv.jpg")),
        vars(Room(hotel_ids[2], 2, 8, 250.0, True, "https://q-xx.bstatic.com/xdata/images/hotel/840x460/205684046.jpg?k=edd4b442376ac9cf1784cb06c8de0dc8a6037a871e50f060ba8bbcdc297cb74a&o=")),
        vars(Room(hotel_ids[2], 3, 9, 300.0, True, "https://gladstonehouse.agencydominion.net/uploads/2021/09/Gladstone_House_Guestroom-NoArt-King-1440x700.jpg")),
        vars(Room(hotel_ids[2], 4, 10, 460.0, True, "https://imageio.forbes.com/specials-images/imageserve/5cdb058a5218470008b0b00f/Nobu-Ryokan-Malibu/0x0.jpg?format=jpg&height=1009&width=2000")),
]
pprint.pprint()
room_check = mongo.rooms.insert_many(room_data)
