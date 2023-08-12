#library for displaying list in table form
from tabulate import tabulate

#list for storing clients data
clients = []

#function for adding new client
def add_client():
    name = input("Enter your Name:")
    age = int(input("Enter your age:"))
    cnic = int(input("Enter your CNIC Number:"))
    phone_number = int(input("Enter your phone number:"))

    client = {
        "Name": name,
        "Age": age,
        "Cnic": cnic,
        "Phone_number": phone_number
    }

    # add client in the clients list
    clients.append(client)
    print("Client added")

# function for displaying or viewing the client list
def view_clients():
    if not clients:
        print("No Clients found.")
    else:
        table = tabulate(clients, headers="keys", tablefmt="grid")
        print("Client List:")
        print(table)
