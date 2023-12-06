import tkinter
from tkinter import *

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def mark_as_done():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, {'bg': 'light green'})

def mark_as_not_done():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, {'bg': 'white'})
        
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
 

root = Tk()
root.title("To-Do List")

task_entry = Entry(root, width=30)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

task_listbox = Listbox(root, selectbackground='light blue', selectmode='SINGLE', height=15, width=40)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

done_button = Button(root, text="Mark as Done", command=mark_as_done)
done_button.grid(row=2, column=0, padx=10, pady=10)

not_done_button = Button(root, text="Mark as Not Done", command=mark_as_not_done)
not_done_button.grid(row=2, column=1, padx=10, pady=10)

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
