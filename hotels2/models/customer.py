class Customer:
    def __init__(self, name, surname, email, password, bookings=None):
        if bookings is None:
            bookings = []
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.bookings = bookings
