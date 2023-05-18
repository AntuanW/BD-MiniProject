import certifi
import os
from pymongo import MongoClient
from dotenv import load_dotenv
import pprint

load_dotenv('.env')

username: str = os.getenv("MONGODB_USERNAME")
password: str = os.getenv("MONGODB_PASSWORD")


class MongoConnection:
    def __init__(self):
        self.db = None
        self.client = None
        self.uri = f"""mongodb+srv://{username}:{password}@hotelscluster.53jqjfk.mongodb.net/?retryWrites=true&w=majority"""
        self.customers = None
        self.hotels = None
        self.rooms = None

    def init_mongo_connection(self):
        self.client = MongoClient(self.uri, tlsCAFile=certifi.where())
        self.db = self.client["HotelsDB"]
        self.customers = self.db["Customers"]
        self.hotels = self.db["Hotels"]
        self.rooms = self.db["Rooms"]


if __name__ == '__main__':
    mongo = MongoConnection()
    mongo.init_mongo_connection()