import random
from tkinter import *

def generate_password():
    password_length = int(e1.get())  # Length of the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for i in range(password_length))
    password_label.config(text=password)

root = Tk()
root.title("Password Generator")
root.minsize(width=400,height=400)
root.geometry("500x500")

Label(root, text="Enter length of password").pack()

e1=Entry(root, text= "Enter length of password")
e1.pack()

b1 = Button(root, text="Generate Password", command=generate_password)
b1.pack()

Label(root,text="New password is: ").pack()

password_label = Label(root, text="")
password_label.pack()

root.mainloop()