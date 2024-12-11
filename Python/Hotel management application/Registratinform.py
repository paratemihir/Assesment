import tkinter
from tkinter import *

class Registration_form():

  root = Tk()
  root.title("Registration Form")
  root.geometry("500x500")
  root.config(background="lightgray")

  def widget(self):
    heading = Label(self.root,text="Please enter details below",font=("Arial",12),bg="orange",fg="white").pack(fill="x")

  def fields(self):
    # Name field
    name = Label(self.root,text="Name * ",font=("Arial",12),bg="lightgray")
    name.place(x=20,y=50)
    E_name = Entry(self.root,bg="lightgray")
    E_name.place(x=120,y=50,height=25,width=200)

    # Contact field
    contact = Label(self.root,text="Contact * ",font=("Arial",12),bg="lightgray")
    contact.place(x=20,y=100)
    E_contact = Entry(self.root,bg="lightgray")
    E_contact.place(x=120,y=100,height=25,width=200)

    # Email field
    email = Label(self.root,text="Email * ",font=("Arial",12),bg="lightgray")
    email.place(x=20,y=150)
    E_email = Entry(self.root,bg="lightgray")
    E_email.place(x=120,y=150,height=25,width=200)

    # Gender field
    gender = Label(self.root,text="Gender * ",font=("Arial",12),bg="lightgray")
    gender.place(x=20,y=200)
    male_radio = Radiobutton(self.root, text="Male",value="Male", bg="lightgray")
    male_radio.place(x=120, y=200)
    female_radio = Radiobutton(self.root, text="Female", value="Female", bg="lightgray")
    female_radio.place(x=200, y=200)

    # City field
    city = Label(self.root, text="City * ", font=("Arial", 12), bg="lightgray")
    city.place(x=20, y=250)
    self.city_var = StringVar(value="Select City")
    city_menu = OptionMenu(self.root, self.city_var, "Ahmedabad", "Surat", "Rajkot", "Vadodara")
    city_menu.place(x=120, y=250, width=200)

    # state field
    state_label = Label(self.root, text="State * ", font=("Arial", 12), bg="lightgray")
    state_label.place(x=20, y=300)
    self.state_var = StringVar(value="Select State")
    state_menu = OptionMenu(self.root, self.state_var, "Gujarat", "Rajasthan", "Maharastra", "Delhi")
    state_menu.place(x=120, y=300, width=200)

    # Register button
    register_button = Button(self.root, text="Register", bg="orange", fg="black", font=("Arial", 12))
    register_button.place(x=180, y=370, width=100)


  def run(self):
    self.widget()
    self.fields()
    self.root.mainloop()

obj = Registration_form()
obj.run()
