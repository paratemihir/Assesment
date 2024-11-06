import logging

from Fruit_Manager import *

manager = fruitManager() 

class Customer:
  # this function display available fruit stocks
  def view_available_fruits(self):
    # print("Available fruits")
    manager.view_fruit_stock()
    logging.info("Customer viewed available fruits.")

# make obj
customer = Customer()
    
    
    