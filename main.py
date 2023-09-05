from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_symbol + password_letter
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_entry.get()
    password = password_entry.get()
    user_name = email_entry.get()
    new_data = {
        web: {
            "email": user_name,
            "password": password,
        }
    }

    is_empty = password == "" or user_name == ""
    if is_empty:
        messagebox.showwarning(title="warning", message="please fill all the details")
    else:
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(file="data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Search ------------------------------- #
def search_pass():
    web = website_entry.get()

    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)
            if web in data:
                account_info = data[web]
                messagebox.showinfo(title="Account info", message=account_info)
            else:
                messagebox.showwarning(title="waring", message="No Account Found ")
    except FileNotFoundError:
        messagebox.showwarning(title="waring", message="NO File found ")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manger App")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# Label
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "ketankinniwadi@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Button
generate_button = Button(text="Generate Password", command=gen_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="ADD", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=search_pass)
search_button.grid(column=2, row=1)

window.mainloop()
