from tkinter import ttk
import tkinter as tk
import json
from tkinter.messagebox import showinfo

import requests

def click():
    url = 'https://api.github.com/users/kubernetes'
    data = requests.get(url).json()

    keys = {'company', 'created_at', 'email', 'id', 'name', 'url'}
    sorted_data = {key: data[key] for key in keys if key in data}

    with open('data.json', 'w') as data_file:
        json.dump(sorted_data, data_file, indent=2)

    messagebox()

def messagebox():
    showinfo(title='Информация', message="Файл загружен")


root = tk.Tk()
root.geometry('700x200')
root.title('ПР 11')

lbl = ttk.Label(root, text = 'Номер зачётки 1', font = ('Calibri', 30))
lbl.pack(anchor = 'center', pady = 20)

btn_download = ttk.Button(root, text = 'cкачать json', cursor = 'hand2', command = click)
btn_download.pack(anchor = 'center')

root.mainloop()

