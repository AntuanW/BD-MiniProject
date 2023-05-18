class Customer:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.bookings = []
        self.password = password

    def add_booking(self, room_id, check_in_date, check_out_date):
        booking = {
            "room_id": room_id,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date
        }
        self.bookings.append(booking)

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "bookings": self.bookings,
            "password": self.password
        }
