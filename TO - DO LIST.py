import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import date

def add_task():
    task = entry.get()
    priority = priority_var.get()
    due_date = due_date_var.get()

    if task:
        task_info = f"Priority: {priority}, Due Date: {due_date}"
        listbox.insert(tk.END, f"☐ {task} ({task_info})")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")
 
def mark_task_as_done():
    selected_task = listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task = listbox.get(index)
        if "☐" in task:
            task = task.replace("☐", "☑")
            listbox.delete(index)
            listbox.insert(index, task)
            listbox.itemconfig(index, {'bg': 'light green'})
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")
 
def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")
 
def clear_completed():
    for i in reversed(range(listbox.size())):
        task = listbox.get(i)
        if "☑" in task:
            listbox.delete(i)
 
def save_tasks():
    with open("tasks.txt", "w") as file:
        for i in range(listbox.size()):
            task = listbox.get(i)
            file.write(task + "\n")
 
def load_tasks():
    listbox.delete(0, tk.END)
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        messagebox.showinfo("Info", "No saved tasks found.")

 
root = tk.Tk()
root.title("To-Do List")
 
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save Tasks", command=save_tasks)
file_menu.add_command(label="Load Tasks", command=load_tasks)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
 
entry = tk.Entry(root, font=("Arial", 14), bd=2, relief=tk.SOLID)
entry.insert(0, "Add a new task...")
entry.pack(pady=10)
 
priorities = ["High", "Medium", "Low"]
priority_var = tk.StringVar()
priority_var.set("Medium")  
priority_label = tk.Label(root, text="Priority:")
priority_label.pack()
priority_menu = ttk.Combobox(root, textvariable=priority_var, values=priorities)
priority_menu.pack(pady=5)
 
today = date.today()
due_date_var = tk.StringVar()
due_date_var.set(today.strftime("%d-%m-%y"))  
due_date_label = tk.Label(root, text="Due Date:")
due_date_label.pack()
due_date_entry = tk.Entry(root, textvariable=due_date_var)
due_date_entry.pack(pady=5)
 
listbox_frame = tk.Frame(root)
listbox_frame.pack()
listbox = tk.Listbox(listbox_frame, font=("Arial", 14), bg="lightgray")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
 
add_button = tk.Button(root, text="Create New Task", command=add_task, font=("Helvetica", 12), bg="green", fg="white")
mark_button = tk.Button(root, text="Mark as Done", command=mark_task_as_done, font=("Arial", 12), bg="blue", fg="white")
remove_button = tk.Button(root, text="Remove completed Tasks", command=remove_task, font=("Verdana", 12), bg="red", fg="white")
clear_button = tk.Button(root, text="Clear Completed Tasks", command=clear_completed, font=("Arial", 12), bg="orange", fg="white")
add_button.pack(pady=10)
mark_button.pack(pady=5)
remove_button.pack(pady=5)
clear_button.pack(pady=5)
 
root.mainloop()
