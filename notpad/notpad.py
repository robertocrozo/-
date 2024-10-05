import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class MyNotepadApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Notepad")
        self.window.geometry("800x600")
        self.window.configure(bg="#f0f0f0")

        self.text_box = tk.Text(self.window, wrap="word", undo=True, bg="#ffffff", fg="#333333", font=("Arial", 12))
        self.text_box.pack(expand=1, fill="both")


        self.menu_bar = tk.Menu(self.window, bg="#dddddd", fg="#333333")
        self.window.config(menu=self.menu_bar)


        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#dddddd", fg="#333333")
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_existing_file)
        self.file_menu.add_command(label="Save", command=self.save_current_file)
        self.file_menu.add_command(label="Quit", command=self.quit_application)
        self.file_menu.add_separator()
        

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#dddddd", fg="#333333")
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Change Font Color", command=self.change_font_color)

        self.current_file = None

    def open_existing_file(self):
        file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.current_file = file
            with open(file, "r") as f:
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, f.read())

    def save_current_file(self):
        if self.current_file:
            with open(self.current_file, "w") as f:
                f.write(self.text_box.get(1.0, tk.END))
        else:
            self.save_as_new_file()

    def save_as_new_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.current_file = file
            with open(file, "w") as f:
                f.write(self.text_box.get(1.0, tk.END))

    def change_font_color(self):
        color = simpledialog.askstring("Font Color", "Enter color name or hex code (e.g., 'red' or '#ff0000'):")
        if color:
            self.text_box.config(fg=color)

    def quit_application(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyNotepadApp(root)
    root.mainloop()
