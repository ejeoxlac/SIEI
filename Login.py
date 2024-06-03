# Libraries
from customtkinter import *
from tkinter import messagebox
from PIL import Image

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# User validator to enter the system
def login():
  user = name.get ()
  psw = password.get ()
  Resources.Connection.loginv (user, psw)
  if Resources.Connection.cur.fetchall ():
    messagebox.showinfo ('Login', 'Acceso permitido')
  elif not (user and psw):
    messagebox.showerror ('Error', 'Debes llenar las celdas')
  else:
    messagebox.showerror ('Error','Acceso denegado')

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

# Format of the window interface
main = CTk ()
main.title ('Inicio de sesión a el SIEI')
main.geometry ('500x500')
main.resizable (False, False)

# Format to create the background of the application
bg_image = CTkImage (Image.open('Resources\\Img\\Bggradient.jpg'), size=(500, 500))
bg_image_label = CTkLabel (main, text='', image=bg_image)
bg_image_label.place (x=0, y=0)

# Format of the frame that forms the main body of the window
frame = CTkFrame (main)
frame.pack (expand=True, fill='both', padx=50, pady=60)

# Title
CTkLabel (frame, text='Inicio de sesión', font=('Roboto', 26)).pack (pady=20)

# Data entry for the login
name = CTkEntry (frame, placeholder_text='Nombre', width=250)
name.pack ()

password = CTkEntry (frame, placeholder_text='Contraseña', width=250)
password.pack (pady=15)

# login button
CTkButton (frame, text='Acceder', command=login).pack ()

main.mainloop ()
