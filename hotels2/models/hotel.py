class Hotel:
    def __init__(self, name, street, city, zip_code):
        self._id = None
        self.name = name
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def to_dict(self):
        return {
            "name": self.name,
            "street": self.street,
            "city": self.city,
            "zip_code": self.zip_code
        }

    def to_obj(data):
        pass
