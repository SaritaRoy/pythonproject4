import tkinter as tk

# Function to update the expression in the input field
def button_click(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)  # Clear the current expression
    entry.insert(tk.END, current_expression + str(value))

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Initialize the root window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for displaying the input/output
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Create the calculator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=clear)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Start the main loop
root.mainloop()
