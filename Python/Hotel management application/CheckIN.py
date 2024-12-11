import tkinter as tk
from tkinter import messagebox
import DB 
import random

class Person:
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number

class Customer(Person):
    def __init__(self, name, address, number, balance):
        super().__init__(name, address, number)
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

class Checkin_Form:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("600x500")
        self.root.configure(bg='lightgrey')

        self.name_entry = None
        self.address_entry = None
        self.number_entry = None
        self.days_entry = None
        self.room_var = tk.StringVar()
        self.payment_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # heading
        tk.Label(self.root, text="YOU CLICKED ON: CHECK IN", font=("Verdana", 20), bg='lightgrey').grid(row=0, columnspan=3, pady=15)

        # Name Entry
        tk.Label(self.root, text="Enter Your Name:", font=("Calibri", 14, "bold"), bg='lightgrey').grid(row=1, column=0, sticky='e', padx=10, pady=5)
        self.name_entry = tk.Entry(self.root, name="name_entry")
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.root, text="OK", command=self.name_ok).grid(row=1, column=2, padx=5, pady=5)

        # Address Entry
        tk.Label(self.root, text="Enter Your Address:", font=("Calibri", 14, "bold"), bg='lightgrey').grid(row=2, column=0, sticky='e', padx=10, pady=5)
        self.address_entry = tk.Entry(self.root, name="address_entry")
        self.address_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.Button(self.root, text="OK", command=self.address_ok).grid(row=2, column=2, padx=5, pady=5)

        # Mobile Number Entry
        tk.Label(self.root, text="Enter Your Number:", font=("Calibri", 14, "bold"), bg='lightgrey').grid(row=3, column=0, sticky='e', padx=10, pady=5)
        self.number_entry = tk.Entry(self.root, name="number_entry")
        self.number_entry.grid(row=3, column=1, padx=10, pady=5)
        tk.Button(self.root, text="OK", command=self.number_ok).grid(row=3, column=2, padx=5, pady=5)

        # Number of Days Entry
        tk.Label(self.root, text="Number of Days:", font=("Calibri", 14, "bold"), bg='lightgrey').grid(row=4, column=0, sticky='e', padx=10, pady=5)
        self.days_entry = tk.Entry(self.root, name="days_entry")
        self.days_entry.grid(row=4, column=1, padx=10, pady=5)
        tk.Button(self.root, text="OK", command=self.days_ok).grid(row=4, column=2, padx=5, pady=5)

        # Room Type Selection
        tk.Label(self.root, text="Choose Your Room:", font=("Calibri", 14, "bold"), bg='lightgrey').grid(row=5, column=0, sticky='e', padx=10, pady=5)
        tk.Radiobutton(self.root, text="Deluxe", variable=self.room_var, value="Deluxe", bg='lightgrey').grid(row=5, column=1, sticky='w')
        tk.Radiobutton(self.root, text="Full Deluxe", variable=self.room_var, value="Full Deluxe", bg='lightgrey').grid(row=5, column=1, padx=85)
        tk.Radiobutton(self.root, text="General", variable=self.room_var, value="General", bg='lightgrey').grid(row=5, column=1, sticky='e', padx=5)

        # Payment Method Selection
        tk.Label(self.root, text="Choose Payment Method:", font=("Calibri", 14, "bold"), bg='lightgrey').grid(row=6, column=0, sticky='e', padx=10, pady=5)
        tk.Radiobutton(self.root, text="By Cash", variable=self.payment_var, value="By Cash", bg='lightgrey').grid(row=6, column=1, sticky='w', padx=5)
        tk.Radiobutton(self.root, text="By Credit/Debit Card", variable=self.payment_var, value="By Credit/Debit Card", bg='lightgrey').grid(row=6, column=1, padx=85)

        # Submit Button
        tk.Button(self.root, text="Submit", command=self.validate_input, font=("Calibri", 14, "bold")).grid(row=7, columnspan=3, pady=20)
        tk.Button(self.root, text="Exit", command=root.quit ,font=("Calibri", 14, "bold")).grid(row=8, columnspan=3, pady=20)

    def name_ok(self):
        print("Name has been inputted")

    def address_ok(self):
        print("Address has been inputted")

    def number_ok(self):
        print("Mobile number has been inputted")

    def days_ok(self):
        print("Number of days has been inputted")

    def validate_input(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        number = self.number_entry.get()
        days = self.days_entry.get()
        room_type = self.room_var.get()
        payment_method = self.payment_var.get()

# invalid input to show a message box
        if not name:
            messagebox.showerror("Input Error", "Please enter your name.")
            return
        if not address:
            messagebox.showerror("Input Error", "Please enter your address.")
            return
        if not number.isdigit() or len(number) != 10:
            messagebox.showerror("Input Error", "Please enter a valid 10-digit mobile number.")
            return
        if not days.isdigit() or int(days) <= 0:
            messagebox.showerror("Input Error", "Please enter a valid number of days.")
            return

        # Generate a random room number
        room_number = random.randint(100, 999)

        # Insert into database
        DB.insert_guest(name, address, number, days, room_number,room_type, payment_method)
        messagebox.showinfo("Success", f"Form submitted successfully!\nYour room number is {room_number}")

root = tk.Tk()
app = Checkin_Form(root)
root.mainloop()
