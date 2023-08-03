#library for dsiplay list in table form
from tabulate import tabulate

#list for storing clients data
clients = []

#function for adding new client
def add_client():
	name = input("Enter your Nmae:")
	age = int(input("Enter your age:"))
	cnic = int(input("Enter your cnic Number:"))
	phone_number = int(input ("Enter your phone number:"))

	client ={

	"name" : name,
	"age" : age,
	"cnic" : cnic,
	"phone_number" : phone_number

	}

#add client in new list
	clients.append(client)
	print("Client added")


#function for display or view the client list
def view_client():
	if not client:
		print("No Client found.")

	else:
		table = tabulate(clients,heaers="keys",tablefmt="grid")
		print("Client List:")

		print(table)

