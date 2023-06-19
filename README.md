# BD-MiniProject

Grzegorz Piśkorski: piskorski@student.agh.edu.pl

Antoni Wójcik: antoniwojcik@student.agh.edu.pl

Temat projektu:
    Rezerwowanie noclegów w hotelach. Aplikacja będzie pozwalała na rezerwację pokojów w kilku wybranych hotelach.

Technologia:
    MongoDB, Python Flask


# Główna założenia projektu:
- możliwość zarezerwowania noclegu w jednym z dostępnych hotelów w bazie danych (wyświetlenie dostępnych pokoi w danym okresie czasu)
- możliwość zarządzania swoją rezerwacją (dodanie nowej, modyfikacja jednej z "posiadanych" rezerwacji, rezygnacja z rezerwacji)

# Propozycja bazy danych:

### Hotels
```
{  
    "name": string,  
    "street": string,  
    "city": string,  
    "zip_code": string  
}
```

### Rooms
```
{   
    "hotel_id": ObjectId(),  
    "room_type": string,  
    "room_number": string,  
    "price_per_night": number,  
    "is_available": boolean,
    "bookings": [
      {
        "booking_id": ObjectId
        "customer_id": ObjectId,
        "date_from": date,
        "date_to": date
      }
    ]
}
```

### Customers
```
{   
    "name": string,  
    "surname": string,  
    "email": string,  
    "bookings": [ {
        "booking_id": ObjectId <- generowanie automatyczne
        "room_id": ObjectId,  
        "date_from": string,  
        "date_to": string
    } ],
    "password": string
}
```

### Booking_logs
```
{
  "booking_id": ObjectId
  "customer_id": ObjectId,
  "room_id": ObjectId,
  "date_from": date,
  "date_to": date
}
```

# Metody i funcje operujące na poszczególnych kolekcjach - część z nich, nie jest wykorzystywana w aplikacji, ponieważ nie udało się zaimplementować, niektórych funkcjonalności, ale przydatne są przy zarządzaniu bazą danych:

- Hotels
  - get_all_hotels() - zwraca listę z danymi o hotelach
  - get_all_cities() - zwraca listę miast, z których są hotele (przydatna w filtrach)
  - add_hotel(name, street, city, zip_code, img) - dodaje hotel do bazy
  - remove_hotel(hotel_id) - usuwa hotel z bazy wraz z jego pokojami (zał. nie ma żadnych rezerwacji na pokoje z danego hotelu)
- Rooms
  - get_wrong_bookings(room_id, check_in, check_out, booking_id) - zwraca listę rezerwacji nachądzących na podany okres czasu
  - get_occupied_rooms(check_in, check_out) - zwraca listę pokoi, które są zarezerwowane w podanym okresie czasu
  - add_room(hotel_id, room_type, room_number, ppn, img, availability) - dodaje pokój od bazy
  - remove_room(room_id) - usuwa pokój z bazy danych
  - set_price_per_night(room_id, new_price) - zmienia cenę za noc danego pokoju
  - set_availability(room_id, availability) - uaktualnia dostępność danego pokoju (chodzi o dostępność w razie np. remontu pokoju)
- Customers
  - add_customer(name, surname, mail, passwd) - dodaje nowego użytkownika do bazy danych
  - get_all_user_bookings(user_id) - zwraca listę wszystkich rezerwacji danego użytkownika
  - get_user_email(email) - zwraca użytkownika o podanym emailu - przydatna w uwierzytelnianiu użytkownika
  - remove_customer(customer_id) - usuwa użytkownika z bazdy danych

# Metody i funkcje korzystające z więcej niż jednej kolekcji
- can_be_booked(room_id, check_in, check_out, booking_id) - funkcja pomocnicza, korzystająca z get_wrong_bookings - sprawdza czy można zarezerwować podany pokój na konkretny termin
- push_bookings(booking_id, customer_id, room_id, check_in, check_out) - funkcja pomocnicza - dodaje odpowiednie dane do odpowiedniego pokoju i użytkownika na temat rezerwacji
- add_new_booking(customer_id, room_id, check_in, check_out) - dodanie nowej rezerwacji - dodawana jest w kolekcji Customers i Rooms (o ile to możliwe)
- change_booking(customer_id, room_id, booking_id, check_in, check_out) - zmiana rezerwacji danego pokoju przez klienta, wprowadza zmiany w obu kolekcjach (o ile to możliwe)
- filter_rooms(check_in, check_out, min_price, max_price, room_type, hotel_city) - zwraca listę pokoi, spełniających podane kryteria (np. cena min i max, liczba osób w pokoju, pokoje wolne w danym terminie itp.)
- remove_booking(booking_id, customer_id, room_id) - usuwa danę rezerwację z obu kolekcji - Rooms i Customers
- add_validators() - dodaje do bazy danych walidatory, których schemat pokazany jest poniżej

# Schema validators dla naszego schematu

## Hotels
```
{
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "street", "city", "zip_code", "imgUrl"],
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
            },
            "imgUrl": {
                "bsonType": "string"
            }
        }
    }
}
```

## Rooms
```
{
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["hotel_id", "room_type", "room_number", "price_per_night", "is_available", "imgUrl"],
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
            "imgUrl": {
                "bsonType": "string"
            },
            "bookings": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "properties": {
                        "booking_id": {
                            "bsonType": "objectId"
                        },
                        "customer_id": {
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
```

## Customers
```
{
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
                        "booking_id": {
                            "bsonType": "objectId"
                        },
                        "room_id": {
                            "bsonType": "objectId",
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
```

## Booking_Logs
```
{
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["booking_id", "customer_id", "room_id", "date_from", "date_to"],
        "properties": {
            "booking_id": {
                "bsonType": "objectId"
            },
            "customer_id": {
                "bsonType": "objectId"
            },
            "room_id": {
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
```

# Widoki - frontend
- start_page - strona startowa, którą widzimy po wejściu do aplikacji
- login - widok logowania
- signup - widok tworzenia konta
- rooms_list - lista pokoi (wraz z filtrami), kiedy nie jesteśmy zalogowani
- my_bookings - widok dla zalogowanego użytkownika - wyświetla wszystkie nasze (przyszłe i przeszłe) rezerwacje oraz daje możliwość modyfikacji rezerwacji
- reserve_rooms - widok dla zalogowanego użytkownika - taki sam jak widok rooms_list, ale z opcją rezerwacji pokoju
