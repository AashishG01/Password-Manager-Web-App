from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    password_entry.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = user_entry.get()
    pass_word = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": pass_word
        }

    }

    if len(website) == 0 or len(username) == 0 or len(pass_word) == 0:
        messagebox.askokcancel(title=website, message=f"hey! you left some detail unfilled")
    else:
        # is_okay = messagebox.askokcancel(title=website,
        #                                  message=f"These are the details entered: \nEmail:{username}\nPassword:{pass_word}\nIs it okay to save?")
        is_okay = True
        if is_okay:
            f = open("data.txt", "a")
            f.write(f"website:{website} \nusername:{username} \npassword:{pass_word} \n\n")
            website_entry.delete(0, END)
            # user_entry.delete(0, END)
            password_entry.delete(0, END)
            f.close()
            # with open("data.json", "r") as data_file:
            #     # json.dump(new_data, data_file, indent=4)
            #     data = json.load(data_file)
            #     print(data)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# lock ui
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
# website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky='w')
# website Entry
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()
# email/username
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky='w')
# user entry
user_entry = Entry(width=50)
user_entry.grid(column=1, row=2, columnspan=2, sticky='w')
user_entry.insert(0, "aashish@guptagamil.com")
# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky='w')
# password entry
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, columnspan=2, sticky='w')
# generate password button
gen_button = Button(text="Generate Password:", command=generate_pass)
gen_button.grid(column=2, row=3, columnspan=1, sticky='w')
# add button
add_button = Button(text="Add", width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')
window.mainloop()
