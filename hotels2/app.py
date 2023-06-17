from flask import Flask
from hotels2 import create_app
import pymongo
from hotels2.server.dbOperations import *
import pprint
from datetime import datetime

# app = create_app()


if __name__ == '__main__':
    # add_hotel("Heron", "Ogrodowa 10", "Kraków", "17453")
    # remove_hotel("648b4b654efd3cfbb52bccb2")
    # pprint.pprint(get_all_hotels())
    # add_room("648b4c2ed0ff45bbcee56bf1", 3, 1, 90)
    # remove_room("648b4d2cbc4ecc67d5dd4f02")
    # set_price_per_night("648b4ddaa5d9d069080dbde4", 110)
    # set_availability("648b4ddaa5d9d069080dbde4", False)
    # add_customer("Hank", "Schrader", "schrader@mail.com", "674645")
    # remove_customer("648b4e9b273a6e78d1426ea1")
    # set_password("648b44e51905fb3623930789", "hd832r")
    # pprint.pprint(list_all_bookings("648b44e51905fb3623930785"))
    # pprint.pprint(can_be_booked(ObjectId("648b44e51905fb362393077c"), datetime(2023, 7, 1), datetime(2023, 7, 5), ObjectId('648b4a6492dececdfc9df7ed')))
    change_booking("648b44e51905fb3623930785", "648b44e51905fb362393077d", "648b4a6492dececdfc9df7e8", datetime(2023, 6, 26), datetime(2023, 7, 1))
    pass

