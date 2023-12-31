from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website= website_input.get() 
    email = email_input.get()
    Password = password_input.get()
    new_data = {
        website : {
            "email" : email,
            "password" : Password,
        }
    }
    if len(website) == 0 or len(Password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty! ")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
            
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
            
        else:
            #updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
        finally:       
            website_input.delete(0, END)
            password_input.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website= website_input.get() 
    try:
        with open("data.json") as data_file:
            data = json.load( data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found")       
    else:
        if website in data:
            email = data[website]["email"]
            Password = data[website]["password"]    
            messagebox.showinfo(title=website, message=f"email: {email}\n password: {Password}")
        else:
             messagebox.showinfo(title="Error", message=f"No detail for {website} exist ")       


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#label
website = Label(text="Website:", fg="black")
website.grid(column= 0, row=1)

email = Label(text="Email/Username:", fg="black")
email.grid(column= 0, row=2)

Password = Label(text="Password:", fg="black")
Password.grid(column= 0, row=3)

# entry
website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

email_input = Entry(width=40)
email_input.insert(0, "nyamongogerald@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#button
add_button = Button(text="Add",  width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


G_password = Button(text="Generate password", command=generate_password)
G_password.grid(column=2, row=3)

s_button = Button(text="Search", width=13, command=find_password)
s_button.grid(column=2, row=1)


















window.mainloop()














