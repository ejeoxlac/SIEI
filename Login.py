# Libraries
from customtkinter import *
from tkinter import messagebox
from PIL import Image
import subprocess

# Communicating with SQLite3 to get the login data from the database
import Resources.Connection

# User validator to enter the system
def login():
  user = name.get ()
  psw = password.get ()
  Resources.Connection.loginv (user, psw)
  if Resources.Connection.cur.fetchall ():
    messagebox.showinfo ('Login', 'Acceso permitido')
    main.destroy ()
    subprocess.run (['python', 'Menu.py'])
  elif not (user and psw):
    messagebox.showerror ('Error', 'Debes llenar las celdas')
  else:
    messagebox.showerror ('Error','Acceso denegado')

# Defined appearance
set_appearance_mode ('dark')
set_default_color_theme ('blue')

# Format of the window interface
main = CTk ()
main.iconbitmap ('Resources\\Img\\Ico.ico')
main.title ('Inicio de sesión al sistema SIEI')
main.geometry ('400x400')
main.resizable (False, False)

# Format to create the background of the application
bg_image = CTkImage (Image.open('Resources\\Img\\Bggradient.jpg'), size=(400, 400))
bg_image_label = CTkLabel (main, text='', image=bg_image)
bg_image_label.place (x=0, y=0)

# Format of the frame that forms the main body of the window
frame = CTkFrame (main)
frame.pack (expand=True, fill='both', padx=50, pady=60)

# Title
CTkLabel (frame, text='SIEI', font=('Roboto', 26)).pack (pady=20)

# Data entry for the login
name = CTkEntry (frame, placeholder_text='Usuario', show='*', width=250, height=40)
name.pack (pady=5)

password = CTkEntry (frame, placeholder_text='Contraseña', show='*', width=250, height=40)
password.pack (pady=15)

# login button
CTkButton (frame, text='Acceder', command=login, corner_radius=15).pack (pady=20)

main.mainloop ()
