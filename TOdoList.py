import tkinter as tk
from tkinter import messagebox, simpledialog
tasks = []
def refresh_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "YES" if task["completed"] else "NO"
        task_listbox.insert(tk.END, f"{i + 1}. {task['task']} (Due: {task['due_date']}) {status}")
def add_task():
    task = task_entry.get()
    due_date = due_date_entry.get()
    if not task or not due_date:
        messagebox.showwarning("Input Error", "Please enter both task and due date.")
        return
    tasks.append({"task": task, "due_date": due_date, "completed": False})
    refresh_task_list()
    task_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
def mark_task_completed():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["completed"] = True
        refresh_task_list()
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a task to mark as completed.")
def remove_task():
    try:
        index = task_listbox.curselection()[0]
        removed = tasks.pop(index)
        refresh_task_list()
        messagebox.showinfo("Task Removed", f"Removed: {removed['task']}")
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a task to remove.")
root = tk.Tk()
root.title(" To-Do List")
root.geometry("500x450")
root.config(bg="#f5f5f5")
tk.Label(root, text="To-Do List Manager", font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=10)
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=5)
tk.Label(frame, text="Task:", font=("Arial", 12), bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5)
task_entry = tk.Entry(frame, font=("Arial", 12), width=25)
task_entry.grid(row=0, column=1, padx=5)
tk.Label(frame, text="Due Date:", font=("Arial", 12), bg="#f5f5f5").grid(row=1, column=0, padx=5, pady=5)
due_date_entry = tk.Entry(frame, font=("Arial", 12), width=25)
due_date_entry.grid(row=1, column=1, padx=5)
tk.Button(root, text="+ Add Task", command=add_task, font=("Arial", 12), bg="#d1e7dd").pack(pady=10)
task_listbox = tk.Listbox(root, width=65, height=10, font=("Arial", 11))
task_listbox.pack(pady=10)
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="YES Mark as Completed", command=mark_task_completed, font=("Arial", 11), bg="#d4edda").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="X Remove Task", command=remove_task, font=("Arial", 11), bg="#f8d7da").grid(row=0, column=1, padx=10)
refresh_task_list()
root.mainloop()
