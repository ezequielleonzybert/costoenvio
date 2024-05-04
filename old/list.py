import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

listbox = tk.Listbox()
# listbox.pack(fill=tk.BOTH, expand=True)
listbox.grid(column=0, row=0,sticky='nsew')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()