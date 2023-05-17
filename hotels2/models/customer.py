class Customer:
    def __init__(self, name, surname, email, _id=None):
        self._id = _id
        self.name = name
        self.surname = surname
        self.email = email
        self.bookings = []

    def add_booking(self, room_id, check_in_date, check_out_date):
        booking = {
            "room_id": room_id,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date
        }
        self.bookings.append(booking)

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "bookings": self.bookings
        }

    def to_obj(self, data):
        customer = Customer(
            data["name"],
            data["surname"],
            data["email"],
            data["_id"],
        )

        customer.bookings = data["bookings"]
        return customer