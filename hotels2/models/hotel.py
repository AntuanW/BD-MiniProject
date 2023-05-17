def to_obj(data):
    hotel = Hotel(
        data["name"],
        data["street"],
        data["city"],
        data["zip_code"],
        data["_id"]
    )

    return hotel


class Hotel:
    def __init__(self, name, street, city, zip_code, id_=None):
        self._id = id_
        self.name = name
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def to_dict(self):
        return {
            "_id": self._id,
            "name": self.name,
            "street": self.street,
            "city": self.city,
            "zip_code": self.zip_code
        }
