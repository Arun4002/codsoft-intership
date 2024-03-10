import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        view_button = tk.Button(root, text="View Tasks", command=self.view_tasks, bg="blue", fg="white")
        view_button.grid(row=0, column=2, padx=10, pady=10)

        clear_button = tk.Button(root, text="Clear Tasks", command=self.clear_tasks, bg="red", fg="white")
        clear_button.grid(row=0, column=3, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        complete_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Task Added", f'Task "{task}" added successfully!')
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("No tasks", "No task available.")
        else:
            task_list = "\n".join(self.tasks)
            messagebox.showinfo("Tasks", f'Tasks:\n{task_list}')

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            completed_task = self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)
            messagebox.showinfo("Task Completed", f'Task "{completed_task}" marked as completed!')
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.")

    def clear_tasks(self):
        self.tasks = []
        self.task_listbox.delete(0, tk.END)
        messagebox.showinfo("Tasks Cleared", "All tasks cleared successfully!")

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
