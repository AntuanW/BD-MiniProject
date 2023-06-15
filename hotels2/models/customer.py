class Customer:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.bookings = []
        self.password = password

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "password": self.password,
            "bookings": self.bookings
        }
