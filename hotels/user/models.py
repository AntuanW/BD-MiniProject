from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class User:
    def signup(self):
        # Create new user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "last_name": request.form.get('last-name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        
        # Check if email uniq
        if db.Users.find_one({ "email": user['email'] }):
            return jsonify({"error": "Email already in use"}), 400

        if db.Users.insert_one(user):
            return jsonify(user), 200

        return jsonify({ "error": "Signup failed" }), 400