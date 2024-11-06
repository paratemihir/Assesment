import logging
logging.basicConfig(filename='Fruits_Data.log',level=logging.INFO,format='%(asctime)s  %(message)s')

class fruitManager:
  # empty dictionary to store Fruit stocks
  def __init__(self):
    self.fruit_stock = {}

                                    #Add fruit stocks
                                    
  def Add_fruit_stock(self):
    # user input fruit name,qty and pricce
    fruit_name = input("Enter fruit name : ").lower()
    quantity = int(input("Enter qty (in kg) : "))
    price = float(input("Enter price : "))

    # if fruit already exits to do, only add on price and quantity
    if fruit_name in self.fruit_stock:
      self.fruit_stock[fruit_name]['price'] = price
      self.fruit_stock[fruit_name]['quantity'] += quantity
      logging.info(f"\nUpdated stock :\n Fruit Name : {fruit_name}\n Quantity : {quantity}\n Price : {price}.\n")
    # or fruit not exitst to add in dictionary new fruit
    else:
      self.fruit_stock[fruit_name] = {'quantity': quantity, 'price': price}
      logging.info(f"\nAdded new stock: \nFruit Name : {fruit_name}\n Quantity : {quantity} \n Price : {price}.")
      print(f"Fruit : {fruit_name}, Quantity : {quantity}, Price : {price}")
      print(f"**Added Succesfully**")


                                  # View fruit stock

  def view_fruit_stock(self):
    # if fruits not in stocks-execute this condition
    if not self.fruit_stock:
      print("No fruits in stock!")
      logging.info("No fruits available.\n")
    else:
    # or disply available fruits
      print("\nCurrent fruit stocks:")
      for fruit,details in self.fruit_stock.items():
        quantity = details['quantity']
        price = details['price']
        print(f"Fruit : {fruit}, Quantity : {quantity}, Price : {price}")
      logging.info("\nView fruit stocks.")

                                # Update fruit stocks

  def update_fruit_stock(self):
    fruit_name = input("Enter the name of the fruit to update : ").lower()
    # fruit is exits in stocks to make update otherwise
    if fruit_name in self.fruit_stock:
      new_quantity = int(input(f"Enter new quantity for {fruit_name} : "))
      new_price = float(input(f"Enter new price for {fruit_name} : "))
      self.fruit_stock[fruit_name]['quantity'] = new_quantity
      self.fruit_stock[fruit_name]['price'] = new_price
      logging.info(f"\nUpdated Stock : \nFruit Name : {fruit_name} \n New Quantity : {new_quantity}\n New Price {new_price}.")
      print(f"**Updated Sucessfully**")
    # not updated
    else:
      print(f"{fruit_name} not found in the stocks!")
      logging.warning(f"{fruit_name} not found in the stocks.")

# make obj 
manager = fruitManager()