from hotels2.server.dbOperations import *
user_data = [
    ("Adam", "Nowak", "adam.nowak@example.com", "h2Jp#9g$4"),
    ("Marta", "Kowalska", "marta.kowalska@example.com", "b!G6@eWd1"),
    ("Michał", "Wiśniewski", "michal.wisniewski@example.com", "s9#kF!7lR"),
    ("Anna", "Lewandowska", "anna.lewandowska@example.com", "T1*rG$0mN"),
    ("Piotr", "Nowicki", "piotr.nowicki@example.com", "d#s2B$1kZ")
]

for usr_data in user_data:
    add_customer(usr_data[0], usr_data[1], usr_data[2], usr_data[3])
