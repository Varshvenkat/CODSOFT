import tkinter as tk

def perform_calculation():
    input_text = entry.get()
    try:
        result = str(eval(input_text))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_click(text):
    if text == "=":
        perform_calculation()
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text + text)

def create_button(root, text, row, col, button_color, font_size=18):
    return tk.Button(root, text=text, font=("Arial", font_size), padx=20, pady=20, bd=8, bg=button_color, command=lambda: button_click(text)).grid(row=row, column=col)

root = tk.Tk()
root.geometry("400x550")
root.title("Calculator")

# Entry widget for input and results
entry = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=4, width=14, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define colors for operation buttons and digit buttons
operation_button_color = "green"
digit_button_color = "lightblue"

# Buttons
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0)

button_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 2, 0
for button in button_list:
    button_color = operation_button_color if button in '/+*-=' else digit_button_color
    create_button(button_frame, button, row, col, button_color)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
