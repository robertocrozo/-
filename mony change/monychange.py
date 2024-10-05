import tkinter as tk

class MoneyConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Money Converter")
        master.geometry("300x200")
        master.configure(bg='LightCyan4')

        self.conversion_type = tk.StringVar(value="Tomans to Dollars")


        self.conversion_frame = tk.Frame(master, bg='LightCyan4')
        self.conversion_frame.pack(pady=10)


        self.tomans_to_dollars_button = tk.Radiobutton(
            self.conversion_frame,
            text="Tomans to Dollars",
            variable=self.conversion_type,
            value="Tomans to Dollars",
            bg='LightCyan4'
        )
        self.tomans_to_dollars_button.pack(side=tk.LEFT)

        self.dollars_to_tomans_button = tk.Radiobutton(
            self.conversion_frame,
            text="Dollars to Tomans",
            variable=self.conversion_type,
            value="Dollars to Tomans",
            bg='LightCyan4'
        )
        self.dollars_to_tomans_button.pack(side=tk.LEFT)


        self.money_entry = tk.Entry(master, width=10, bg="orange")
        self.money_entry.pack(pady=10)


        self.convert_button = tk.Button(master, text="Convert", command=self.convert_money, bg="orange")
        self.convert_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_conversion, bg="orange")
        self.reset_button.pack(pady=5)


        self.result_label = tk.Label(master, text="", bg='LightCyan4')
        self.result_label.pack(pady=10)

    def convert_money(self):
        try:
            if self.conversion_type.get() == "Tomans to Dollars":
                tomans = float(self.money_entry.get())
                dollars = tomans / 60000
                self.result_label.config(text=f"{tomans} Tomans = {dollars:.2f} Dollars")
            else:
                dollars = float(self.money_entry.get())
                tomans = dollars * 60000
                self.result_label.config(text=f"{dollars} Dollars = {tomans:.2f} Tomans")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def reset_conversion(self):
        self.money_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.conversion_type.set("Tomans to Dollars")

if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyConverterApp(root)
    root.mainloop()