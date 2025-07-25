import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect('contacts.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT,
        address TEXT
    )
''')
conn.commit()

# Functions
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    address = address_var.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required")
        return

    c.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
              (name, phone, email, address))
    conn.commit()
    clear_fields()
    load_contacts()

def load_contacts():
    contact_list.delete(0, tk.END)
    for row in c.execute("SELECT id, name, phone FROM contacts"):
        contact_list.insert(tk.END, f"{row[0]}. {row[1]} - {row[2]}")

def search_contact():
    query = search_var.get()
    contact_list.delete(0, tk.END)
    for row in c.execute("SELECT id, name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?",
                         (f"%{query}%", f"%{query}%")):
        contact_list.insert(tk.END, f"{row[0]}. {row[1]} - {row[2]}")

def delete_contact():
    try:
        contact_id = int(contact_list.get(contact_list.curselection()).split(".")[0])
        c.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
        load_contacts()
    except:
        messagebox.showwarning("Select Error", "Please select a contact to delete")

def update_contact():
    try:
        contact_id = int(contact_list.get(contact_list.curselection()).split(".")[0])
        name = name_var.get()
        phone = phone_var.get()
        email = email_var.get()
        address = address_var.get()

        c.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
                  (name, phone, email, address, contact_id))
        conn.commit()
        load_contacts()
    except:
        messagebox.showwarning("Update Error", "Select a contact and fill in updated details")

def load_selected_contact(event):
    try:
        contact_id = int(contact_list.get(contact_list.curselection()).split(".")[0])
        c.execute("SELECT name, phone, email, address FROM contacts WHERE id=?", (contact_id,))
        data = c.fetchone()
        name_var.set(data[0])
        phone_var.set(data[1])
        email_var.set(data[2])
        address_var.set(data[3])
    except:
        pass

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")

# GUI
root = tk.Tk()
root.title("Contact Book")

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

tk.Label(root, text="Phone").grid(row=1, column=0)
tk.Entry(root, textvariable=phone_var).grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
tk.Entry(root, textvariable=email_var).grid(row=2, column=1)

tk.Label(root, text="Address").grid(row=3, column=0)
tk.Entry(root, textvariable=address_var).grid(row=3, column=1)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, pady=5)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=1)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=4, column=2)

tk.Label(root, text="Search").grid(row=5, column=0)
tk.Entry(root, textvariable=search_var).grid(row=5, column=1)
tk.Button(root, text="Search", command=search_contact).grid(row=5, column=2)

contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=6, column=0, columnspan=3, pady=10)
contact_list.bind('<<ListboxSelect>>', load_selected_contact)

load_contacts()

root.mainloop()
