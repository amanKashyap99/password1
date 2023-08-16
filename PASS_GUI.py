import tkinter as tk
from tkinter import ttk
import random as r
class app():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("350x200")
        self.root.title("Strong Password Generator ")
        self.mainframe = tk.Frame(self.root,background = '#cccccc')
        self.mainframe.pack(fill='both', expand=True)
        self.text1 = ttk.Label(self.mainframe, text="Enter the length of Password :",foreground = '#000000',background = "#cccccc", font=('Berlin Sans FB', 20))
        self.text1.grid(row=0,pady = 10, column=0)
        self.l = ttk.Entry(self.mainframe)
        self.l.grid(row=1, column=0, pady=10, sticky='NWES', padx = 10)
        self.gen_btn = ttk.Button(self.mainframe, text=' Generate ',command =self.password)
        self.gen_btn.grid(row=2, column=0,pady=5)
        self.res = ttk.Label(self.mainframe, text="                                        ", foreground='#000000', background="#cccccc",font=('Arial', 20))
        self.root.mainloop()
    def password(self):
        l = int(self.l.get())
        low = "abcdefghijklmnopqrstuvwxyz"
        upp = low.upper()
        spc = "!@#$%^&*?<>{}+=_-~\|"
        nm = "1234567890"
        mix = low + spc + upp + nm
        password = ""
        for i in range(l):
            password = "".join([password, r.choice(mix)])
        self.res.grid(row=3,column=0,pady=10)
        self.res.config(text =password)
app()