from flask import Flask
import pymongo


app = Flask(__name__)
app.secret_key = b'!yny\x99{\x88,F\x85\x19y\xd67yL'


if __name__ == '__main__':
    app.run(debug=True)
