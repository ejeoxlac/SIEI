from customtkinter import *
from tkinter import messagebox

import sqlite3

db = sqlite3.connect("Resources\SIEIDB.db")
cur = db.cursor()

set_appearance_mode ("dark")
set_default_color_theme ("blue")

def login():
  user = em.get()
  psw = ps.get()
  cur.execute ('SELECT * FROM "Usuarios-Sis" WHERE Usuario = ? AND PSW = ?', [user, psw])
  if cur.fetchall():
    messagebox.showinfo ('Login', 'Acceso permitido')
  else:
    messagebox.showerror ('Error','Acceso denegado')

main = CTk ()
main.title ("CTK - Login")
main.geometry ("500x500")

user = CTkFrame (main)
user.pack (expand = True, fill = "both", padx = 20, pady = 60 )

CTkLabel (user, text = "Login system", font= ("Roboto", 26)).pack (pady = 20)

em = CTkEntry (user, placeholder_text = "Email", width=250)
em.pack ()

ps= CTkEntry (user, placeholder_text = "Password", width=250)
ps.pack (pady = 15)

CTkButton (user, text = "Login", command=login).pack ()

main.mainloop ()