import tkinter as tk
from tkinter import ttk
import DB  # Import the database connectivity functions

class ShowGuestList:
    def __init__(self, root):
        self.root = root
        self.root.title("Guest List")
        self.root.geometry("1500x400")
        self.root.configure(bg='lightgrey')

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Guest List", font=("Verdana", 20), bg='lightgrey').pack(pady=10)

        # Creating the table to show the guest list
        columns = ("Name", "Address", "Number","RoomNumber", "Days", "Room Type", "Payment Method")
        tree = ttk.Treeview(self.root, columns=columns, show='headings')

        # Define headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor=tk.CENTER)

        # Insert data into the table
        guests = DB.fetch_all_guests()
        for guest in guests:
            tree.insert('', tk.END, values=guest)

        tree.pack(pady=10, fill=tk.BOTH, expand=True)

root = tk.Tk()
app = ShowGuestList(root)
root.mainloop()
