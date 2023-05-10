# BD-MiniProject

Grzegorz Piśkorski: piskorski@student.agh.edu.pl

Antoni Wójcik: antoniwojcik@student.agh.edu.pl

Temat projektu:
    Rezerwowanie noclegów w hotelach. Aplikacja będzie pozwalała na rezerwację pokojów w kilku wybranych hotelach.

Technologia:
    MongoDB, Python Flask


# Wstępny schemat bazy danych w MongoDB
| booking |   rooms    |  hotels |   users    |
|  :---:  |   :---:    |  :---:  |   :---:    |
| room()  | type       | name    | name       |
| hotel() | capacity   | desc    | surname    |
| date    | price      | rating  | bookings[] |
| user()  | hotel()    | address | e-mail     |
|         | bookings() | rooms[] | password   |


# Główna funkcje projektu:
- możliwość zarezerwowania noclegu w jednym z dostępnych hotelów w bazie danych (wyświetlenie dostępnych pokoi w danym okresie czasu)
- możliwość zarządzania swoją rezerwacją (dodanie nowej, modyfikacja jednej z "posiadanych" rezerwacji, rezygnacja z rezerwacji)

# Nowa propozycja bazy danych:

## Nazwa: HotelsMiniProject

## Kolekcje:
### Hotels
{  
    "_id": ObjectId(),  
    "name": string,  
    "street": string,  
    "city": string,  
    "zipCode": string  
}  

### Rooms
{  
    "_id": ObjectId(),  
    "hotelId": ObjectId(),  <- foreign key z Hotels  
    "type": string,  
    "roomNumber": string,  
    "pricePerNight": number,  
    "isAvailable": boolean  
}  

### Customers
{  
    "_id": ObjectId(),  
    "name": string,  
    "surname": string,  
    "email": string,  
    "bookings": [{  
        "roomId": ObjectId,  
        "checkInDate": string,  
        "checkOutDate": string  
    }]  
}  