import tkinter as tk
from geopy.geocoders import Nominatim
from functools import partial

geolocator = Nominatim(user_agent="costoenvio")

def consultar():
    query = input_destino.get()
    results = geolocator.geocode(query, exactly_one=False)
    print(results)

def on_destino_change(event):
    listbox.delete(0, tk.END)
    query = input_destino.get()
    results = geolocator.geocode(query, exactly_one=False, country_codes='AR')
    for result in results:
        listbox.insert(tk.END, result)
    print(results)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root_width = 400
root_height = 400
root.geometry(
    f'{root_width}x'
    f'{root_height}+'
    f'{int(screen_width/2 - root_width/2)}+'
    f'{int(screen_height/2 - root_height/2)}'
    )
root.resizable(False,False)
root.title('costo de envío')

root.columnconfigure(1,weight=1)
root.rowconfigure(1,weight=1)

label_1 = tk.Label(root, text='destino')
label_1.grid(row=0,column=0,padx=8)

input_destino = tk.Entry(root)
input_destino.grid(row=0,column=1,sticky='ew',padx=16,pady=8)
input_destino.bind("<KeyRelease>", on_destino_change)

listbox = tk.Listbox(root)
listbox.grid(row=1,column=0,columnspan=2,sticky='nsew',padx=16,pady=8)

button = tk.Button(root, text='consultar', command=consultar)
button.grid(row=2,column=0,sticky='nsew',columnspan=2,padx=16,pady=8)

root.mainloop()