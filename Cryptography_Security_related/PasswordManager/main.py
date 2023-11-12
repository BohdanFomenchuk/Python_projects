import tkinter
from tkinter import messagebox
import secrets
import pyperclip
import json


# ---------------------------- DATA SEARCHING ------------------------------- #
def password_search():
    website = website_input.get()
    with open("data.json") as file:
        data = json.load(file)
    try:
        password = data[website]["password"]
    except KeyError:
        messagebox.showerror(title="Error", message="No entry found")
    else:
        email = data[website]["email"]
        messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n Password: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_input.delete(0, "end")
    rand_password = secrets.token_urlsafe(12)
    password_input.insert(0, rand_password)
    pyperclip.copy(rand_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please enter a valid value")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nEmail: {email} \nPassword: {password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            # Possible place where error can occur
            try:
                with open("data.json", 'r') as file:
                    data = json.load(file)

            # Actions to be taken if error occurred (create new file)
            except FileNotFoundError:
                with open("data.json", 'w') as file:
                    json.dump(new_data, file, indent=4)

            # Actions to be taken if NO error occurred (update data)
            else:
                data.update(new_data)

                with open("data.json", 'w') as file:
                    json.dump(data, file, indent=4)

            # Actions to be taken no matter error occurred or not (clear entry lines)
            finally:
                website_input.delete(0, "end")
                password_input.delete(0, "end")
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tkinter.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

# Canvas
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website")
website_label.grid(row=1, column=0)
uname_label = tkinter.Label(text="Email/Username")
uname_label.grid(row=2, column=0)
pass_label = tkinter.Label(text="Password")
pass_label.grid(row=3, column=0)

# Button
generate_button = tkinter.Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", command=add_data, width=43)
add_button.grid(row=4, column=1, columnspan=2)
search_button = tkinter.Button(text="Search", command=password_search, width=14)
search_button.grid(row=1, column=2)

# Input bar
website_input = tkinter.Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = tkinter.Entry(width=51)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "bohdan@gmail.com")
password_input = tkinter.Entry(width=33)
password_input.grid(row=3, column=1)
window.mainloop()
