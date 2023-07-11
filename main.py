from tkinter import *
from tkinter import messagebox
import pyperclip
# ------------------------ PASSWORD GENERATOR ------------------------------- #
import random


def generate_pass():
    for i in range(8):
        passwordgen = random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+")
        password_entry.insert(0, passwordgen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(message="Fields can't be empty")
    else:
        is_yes = messagebox.askyesno(title="Alert", message="Are you okay with the details entered?")

        if is_yes is True:
            with open("data.txt", "a") as file:
                file.write(website_entry.get())
                file.write("||")
                file.write(email_entry.get())
                file.write("||")
                file.write(password_entry.get())
                file.write("\n")
                pyperclip.copy(password_entry.get())  # copies password to clipboard
                website_entry.delete(0, END)  # to clear off these fields after the data is added
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
myimg = PhotoImage(file='logo.jpg')
canvas.create_image(100, 100, image=myimg)
canvas.pack()
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website: ")
website.grid(row=1, column=0)
email = Label(text="Email/Username: ")
email.grid(row=2, column=0)
password = Label(text="Password:  ")
password.grid(row=3, column=0)

# entries - input feilds
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "donasussan2000@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Generate password button
generate_pass = Button(text="Generate Password", width=15, command=generate_pass)
generate_pass.grid(row=3, column=2)

# Add password button
add_pass = Button(text="Add", width=35, command=save_data)
add_pass.grid(row=4, column=1, columnspan=2)
window.mainloop()