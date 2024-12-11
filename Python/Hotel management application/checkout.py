import tkinter as tk
from tkinter import messagebox
import DB

class CheckoutPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management - Check Out")
        self.root.geometry("600x400")
        self.root.configure(bg='lightgrey')

        self.room_entry = None
        self.message_area = None

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Check out", font=("Verdana", 20), bg='lightgrey').pack(pady=20)

        # Room Number Entry
        tk.Label(self.root, text="ENTER THE ROOM NO.:", font=("Calibri", 16, "bold"), bg='lightgrey').pack(pady=10)
        self.room_entry = tk.Entry(self.root, font=("Calibri", 16), width=10)
        self.room_entry.pack(pady=10)

        # Checkout Button
        tk.Button(self.root, text="CHECK OUT", font=("Verdana", 15, "bold"), command=self.check_out).pack(pady=20)

        # Message Area
        self.message_area = tk.Text(self.root, height=5, width=50, font=("Calibri", 14), bg='lightgrey')
        self.message_area.pack(pady=20)

    def check_out(self):
        room_number = self.room_entry.get()
        
        if not room_number:
            messagebox.showerror("Input Error", "Please enter a room number.")
            return
        
        # You can add a function in DB.py to check the room number validity.
        valid_room = DB.is_valid_room(room_number)
        
        if valid_room:
            self.message_area.delete('1.0', tk.END)
            self.message_area.insert(tk.END, f"Room number {room_number} is valid.\nTHANK YOU FOR VISITING US")
        else:
            self.message_area.insert(tk.END, f"Room number {room_number} is not valid.\n")
            
root = tk.Tk()
app = CheckoutPage(root)
root.mainloop()
