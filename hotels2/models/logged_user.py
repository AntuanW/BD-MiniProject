from flask_login import UserMixin


class LoggedUser(UserMixin):
    def __init__(self, _id, name, surname, email, password, bookings=None):
        if bookings is None:
            bookings = []
        self._id = _id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.bookings = bookings

    def get_id(self):
        return self._id
