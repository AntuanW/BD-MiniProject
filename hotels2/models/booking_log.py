class BookingLog:
    def __init__(self, booking_id, customer_id, date_from, date_to):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.date_from = date_from
        self.date_to = date_to

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "customer_id": self.customer_id,
            "date_from": self.date_from,
            "date_to": self.date_to
        }
