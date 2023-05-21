from flask import Flask
from hotels2 import create_app
import pymongo
from server.dbOperations import *
import pprint

app = create_app()

if __name__ == '__main__':
    # app.run(debug=True)
    # add_hotel("Perła południa", "Kwiatowa 8", "Nowy Sącz", "33300")
    # add_hotel("Helion", "Kawiory 8", "Kraków", "30091")
    # remove_hotel("646a2a0b34546d0ca929772f")
    # print(get_all_rooms())
    # print(get_all_hotels())
    # add_room("646a2f648a4e890c2cd87280", 1, 1, 100, True)
    # pprint.pprint(get_all_rooms_of_specific_hotel("646a2a34f9a06bd06034a12e"))
    # set_price_per_night("646a2f93907ce15c59aa479f", 150)
    # set_availability("646a2f93907ce15c59aa479f", False)

    pass
