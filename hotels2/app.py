from flask import Flask
from hotels2 import create_app
import pymongo
from hotels2.server.dbOperations import *
import pprint
from datetime import datetime

# app = create_app()


def create_data():
    # add_hotel('Marina Resort', 'Bulwar Nadmorski 10', 'Gdynia', '81001')
    # add_room("646cf9e0c4ab2ad0c9bb1db5", 2, 1, 150)
    # add_room("646cf9e0c4ab2ad0c9bb1db5", 3, 2, 300)
    # add_room("646cf9e0c4ab2ad0c9bb1db5", 4, 3, 450)
    # add_customer("Jacek", "Długopolski", "test@test.pl", "fpga")
    # add_customer("Jan", "Małopolski", "test@test.edu.pl", "fpga123")
    # add_customer("Piotr", "Faliszewski", "test@test.agh.pl", "toizo")
    pass


if __name__ == '__main__':
    # app.run(debug=True)
    # add_hotel('Marina Resort', 'Bulwar Nadmorski 10', 'Gdynia', '81001')
    # remove_hotel("646c85942b4cd2d529157109")
    # pprint.pprint(get_all_hotels())
    # add_room("646c853b0436f81e3501b112", 2, 1, 150)
    # add_room("646c853b0436f81e3501b112", 3, 2, 300)
    # add_room("646c853b0436f81e3501b112", 4, 3, 450)
    # add_room("146c853b0436f81e3501b112", 4, 3, 450)
    # remove_room("646c888aa4857af41df43c86")
    # set_price_per_night("46c8870c25694ae5532b751", 350.0)
    # set_availability("146c8870c25694ae5532b751", False)
    # add_customer("Jacek", "Długopolski", "test@test.pl", "fpga")
    # add_customer("Jan", "Małopolski", "test@test.pl", "fpga")
    # set_password("646c904b44697a21f43d223d", "test")
    # add_new_booking("646c901812082ee1f12148fe", "646c886fc25694ae5532b750", datetime(2023, 5, 13), datetime(2023, 5, 15))
    # add_validators()
    # add_room("646c853b0436f81e3501b112", 4, 2, 160.0)
    # set_password("646c901812082ee1f12148fe", "fpga123")

    # add_customer("Piotr", "Faliszewski", "test@test.agh.pl", "toizo")
    # add_new_booking("646cf7c17e5f01d84c87773b", "646c886fc25694ae5532b750", datetime(2023, 5, 22), datetime(2023, 5, 31))


    # create_data()
    # print(can_be_booked(ObjectId("646cf9f8e31893a53be72ec7"), datetime(2023, 5, 18), datetime(2023, 5, 20)))    # false
    # print(can_be_booked(ObjectId("646cf9f8e31893a53be72ec7"), datetime(2023, 5, 15), datetime(2023, 5, 16)))    # false
    # print(can_be_booked(ObjectId("646cf9f8e31893a53be72ec7"), datetime(2023, 5, 12), datetime(2023, 5, 14)))    # false
    # print(can_be_booked(ObjectId("646cf9f8e31893a53be72ec7"), datetime(2023, 5, 20), datetime(2023, 5, 23)))    # false
    # print(can_be_booked(ObjectId("646cf9f8e31893a53be72ec7"), datetime(2023, 5, 11), datetime(2023, 5, 13)))    # true
    # print(can_be_booked(ObjectId("646cf9f8e31893a53be72ec7"), datetime(2023, 5, 22), datetime(2023, 5, 25)))    # true
    # print(can_be_booked(ObjectId("646cf9f8e31893a53be72ec7"), datetime(2023, 5, 10), datetime(2023, 5, 12)))    # true
    # print(can_be_booked(ObjectId("646cf9f8e31893a53be72ec7"), datetime(2023, 5, 25), datetime(2023, 5, 30)))    # true

    # can_be_booked(ObjectId("646cf9f8e31893a53be72ec7"), datetime(2023, 5, 18), datetime(2023, 5, 20))
    # add_new_booking("646cfa23a2874ff1ffd18faf", "646cf9f8e31893a53be72ec7", datetime(2023, 5, 15), datetime(2023, 5, 22))
    # print(get_all_hotels())
    print(list_all_bookings("646cfa23a2874ff1ffd18fad"))
    pass
