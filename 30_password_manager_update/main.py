from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json



def find_password():
    website = website_entry.get()
    if website == "":
        messagebox.showwarning(title="Empty fields", message="Hey, your website field is empty!")
    else:
        try:
            # reading old file
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title="Password file", message="Hey, your password file does not exists, did you stored any password?")
        else:
            entry = data.get(website)
            if entry != None:
                messagebox.showwarning(title=f"{website}", message=f"Usertname: {entry["username"]}\nPassword: {entry["password"]}")
            else:
                messagebox.showwarning(title="Website not found", message="Hey, this website does not exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(title="Empty fields", message="Hey, your website or password are empty!")
    else:
        try:
            # reading old file
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # creating file
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()   
window.config(padx=50, pady=50, bg="white")
# window.minsize(width=600, height=600)
window.title("Password manager")
logo_image = PhotoImage(file="logo.png")

# Row 0
canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Row 1
website_label = Label(text="Website:", bg="white", pady=10)
website_label.grid(column=0, row=1)

website_entry = Entry(width=22, bg="white")
website_entry.grid(column=1, row=1)
website_entry.focus()

seach_button = Button(text="Search", bg="white",  width=14, command=find_password)
seach_button.grid(column=2, row=1)

# Row 2
username_label = Label(text="E-mail/Username:", bg="white", pady=10, padx=5)
username_label.grid(column=0, row=2)

username_entry = Entry(width=40, bg="white")
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "user@email.com")

# Row 3
password_label = Label(text="Password:", bg="white", pady=10)
password_label.grid(column=0, row=3)

password_entry = Entry(width=22, bg="white")
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", bg="white", width=14, command=generate)
generate_button.grid(column=2, row=3)

# Row 4
add_button = Button(text="Add", bg="white", width=37, command=save_data)
add_button.grid(column=1, row=4, columnspan=3)


window.mainloop()