import tkinter as tk
import pyperclip
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = ""
    if include_uppercase.get():
        characters += string.ascii_uppercase
    if include_lowercase.get():
        characters += string.ascii_lowercase
    if include_numbers.get():
        characters += string.digits
    if include_special.get():
        characters += string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

def copy_to_clipboard():
    pyperclip.copy(result_label.cget("text"))

root = tk.Tk()
root.title("Générateur de Mots de Passe")

tk.Label(root, text="Longueur:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

include_uppercase = tk.BooleanVar()
tk.Checkbutton(root, text="Majuscules", variable=include_uppercase).grid(row=1, column=0, columnspan=2)

include_lowercase = tk.BooleanVar()
tk.Checkbutton(root, text="Minuscules", variable=include_lowercase).grid(row=2, column=0, columnspan=2)

include_numbers = tk.BooleanVar()
tk.Checkbutton(root, text="Chiffres", variable=include_numbers).grid(row=3, column=0, columnspan=2)

include_special = tk.BooleanVar()
tk.Checkbutton(root, text="Caractères spéciaux", variable=include_special).grid(row=4, column=0, columnspan=2)

tk.Button(root, text="Générer", command=generate_password).grid(row=5, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2)

tk.Button(root, text="Copier", command=copy_to_clipboard).grid(row=7, column=0, columnspan=2)

root.mainloop()
