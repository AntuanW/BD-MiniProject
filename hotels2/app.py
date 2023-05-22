from flask import Flask
from hotels2 import create_app
import pymongo
from hotels2.server.dbOperations import *
import pprint

#app = create_app()

if __name__ == '__main__':
    #app.run(debug=True)
    add_validators()
    # add_room("646ba9cec1305c12cedb02bb", 2, 3, 100.0, True)

    pass
