from flask import Flask
from app import app
from models import User


@app.route('/user/signup', methods=['GET'])
def signup():
    return User().signup()
