import tkinter as tk
from tkinter import messagebox
contacts = []
 
selected_contact = None

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append((name, phone, email, address))
        name_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        address_entry.delete(0, 'end')
        update_contact_list()
    else:
        messagebox.showerror("Error", "Name and Phone fields are required.")

def update_contact_list():
    contact_list.delete(0, 'end')
    for contact in contacts:
        contact_list.insert('end', contact[0])

def search_contact():
    search_name = search_entry.get()
    contact_list.delete(0, 'end')
    found = False
    for contact in contacts:
        if search_name.lower() in contact[0].lower() or search_name in contact[1]:
            contact_list.insert('end', contact[0])
            found = True
    if not found:
        messagebox.showinfo("Not Found", "No matching contacts found.")

def open_update_window():
    global selected_contact
    selected_contact = contact_list.get(contact_list.curselection())

    update_window = tk.Toplevel(root)
    update_window.title("Update Contact")
    update_window.geometry("300x200")
 
    name_label = tk.Label(update_window, text="Name:")
    name_entry = tk.Entry(update_window)
    phone_label = tk.Label(update_window, text="Phone:")
    phone_entry = tk.Entry(update_window)
    email_label = tk.Label(update_window, text="Email:")
    email_entry = tk.Entry(update_window)
    address_label = tk.Label(update_window, text="Address:")
    address_entry = tk.Entry(update_window)
 
    for contact in contacts:
        if selected_contact == contact[0]:
            name_entry.insert(0, contact[0])
            phone_entry.insert(0, contact[1])
            email_entry.insert(0, contact[2])
            address_entry.insert(0, contact[3])

    def update_selected_contact():
        for i, contact in enumerate(contacts):
            if selected_contact == contact[0]:
                contacts[i] = (
                    name_entry.get(),
                    phone_entry.get(),
                    email_entry.get(),
                    address_entry.get()
                )
        update_contact_list()
        update_window.destroy()

    update_button = tk.Button(update_window, text="Update", command=update_selected_contact)
    name_label.pack()
    name_entry.pack()
    phone_label.pack()
    phone_entry.pack()
    email_label.pack()
    email_entry.pack()
    address_label.pack()
    address_entry.pack()
    update_button.pack()

def delete_contact():
    global selected_contact
    selected_contact = contact_list.get(contact_list.curselection())

    for contact in contacts:
        if selected_contact == contact[0]:
            contacts.remove(contact)
    update_contact_list()

def view_all_contacts():
    contact_list.delete(0, 'end')
    for contact in contacts:
        contact_list.insert('end', contact[0])
 
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x300")
 
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
phone_label = tk.Label(root, text="Phone:")
phone_entry = tk.Entry(root)
email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)
address_label = tk.Label(root, text="Address:")
address_entry = tk.Entry(root)
 
contact_list = tk.Listbox(root, selectmode=tk.SINGLE)
 
search_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_contact)
 
add_button = tk.Button(root, text="Add Contact", command=add_contact)
update_button = tk.Button(root, text="Update Contact", command=open_update_window)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
view_all_button = tk.Button(root, text="View All Contacts", command=view_all_contacts)
 
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry.grid(row=0, column=1, padx=5, pady=5)
phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry.grid(row=1, column=1, padx=5, pady=5)
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry.grid(row=2, column=1, padx=5, pady=5)
address_label.grid(row=3, column=0, padx=5, pady=5)
address_entry.grid(row=3, column=1, padx=5, pady=5)

contact_list.grid(row=0, column=2, rowspan=6, padx=5, pady=5)
search_entry.grid(row=6, column=2, padx=5, pady=5)
search_button.grid(row=6, column=3, padx=5, pady=5)

add_button.grid(row=4, column=0, padx=5, pady=5)
update_button.grid(row=4, column=1, padx=5, pady=5)
delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
view_all_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.configure(bg="blue")   
contact_list.configure(bg="white")   
 
root.mainloop()
