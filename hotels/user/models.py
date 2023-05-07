from flask import Flask, jsonify, request
import uuid


class User:
    def signup(self):
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "last_name": request.form.get('last-name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        return jsonify(user), 200