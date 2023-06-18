from flask import Flask
from hotels2 import create_app
import pymongo
from hotels2.server.dbOperations import *
import pprint
from datetime import datetime

# jak chcesz cos testowac bez frontendu to to zakomentuj (app.run też ofc)
# app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    # add_new_booking('648e11b8065730487e617029', '648b44e51905fb362393077b', datetime(2023, 6, 14), datetime(2023, 6, 26))
    # change_booking('648e11b8065730487e617029', '648b4ddaa5d9d069080dbde4', '648f6c8a4f455597330fd1c5', datetime(2023, 7, 10), datetime(2023, 7, 12))
    pprint.pprint(get_all_user_bookings('648e11b8065730487e617029'))
    pass