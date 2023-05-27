import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import os


class CC():
    """Currency Converter application using Tkinter."""

    def __init__(self):
        """Initialize the Currency Converter application."""

        self.root = tk.Tk()

        self.file_path = "currency_table.json"

        try:
            self.data = json.loads(requests.get("http://api.nbp.pl/api/exchangerates/tables/a/").text)[0]["rates"]
            self.save_currency_table()
        except:
            if not os.path.exists(self.file_path):
                raise ConnectionError("There is no data backup and internet connection")
            else:
                self.data = self.load_currency_table()


        self.root.title("Wirtualny kantor")

        self.currency_list = [i["currency"] for i in self.data]
        self.mid_list = [i["mid"] for i in self.data]
        self.currency_dict = dict(zip(self.currency_list, self.mid_list))

        self.intro = tk.Label(self.root, text="Witaj w wirtualnym kantorze!", fg="white", bg="blue", font=("Arial", 20))
        self.intro.pack(pady=20, padx=5)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)

        self.text1 = tk.Label(self.frame, text="Kwota początkowa:")
        self.text1.grid(row=0, column=0)
        self.text2 = tk.Label(self.frame, text="Waluta początkowa:")
        self.text2.grid(row=1, column=0)
        self.text3 = tk.Label(self.frame, text="Kwota po przewalutowaniu:")
        self.text3.grid(row=0, column=2)
        self.text4 = tk.Label(self.frame, text="Waluta docelowa:")
        self.text4.grid(row=1, column=2)


        self.inmoney = tk.Entry(self.frame)
        self.inmoney.grid(row=0, column=1, pady=5)

        self.incombo = ttk.Combobox(self.frame, textvariable=tk.StringVar())
        self.incombo["values"] = self.currency_list
        self.incombo.grid(row=1, column=1, pady=5)

        self.outmoney = tk.Text(self.frame, height=1, width=15, state="disabled")
        self.outmoney.grid(row=0, column=3, pady=5)

        self.outcombo = ttk.Combobox(self.frame, textvariable=tk.StringVar())
        self.outcombo["values"] = self.currency_list
        self.outcombo.grid(row=1, column=3, pady=5)

        self.frame.pack()

        self.calculate = tk.Button(text="Oblicz", command=self.calc)
        self.calculate.pack(side="left", padx=100, pady=25)

        self.terminate = tk.Button(text="Zakończ", command=self.on_closing)
        self.terminate.pack(side="right", padx=100, pady=25)
        
        self.root.mainloop()


    def save_currency_table(self):
        """Save the currency table to a JSON file."""

        with open(self.file_path, "w") as file:
            json.dump(self.data, file)


    def load_currency_table(self):
        """
        Load the currency table from a JSON file.

        Returns:
            dict: The loaded currency table.
        """

        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return None  

    
    def calc(self):
        """Perform the currency conversion calculation."""

        self.outmoney.configure(state="normal")
        self.outmoney.delete("1.0", tk.END)

        currencyin = self.incombo.get()
        currencyout = self.outcombo.get()

        try:
            inmoney = float(self.inmoney.get())
        except:
            messagebox.showerror("Błędna kwota", "Podana kwota nie może zostać przeliczona")
            return None

        if currencyin not in self.currency_list or currencyout not in self.currency_list:
            messagebox.showerror("Błędna waluta", "Podana waluta nie znajduje się w bazie danych")
            return None

        outmoney = round(inmoney * self.currency_dict[currencyin] / self.currency_dict[currencyout], 2)

        self.outmoney.insert(tk.END, outmoney)
        self.outmoney.configure(state="disabled")

    
    def on_closing(self):
        """Handle the closing of the application window."""

        if messagebox.askyesno(title="Wyjść?", message="Czy na pewno chcesz wyjść?"):
            self.root.destroy()


if __name__ == "__main__":
    CC()
    