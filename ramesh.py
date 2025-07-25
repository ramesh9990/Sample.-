import tkinter as tk
from tkinter import ttk, messagebox

def add_entry():
    tree.insert("", "end", values=(desc_var.get(), amount_var.get()))
    desc_var.set("")
    amount_var.set("")

root = tk.Tk()
root.title("Personal Finance Tracker")

desc_var = tk.StringVar()
amount_var = tk.StringVar()

tk.Label(root, text="Description").grid(row=0, column=0)
tk.Entry(root, textvariable=desc_var).grid(row=0, column=1)

tk.Label(root, text="Amount").grid(row=1, column=0)
tk.Entry(root, textvariable=amount_var).grid(row=1, column=1)

tk.Button(root, text="Add Entry", command=add_entry).grid(row=2, column=0, columnspan=2)

tree = ttk.Treeview(root, columns=("Description", "Amount"), show="headings")
tree.heading("Description", text="Description")
tree.heading("Amount", text="Amount")
tree.grid(row=3, column=0, columnspan=2)

root.mainloop()
