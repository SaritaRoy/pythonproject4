import tkinter as tk

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()
        listbox.delete(selected_task_index)
    except IndexError:
        pass

# GUI setup
root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=1, column=0, columnspan=2)

listbox = tk.Listbox(root, width=50, height=10)
listbox.grid(row=2, column=0, columnspan=2)

root.mainloop()
