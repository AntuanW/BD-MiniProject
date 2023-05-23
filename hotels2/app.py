from flask import Flask
from hotels2 import create_app
import pymongo
from hotels2.server.dbOperations import *
import pprint
from datetime import datetime

# app = create_app()

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
    add_new_booking("646c901812082ee1f12148fe", "646c886fc25694ae5532b750", datetime(2023, 5, 13), datetime(2023, 6, 2))
    # add_validators()
    # add_room("646c853b0436f81e3501b112", 4, 2, 160.0)
    # set_password("646c901812082ee1f12148fe", "fpga123")
    # add_customer("Piotr", "Faliszewski", "test-test.pl", "toizo")
    pass
