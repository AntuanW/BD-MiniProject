from flask import Flask, render_template, redirect, session
from functools import wraps
import pymongo


app = Flask(__name__)
app.secret_key = b'!yny\x99{\x88,F\x85\x19y\xd67yL'

#Database
client = pymongo.MongoClient('localhost', 27017)
db = client.HotelsDBProject

# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*arg, **kwargs):
        if 'logged_in' in session:
            return f(*arg, **kwargs)
        else:
            return redirect('/')
    return wrap

#Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')