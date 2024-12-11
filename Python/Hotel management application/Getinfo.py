import tkinter as tk
from tkinter import messagebox
import DB

class GetInfoPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Get info of any guest")
        self.root.geometry("600x400")
        self.root.configure(bg='lightgrey')

        self.room_entry = None
        self.message_area = None

        self.create_widgets()

    def create_widgets(self):
        # Title 
        tk.Label(self.root, text="Get info of any guest", font=("Verdana", 20), bg='lightgrey').pack(pady=20)

        # Room Number
        tk.Label(self.root, text="ENTER THE ROOM NO.:", font=("Calibri", 16, "bold"), bg='lightgrey').pack(pady=10)
        self.room_entry = tk.Entry(self.root, font=("Calibri", 16), width=10)
        self.room_entry.pack(pady=10)

        # Submit Button
        tk.Button(self.root, text="Submit", font=("Verdana", 15, "bold"), command=self.get_info).pack(pady=20)

        # Message Area
        self.message_area = tk.Text(self.root, height=5, width=50, font=("Calibri", 14), bg='lightgrey')
        self.message_area.pack(pady=20)


    def get_info(self):
        room_number = self.room_entry.get()
        
        if not room_number:
            messagebox.showerror("Input Error", "Please enter a room number.")
            return
        
        # Check if the room number is valid or not
        guest_details = DB.is_valid_room(room_number)
        
        if guest_details:
            self.message_area.delete('1.0', tk.END)
            self.message_area.insert(tk.END, f"Valid room number.\nGuest Name: {guest_details[0]}")
        else:
            self.message_area.delete('1.0', tk.END)
            self.message_area.insert(tk.END, "Wrong room number.")

root = tk.Tk()
app = GetInfoPage(root)
root.mainloop()
