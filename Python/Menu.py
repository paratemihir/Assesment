from Fruit_Manager import *
from Customer import *

class menu:
  print("WELCOME TO FRUIT MARKET")
  while True:
    print("Select Your Role : ")
    print("(1) Manager")
    print("(2) Customer")
    print("(3) Exit")

    # user input role
    role = input("Select your role : ")

    # Manager menu
    if role == '1':
      while True:
        print("\nFruit Market Manager\n")
        print("(1) Add fruit stocks")
        print("(2) View fruit stocks")
        print("(3) Update fruit stocks")
        print("(4) Back to main menu\n")

        choice = input("Enter your choice : ")

        if choice == '1':
          manager.Add_fruit_stock()
        elif choice == '2':
          manager.view_fruit_stock()
        elif choice == '3':
          manager.update_fruit_stock()
        elif choice == '4':
          break
        else:
          print("Invalid choice!")
          logging.warning("Invalid choice in Manager menu.")

    # Customer menu
    elif role == '2':
        while True:
          print("\nCustomer menu")
          print("(1) View available fruits")
          print("(2) Back to main menu")

          choice = input("Enter your choice : ")

          if choice == '1':
            customer.view_available_fruits()
          elif choice == '2':
            break
          else:
            print("Invalid choice!")
            logging.warning("Invalid choice in Customer menu.")

    # user input 3 number to exit the application
    elif role == '3':
      logging.info("Customer Exit the Fruit Market application.")
      print("Exiting the Fruit Market application.")
      break
    
    # invalid choice
    else:
      logging.warning("Invalid role!!.")
      print("Invalid role.Please enter a valid option.\n")

# make obj
Menu = menu()
                

