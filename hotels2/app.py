from flask import Flask
from hotels2 import create_app
import pymongo


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
