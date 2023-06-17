from flask import Flask
from hotels2 import create_app
import pymongo
from hotels2.server.dbOperations import *
import pprint
from datetime import datetime

# jak chcesz cos testowac bez frontendu to to zakomentuj (app.run też ofc)
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


