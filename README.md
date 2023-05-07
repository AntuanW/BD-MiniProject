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