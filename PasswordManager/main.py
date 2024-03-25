from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json


# ----------------------------------FIND PASSWORD---------------------------------- #

def find_password():
    website = website_entry.get().title()
    try:
        with open('data.json', mode='r') as data:
            json_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data file found!')
    else:
        if website in json_data:
            messagebox.showinfo(title=website, message=f"Email: {json_data[website]['email']}\nPassword:"
                                                       f" {json_data[website]['password']}")
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exists!')


# ----------------------------------PASSWORD GENERATOR---------------------------------- #'

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    copy(password)


# ----------------------------------SAVE PASSWORD---------------------------------- #


def save():
    email_id = username_entry.get()
    website = website_entry.get().title()
    password = password_entry.get()

    new_data = {
        website: {
            'email': email_id,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message='Dont leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'You entered\nEmail: {email_id}\n'
                                                              f'Password: {password}\nIt is ok?')

        if is_ok:
            try:
                with open('data.json', mode='r') as data:
                    # Reading old data
                    old_data = json.load(data)
            except FileNotFoundError:
                with open('data.json', mode='w') as data:
                    json.dump(new_data, data, indent=4)
            else:
                # Updating old data
                old_data.update(new_data)
                with open('data.json', mode='w') as data:
                    # Writing new data to file
                    json.dump(old_data, data, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ----------------------------------UI SETUP---------------------------------- #

# Window
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

username_entry = Entry(width=35)
username_entry.insert(0, 'kartik.goklani@gmail.com')
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_pwd_button = Button(text='Generate', width=10, command=generate_password)
generate_pwd_button.grid(column=2, row=3)

add_button = Button(text='Add', width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=10, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
