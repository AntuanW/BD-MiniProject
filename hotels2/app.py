from flask import Flask
from hotels2 import create_app
import pymongo
from hotels2.server.dbOperations import *
import pprint
from datetime import datetime

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    pprint.pp(get_occupied_rooms(datetime(2123, 6, 19), datetime(2123, 12, 12)))
    pprint.pprint(get_all_cities())