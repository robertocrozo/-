import tkinter as tk


root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
entry.grid(row=0, column=0, columnspan=30, padx=10, pady=10)


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))


def calculate():
    try:
        result = eval(entry.get())
        if isinstance(result, (int, float)):
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        else:
            raise ValueError("Invalid result type")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def clear():
    entry.delete(0, tk.END)

buttons = [
    ('7', 1), ('8', 2), ('9', 3), ('/', 4),
    ('4', 5), ('5', 6), ('6', 7), ('*', 8),
    ('1', 9), ('2', 10), ('3', 11), ('-', 12),
    ('C', 13), ('0', 14), ('=', 15), ('+', 16),
]


for (text, index) in buttons:
    if text == 'C':
        action = clear
    elif text == '=':
        action = calculate
    else:
        action = lambda x=text: button_click(x)

    button = tk.Button(root, text=text, command=action, font=('Arial', 18), width=4, height=2)
    button.grid(row=(index - 1) // 4 + 1, column=(index - 1) % 4, padx=5, pady=5)



root.mainloop()
