import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())

        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return

        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Ensure at least one character from each category
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]

        # Remaining characters
        all_characters = lowercase + uppercase + digits + symbols

        for _ in range(length - 4):
            password.append(random.choice(all_characters))

        # Shuffle password
        random.shuffle(password)

        password = "".join(password)

        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to copy password
def copy_password():
    password = entry_password.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first.")

# Main Window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Heading
title = tk.Label(root, text="Random Password Generator",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

# Password Length
tk.Label(root, text="Enter Password Length:",
         font=("Arial", 11)).pack()

entry_length = tk.Entry(root, width=10, font=("Arial", 12))
entry_length.pack(pady=5)

# Generate Button
btn_generate = tk.Button(root,
                         text="Generate Password",
                         font=("Arial", 11),
                         command=generate_password)
btn_generate.pack(pady=10)

# Password Display
entry_password = tk.Entry(root,
                          width=30,
                          font=("Arial", 12),
                          justify="center")
entry_password.pack(pady=5)

# Copy Button
btn_copy = tk.Button(root,
                     text="Copy Password",
                     font=("Arial", 11),
                     command=copy_password)
btn_copy.pack(pady=10)

root.mainloop()