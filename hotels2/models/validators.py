# Mongo schemas ###

hotel_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "street", "city", "zip_code"],
        "properties": {
            "name": {
                "bsonType": "string"
            },
            "street": {
                "bsonType": "string"
            },
            "city": {
                "bsonType": "string"
            },
            "zip_code": {
                "bsonType": "string",
                "description": "string consisting of 5 digit without any separators"
            }
        }
    }
}

room_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["hotel_id", "room_type", "room_number", "price_per_night", "is_available"],
        "properties": {
            "hotel_id": {
                "bsonType": "objectId"
            },
            "room_type": {
                "bsonType": "int"
            },
            "room_number": {
                "bsonType": "int"
            },
            "price_per_night": {
                "bsonType": "double",
                "minimum": 0.0,
                "exclusiveMinimum": True
            },
            "is_available": {
                "bsonType": "bool"
            },
            "bookings": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "booking_id": {
                            "bsonType": "objectId"
                        },
                        "date_from": {
                            "bsonType": "date"
                        },
                        "date_to": {
                            "bsonType": "date"
                        }
                    }
                }
            }
        }
    }
}

customer_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "surname", "email", "password", "bookings"],
        "properties": {
            "name": {
                "bsonType": "string"
            },
            "surname": {
                "bsonType": "string"
            },
            "email": {
                "bsonType": "string"
            },
            "password": {
                "bsonType": "string"
            },
            "bookings": {
                "bsonType": ["array"],
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "room_id": {
                            "bsonType": "objectId",
                        },
                        "check_in_date": {
                            "bsonType": "date"
                        },
                        "check_out_date": {
                            "bsonType": "date"
                        }
                    }
                }
            }
        }
    }
}


# room_validator = {
#     "$jsonSchema": {
#         "bsonType": "object",
#         "required": ["hotel_id", "room_type", "room_number", "price_per_night", "is_available"],
#         "properties": {
#             "hotel_id": {
#                 "bsonType": "objectId"
#             },
#             "room_type": {
#                 "bsonType": "int"
#             },
#             "room_number": {
#                 "bsonType": "int"
#             },
#             "price_per_night": {
#                 "bsonType": "double"
#             },
#             "is_available": {
#                 "bsonType": "bool"
#             },
#             "bookings": {
#                 "bsonType": "array",
#                 "minItems": 0,
#                 "items": {
#                     "bsonType": ["object", "null"],
#                     "required": ["booking_id", "date_from", "date_to"],
#                     "properties": {
#                         "booking_id": {
#                             "bsonType": "objectId"
#                         },
#                         "date_from": {
#                             "bsonType": "date"
#                         },
#                         "date_to": {
#                             "bsonType": "date"
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }

# customer_validator = {
#     "$jsonSchema": {
#         "bsonType": "object",
#         "required": ["name", "surname", "email", "password", "bookings"],
#         "properties": {
#             "name": {
#                 "bsonType": "string"
#             },
#             "surname": {
#                 "bsonType": "string"
#             },
#             "email": {
#                 "bsonType": "string"
#             },
#             "password": {
#                 "bsonType": "string"
#             },
#             "bookings": {
#                 "bsonType": "array",
#                 "items": {
#                     "bsonType": "object",
#                     "required": ["room_id", "check_in_date", "check_out_date"],
#                     "properties": {
#                         "room_id": {
#                             "bsonType": "objectId"
#                         },
#                         "check_in_date": {
#                             "bsonType": "date"
#                         },
#                         "check_out_date": {
#                             "bsonType": "date"
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }
