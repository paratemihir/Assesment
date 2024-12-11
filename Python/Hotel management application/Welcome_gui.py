from tkinter import *
import tkinter
import os

class HotelManagement:
    root = tkinter.Tk()

    root.title("Hotel Management")
                  # w x h
    root.geometry("1000x600")

    root.configure(background='lightgrey')

    welcome = Label(root, text="WELCOME", font=("Verdana", 25, "bold"), bg="lightgray")
    welcome.place(x=410, y=30)

    text1 = Label(root, text="HOTEL MANAGEMENT \n \nPYTHON TKINTER \n \n GUI", font=("Verdana", 30, "bold"), bg="lightgray")
    text1.place(x=500, y=120)

    def open_check_in():
        os.system('python CheckIN.py')

    def open_showguestlist():
        os.system('python show_guest_list.py')
    
    def open_checkout():
        os.system('python checkout.py')
    
    def open_getinfo():
        os.system('python Getinfo.py')

    check_in = Button(root, text="1.CHECK IN", font=("Verdana", 15, "bold"), command=open_check_in)
    check_in.place(x=90, y=100, width=400, height=50)

    show_guest = Button(root, text="2.SHOW GUEST LIST", font=("Verdana", 15, "bold"),command=open_showguestlist)
    show_guest.place(x=90, y=170, width=400, height=50)

    check_out = Button(root, text="3.CHECK OUT", font=("Verdana", 15, "bold"),command= open_checkout)
    check_out.place(x=90, y=240, width=400, height=50)

    get_info = Button(root, text="4.GET INFO OF ANY GUEST", font=("Verdana", 15, "bold"),command=open_getinfo)
    get_info.place(x=90, y=310, width=400, height=50)

    exit_button = Button(root, text="5.Exit", font=("Verdana", 15, "bold"), command=root.quit)
    exit_button.place(x=90, y=380, width=400, height=50)

    root.mainloop()

obj = HotelManagement()
