from flask import Flask
from flask_login import LoginManager

from hotels2.models.logged_user import LoggedUser
from hotels2.server.dbOperations import *


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'!yny\x99{\x88,F\x85\x19y\xd67yL'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        user_data = mongo.customers.find_one({"_id": ObjectId(user_id)})
        if user_data:
            return LoggedUser(str(user_data['_id']), user_data['name'], user_data['surname'],
                              user_data['email'], user_data['password'], user_data['bookings'])
        return None

    from hotels2.routes.views import views
    from hotels2.routes.auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
