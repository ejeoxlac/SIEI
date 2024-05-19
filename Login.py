
# Libraries
from customtkinter import *
from tkinter import messagebox

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# User validator to enter the system
def login():
  user = em.get()
  psw = ps.get()
  Resources.Connection.loginc(user, psw)
  if Resources.Connection.cur.fetchall():
    messagebox.showinfo ('Login', 'Acceso permitido')
  else:
    messagebox.showerror ('Error','Acceso denegado')

# Defined appearance
set_appearance_mode ("dark")
set_default_color_theme ("blue")

# Format of the window interface
main = CTk ()
main.title ("CTK - Login")
main.geometry ("500x500")

# Format of the frame that forms the main body of the window
user = CTkFrame (main)
user.pack (expand = True, fill = "both", padx = 20, pady = 60 )

# Title
CTkLabel (user, text = "Login system", font= ("Roboto", 26)).pack (pady = 20)

# Data entry for the login
em = CTkEntry (user, placeholder_text = "Email", width=250)
em.pack ()

ps= CTkEntry (user, placeholder_text = "Password", width=250)
ps.pack (pady = 15)

# login button
CTkButton (user, text = "login", command=login).pack ()

main.mainloop ()