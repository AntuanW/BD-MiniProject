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

## Kolekcje:
### Hotels
```
{  
    "_id": ObjectId(),  
    "name": string,  
    "street": string,  
    "city": string,  
    "zipCode": string  
}
```

### Rooms
```
{  
    "_id": ObjectId(),  
    "hotelId": ObjectId(),  <- foreign key z Hotels  
    "type": string,  
    "roomNumber": string,  
    "pricePerNight": number,  
    "isAvailable": boolean  
}
```

### Customers
```
{  
    "_id": ObjectId(),  
    "name": string,  
    "surname": string,  
    "email": string,  
    "bookings": [ {  
        "roomId": ObjectId,  
        "checkInDate": string,  
        "checkOutDate": string  
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
- Customers
  - addCustomer(): dodaje użytkownika do kolekcji
  - removeCustomer(): usuwa użytkownika
  - setPassword(): zmień hasło
  - addBooking(): dodaj rezerwację
  - listBookings(): zwraca listę rezerwacji
  - changeRoom(): zmień pokój w rezeracji
  - changeDate(): zmień datę pobytu

# Pozostałe metody i funkcje:
- filterRooms(): pokaż dostępne pokoje w danym przedziale czasu