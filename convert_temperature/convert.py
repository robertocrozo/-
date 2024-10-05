import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        if conversion_type.get() == "Celsius to Fahrenheit":
            celsius = float(temperature_entry.get())
            fahrenheit = (celsius * 9/5) + 32
            result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
        else:
            fahrenheit = float(temperature_entry.get())
            celsius = (fahrenheit - 32) * 5/9
            result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def reset_conversion():
    temperature_entry.delete(0, tk.END)
    result_label.config(text="")
    conversion_type.set("Celsius to Fahrenheit")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")
root.configure(bg='dim gray')

conversion_type = tk.StringVar(value="Celsius to Fahrenheit")

conversion_frame = tk.Frame(root, bg='dim gray')
conversion_frame.pack(pady=10)


conversion_combobox = ttk.Combobox(conversion_frame, textvariable=conversion_type, 
                                    values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"], 
                                    state='readonly')
conversion_combobox.pack(side=tk.LEFT)
conversion_combobox.current(0) 

temperature_entry = tk.Entry(root, width=10)
temperature_entry.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_temperature,bg='red')
convert_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_conversion,bg='red')
reset_button.pack(pady=5)

result_label = tk.Label(root, text="", bg='dim gray')
result_label.pack(pady=10)

root.mainloop()