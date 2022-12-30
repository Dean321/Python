# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:40:10 2022

@author: Dean321
"""
from tkinter import *
from tkinter import messagebox
import math
from random import randint, choice, shuffle
import pyperclip
import json

def searchData():
    d = {} 
    try:
        with open("data.json", mode="r") as file: 
            d = json.load(file)
            website = wip.get().lower()
            v = d.get(website)
            print(v)
            if v:
                msg = f'''
                For {website} 
                Username: {v["email"]}
                Password: {v["password"]}
                '''
                messagebox.showinfo(title="Found it!!!", message=msg)
            else:
                messagebox.showinfo(title="Does not exist!!", message="No Data found", icon="error")
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No Data file found", icon="error")
        with open("data.json", mode="w") as file: 
            json.dump(d, file, indent=4)

def genpass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pip.insert(0, password)
    pyperclip.copy(password)

def addData():
    website = wip.get().lower()
    email = uip.get().lower()
    password = pip.get()
    data = {
        website:{
            "email":email,
            "password":password
            }
        }
    message = f'''
    You have entered username & password for {website}
    Password: {password}
    email: {email}
    Is it all ok?
    '''
    if len(website) and len(password) and len(email):
        is_ok = messagebox.askokcancel(title=website, message=message)
        if is_ok:
            try:
                with open("data.json", mode="r") as file: 
                    d = json.load(file)
                    print(d)
            except FileNotFoundError:
                with open("data.json", mode="w") as file: 
                    json.dump(data, file, indent=4)
            else:
                d.update(data)
    
                with open("data.json", mode="w") as file: 
                    json.dump(d, file, indent=4)
            finally:
                wip.delete(0,END)
                pip.delete(0,END)
    else:
        messagebox.showinfo(title="Oops!!!", message="Please don't leave any feilds empty.", icon="error")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#4FA095")
window.iconbitmap("favicon.ico")

canvas = Canvas(width=200, height=200, bg="#4FA095", highlightthickness=0)
logo_img = PhotoImage(file="image.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

lblw = Label(text="Website: ",font=("Arial", 9, "bold"), fg="#153462", bg="#4FA095")
lblw.grid(column=0, row=1,pady=2)

wip = Entry(width=31, bd=0, bg="#BAD1C2", fg="#153462")
wip.grid(column=1, row=1, columnspan=1,pady=2)
wip.focus()

searchBtn = Button(text="Search", command=searchData,font=("Arial", 6, "bold"), highlightthickness=0,height=1, width=8, bg="#F6F6C9",fg="#4FA095",bd=1,activebackground="#4FA095", activeforeground="#F6F6C9")
searchBtn.grid(column=2, row=1, columnspan=1,sticky="e")

lblu = Label(text="Email/Username: ",font=("Arial", 9, "bold"), fg="#153462", bg="#4FA095")
lblu.grid(column=0, row=2,pady=2)

uip = Entry(width=38, bd=0, bg="#BAD1C2", fg="#153462")
uip.grid(column=1, row=2, columnspan=2,pady=2)
uip.insert(END, "dean321@email.com", )

lblp = Label(text="Password: ",font=("Arial", 9, "bold"), fg="#153462", bg="#4FA095")
lblp.grid(column=0, row=3,pady=2)

pip = Entry(width=31, bd=0, bg="#BAD1C2", fg="#153462")
pip.grid(column=1, row=3, columnspan=1,pady=2)

genBtn = Button(text="Gen Pass", font=("Arial", 7, "bold"),command=genpass, bg="#F6F6C9",fg="#4FA095",bd=1,activebackground="#4FA095", activeforeground="#F6F6C9", highlightthickness=0)
genBtn.grid(column=2, row=3,pady=2,sticky="w")

addBtn = Button(text="Add", command=addData,font=("Arial", 6, "bold"), highlightthickness=0,height=1, width=47, bg="#F6F6C9",fg="#4FA095",bd=1,activebackground="#4FA095", activeforeground="#F6F6C9")
addBtn.grid(column=1, row=4, columnspan=2,sticky="e")


window.mainloop()