from fruit_manager import *

# View available fruit function
def view_available_fruits():
    view_stock()

# Customer menu
def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1.View Available Fruits")
        print("2.Back to Main Menu")

        # user input choice
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
            # user choose 1 to print available fruits
            if choice == 1:
                view_available_fruits()
            elif choice == 2:
                break
            else:
                print("Invalid choice!")
        except:
            print("Invalid input.Please enter a number.")