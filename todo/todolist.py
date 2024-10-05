import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List Mammad")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)
        self.root.configure(bg="LightCyan4")

        
        self.style = ttk.Style()
        self.style.configure("TLabel", background="LightCyan4", foreground="gainsboro")
        self.style.configure("TButton", foreground="gray28")
        self.style.configure("TEntry", fieldbackground="LightCyan4", foreground="gray28")

        
        self.FrameTitle = tk.Frame(root, bg="LightCyan4")
        self.FrameTitle.pack(fill="both")

        self.FrameTask = tk.Frame(root, bg="LightCyan4")
        self.FrameTask.pack(side="left", fill="both")

        self.FrameEntry = tk.Frame(root, bg="LightCyan4")
        self.FrameEntry.pack(side="right", fill="both")

        
        self.labelTitle = ttk.Label(
            self.FrameTitle,
            text="To Do List",
            font=("Brush Script MT", "40"),
        )
        self.labelTitle.pack(padx=20, pady=20)

        
        self.labelFrameTask = ttk.Label(
            self.FrameTask,
            text="What's Your Task:",
            font=("Consolas", "11", "bold"),
        )
        self.labelFrameTask.pack(padx=10)

        
        self.EntryField = ttk.Entry(
            self.FrameTask,
            font=("Consolas", "12"),
            width=18,
        )
        self.EntryField.pack(padx=10)

        
        self.add_button = ttk.Button(
            self.FrameTask,
            text="Add Task",
            width=24,
            command=self.add_task
        )
        self.add_button.pack(padx=10)

        self.del_button = ttk.Button(
            self.FrameTask,
            text="Delete Task",
            width=24,
            command=self.delete_task
        )
        self.del_button.pack(padx=10)

        self.del_all_button = ttk.Button(
            self.FrameTask,
            text="Delete All Tasks",
            width=24,
            command=self.delete_all_tasks
        )
        self.del_all_button.pack(padx=10)

        self.exit_button = ttk.Button(
            self.FrameTask,
            text="Exit",
            width=24,
            command=self.close
        )
        self.exit_button.pack(padx=10)

        
        self.task_listbox = tk.Listbox(
            self.FrameEntry,
            width=26,
            height=13,
            selectmode='SINGLE',
            background="gainsboro",
            foreground="gray22",
            font="bold"
        )
        self.task_listbox.pack()

        self.tasks = []  # Use self.tasks for instance variable

    def add_task(self):
        task_string = self.EntryField.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task_string)
            self.EntryField.delete(0, 'end')
            self.update_task_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()

    def delete_all_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()

    def close(self):
        self.root.quit()

    def update_task_listbox(self):
        self.task_listbox.delete(0, 'end')
        for task in self.tasks:
            self.task_listbox.insert('end', task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = Todo(root)
    root.mainloop()
