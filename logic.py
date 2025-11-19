import random
import string
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_password():
    nr_letters = int(letter_entry.get())
    nr_symbols = int(symbol_entry.get())
    nr_numbers = int(number_entry.get())

    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = (
        ''.join(random.choice(letters) for _ in range(nr_letters)) +
        ''.join(random.choice(symbols) for _ in range(nr_symbols)) +
        ''.join(random.choice(numbers) for _ in range(nr_numbers))
    )
    password = ''.join(random.sample(password, len(password)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showinfo(title="Oops", message="Please fill in all required fields.")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nSave?"
        )
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#f9f9f9")  
# Canvas for logo
canvas = Canvas(width=200, height=200, bg="#f9f9f9", highlightthickness=0)
img = Image.open("lock.jpg").resize((200, 200))
logo_img = ImageTk.PhotoImage(img)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=(0, 20))

# Labels
label_bg = "#f9f9f9"
label_fg = "#704646"
website_label = Label(text="Website:", bg=label_bg, fg=label_fg, font=("Arial", 12))
website_label.grid(row=1, column=0, sticky="e", pady=5)
email_label = Label(text="Email/Username:", bg=label_bg, fg=label_fg, font=("Arial", 12))
email_label.grid(row=2, column=0, sticky="e", pady=5)
password_label = Label(text="Password:", bg=label_bg, fg=label_fg, font=("Arial", 12))
password_label.grid(row=3, column=0, sticky="e", pady=5)

# Entries
entry_bg = "#ffffff"
website_entry = Entry(width=42, bg=entry_bg, fg="#000000", font=("Arial", 12))
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email_entry = Entry(width=42, bg=entry_bg, fg="#000000", font=("Arial", 12))
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "radha@mail.com")

password_entry = Entry(width=27, bg=entry_bg, fg="#000000", font=("Arial", 12))
password_entry.grid(row=3, column=1, pady=5)

generate_password_button = Button(
    text="Generate", width=13, bg="#4caf50", fg="white", font=("Arial", 10, "bold"),
    command=generate_password
)
generate_password_button.grid(row=3, column=2, pady=5)
settings_frame = Frame(window, bg="#f9f9f9")
settings_frame.grid(row=4, column=1, columnspan=2, pady=(10, 20))

Label(settings_frame, text="Letters:", bg="#f9f9f9", font=("Arial", 10)).grid(row=0, column=0)
letter_entry = Entry(settings_frame, width=5)
letter_entry.grid(row=0, column=1, padx=5)
letter_entry.insert(0, "8")

Label(settings_frame, text="Symbols:", bg="#f9f9f9", font=("Arial", 10)).grid(row=0, column=2)
symbol_entry = Entry(settings_frame, width=5)
symbol_entry.grid(row=0, column=3, padx=5)
symbol_entry.insert(0, "2")

Label(settings_frame, text="Numbers:", bg="#f9f9f9", font=("Arial", 10)).grid(row=0, column=4)
number_entry = Entry(settings_frame, width=5)
number_entry.grid(row=0, column=5, padx=5)
number_entry.insert(0, "2")

# Add Button
add_button = Button(
    text="Add", width=36, bg="#2196f3", fg="white", font=("Arial", 12, "bold"),
    command=save
)
add_button.grid(row=5, column=1, columnspan=2, pady=10)

window.mainloop()
