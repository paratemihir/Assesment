from fruit_manager import *
from customer import *

def main():
    print("\nWELCOME TO FRUIT MARKET")
    while True:
        print("1.Manager")
        print("2.Customer")
        print("3.Exit")

        # user input choice
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
            # user choose 1 to print manager menu
            if choice == 1:
                fruit_manager_menu()
            # user choose 2 to print customer menu
            elif choice == 2:
                customer_menu()
            # user choose 3 to exit the program
            elif choice == 3:
                print("Exiting...Thank you!")
                break
            else:
                print("Invalid choice!!")
        # user input string to print this type of error
        except ValueError:
            print("Invalid input.Please enter a number.")

# Fuction calling
main()