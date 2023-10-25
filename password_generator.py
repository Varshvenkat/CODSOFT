import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length = length_var.get()
    complexity = [
        lowercase_var.get(),
        uppercase_var.get(),
        digits_var.get(),
        special_chars_var.get()
    ]

    if not any(complexity):
        messagebox.showerror("Error", "Select at least one complexity option.")
        return

    characters = ""
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if digits_var.get():
        characters += string.digits
    if special_chars_var.get():
        characters += string.punctuation

    if length < 1:
        messagebox.showerror("Error", "Password length must be at least 1.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

length_var = tk.IntVar()
password_var = tk.StringVar()
lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_chars_var = tk.BooleanVar()

frame = tk.Frame(root, bg="lightblue")  
frame.place(relwidth=1, relheight=1)  

length_label = tk.Label(frame, text="Password Length:")
length_scale = tk.Scale(frame, from_=1, to=32, orient="horizontal", variable=length_var, length=200)
lowercase_check = tk.Checkbutton(frame, text="Lowercase", variable=lowercase_var)
uppercase_check = tk.Checkbutton(frame, text="Uppercase", variable=uppercase_var)
digits_check = tk.Checkbutton(frame, text="Digits", variable=digits_var)
special_chars_check = tk.Checkbutton(frame, text="Special Characters", variable=special_chars_var)
generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
password_label = tk.Label(frame, text="Generated Password:")
password_entry = tk.Entry(frame, textvariable=password_var, width=30)
copy_button = tk.Button(frame, text="Copy to Clipboard", command=lambda: root.clipboard_append(password_var.get()))

length_label.pack()
length_scale.pack()
lowercase_check.pack(anchor="w")
uppercase_check.pack(anchor="w")
digits_check.pack(anchor="w")
special_chars_check.pack(anchor="w")
generate_button.pack(pady=10)
password_label.pack()
password_entry.pack()
copy_button.pack(pady=5)

generate_button.configure(bg="green", fg="white")
password_label.configure(fg="blue")
copy_button.configure(bg="blue", fg="white")

root.mainloop()
