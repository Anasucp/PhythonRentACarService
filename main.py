import client 
import car 
import driver 
import booking 
import history 

#main menu function
def main_menu():
	while true:
		print("Welcome to Rent a Car service")
		print("Main menu.")
		print("1.Add client")
		print("2.view client")
		print("3.Add Car")
		print("4.view Car")
		print("5.Add Driver")
		print("6.view Driver")
		print("7.History")
		print("8.Booking")
		print("9.Exit")

		choice = input("Enter Your Choice:")
			
		if choice == "1":
			client.add_client()

		elif choice == "2":
			client.view_client()
			
			'''elif choice == 3:

			elif choice == 4:

			elif choice == 5:

			elif choice == 6:	

			elif choice == 7:

			elif choice == 8:'''	

		'''else choice == 9:
			print("Thanks for choosing our Service")
			break


