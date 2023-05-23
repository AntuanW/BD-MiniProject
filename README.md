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
        "booking_id": ObjectId(),
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
        "room_id": ObjectId,  
        "check_in_date": string,  
        "check_out_date": string  
    } ],
    "password": string
}
```

# Metody i funcje operujące na poszczególnych kolekcjach:

- Hotels
  - add_hotel(name, street, city, zip_code): dodanie hotelu do oferty
  - remove_hotel(hotel_id): usunięcie hotelu wraz z pokojami
  - get_all_hotels(): zwrca listę dostępnych hoteli
- Rooms
  - add_room(): dodawanie pokoju
  - remove_room(): usuwanie pokoju
  - get_all_rooms(): zwraca listę dostepnych pokoi
  - get_all_rooms_of_specific_hotel(): zwraca listę dostępnych pokoi należących do konkretnego hotelu
  - set_price_per_night(): zmień cenę danego pokoju
  - set_availability() : zmienia dostępność pokoju
  - filter_rooms(): pokaż dostępne pokoje ze wskazanymi filtrami
- Customers
  - addCustomer(): dodaje użytkownika do kolekcji
  - removeCustomer(): usuwa użytkownika
  - setPassword(): zmień hasło
  - addBooking(): dodaj rezerwację
  - listBookings(): zwraca listę rezerwacji
  - changeRoom(): zmień pokój w rezeracji
  - changeDate(): zmień datę pobytu

# Schema validators dla naszego schematu

## Hotels
```
{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'name',
      'street',
      'city',
      'zip_code'
    ],
    properties: {
      name: {
        bsonType: 'string'
      },
      street: {
        bsonType: 'string'
      },
      city: {
        bsonType: 'string'
      },
      zip_code: {
        bsonType: 'string',
        description: 'string consisting of 5 digit without any separators'
      }
    }
  }
}
```

## Rooms
```
{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'hotel_id',
      'room_type',
      'room_number',
      'price_per_night',
      'is_available'
    ],
    properties: {
      hotel_id: {
        bsonType: 'objectId'
      },
      room_type: {
        bsonType: 'int'
      },
      room_number: {
        bsonType: 'int'
      },
      price_per_night: {
        bsonType: 'double',
        minimum: 0,
        exclusiveMinimum: true
      },
      is_available: {
        bsonType: 'bool'
      },
      bookings: {
        bsonType: 'array',
        items: {
          bsonType: 'object',
          properties: {
            booking_id: {
              bsonType: 'objectId'
            },
            date_from: {
              bsonType: 'date'
            },
            date_to: {
              bsonType: 'date'
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
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'name',
      'surname',
      'email',
      'password',
      'bookings'
    ],
    properties: {
      name: {
        bsonType: 'string'
      },
      surname: {
        bsonType: 'string'
      },
      email: {
        bsonType: 'string'
      },
      password: {
        bsonType: 'string'
      },
      bookings: {
        bsonType: [
          'array'
        ],
        items: {
          bsonType: 'object',
          properties: {
            room_id: {
              bsonType: 'objectId'
            },
            check_in_date: {
              bsonType: 'date'
            },
            check_out_date: {
              bsonType: 'date'
            }
          }
        }
      }
    }
  }
}
```
