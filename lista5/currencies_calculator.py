import tkinter as tk
from tkinter import ttk
import requests
import json


class CC():
    def __init__(self):
        self.root = tk.Tk()

        self.data = json.loads(requests.get("http://api.nbp.pl/api/exchangerates/tables/a/").text)[0]["rates"]
        print(self.data)
        
        self.root.title("Currency Calculator")

        self.inmoney = tk.Entry(self.root)
        self.inmoney.pack()


        self.currency_list = [i["currency"] for i in self.data]
        self.mid_list = [i["mid"] for i in self.data]
        self.currency_dict = dict(zip(self.currency_list, self.mid_list))

        self.incombo = ttk.Combobox(self.root, textvariable=tk.StringVar())
        self.incombo["values"] = self.currency_list
        self.incombo.pack()

        self.outmoney = tk.Text(self.root, height=1, width=15, state="disabled")
        self.outmoney.pack()

        self.outcombo = ttk.Combobox(self.root, textvariable=tk.StringVar())
        self.outcombo["values"] = self.currency_list
        self.outcombo.pack()

        self.calculate = tk.Button(text="Oblicz", command=self.calc)
        self.calculate.pack()

        self.terminate = tk.Button(text="Zakończ")
        self.terminate.pack()
        
        self.root.mainloop()

    
    def calc(self):
        self.outmoney.configure(state="normal")



        self.outmoney.insert(tk.END, "cos")
        self.outmoney.configure(state="disabled")



if __name__ == "__main__":
    CC()