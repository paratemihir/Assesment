import logging
logging.basicConfig(filename='fruit.log',level=logging.INFO,format='%(asctime)s  %(message)s')

# empty dict to store a fruits details
fruit_stock = {}

# Add fruit
def add_fruit():
    # input fruit name,qty,price
    fruit_name = input("Enter fruit name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    # Add data in log file
    logging.info(f"Add fruits:\n Fruit name : {fruit_name}, Quantity : {quantity}, Price : {price}")

    # fruit name already exits in dict then add only a quantity and price
    fruit_stock[fruit_name] = {'quantity': quantity, 'price': price}

    print(f"{fruit_name} added succesfully in a stock.")

# View stock
def view_stock():
    # if fruit stock not available
    if not fruit_stock:
        print("No fruits in stock.")

        # Add data in log file
        logging.warning(f"\nNo fruits available in the stock!")
    # else : view available fruits staoc
    else:
        print("\nFruit Stock:")
        for fruit, details in fruit_stock.items():
            print(f"{fruit}: Quantity : {details['quantity']}, Price : {details['price']}")
        
        # Add data in log file
        logging.info(f"View stocks:\n Fruit name : {fruit}, Quantity : {details['quantity']}, Price : {details['price']}")

# Update fruit stock
def update_stock():
    fruit_name = input("Enter fruit name to update: ")
    # if fruit in stock to update qty and price
    if fruit_name in fruit_stock:
        new_quantity = int(input("Enter new quantity: "))
        new_price = float(input("Enter new price: "))

        # Add data in log file
        logging.info(f"Updated stocks:\n Fruit name : {fruit_name}, Quantity : {new_quantity}, Price : {new_price}")

        fruit_stock[fruit_name]['quantity'] = new_quantity
        fruit_stock[fruit_name]['price'] = new_price
        print("Stock updated..")
    # user enter fruit is not in stock 
    else:
        print("Fruit not found in stock.")

# print manager menu
def fruit_manager_menu():
    while True:
        print("\nFruit Market Manager:")
        print("1.Add Fruit")
        print("2.View Stock")
        print("3.Update Stock")
        print("4.Back to Main Menu")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
            if choice == 1:
                add_fruit()  #fruit add function
            elif choice == 2:
                view_stock() #view fruit stock fuuction
            elif choice == 3:
                update_stock() #update fruit stock function
            elif choice == 4:
                break
            else:
                print("Invalid choice!!")
        except:
            print("Invalid input.Please enter a number.")
