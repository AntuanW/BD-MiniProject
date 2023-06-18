class Room:
    def __init__(self, hotel_id, room_type, room_number, price_per_night, is_available, imgUrl):
        self.hotel_id = hotel_id
        self.room_type = room_type
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.is_available = is_available
        self.imgUrl = imgUrl
        self.bookings = []
