
import customtkinter
from customtkinter import *
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# from sqlite3 import Communication
import Resources.Connection

set_appearance_mode ("dark")
set_default_color_theme ("blue")

app = customtkinter.CTk()
app.title ('CTK - SQLTool')
app.geometry ('850x650')


status = StringVar()
options = ['Operativo', 'Inoperativo']

stat_options = CTkComboBox(app,text_color='#000', fg_color='#fff',dropdown_hover_color='#7d01b2', button_color='#7d01b2',button_hover_color='#7d01b2',border_color="#7d01b2", width=150, variable=status, values=options, state='readonly')
stat_options.set('Operativo')
stat_options.place(x=460, y=15)

def find():

    # clear treeview
    for item in trv.get_children():
        trv.delete(item)

    stat = status.get()
    val = entry_search.get()
    Resources.Connection.search(val, stat)
    BO = Resources.Connection.cur.fetchall()

    for row in BO:
        trv.insert('',END, values=row)

frame = tk.Frame(app)

title_label = CTkLabel(app, text='Computadoras registradas', text_color='#fff', font = ('Roboto',20, 'bold'))
title_label.place(x=350, y=45)

entry_search = CTkEntry(app, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=300)
entry_search.place(x=30, y=15)

button_search = CTkButton(app, command=find, text_color='#fff', text='Buscar',fg_color='#02ab10',hover_color='#02920D', bg_color='#292933', cursor='hand2',corner_radius=5, width=100)
button_search.place(x=350, y=15)


trv = ttk.Treeview(app, height=22, show="headings")

trv.configure(columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))

trv.column(1, stretch=NO, width=20)
trv.column(2, stretch=NO, width=100)
trv.column(3, stretch=NO, width=100)
trv.column(4, stretch=NO, width=100)
trv.column(5, stretch=NO, width=100)
trv.column(6, stretch=NO, width=100)
trv.column(7, stretch=NO, width=100)
trv.column(8, stretch=NO, width=100)
trv.column(9, stretch=NO, width=100)
trv.column(10, stretch=NO, width=100)
trv.column(11, stretch=NO, width=100)

trv.heading(1, text='ID',anchor=tk.CENTER)
trv.heading(2, text='Nombre',anchor=tk.CENTER)
trv.heading(3, text='Modelo',anchor=tk.CENTER)
trv.heading(4, text='Serial',anchor=tk.CENTER)
trv.heading(5, text='Color', anchor=tk.CENTER)
trv.heading(6, text='Color-MB', anchor=tk.CENTER)
trv.heading(7, text='CPU', anchor=tk.CENTER)
trv.heading(8, text='RAM', anchor=tk.CENTER)
trv.heading(9, text='HDDvsSSD', anchor=tk.CENTER)
trv.heading(10, text='Estado', anchor=tk.CENTER)
trv.heading(11, text='Usuario', anchor=tk.CENTER)

scrollbary = ttk.Scrollbar(app, orient=tk.VERTICAL, command=trv.yview)
trv.configure(yscroll=scrollbary.set)
trv.configure(selectmode="extended")
scrollbary.place(x=820, y=50, width=20, height=485)

scrollbarx = ttk.Scrollbar(app, orient=tk.HORIZONTAL, command=trv.xview)
trv.configure(xscroll=scrollbarx.set)
scrollbarx.place(x=30, y=515, width=789, height=20)

trv.place(x=30, y=50, width=789, height=465)

button_search ['command'] = find

find()

# def bmo():
#     frame = tk.Frame(app)

#     title_label = CTkLabel(app, text='Computadoras registradas', text_color='#fff',bg_color='#292933', font = ('Roboto',20, 'bold'))
#     title_label.place(x=425, y=15)

#     entry_search = CTkEntry(app, text_color='#000', fg_color='#fff', border_color='#B2016C', border_width=2, width=150)
#     entry_search.place(x=50, y=15)

#     button_search = CTkButton(app, command=find, text_color='#fff', text='Buscar',fg_color='#02ab10',hover_color='#02920D', bg_color='#292933', cursor='hand2',corner_radius=5, width=100)
#     button_search.place(x=60, y=15)

#     trv = ttk.Treeview(app, height=22, show="headings")

#     trv.configure(columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))

#     trv.column(1, stretch=NO, width=20)
#     trv.column(2, stretch=NO, width=100)
#     trv.column(3, stretch=NO, width=100)
#     trv.column(4, stretch=NO, width=100)
#     trv.column(5, stretch=NO, width=100)
#     trv.column(6, stretch=NO, width=100)
#     trv.column(7, stretch=NO, width=100)
#     trv.column(8, stretch=NO, width=100)
#     trv.column(9, stretch=NO, width=100)
#     trv.column(10, stretch=NO, width=100)
#     trv.column(11, stretch=NO, width=100)

#     trv.heading(1, text='ID',anchor=tk.CENTER)
#     trv.heading(2, text='Nombre',anchor=tk.CENTER)
#     trv.heading(3, text='Modelo',anchor=tk.CENTER)
#     trv.heading(4, text='Serial',anchor=tk.CENTER)
#     trv.heading(5, text='Color', anchor=tk.CENTER)
#     trv.heading(6, text='Color-MB', anchor=tk.CENTER)
#     trv.heading(7, text='CPU', anchor=tk.CENTER)
#     trv.heading(8, text='RAM', anchor=tk.CENTER)
#     trv.heading(9, text='HDDvsSSD', anchor=tk.CENTER)
#     trv.heading(10, text='Estado', anchor=tk.CENTER)
#     trv.heading(11, text='Usuario', anchor=tk.CENTER)

#     scrollbary = ttk.Scrollbar(app, orient=tk.VERTICAL, command=trv.yview)
#     trv.configure(yscroll=scrollbary.set)
#     trv.configure(selectmode="extended")
#     scrollbary.place(x=820, y=50, width=20, height=485)

#     scrollbarx = ttk.Scrollbar(app, orient=tk.HORIZONTAL, command=trv.xview)
#     trv.configure(xscroll=scrollbarx.set)
#     scrollbarx.place(x=300, y=515, width=520, height=20)

#     trv.place(x=300, y=50, width=519, height=465)


app.mainloop ()