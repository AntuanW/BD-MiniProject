from flask import Flask, jsonify


class User:
    def signup(self):
        user = {
            "_id": "",
            "name": "",
            "last_name": "",
            "email": "",
            "password": ""
        }

        return jsonify(user), 200