from flask import Flask
from hotels2 import create_app
import pymongo
from hotels2.server.dbOperations import *
import pprint
from datetime import datetime

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    pprint.pp(get_occupied_rooms(datetime(2023, 6, 19), datetime(2023, 12, 12)))